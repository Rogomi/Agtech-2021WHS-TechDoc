[Back](index.md)

# WHS Android

## Technical Documentation

### GETTING STARTED

### INSTALLATION AND DEVELOPMENT

In order to start the development, first, you need to start Android Studio. Import the Agtech-2021WHS project and then wait for the build to finish.

### PROGRAMMING LANGUAGE

WHS uses Java for development

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
    - `showVerification`
    - `closeDrawer`
    - `setupDrawer`
    - `initToolBar`
    - `setToolbarTransparentBackground`
    - `setToolbarNormalBackground`
    - `setTitle`
    - `goToSettings`
    - `getComponent`
    - `initializeInjector`
    - `goToVerificationPage`
- **LoginActivity** - handles the login screen
    - `continueAction`
    - `initializeInjector`
    - `initializeActivity`
    - `initializeInjector`
    - `getComponent`
    - `getCallingIntent`
- **SearchActivity** - handles the search page
    - `getCallingIntent`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **SettingsActivity** - handles the settings page
    - `getCallingIntent`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **PdfViewerActivity** - handles the PDF viewer page
    - `getCallingIntent`
    - `getCallingIntent` // two functions called getCallingIntent
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **HazardActivity** - handles the hazard page
    - `getCallingIntent`
    - `getCallingIntentTask`
    - `getCallingIntent` // two functions called getCallingIntent
    - `getComponent`
    - `getMainLayout`
    - `initializeActivity`
    - `initializeInjector`
    - `initActionBar`
    - `goToForm`
- **EmailReportActivity** - handles the email report page
    - `getCallingIntent`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **ActionListActivity** - handles the action list page
    - `getCallingIntent`
    - `getCallingIntent` // two functions called getCallingIntent
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **AddEditActionActivity** - handles the add, edit action page
    - `getCallingIntent`
    - `getCallingIntent` // two functions called getCallingIntent
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
    - `getActionString`
- **AttachmentDetailActivity** - handles the attachment details page
    - `getCallingIntent`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **AttachmentListActivity** - handles the attachment list page
    - `getCallingIntent`
    - `getCallingIntent` 
    - `getCallingIntent` // three functions called getCallingIntent
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **ChangePasswordActivity** - handles the change password page
    - `getCallingIntent`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **ChemicalRegisterActivity** - handles the chemical registry page
    - `getCallingIntent`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **MsdsProductDetailActivity** - handles the product detail page
    -  `getCallingIntent`
    -  `getMainLayout`
    -  `initActionBar`
    -  `initializeInjector`
    -  `initializeActivity`
    -  `getComponent`
- **MsdsSearchResultActivity** - handles the search result page
    - `getCallingIntent`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **RecordDetailActivity** - handles the record detail page
    - `getCallingIntent`
    - `getCallingIntent`
    - `getCallingIntent` // three functions called getCallingIntent
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **RecordSearchResultActivity** - handles the record search result page
    - `getCallingIntent`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **RecordTabsActivity** - handles the record tabs page
    - `getCallingIntent`
    - `getCallingIntent`
    - `getCallingIntent`
    - `getCallingIntent`  //four functions called getCallingIntent
    - `initTabView`
    - `initActionBar`
- **ReferenceFormActivity** - contains the reference form
    - `getCallingIntent`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **ReferenceListActivity** - handles the reference list page
    - `getCallingIntent`
    - `getCallingIntent`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **TimeSheetActivity** - handles the time sheet page
    - `getCallingIntent`
    - `initPresenter`
    - `initActionBar`
    - `initAdapter`
    - `showLoading`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
    - `getScreenContext`
    - `renderTimeSheet`
    - `getTimeSheets`
- **BeaconTimeInActivity** - handles the beacon time in page
    - `getCallingIntent`
    - `initBluetoothScanner`
    - `initActionBar`
    - `initPresenter`
    - `renderDeviceDetails`
    - `checkPinStatus`
    - `successTimeIn`
    - `successTimeOut`
    - `showPinDialog`
    - `showLoading`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
    - `onLeScan`
- **NFCTimeInActivity** - handles the NFC time in page
    - `getCallingIntent`
    - `initScanner`
    - `initActionBar`
    - `initPresenter`
    - `extractLinks`
    - `renderDeviceDetails`
    - `checkPinStatus`
    - `successTimeIn`
    - `showPinDialog`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
- **QrTimeInActivity** - handles the QR time in page
    - `getCallingIntent`
    - `initScanner`
    - `run`
    - `initActionBar`
    - `initPresenter`
    - `renderDeviceDetails`
    - `checkPinStatus`
    - `successTimeIn`
    - `successTimeOut`
    - `showPinDialog`
    - `showLoading`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
- **TaskFormActivity** - handles the task form page
    - `getCallingIntent`
    - `getCallingIntent` // two functions called getCallingIntent
    - `setupUi`
    - `bindFields`
    - `getDetails`
    - `saveTask`
    - `showFileChooser`
    - `calculateCost`
    - `setReferenceFields`
    - `initActionBar`
    - `uploadAttachment`
    - `getFileName`
    - `getPath`
    - `showLoading`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
    - `UploadAttachmentTask`
    - `doInBackground`
    - `uploadToNetwork`
    - `getMimeType`
    - `createClient`
