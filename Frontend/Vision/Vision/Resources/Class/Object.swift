
import Foundation

class Object {
    var name: String = "";
    var height: Int;
    var width: Int;
    var x: Int;
    var y: Int;
    var confidence : Float;
    var color: String = "";
    
    init(name: String, height: Int, width: Int, x: Int, y: Int, confidence: Float, color: String) {
        self.color = color;
        self.name = name;
        self.height = height;
        self.width = width;
        self.x = x;
        self.y = y;
        self.confidence = confidence;
    }
}
