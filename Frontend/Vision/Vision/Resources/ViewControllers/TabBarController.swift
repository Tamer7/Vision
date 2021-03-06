// This is the tab screen
// Once the user is loaded to the application the voice function is activated
// Depending on the tab the user is in.

import UIKit

class TabbarViewController: UITabBarController {
    
    override func viewDidLoad() {
        let vc = VoiceOver()
        vc.sayThis("This is the Vision tab. Tap to detection.")
        
    }
    
    override func tabBar(_ tabBar: UITabBar, didSelect item: UITabBarItem) {
        
        let vc = VoiceOver()
        switch(self.selectedIndex) {
        case 0:
            vc.sayThis("News. Swipe up for articles. Tap to hear it. Tap top of device to ask about article")
        case 1:
            vc.sayThis("This is the Vision tab. Tap to detection.")
        default:
            break
        }
        print("Selected Index :\(self.selectedIndex)");
    }
    
}