- **MobileVerificationActivity** - handles the mobile verification page
    - `getCallingIntent`
    - `initPresenter`
    - `valid`
    - `showLoading`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
- **SigneeFormActivity** - handles the signee form page
    - `getCallingIntent`
    - `sign`
    - `initActionBar`
    - `initPresenter`
    - `initSignatureField`
    - `saveSignature`
    - `getSignatureFile`
    - `showLoading`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
    - `getScreenContext`
- **SearchActivity** - handles the main search page
    - `getCallingIntent`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **RegisterActionFragment** - handles the register page
    - `newInstance`
    - `saveAction`
    - `setupUi`
    - `bindFields`
    - `initialize`
    - `renderFlexiFields`
    - `errorFlex`
    - `setReferenceFields`
    - `showLoading`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
    - `renderInitialReference`
    - `callDetails`
    - `renderCategoryReference`
    - `renderControlMeasure`
    - `renderActionDetail`
    - `renderSuccessResult`
    - `showIncidentActions`
    - `isEdit`
    - `getScreenContext`
- **RiskAssessmentActionFragment** - handles the Risk Assessment Action page
    - `Fragment newInstance // RiskAssessmentActionFragment`
    - `saveAction`
    - `setupUi`
    - `bindFields`
    - `initialize`
    - `setReferenceFields`
    - `showLoading`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
    - `renderInitialReference`
    - `callDetails`
    - `renderCategoryReference`
    - `renderActionDetail`
    - `renderSuccessResult`
    - `isEdit`
    - `getScreenContext`
- **SwmsActionFragment** - handles the SWMS Action page
    - `Fragment newInstance // SwmsActionFragment
    - `saveAction`
    - `setupUi`
    - `bindFields`
    - `initialize`
    - `setReferenceFields`
    - `showLoading`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
    - `renderInitialReference`
    - `callDetails`
    - `renderCategoryReference`
    - `renderActionDetail`
    - `renderSuccessResult`
    - `isEdit`
    - `getScreenContext`
- **SearchActivity** - handles the main search page
    - `getCallingIntent(`
    - `getMainLayout`
    - `initActionBar`
    - `initializeInjector`
    - `initializeActivity`
    - `getComponent`
- **ActionListFragment** - handles list of actions
    - `Fragment newInstance // ActionListFragment
    - `initRecordList`
    - `initialize`
    - `showLoading`
    - `hideLoading`
    - `showRetry`
    - `hideRetry`
    - `showError`
    - `loadLocalAction`
    - `renderActionList`
    - `getScreenContext`
- **AuditsAndInspectionFragment** - handles list of audits and inspections page
    - `onCreateView`
    - `initMenuView`
- **BaseFragment** - contains snackbars and base fragment
- **BasePreferenceFragment** - handles navigator and part of base fragment
- **ChangePasswordFragement** - handles change password
- **ChangePinFragment** - handles changing of account pin
- **DynamicTemplateFragment** - contains the template of application
- **EmailReportFragment** - handles email reporting
- **HomeFragment** - contains home page of application
- **IncidentReportingFragment** - handles reporting of errors
- **LoginFragment** - handles login page
- **MenuListFragment** - handles the menu list page
- **OfflinePdfFragment** - handles offline pdf viewer
- **OperationalSafetyFragment** - handles recording of data
- **PdfViewerFragment** - handles viewing of pdf files
- **PoliciesFragment** - handles policies of application
- **RecordAssessmentFragment** - handles recording of assessment
- **RecordDetailFragment** - handles recording of detail
- **RecordHazardFragment** - handles records of hazard
- **RecordIncidentWitnessFragment** - handles recording of incident witness
- **RecordListFragment** - handles list of records
- **RecordQChartChemicalSafetyFragment** - handles recording of chemical safety
- **RecordQChartDetailFragment** - handles Qchart detail recording
- **RecordQChartHazard** - handles recording of Qchart hazards
- **RecordSearchResultFragment** - handles recording of search results
- **RecordTaskFragment** - Recording of tasks within the application
- **RegistersFragment** - Handles registration of accounts
- **RiskManagementFragment** - contains list of risk management policies
- **SettingsFragment** - handles settings page
- **SignatureListFragment** - contains list of signatures
- **SigneeFragment** - handles signing page
- **SigneesAndActionsFragment** - handles signee and their actions in application
- **SignOffFragment** - handles the logging off page
- **StartAuditFragment** - handles the starting of audit
- **SwpDetailFragment** - contains details of SWP in the application

#### **Model**

The model houses the logic for the program, which is retrieved by the ViewModel upon its own receipt of input from the user through View.
 
#### **View**

View is the collection of visible elements, which also receives user input. This includes user interfaces (UI), animations and text. The content of View is not interacted with directly to change what is presented.
#### **ViewModel**
ViewModel is located between the View and Model layers. This is where the controls for interacting with View are housed, while binding is used to connect the UI elements in View to the controls in ViewModel.





