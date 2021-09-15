import Foundation
import UIKit
extension FirstViewController {
    
    //Add floating(blur, shadow, transluency) view to the screen
    func addFloatingView(previewView: UIView, x: Int, y: Int, width: Int, height: Int) {
        let floatingView = BlurredRoundedView(frame: CGRect(x: x, y: y, width: width, height: height))
        previewView.addSubview(floatingView)
    }
    
}
