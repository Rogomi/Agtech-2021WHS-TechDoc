[Back](../index.md)

# WHS iOS

## Technical Documentation

### GETTING STARTED
WHS requires Xcode 11.0 and above for development. This project uses Objective-C as the Programming Language, Storyboard for the Interface and CocoaPods for Third Party Libraries. The current Xcode version used for development is 11.5. The minimum iOS Version required is iOS 11.0


### INSTALLATION AND DEVELOPMENT
In order to start with the development, first, you will need an Apple account for development. It must be under the team MSDS.COM.AU PTY LTD. Then, open the WHS Monitor iOS.xcworkspace under the repository root directory. If possible, do a pods repo update in order to avoid missing library errors. 


### PROGRAMMING LANGUAGE
WHS uses the latest Objective-C and Swift for development.


### MINIMUM VERSION
WHS requires devices with at least iOS 11.0


### APPLICATION ID
au.com.msds.WHS-Monitor


### DEBUGGING
We use a few debugging tools to test functionalities.

For the Native App, we use Xcode's debugging console to create breakpoints and test variables, API responses, and identify null objects which sometimes causes the crash.

To test the API before integrating for app usage, we use Postman. Postman is a very reliable REST API tool. We can test different HTTP Methods especially POST, PATCH, PUT, DELETE and GET. We can also add header variables to test SSO and token authentications.

We also use iOS Simulator in order to test the apps in different screen sizes and iOS Versions.


### THIRD-PARTY LIBRARIES

#### Cocoapods
Most of the third party libraries are installed using CocoaPods. They can be added by searching library names found in https://cocoapods.org/, inserting them in the Podfile and running the pod install command in the Terminal.

#### Important Libraries

**Alamofire** - used to handle app communication with the Web API.  
**SwiftyJSON** - used to handle JSON objects and have the fields be easily checked for nulls before converting to swift objects. 
**Firebase/Analytics** - a mobile SDK library for Google Analytics platform used to analyze usage data from users.  
**Firebase/Crashlytics** - used to report crashes from Users that are not encountered during development and debugging.  
**GoogleMaps**  
**AFNetworking**
**MagicalRecord**
**UITextView+Placeholder**
**TTTAttributedLabel**
**UIAlertController**


### ACTIVITIES AND CONTROLLERS  

#### Core Classes
- **AppDelegate** - manages most of the pre-startup items like Firebase configurations, etc.
  ##### Configured items
  Firebase
    

#### View Controllers
  <br/>after uwu