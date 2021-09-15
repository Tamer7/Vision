// This class is dedicated to implement the voice response for the application

import Foundation
import AVFoundation
class VoiceOver {
    let voices = AVSpeechSynthesisVoice.speechVoices()
    let voiceSynth = AVSpeechSynthesizer()
    var voiceToUse: AVSpeechSynthesisVoice?
    
    init(){
        for voice in voices {
            if voice.name == "Samantha"  && voice.quality == .enhanced {
                voiceToUse = voice
            }
        }
    }
    
    func sayThis(_ phrase: String){
        let utterance = AVSpeechUtterance(string: phrase)
        utterance.voice = voiceToUse
        utterance.rate = 0.5
        
        voiceSynth.speak(utterance)
    }
    
    func sayThis(_ phrase: String, speed: Float){
            let utterance = AVSpeechUtterance(string: phrase)
            utterance.voice = voiceToUse
            utterance.rate = speed
            
            voiceSynth.speak(utterance)
    }
}
