import Foundation

#if os(macOS)

#endif


class PlatformDetector {

    static func getPlatformWithVersion() -> String {

        if #available(iOS 9.0, *) {
            return "iOS9.0"
        }
        
        if #available(iOS 10.0, *) {
            return "iOS10.0"
        }

        if #available(iOS 11.0, *) {
            return "iOS11.0"
        }
    }
}