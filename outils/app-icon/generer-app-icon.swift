// Génère AppIcon.appiconset (1024x1024 : clair, sombre, teinté) à partir du design de overrides/images/favicon.svg
// Usage : swift outils/app-icon/generer-app-icon.swift
import CoreGraphics
import Foundation
import ImageIO
import UniformTypeIdentifiers

let taille = 1024
let echelleContenu: CGFloat = 0.78   // réduit le téléphone pour respecter la zone de sécurité iOS

struct Palette { let fond: CGColor?; let trait: CGColor; let barre: CGColor }

func rgb(_ hex: UInt32, _ a: CGFloat = 1) -> CGColor {
    CGColor(srgbRed: CGFloat((hex >> 16) & 0xFF) / 255, green: CGFloat((hex >> 8) & 0xFF) / 255,
            blue: CGFloat(hex & 0xFF) / 255, alpha: a)
}

func dessiner(_ p: Palette, vers url: URL) {
    let ctx = CGContext(data: nil, width: taille, height: taille, bitsPerComponent: 8, bytesPerRow: 0,
                        space: CGColorSpace(name: CGColorSpace.sRGB)!,
                        bitmapInfo: (p.fond == nil ? CGImageAlphaInfo.premultipliedLast : CGImageAlphaInfo.noneSkipLast).rawValue)!
    // Repère SVG 64x64, axe Y vers le bas
    ctx.translateBy(x: 0, y: CGFloat(taille)); ctx.scaleBy(x: CGFloat(taille) / 64, y: -CGFloat(taille) / 64)
    if let fond = p.fond { ctx.setFillColor(fond); ctx.fill(CGRect(x: 0, y: 0, width: 64, height: 64)) } // plein cadre : iOS applique le masque arrondi

    ctx.translateBy(x: 32, y: 32); ctx.scaleBy(x: echelleContenu, y: echelleContenu); ctx.translateBy(x: -32, y: -32)
    ctx.setLineCap(.round); ctx.setLineJoin(.round)

    // iPhone
    ctx.setStrokeColor(p.trait); ctx.setLineWidth(4.5)
    ctx.addPath(CGPath(roundedRect: CGRect(x: 16, y: 5, width: 32, height: 54), cornerWidth: 8, cornerHeight: 8, transform: nil))
    ctx.strokePath()
    ctx.setFillColor(p.trait)
    ctx.addPath(CGPath(roundedRect: CGRect(x: 26.5, y: 10.5, width: 11, height: 4.5), cornerWidth: 2.25, cornerHeight: 2.25, transform: nil))
    ctx.fillPath()
    ctx.setLineWidth(3); ctx.move(to: CGPoint(x: 27, y: 52.5)); ctx.addLine(to: CGPoint(x: 37, y: 52.5)); ctx.strokePath()

    // </>
    ctx.setLineWidth(4)
    ctx.move(to: CGPoint(x: 27.5, y: 26)); ctx.addLine(to: CGPoint(x: 22, y: 32)); ctx.addLine(to: CGPoint(x: 27.5, y: 38))
    ctx.move(to: CGPoint(x: 36.5, y: 26)); ctx.addLine(to: CGPoint(x: 42, y: 32)); ctx.addLine(to: CGPoint(x: 36.5, y: 38))
    ctx.strokePath()
    ctx.setStrokeColor(p.barre); ctx.setLineWidth(3.5)
    ctx.move(to: CGPoint(x: 34, y: 24)); ctx.addLine(to: CGPoint(x: 30, y: 40)); ctx.strokePath()

    let dest = CGImageDestinationCreateWithURL(url as CFURL, UTType.png.identifier as CFString, 1, nil)!
    CGImageDestinationAddImage(dest, ctx.makeImage()!, nil)
    CGImageDestinationFinalize(dest)
}

let dossier = URL(fileURLWithPath: #filePath).deletingLastPathComponent().appendingPathComponent("AppIcon.appiconset")
try FileManager.default.createDirectory(at: dossier, withIntermediateDirectories: true)

dessiner(Palette(fond: rgb(0x0D9488), trait: rgb(0xFFFFFF), barre: rgb(0x89F5E7)), vers: dossier.appendingPathComponent("AppIcon.png"))
dessiner(Palette(fond: nil, trait: rgb(0x2DD4BF), barre: rgb(0x89F5E7)), vers: dossier.appendingPathComponent("AppIcon-Dark.png"))
dessiner(Palette(fond: rgb(0x000000), trait: rgb(0xFFFFFF), barre: rgb(0xB3B3B3)), vers: dossier.appendingPathComponent("AppIcon-Tinted.png"))

let contents = """
{
  "images" : [
    { "filename" : "AppIcon.png", "idiom" : "universal", "platform" : "ios", "size" : "1024x1024" },
    { "appearances" : [ { "appearance" : "luminosity", "value" : "dark" } ],
      "filename" : "AppIcon-Dark.png", "idiom" : "universal", "platform" : "ios", "size" : "1024x1024" },
    { "appearances" : [ { "appearance" : "luminosity", "value" : "tinted" } ],
      "filename" : "AppIcon-Tinted.png", "idiom" : "universal", "platform" : "ios", "size" : "1024x1024" }
  ],
  "info" : { "author" : "xcode", "version" : 1 }
}
"""
try contents.write(to: dossier.appendingPathComponent("Contents.json"), atomically: true, encoding: .utf8)
print("Généré : \(dossier.path)")
