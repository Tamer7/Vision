import Foundation
import Emojimap

class StringProcess {
    
    var items = [String]()
    
    func appendItem(x: String) {
        self.items.append(x)
    }
    
    func LabelCountingToResult() -> String {
        // Convert items to an array of key-value pairs using tuples, where each value is the number 1
        let mappedItems = items.map { ($0, 1) }
        
        // Create a Dictionary from that items array, asking it to add the 1s together every time it finds a duplicate key
        let counts = Dictionary(mappedItems, uniquingKeysWith: +)
        
        // Create resultLabel String
        var resultLabel: String; resultLabel=""
        if counts.isEmpty {
            resultLabel = "I could not identify this object"
        } else {
            for (item, numbers) in counts {
                var emoji: String; emoji=""
                
                //Checking if match any emoji
                let mapping = EmojiMap()
                for match in mapping.getMatchesFor(item) {
                    emoji = match.emoji
                    break
                }
                resultLabel += "\(numbers) \(item), "
            }
            
            //Check and remove last space unexpected
            let checking = resultLabel.suffix(2)
            if (checking == ", ") {
                resultLabel = String(resultLabel.dropLast(2))
            }
        }
        return resultLabel
    }
}
