[Back](./README.md)

# WHS Android

## Technical Documentation

### GETTING STARTED

### INSTALLATION AND DEVELOPMENT

In order to start the development, first, you need to start Android Studio. Import the Agtech-2021WHS project and then wait for the build to finish.

### PROGRAMMING LANGUAGE

WHS uses Kotlin for development

### MINIMUM VERSION

WHS can run on Android Systems with minimum SDK version 16 (Jellybean). It may encounter multiple issues on lower SDK versions.

### APPLICATION ID
com.au.whs.agtech

### DEBUGGING

We use Android Virtual Device in Android Studio in order to test the Native Apps in different screen sizes and SDK Versions.

### THIRD-PARTY LIBRARIES

Most of the third-party libraries are integrated using Gradle. They can be added by searching library names found in the Dependencies tab in the Project Structure window.

#### Important Libraries

- **Firebase/Crashlytics** - used to report crashes from Users that are not encountered during development and debugging.
- **RxJava** - is a concurrency design pattern that you can use on Android to simplify code that executes asynchronously.
- **Retrofit** - is type-safe REST client for Android and Java which aims to make it easier to consume RESTful web services.

#### Main Utilities
- **NetworkUtils** - a class where network related functions are placed
- **ActionApi** - a class that contains action endpoints
- **ApiConnection** - a class where API connection is configured
- **AttachmentApi** - a class that contains attachment endpoints

#### Activities/Fragments

- **MainActivity** - is the main activity that contains the child fragments and sibling activities
- **LoginActivity** - handles the login screen
- **SearchActivity** - handles the search page
- **SettingsActivity** - handles the settings page
- **PdfViewerActivity** - handles the PDF viewer page
- **HazardActivity** - handles the hazard page
- **EmailReportActivity** - handles the email report page
- **ActionListActivity** - handles the action list page
- **AddEditActionActivity** - handles the add, edit action page
- **AttachmentDetailActivity** - handles the attachment details page
- **AttachmentListActivity** - handles the attachment list page
- **ChangePasswordActivity** - handles the change password page
- **ChemicalRegisterActivity** - handles the chemical registry page
- **MsdsProductDetailActivity** - handles the product detail page
- **MsdsSearchResultActivity** - handles the search result page
- **RecordDetailActivity** - handles the record detail page
- **RecordSearchResultActivity** - handles the record search result page
- **RecordTabsActivity** - handles the record tabs page
- **ReferenceFormActivity** - contains the reference form
- **ReferenceListActivity** - handles the reference list page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page
- **SearchActivity** - handles the main search page





