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
  <br/>##### **AIMandatoryTableViewController** - handles AI Mandatory screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `allRequiredFilled`
- `tableView(... heightForRowAt)`
- `tableView(didSelectRowAt)`
- `textFieldShouldBeginEditing`
- `textField(...shouldChangeCharactersIn)`
- `getLocAddr`
- `clearLocation`
- `clearType`
- `showDateInput`
<br/></br>##### **AISelectTemplateViewController** - handles the selection of the Risk Template

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `toggleTopFive`
- `fetchTemplate`
- `numberOfSections(in tableView...)`
- `tableView(...didSelectRowAt)`
- `fetchFields`
- `organizeFields`<br/></br>##### **DynamicFormTableViewController** - is a dynamic table view that can be used in different forms such as start audit

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `saveOrNext`
- `submitToApi`
- `checkAutoHazardWithRegID`
- `mandatoryFieldsFilled`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `hasSignoffSection`
- `titleForSection`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `textViewDidChange`
- `proceedToFileUpload`
- `openCamera`
- `imagePickerControllerDidCancel`
- `imagePickerController: ... didFinishPickingMediaWithInfo`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `formatPickedItems: ... dataToBeExtractedKey: ... indent: ... indentationString`
- `formatPickedDataset: ... dataToBeExtractedKey: ... indent: ... indentationString`
- `documentPickerWasCancelled`
- `documentPicker: ... didPickDocumentAtURL`
- `showDocumentPicker`
- `setAllowedUTIs`
- `uploadDTFile: ... sessionID: ... filename`
- `switchCellValueDidChanged`
- `moreButtonTapped`
- `showTimelinePickerViewWithPickerType: ... indexPath`
- `showDatePickerWithTitle: ... pickerMode: ... initialDate: ... doneBlock: ... cancelBlock: ... showInView: ... isTableGrouped`
- `showDropdownPickerViewWithMultipleModifier`
- `showSectionPicker`
- `createJSON`
- `didSelectUser`
- `showSignatureViewController`
- `didFinishSigningWithImage`
- `saveSignOff `
- `requiredFieldsValid`
- `validToSave`
- `showProgressHUD`
- `showPersonInvolvedTypeView`
- `refreshActionedByFields`
- `uploadOfflineAttachmentsAndSubmit`
- `adhocAddDataControllerDidFinish`
- `adhocAddDataController: ... didSave`
- `tableDatasetCellDidTapAddData`
- `tableDatasetCellDidUpdateData: ... tableData`
- `locationManager: ... didChangeAuthorizationStatus`
<br/></br>##### **GenericTableViewController** - handles generic table view types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
<br/></br>##### **MyStorageAddNewWorkerViewController** - handles the adding of new workers in my storage

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `dealloc`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeUI`
- `initializeDoneBarButton`
- `doneBarButtonTapped`
- `textFieldFirstNameDidChange`
- `textFieldLastNameDidChange`
- `validateEnteredName`<br/></br>##### **MyStorageCompatibilityViewControllerr** - handles the storage compatibility view

###### **Methods and Calculated Variables**
- `initWithCoder`
- `didReceiveMemoryWarning`
- `dealloc`
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `viewWillDisappear`
- `viewDidUnload`
- `fetchProductCompatibility`
- `prepareForSegue: ... sender`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... willDisplayCell: ... forRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `connection: ... didFailWithError`
- `initializeViewStorageDetails`
- `showStorageViewPicker`
- `getStorageValueWithKey: ... index`
- `legendButtonPressed`
- `notesButtonPressed`
- `reportButtonPressed`
- `pickDGClassFromDictionary`
<br/></br>##### **MyStorageESQAddBatchViewController** - handles the batch adding in my storage edit stored quantity

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `didReceiveMemoryWarning`
- `dealloc`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `connection: ... didFailWithError`
- `textField: ... shouldChangeCharactersInRange: ... replacementString`
- `doneEditing`
- `cancelledEditing`
- `initializeDataReceivers`
- `initializeUI`
- `initializeTableBatch`
- `showAddSuppliers`
- `showAddPackSizes`
- `showAddUnitSizes`
- `refreshTotalPrice`
- `doneBarbuttonItemDidTapped`
- `textFieldTextDidChanged`
- `fetchSuppliers`
- `fetchPackSizes`
- `fetchUnitSizes`
- `isAllRequiredDataFilledIn`
- `trimLeadingTrailingWhitespace`
- `finishedBatchRec`
- `showSamplePOST`<br/></br>##### **MyStorageESQAddPackSizeViewController** - handles the adding of pack size in my storage ESQ

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `didReceiveMemoryWarning`
- `dealloc`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `connection: ... didFailWithError`
- `textField: ... shouldChangeCharactersInRange: ... replacementString`
- `doneEditing`
- `cancelledEditing`
- `fetchUnitSize`
- `initializeUI`
- `initializeTablePackSizeNew`
- `refreshVisibleCells`
- `showAddUnitSizes`
- `initializeDataReceivers`
- `doneBarButtonItemDidTapped`
- `didSelectedUnit`
- `textFieldTextDidChanged`
- `isAllRequiredInformationFilledIn`
- `trimLeadingTrailingWhiteSpace`
<br/></br>##### **MyStorageESQAddSuppliersViewController** - handles the adding of suppliers in my storage

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `didReceiveMemoryWarning`
- `dealloc`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `connection: ... didFailWithError`
- `fetchExistingSuppliers`
- `initializeDataReceivers`
- `initializeUI`
- `initializeTableSupplyInfo`
- `refreshVisibleCells`
- `doneBarButtonItemDidTapped`
- `didSelectAnExistingSupplier`
- `textFieldTextDidChanged`
- `isAllRequiredInformationFilledIn`
- `trimLeadingTrailingWhiteSpace`<br/></br>##### **MyStorageESQAddUnitSizesViewController** - handles the adding of unit sizes in my storage ESQ

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `didReceiveMemoryWarning`
- `dealloc`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeUI`
- `initializeTableViewNewUnitSizeInfo`
- `doneBarButtonItemDidTapped`
- `textFieldTextDidChanged`
- `isAllRequiredDataFilledIn`
- `trimLeadingTrailingWhitespace`<br/></br>##### **MyStorageESQBatchDetailsViewController** - handles the display of batch details for my storage ESQ

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `didReceiveMemoryWarning`
- `dealloc`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `showStringPickerWithKeyName`
- `initializeUI`
- `initializeBackBarButtonItem`
- `initializeDoneBarButtonItem`
- `showIncompleteDataWarning`
- `initializeTableBatchInfo`
- `JSONSanitizerWithData: ... keys`
- `getID: ... index`
- `getID: ... arrayList: ... index`<br/></br>##### **MyStorageESQInputValueViewController** - handles the input values for my storage ESQ

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `viewWillDisappear`
- `didReceiveMemoryWarning`
- `dealloc`
- `initializeUI`
- `initializeBackBarButtonItem`
- `initializeDoneBarButtonItem`
- `initializeTextFieldHidden`
- `initializeLabelOriginalQuantity`
- `initializeLabelPreferredRate`
- `initializeLabelOperation`
- `initializeViewCalculator`
- `adjustWidthLabelPreferredRate`
- `textField: ... shouldChangeCharactersInRange: ... replacementString`
- `textFieldShouldReturn`
- `doneBarButtonItemDidTapped`
- `labelPreferredRateDidTapped`
- `textFieldHiddenReceiverTextDidChange`<br/></br>##### **MyStorageEditStoredQuantityViewController** - handles the editing of stored quantities in my storage

###### **Methods and Calculated Variables**
- `initWithCoder`
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `viewWillDisappear`
- `didReceiveMemoryWarning`
- `dealloc`
- `numberOfSectionsInTableView`
- `numberOfRowsInSection`
- `cellForRowAtIndexPath`
- `viewForHeaderInSection`
- `heightForHeaderInSection`
- `heightForRowAtIndexPath`
- `didSelectRowAtIndexPath`
- `accessoryButtonTappedForRowWithIndexPath`
- `willSendRequest`
- `didReceiveResponse`
- `didReceiveData`
- `connectionDidFinishLoading`
- `didFailWithError`
- `doneEditingCalculator`
- `cancelledEditingCalculator`
- `doneEditing`
- `cancelledEditing`
- `fetchWorkers`
- `fetchBatchDetails`
- `createPOSTRequest`
- `initializeUI`
- `initializeSaveBarButton`
- `initializeBatchTable`
- `showActionWorkerPicker`
- `showActionWorkerPickerWithTitle`
- `showDateAdjustedPicker`
- `showPreferredEditModeAlertView`
- `pushToESQInputValueView`
- `showAddNewBatchView`
- `showWarningMessage`
- `showSuccessMessage`
- `dismissHandler`
- `showBatchDetailsViewWithData`
- `showNoListFetchedAlertView`
- `showErrorAlertView`
- `addNewWorkerButtonTapped`
- `saveBarButtonDidTapped`
- `textFieldTextDidChanged`
- `initializeTableDelegates`
- `initializePOSTArguments`
- `initializeDataReceivers`
- `selectedBatchRec`
- `addNewBatchRecToDataSource`
- `appendWorkerInfos`
- `isElegibleForFetchingBatchDetails`
<br/></br>##### **MyStorageManifestViewController** - handles the my storage manifest

###### **Methods and Calculated Variables**
- `initWithCoder`
- `dealloc`
- `didReceiveMemoryWarning`
- `viewDidLoad`
- `viewWillAppear`
- `viewWillDisappear`
- `viewDidUnload`
- `viewDidLayoutSubviews`
- `shouldAutorotateToInterfaceOrientation`
- `prepareForSegue: ... sender`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... willDisplayCell: ... forRowAtIndexPath`
- `tableView: ... willSelectRowAtIndexPath`
- `progressHUDDidTapped`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `connection: ... didFailWithError`
- `fetchProductManifest`
- `initializeAnimatedViews`
- `initializeViewStorageDetails`
- `showStorageViewPicker`
- `getStorageValueWithKey: ... index`
- `hideSwitchView`
- `showSwitchView `
- `reportButtonPressed`
- `summaryButtonPressed`
- `segmentedControlValueChanged`
- `switchDidValueChanged`

<br/></br>##### **MyStorageSummaryViewController** - handles the summary display of my storage

###### **Methods and Calculated Variables**
- `initWithNibName: ... bundle`
- `dealloc`
- `didReceiveMemoryWarning`
- `viewWillDisappear`
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `viewDidUnload`
- `shouldAutorotateToInterfaceOrientation`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... viewForHeaderInSection`
- `tableView: ... willDisplayCell: ... forRowAtIndexPath`
- `tableView: ... willSelectRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `progressHUDDidTapped`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `connection: ... didFailWithError`
- `toggledSwitch`
- `fetchSummary`<br/></br>##### **NewDynamicTemplateViewController** - is a dynamic template used in different views such as the side menu

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `didReceiveMemoryWarning`
- `download`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `fetchTemplates`
- `fetchTemplateFields`
- `didSelectObject`
- `toggleTableView`
- `organizeTemplateFields`
- `tableView: ... heightForRowAtIndexPath`
- `tablePickerDidFinishedPicking: ... dataPicked`<br/></br>##### **SignOffTableViewController** - handles the view of signing off of items

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewWillDisappear`
- `didReceiveMemoryWarning`
- `saveSignOff`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `showSignatureViewController`
- `prepareForSegue: ... sender`
- `didFinishSigningWithImage`
- `didSelectUser`
- `connectionDidFinishLoading`
- `connection: ... didReceiveResponse`
- `viewSignature`
- `validToSave`
- `isCompletelySigned`
- `allowedToSign`<br/></br>##### **SignatureViewController** - handles the view that allows the user to write signatures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `didReceiveMemoryWarning`
- `positionForBar`
- `supportedInterfaceOrientations`
- `shouldAutorotate`
- `clearSignature`
- `doneSigning`<br/></br>##### **SubmittedByTableViewController** - handles the view that displays submitted by

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `fetchOffline`
- `didReceiveMemoryWarning`
- `showNoInternetConnectionView`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`<br/></br>##### **WHSSafetyAddServiceHistoryViewController** - handles the adding of service history in safety

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchAutoNum`
- `saveServiceHistoryData`
- `initializeDataSource`
- `createJSON`
- `showRecordTypePickerView`
- `showFaultServicedOrRepairedPickerView`
- `showServiceHistoryTypePickerView`
- `showServicedByPickerView`
- `showDatePickerWithIndexPath`
- `showStatusOrResultPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`<br/></br>WHS2MenuViewController
viewDidLoad
prepare(for segue: UIStoryboardSegue, sender: Any?)
<br/></br>##### **WHS2RecordViewController** - handles the display of Record screen

###### **Methods and Calculated Variables**
- `viewDidLoad`

<br/></br>##### **WHSAIAddPointsRaisedViewController** - handles the adding of points raised in audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `savePointsRaised`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAIAddRecordViewController** - handles the adding of records in audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... willSendRequest`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchAutoNum`
- `fetchLocationAddressData`
- `saveRecordData`
- `initializeDataSource`
- `clearTypeData`
- `clearLocationTypeData`
- `createJSON`
- `registerForOfflineSaving`
- `showInspectionTypePickerView`
- `showInspectionSubTypePickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showStatusPickerView`
- `showDatePickerWithIndexPath`
- `showDateTimePickerWithIndexPath`
- `showRelevantPoliciesPickerView`
- `showRelevantLegislationsPickeriew`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAIEditPointsRaisedViewController** - handles the editing of points raised in audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `registerActionDidSaved: ... responseData`
- `fetchPointRaisedDetailsData`
- `initializeDataSource`
- `showPointRaisedActionsView`
<br/></br>##### **WHSAIEditRecordViewController** - handles the editing of records in audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSAIInspectionTypePickerViewController** - handles the inspection type picker in audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddInspectionTypeView`
- `showEditInspectionTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSAIPointsRaisedViewController** - handles the display of points raised view in audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: .... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `swipeableTableViewCell: ... didTriggerRightUtilityButtonWithIndex`
- `swipeableTableViewCell: ... canSwipeToState`
- `fetchPointsRaisedRecordsData`
- `deletePointsData`
- `initializeDataSource`
- `showEditPointsRaisedView`
- `cellRightUtitilityButtons`
- `openAddRecordView`<br/></br>##### **WHSAISearchResultsViewController** - handles the search results of audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchSearchResultsRecordData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSAISearchViewController** - handles the searching of audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showInspectionTypePickerView`
- `showInspectionSubTypePickerView`
- `showDatePickerWithIndexPath`
- `showStatusPickerView`
- `showSearchResultsViewWithDataList`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSAISplittedViewController** - handles the split view of audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `initializeDataSource`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`<br/></br>##### **WHSAITabViewController** - handles the audit and inspections tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showTasksObservedView`
- `showChecklistView`
- `showPointsRaisedView`
- `showActionsView`<br/></br>##### **WHSActionCategoryPickerViewController** - handles the action category picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddActionCategoryView`
- `showEditActionCategoryView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSActionDetails ManagerViewController** - handles the managing of action details

###### **Methods and Calculated Variables**
- `initializeDataSource`<br/></br>##### **WHSActionManagerViewController** - handles the manager for actions

###### **Methods and Calculated Variables**
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `textViewDidChange`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `initializeEditActionBarButtonItem`
- `initializeSaveActionBarButtonItem`
- `showActionCategoryPickerView`
- `showActionStatusPickerView`
- `showActionPriorityPickerView`
- `showActionToBeImplementedByPickerView`
- `showActionNotificationReceiverPickerView`
- `showActionReviewedByPickerView`
- `showActionApprovedByPickerView`
- `showActionCompletedByPickerView`
- `showActionDatePicker`
- `fetchActionDetails`
- `transferActionData
- `createInData`
- `formatRecipientIDs`
- `saveAction`
- `saveActionButtonDidTapped`
- `editActionButtonDidTapped`
- `postURLConnectionDidFinished`<br/></br>##### **WHSActionViewController** - handles the display of the action view

###### **Methods and Calculated Variables**
- `enableEditingActions`
- `initializeEditActionBarButtonItem`
- `initializeAddActionBarButtonItem`
- `addActionBarButtonItemDidTapped`
- `editActionBarButtonItemDidTapped`
- `viewDidLoad`
- `viewDidAppear`
- `prepareForSegue: ... sender`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`<br/></br>##### **WHSActionsMonitorRecordViewController** - handles the display of action monitor records

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... numberOfRowsInSection`
- `didSelectRowAtIndexPath`
- `fetchActionRecordData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showSearchView`
- `showEditActionView`
<br/></br>##### **WHSActionsMonitorSearchResultsViewController** - handles the search results of actions monitor

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showEditActionView<br/></br>##### **WHSActionsMonitorSearchViewController** - handles the searching of actions monitor

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `showSearchResultsViewWithDataList`
- `showDatePickerWithIndexPath`
- `showRecordGroupPickerView`
- `showActionPriorityPickerView`
- `showPersonResponsiblePickerView`
- `showStatusPickerView`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSAddAIInspectionSubTypeViewController** - handles the adding of inspection sub types in audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAssetType`
- `initializeDataSource
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddAIInspectionTypeViewController** - handles the adding of inspection types in audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAssetType`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddActionCategoryViewController** - handles the adding of categories in actions

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveActionCategory`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddAssetSubTypeViewController** - handles the adding of asset sub types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAssetType`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddAssetTypeViewController** - handles the adding of asset types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAssetType`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddAtmosphericMonitoringTypeViewController** - handles the adding of atmospheric monitoring types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveServiceTypeData`
- `initializeDataSource`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAddAttachmentsViewController** - handles the adding of attachments

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `documentPicker: ... didPickDocumentAtURL`
- `documentPickerWasCancelled`
- `showDocumentTypePickerView`
- `showUploadOptions`
- `showImagePicker`
- `showDocumentPicker`
- `setAllowedUTIs`
- `refreshSelectedRow`
- `imagePickerController: ... didFinishPickingMediaWithInfo`
- `imagePickerControllerDidCancel`
- `acSheet: ... clickedButtonAtIndex`
- `sendPOSTRequest`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAddAttendeeViewController** - handles the adding of attendees

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAttendeeData`
- `initializeDataSource`
- `createJSON`
- `showEmployeePickerView`
- `showAssessmentTypePickerView`
- `showResultPickerView`
- `showCompetenciesPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAddCompetenciesViewController** - handles the adding of competencies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath `
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveCompetencyData`
- `initializeDataSource`
- `createJSON`
- `showLicencePickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAddControlMeasureViewController** - handles the adding of control measures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAddDynamicActionsViewController** - handles the adding of dynamic actions

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `fetchFlexibleForm`
- `fetchOfflineConnection: ... data`
- `connectionDidFinishLoading`
- `handleFlexi`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `textView: ... replacementText`
- `textViewDidChange`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `showActionTypePicker`
- `showActionCategoryPickerView`
- `showGenericPickerViewWithTitle: ... recordType: ... dataReturnedKey`
- `showWorkerPickerView: ... isNotification`
- `showNotificationReceiverPickerView`
- `createJSON`<br/></br>##### **WHSAddEmployeeDepartmentViewController** - handles the adding of employee departments

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAssetType`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddEmployeeDivisionViewController** - handles the adding of employee divisions

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAssetType`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddGenericViewController** - handles the adding of generic views

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAssetType`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddInspectionTypeViewController** - handles the adding of inspection types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonsAtIndex`
- `saveInspectionType`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddLicenceViewController** - handles the adding of licences

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveLicenceData`
- `initializeDataSource`
- `createJSON`
- `showLicenceCategoryPickerView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAddLocationViewController** - handles the adding of location

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveLocationData`
- `initializeDataSource`
- `createJSON`
- `showStatePickerView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAddNoiseAssessmentSubTypeViewController** - handles the adding of noise assessment sub types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAssetType`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`
<br/></br>##### **WHSAddNoiseAssessmentTypeViewController** - handles the adding of noise assessment types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAssetType`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddNotificationReceiverViewController** - handles the adding of notification receivers

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveNotificationReceiver`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createPOSTJSON`<br/></br>##### **WHSAddPointsRaisedViewController** - handles the adding of points raised

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `savePointsRaised`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSAddRecordViewController** - implementation that handles the adding of records

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `textViewDidChange`
- `createInData`
- `initializeSaveBarButtonItem`
- `needTextViewCell`
- `needDropdownCell`
- `needSwitchCell`
- `saveButtonItemDidTapped`
- `switchCellValueDidChanged`
- `getPreferredIndexPath`<br/></br>##### **WHSAddWorkerViewController** - handles the adding of workers

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... willSendRequest`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `showActionEmployeeTypePicker`
- `employeeListForPicker`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveWorkerData`
- `initializeDataSource`
- `createJSON`
- `showEmployeeTypePickerView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAiInspectionSubTypePickerViewController** - handles the inspection sub type picker in audits and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddInspectionSubTypeView`
- `showEditInspectionSubTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSAssetSubTypePickerViewController** - handles the asset sub type picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddView`
- `showEditView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSAssetTypePickerViewController** - handles the picking of asset types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddView`
- `showEditView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSAssetsAddDetailsViewController** - handles the adding of details in assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... viewForHeaderInSection`
- `sectionTapped`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `acSheet: ... clickedButtonAtIndex`
- `fetchLocationAddressData`
- `fetchAutoNum`
- `saveDetails`
- `initializeDataSource`
- `createJSON`
- `showAssetTypePickerView`
- `showAssetSubTypePickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showDatePickerWithIndexPath`
- `showStatePickerView`
- `showYesNoNotDeterminedPickerView`
- `showAuthorityRegistrationPickerView`
- `showLinkCompetenciesPickerView`
- `showLinkJSAPickerView`
- `showLinkSWMSPickerView`
- `showLinkPPEPickerView`
- `showTestingFrequencyPickerView`
- `showServicingFrequencyPickerView`
- `showWorkerPickerView`
- `showRelevantPoliciesPickerView`
- `showRelevantProceduresPickerView`
- `showRelevantLegislationsPickeriew`
- `showRelevantTrainingPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `clearAssetSubType`
- `clearLocationData`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAssetsAddServiceHistoryViewController** - handles the adding of service history

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchAutoNum`
- `saveServiceHistoryData`
- `initializeDataSource`
- `createJSON`
- `showRecordTypePickerView`
- `showFaultServicedOrRepairedPickerView`
- `showServiceHistoryTypePickerView`
- `showServicedByPickerView`
- `showDatePickerWithIndexPath`
- `showStatusOrResultPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAssetsAddTestHistoryViewController** - handles the adding of test history in assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... willSendRequest`
- `connection: ... didReceiveData`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchAutoNum`
- `saveTestHistoryData`
- `setupTestFrequency`
- `initializeDataSource`
- `showTestTypePickerView`
- `showItemsTestedPickerView`
- `showWorkerPicker`
- `showDatePickerWithIndexPath`
- `showStatusPickerView`
- `showSaveSucceededView`
- `showSaveFailedView`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`
- `switchCellValueDidChanged`
- `createJSON`
- `saveSucceeded`
- `saveFailed`
<br/></br>##### **WHSAssetsClassifiedAddDetailsViewController** - handles the adding of details in classified assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`<br/></br>##### **WHSAssetsClassifiedEditDetailsViewController** - handles the editing of details in classified assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`<br/></br>##### **WHSAssetsClassifiedSearchResultsViewController** - handles the search results of classified assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSAssetsClassifiedSearchViewController** - handles the searching of classified assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSAssetsClassifiedTabViewController** - handles the tab functions in classified assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`<br/></br>##### **WHSAssetsClassifiedViewController** - handles the display of classified assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchClassifiedEquipmentListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSAssetsEditDetailsViewController** - handles the editing of details in assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSAssetsEditServiceHistoryViewController** - handles the editing of service history in assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `registerActionDidSaved: ... responseData`
- `registerActionSavingDidFailed: ... responseData`
- `fetchServiceHistoryDetailsData`
- `initializeDataSource`
- `showServiceHistoryActions`
- `showAttachmentsView`<br/></br>##### **WHSAssetsEditTestHistoryViewController** - handles the editing of test history in assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `registerActionDidSaved: ... responseData`
- `registerActionSavingDidFailed: ... responseData`
- `fetchTestHistoryDetailsData`
- `initializeDataSource`
- `showTestHistoryActions`
- `showAttachmentsView`<br/></br>##### **WHSAssetsElectricalAddDetailsViewController** - handles the adding of details in electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSAssetsElectricalAddServiceHistoryViewController** - handles the adding of service history in electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSAssetsElectricalEditDetailsViewController** - handles the editing of details in electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSAssetsElectricalEditServiceHistoryViewController** - handles the editing of service history in electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSAssetsElectricalSearchResultsViewController** - handles the search results for electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSAssetsElectricalSearchViewController** - handles the electrical search

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList<br/></br>##### **WHSAssetsElectricalTabViewController** - handles the electrical assets tab view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`<br/></br>##### **WHSAssetsElectricalViewController** - handles the display of electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchElectricalEquipmentListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSAssetsLiftingAddDetailsViewController** - handles the adding of details in lifting assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSAssetsLiftingEditDetailsViewController** - handles the editing of details in lifting assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSAssetsLiftingSearchResultsViewController** - handles the search results of lifting assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSAssetsLiftingSearchViewController** - handles the search of lifting assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSAssetsLiftingTabViewController** - handles the tab view for lifting assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`<br/></br>##### **WHSAssetsLiftingViewController** - handles the display of lifting assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchLiftingEquipmentListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSAssetsPlantAddDetailsViewController** - handles the adding of details in plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSAssetsPlantAddServiceHistoryViewController** - handles the adding of service history in plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`<br/></br>##### **WHSAssetsPlantEditDetailsViewController** - handles the editing of details in plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSAssetsPlantEditServiceHistoryViewController** - handles the editing of service history in plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue: ... sender`<br/></br>##### **WHSAssetsPlantSearchResultsViewController** - handles the search results of plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSAssetsPlantSearchViewController** - handles the searching of plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSAssetsPlantTabViewController** - handles the tab view for plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`<br/></br>##### **WHSAssetsPlantViewController** - handles the display of plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchPlantEquipmentListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSAssetsSearchRecordResultsViewController** - handles the search record results for assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`<br/></br>##### **WHSAssetsSearchRecordViewController** - handles the searching of records for assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showSearchResultsViewWithDataList`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSAssetsServiceHistoryViewController** - handles the display of service history for assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPat`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchServiceHistories`
- `showEditServiceHistoryDetailsView`
- `openAddRecordView`<br/></br>##### **WHSAssetsTestHistoryViewController** - handles the display of test history for assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `testHistoryDidSaved: ...responseData`
- `testHistorySavingDidFailed: ... responseData`
- `fetchTestHistories`
- `showTestHistoryDetailsView`
- `showTestHistoryEditDetailsView`
- `openAddRecordView`<br/></br>##### **WHSAssetsVehiclesAddDetailsViewController** - handles the adding of details for vehicle assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSAssetsVehiclesEditDetailsViewController** - handles the editing of details for vehicle assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSAssetsVehiclesSearchRecordResultsViewController** - handles the search record results of vehicle assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSAssetsVehiclesSearchRecordViewController** - handles the searching of vehicle assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSAssetsVehiclesTabViewController** - handles the tab view for vehicle assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showTestHistoryView`
- `showServiceHistory`
- `showActionsView`<br/></br>##### **WHSAssetsVehiclesViewController** - handles the display of vehicle assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchVehiclesListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSAssetsViewController** - handles the display of assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `prepareForSegue: ... sender`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `showVehiclesView`
- `showElectricalEquipmentView`
- `showPlantEquipmentView`
- `showLiftingEquipmentView`
- `showClassifiedEquipmentView`<br/></br>##### **WHSAtmosphericMonitoringAddMonitoringHistoryViewController** - handles the adding of monitoring history for atmospheric monitoring

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `exposureLimitsDonePickingSubstances`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveMonitoringHistoryData`
- `initializeDataSource`
- `createJSON`
- `showMonitoringPickerView`
- `showDatePickerWithIndexPath`
- `showExposureLimitsPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSAtmosphericMonitoringAddRecordViewController** - handles the adding of records for atmospheric monitoring

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `exposureLimitsDonePickingSubstances`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchLocationAddressData`
- `fetchAutoNum`
- `fetchConfinedSpacesDetailsData`
- `saveAtmosphericMonitoringData`
- `initializeDataSource`
- `createJSON`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showProductStoragePickerView`
- `showProductPickerView`
- `showProductListPickerView`
- `showDatePickerWithIndexPath`
- `showProjectPickerView`
- `showStatusPickerView`
- `showRelevantPoliciesPickerView`
- `showRelevantProceduresPickerView`
- `showRelevantLegislationsPickeriew`
- `showRelevantTrainingPickerView`
- `showExposureLimitsPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `clearLocationData`
- `isAllRequiredDataFilledUp`
- `isSelectedItemsExists: ... selectedItemTypeID`
- `appendSelectedItemWithIDs: ... itemNames: ... itemTypeID`
- `changeSelectedItemWithIDs: ... itemNames: ... itemTypeID`
- `discardSelectedItemWithStringOfIDs`<br/></br>##### **WHSAtmosphericMonitoringEditMonitoringHistoryViewController** - handles the editing of monitoring history for atmospheric monitoring

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchMonitoringHistoryDetailsData`
- `initializeDataSource`
- `showMonitoringHistoryActionsView`
- `showAttachmentsView`<br/></br>##### **WHSAtmosphericMonitoringEditRecordViewController** - handles the editing of records for atmospheric monitoring

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSAtmosphericMonitoringHistoryViewController** - handles the display of monitoring history for atmospheric monitoring

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchMonitoringHistories`
- `showEditMonitoringHistoryViewController`
- `openAddRecordView`<br/></br>##### **WHSAtmosphericMonitoringTabViewController** - handles the logic of the atmospheric monitoring section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showMonitoringHistoryView`
- `showRegisterActionsView`<br/></br>##### **WHSAtmosphericMonitoringTypePickerViewController** - handles the picking of an atmospheric monitoring type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddMonitoringTypeView`
- `showEditMonitoringTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSAttachmentsViewController** - handles the showing of attatchments

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `openAddRecordView`
- `showEditAttachmentsView`<br/></br>##### **WHSAttendeesSearchResultsViewController** - handles the search results of atendees

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `searchRecords`
- `initializeDataSource`
- `showEditAttendeesDetailsView`<br/></br>##### **WHSAttendeesSearchViewController** - handles the searching of Atendees

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showTypePickerView`
- `showResultPickerView`
- `searchBarButtonItemDidTapped`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSAttendeesViewController** - shows the Attendees

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchAttendeesData`
- `initializeDataSource`
- `showEditAttendeesDetailsView`
- `openAddRecordView`<br/></br>##### **WHSAuditInspectionsDetailsViewController** - handles the showing of details in Audit Inspection

###### **Methods and Calculated Variables**
<br/></br>##### **WHSAuditInspectionsRecordViewController** - handles the recording of Audit Inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchAIRecordsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `fetchOffline`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSAutoHazardViewController** - handles the Auto Hazard view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `acSheet: ... clickedButtonAtIndex`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `fetchAutoHazardList`
- `saveRecordData`
- `createJSON`
- `switchCellValueDidChanged`
- `showSiteRAPicker`
- `saveBarButtonItemDidTapped`<br/></br>##### **WHSCauseHazardsViewController** - handles the Cause Hazards view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `dismissedViewWithRecords`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `extView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchFlexibleForm`
- `fetchCauseAndHazardsData`
- `fetchHazardsListData`
- `saveCauseHazardsData`
- `createJSON`
- `showHazardsPickerView`
- `showAgencyPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`<br/></br>##### **WHSChangePasswordViewController** - handles changing of the password

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `didReceiveMemoryWarning`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `connectionDidFinishLoading`
- `initializeSaveBarButtonItem`
- `showChangePasswordStatusView: ... message`
- `showChangePasswordStatusView: ... message: ... dismissBlock`
- `textFieldValueDidChanged`
- `saveBarButtonItemDidTapped`
- `updateNewApprovedPassword`
- `validatePasswords: ... confirmNewPassword`
- `updateStoredEncryptedPassword`
- `handleChangePasswordResults`<br/></br>##### **WHSChecklistViewController** - handles the Checklist view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `viewWillAppear`
- `backButtonDidTap`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchChecklistData`
- `fetchConditionData`
- `fetchTemplatesField`
- `saveTemplateDetailsData`
- `checkAutoHazardWithRegID`
- `initializeDataSource`
- `updateDataSource`
- `createJSON`
- `showTemplatesPickerView`
- `showDropdownPickerViewWithMultipleModifier`
- `showTimelinePickerViewWithPickerType: ... indexPath`
- `showYesNoNAPickerView`
- `moreButtonTapped`
- `proceedToFileUpload`
- `openCamera`
- `imagePickerControllerDidCancel`
- `imagePickerController: ... didFinishPickingMediaWithInfo`
- `documentPickerWasCancelled`
- `documentPicker`
- `didPickDocumentAtURL`
- `showDocumentPicker`
- `setAllowedUTIs`
- `uploadDTFile: ... sessionID: ... filename`
- `prepareDownloadAttachment`
- `downloadAttachment`
- `openDataAttachment`
- `numberOfPreviewItemsInPreviewController`
- `previewController: ... previewItemAtIndex`
- `showHUD`
- `showSimpleHUD`
- `hideHUD`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `titleForSection`
- `showSectionPicker`<br/></br>##### **WHSChemicalQChartChemicalSafetyViewController** - handles the Chemical Safety view of the ChemicalQ Chart section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `numberOfSectionsInCollectionView`
- `collectionView: ... numberOfItemsInSection`
- `collectionView:: ... cellForItemAtIndexPath`
- `fetchChemicalSafetyData`
- `initializeDataSource`
- `initializeCollectionViews`
- `removeSubViewWithCell`
- `processStorageLegends`<br/></br>##### **WHSChemicalQChartDetailViewController** - shows the details view of the ChemicalQ Chart section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`<br/></br>##### **WHSChemicalQChartDetailsViewController** - shows the details of the ChemicalQ Chart

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`
- `showPDFView`
- `getImageCellWithDequeuedCell: ... cellData`<br/></br>##### **WHSChemicalQChartHazardsViewController** - shows the hazards view in the ChemicalQ Chart section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInCollectionView`
- `collectionView: ... numberOfItemsInSection`
- `collectionView: ... collectionView:`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `fetchHazardsData`
- `initializeDataSource`
- `initializeCollectionViews`<br/></br>##### **WHSChemicalQChartOperationalSafetyViewController** - handles the Operational Safety view in the ChemicalQ Chart section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `numberOfSectionsInCollectionView`
- `collectionView: ... numberOfItemsInSection`
- `collectionView: ... cellForItemAtIndexPath`
- `fetchOperationalSafetyDetailsData`
- `initializeDataSource`
- `initializeCollectionViews`
- `getCellDataWithKey: ... titleKey: ... detailKey`<br/></br>##### **WHSChemicalQChartSearchResultsViewController** - handles the search results in the ChemicalQ Chart section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSChemicalQChartSearchViewController** - handles searching in the ChemicalQ Chart section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `textViewDidChange`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `showSearchResultsView`
- `showGenericPickerViewWithType: ... returnedDataKey`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSChemicalQChartTabViewController** - logic behind the ChemicalQ Chart tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showEmailReportView`
- `showDetailsView`
- `showHazardsView`
- `showChemicalSafetyView`
- `showOperationalSafetyView`
- `initializeDataSource`<br/></br>##### **WHSChemicalQChartViewController** - shows the ChemicalQ Chart screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchQChartListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showSearchView`
- `showTabView``<br/></br>##### **WHSChemicalRegisterProductDetailsViewController** - shows the product details in a Chemical Register 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `prepareForSegue: ... sender`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `mailComposeController: ... didFinishWithResult`
- `initializeEditStoredQuantityBarButtonItem`
- `fetchRegisterItemDetails`
- `editStoredQuantityBarButtonItemDidTapped`
- `sanitizeJSON`
- `reorderSanitizedJSON`<br/></br>##### **WHSChemicalRegisterViewController** - shows the Chemical Register screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `viewWillDisappear`
- `didReceiveMemoryWarning`
- `prepareForSegue: ... sender`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeTableViewProducts`
- `getStorageValueWithKey: ... index`
- `initializeReportBarButtonItem`
- `initializeViewStorageDetails`
- `showStorageViewPicker`
- `fetchRegisterItems`
- `fetchStorageListData`
- `reportButtonDidTapped`
- `riskAssessmentButtonDidTapped`
- `qChartButtonDidTapped`<br/></br>##### **WHSChemicalRiskAssessmentConsequencesViewController** - handles the showing of consequences in the Chemical Risk Assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection `
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `fetchConsequencesData`
- `initializeDataSource`<br/></br>##### **WHSChemicalRiskAssessmentCurrentControlsViewController** - handles the current controls of a Chemical Risk Assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `fetchCurrentControlsData`
- `initializeDataSource`
- `segregateCurrentControlsData`<br/></br>##### **WHSChemicalRiskAssessmentDetailsViewController** - shows the details of a Chemical Risk Assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... viewForHeaderInSection`
- `sectionTapped`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSChemicalRiskAssessmentHazardsConsequencesViewController** - handles the showing of the  hazards consequences screen in the chemical risk assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `fetchHazardsData`
- `fetchConsequencesData`
- `initializeDataSource`<br/></br>##### **WHSChemicalRiskAssessmentHazardsViewController** - handles the showing of the hazards screen in the chemical risk assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `fetchHazardsData`
- `initializeDataSource`<br/></br>##### **WHSChemicalRiskAssessmentNewControlsViewController** - handles the showing of the new controls screen in the chemical risk assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `heightForRowAtIndexPath`
- `didSelectRowAtIndexPath`
- `fetchNewControlsData`
- `initializeDataSource`
- `initializeAddBarButtonItem`
- `showAddActionView`
- `showEditActionView`
- `addBarButtonItemDidTapped`<br/></br>##### **WHSChemicalRiskAssessmentProductExposureLimitsViewController** - handles the showing of the product exposure limits in the chemical risk assessment screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`<br/></br>##### **WHSChemicalRiskAssessmentProductViewController** - handles the showing of a product in the chemical risk assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... viewForHeaderInSection`
- `sectionTapped`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchProductData`
- `initializeDataSource`
- `showMSDSView`
- `showExposureLimitsView`<br/></br>##### **WHSChemicalRiskAssessmentSearchResultsViewController** - handles the showing of the search results in the chemical risk assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `prepareForSegue: ... sender`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSChemicalRiskAssessmentSearchViewController** - handles the search in the chemical risk assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showGenericPickerViewWithType: ... pickerTitle: ... returnedDataKey`
- `showStatusPickerView`
- `showSearchResultsView`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSChemicalRiskAssessmentTabViewController** - handles the logic behind chemical risk assessment tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView`
- `fetchProperTabs`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReport`
- `showNewControlsView`
- `showDetailsView`
- `showProductView`
- `showHazardsView`
- `showConsequencesView`
- `showCurrentControlsView`
- `processTabFlags`<br/></br>##### **WHSChemicalRiskAssessmentViewController** - handles the showing of the chemical risk assessment screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchRiskAssessmentsListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showSearchView`
- `showPDFView`
- `showEmailReportView`
- `showTabView`<br/></br>##### **WHSChemicalRiskManagementViewController** - handles the showing of the chemical risk management screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `showRiskAssessmentView`
- `showQChartView`<br/></br>##### **WHSChemicalsViewController** - handles the showing of the chemicals screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `prepareForSegue: ... sender`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchStorageListData`
- `initializeDataSource`
- `showMSDSSearchView`
- `showChemicalRegistersView`
- `showManifestsView `
- `showCompatibilitiesView`
- `dismissedViewControllerWithStorageID`
- `getStorageValueWithKey: ... index`<br/></br>##### **WHSCompatibilityLegendsViewController** - handles the showing of the compatibility legends

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `cancelButtonDidTapped`
- `initializeHeaderDetails`
- `initializeLegendsDataSource`<br/></br>##### **WHSCompatibilityPDFViewController** handles the showing of the compatibility PDF

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue: ... sender`<br/></br>##### **WHSCompatibilityProductDetailsViewController** - how does the showing of the product details in the compatibility section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `prepareForSegue: ... sender`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `sanitizeJSON`
- `reorderSanitizedJSON`
- `fetchCompatibilityDetails`<br/></br>##### **WHSCompatibilityReportPDFViewController** - handles the showing of the compatibility report PDF

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue: ... sender`<br/></br>##### **WHSCompetenciesPickerViewController** - handles the picking of competencies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddCompetenciesView`
- `showEditCompetenciesView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSConfinedSpacesActionViewController** - how was the showing of an action in the confined spaces section 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `initializeAddRecord`
- `openAddRecordView`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `showEditActionView`
- `fetchActionsData`
- `initializeDataSource`<br/></br>##### **WHSConfinedSpacesAddActionViewController** - handles the adding of an action in the  confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `acSheet: ... clickedButtonAtIndex`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `saveConfinedSpaceDetailsData`
- `createJSON`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `showActionCategoriesPicker`
- `showActionStatusPicker`
- `showActionPriorityPicker`
- `showActionEmailPicker`
- `showWorkerPickerView`
- `showNotificationReceiverPickerView`
- `showDatePickerWithIndexPath`
- `switchCellValueDidChanged`
- `initializeDataSource`<br/></br>##### **WHSConfinedSpacesAddEntryViewController** - handles the adding of an entry in the confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `acSheet: ... clickedButtonAtIndex`
- `saveEntryData`
- `createJSON`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `showPersonnelPickerView`
- `showDatePickerWithIndexPath`
- `showTimePickerWithIndexPath`
- `initializeDataSource`<br/></br>##### **WHSConfinedSpacesAddRecordViewController** - handles the adding of a record in the confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `acSheet: ... clickedButtonAtIndex`
- `saveConfinedSpaceDetailsData`
- `createJSON`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `showConfinedSpaceTypePickerView`
- `showConfinedSpaceSubTypePickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showPurposeOfEntryPickerView`
- `showFrequencyOfEntryPickerView`
- `showStatusPickerView`
- `showYesNoNotDeterminedPickerView`
- `showCompetenciesPickerView`
- `showRiskAssessmentPickerView`
- `showJSAPickerView`
- `showSWMSPickerView`
- `showPPEPickerView`
- `showMonitoringFrequencyPickerView`
- `showPersonMonitoringPickerView`
- `showPoliciesPickerView`
- `showProceduresPickerView`
- `showLegislationsPickerView`
- `showTrainingPickerView`
- `showPersonResponsiblePickerView`
- `showOtherPersonResponsiblePickerView`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`
- `isSelectedItemsExists: ... selectedItemTypeID`
- `setSelectedItemWithIDs: ... itemNames: ... itemTypeID`
- `appendSelectedItemWithIDs: ... itemNames: ... itemTypeID`
- `discardSelectedItemWithStringOfIDs`
- `textViewDidChange`
- `fetchAutoNum`
- `fetchLocationAddressData`
- `initializeDataSource`<br/></br>##### **WHSConfinedSpacesEditActionViewController** - handles the editing of an action in that confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchCSActionDetailsData`
- `initializeDataSource`
- `formatNotificationReceivers`<br/></br>##### **WHSConfinedSpacesEditEntryViewController** - handles the editing of an entry in the confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`<br/></br>##### **WHSConfinedSpacesEditRecordViewController** - handles the editing of a record in the confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchConfinedSpacesDetailsData`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `presentDropdownList`<br/></br>##### **WHSConfinedSpacesEntriesViewController** - handles the showing of the entries in the confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeAddRecord`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchEntriesData`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `openAddRecordView`
- `showEntryDetailsView`
- `initializeDataSource`<br/></br>##### **WHSConfinedSpacesMonitoringHistoryViewController** - handles the showing of the history in the confined spaces monitoring section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath `
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchMonitoringHistories`
- `showEditMonitoringHistoryViewController`
- `openAddRecordView`
- `showMonitoringTabView`<br/></br>##### **WHSConfinedSpacesPermitDetailsViewController** - shows the details of a confined spaces permit

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchConfinedSpacesDetailsData`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `returnNullIfNull`
- `initializeDataSource`
- `showEntriesView`
- `showAttachmentsView`
- `showPDFView`<br/></br>##### **WHSConfinedSpacesPermitsViewController** - shows the permits for confined spaces

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchPermitsData`
- `initializeDataSource`
- `showPermitsView`<br/></br>##### **WHSConfinedSpacesTabViewController** - logic behind the Confined Spaces tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showAttachmentsView`
- `showEmailReportView`
- `showAssessmentView`
- `showEditDetailsView`
- `showPermitsEntriesView`
- `showMonitoringHistoryView`
- `showActionsView`<br/></br>##### **WHSControlMeasureTablePickerViewController** - handles the table picker view of the Control Measure section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `detailsView: Ã¢ÂÂ¦ savedData`
- `showAddControlMeasureView`
- `openAddRecordView`<br/></br>##### **WHSDetailsViewController** - handles the logic behind the details screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `initializeSaveBarButtonItem`
- `initializeSaveNextBarButtonItem`
- `initializeMoreOptionsBarButtonItem`
- `initializeSendBarButtonItem`
- `showSaveBarButtonItem`
- `hideSaveBarButtonItem`
- `hideSaveNextBarButtonItem`
- `hideMoreOptionsBarButtonItem`
- `presentMoreOptionsView`
- `showSaveAlertControllerView`
- `showSaveNextAlertControllerView`
- `showActionSheet: ... sender`
- `showDatePickerWithTitle`
- `showYesNoNAPickerViewWithTitle`
- `showWorkerPickerWithTitle: ... returnedDataKey: ... isMultipleSelection: ... isTableGrouped`
- `showAIWorkerPickerWithTitle: ... returnedDataKey: ... isMultipleSelection: ... isTableGrouped`
- `needDefaultViewCell`
- `needDequeuedDefaultCellWithTableView: ... data`
- `needDefaultCellWithDequeuedCell: ... data`
- `needDetailViewCell`
- `needDequeuedDetailCellWithTableView: ... data`
- `needDetailViewCellWithDequeuedCell: ... data`
- `needTextViewCell: ... data`
- `needDequeuedTextViewCellWithTableView: ... indexPath: ... data`
- `needTextViewCellWithDequeuedCell: ... indexPath: ... data`
- `needDropdownCell: ... data`
- `needDequeuedDropdownCellWithTableView: ... indexPath: ... data`
- `needDropdownCellWithDequeuedCell: ... indexPath: ... data `
- `needSwitchCell: ... data`
- `needDequeuedSwitchCellWithTableView: ... indexPath: ... data`
- `needSwitchCellWithDequeuedCell: ... indexPath: ... data`
- `moreBarButtonItemDidTapped`
- `saveBarButtonItemDidTapped`
- `saveNextBarButtonItemDidTapped`
- `switchValueDidChanged`
- `sendBarButtonItemDidTapped`
- `textViewShouldBeginEditing`
- `getPreferredIndexPath`
- `isAllRequiredDataFilledUp`
- `testSavedDataKey`
- `indexPathForField`
- `indexForField: ... inSection`<br/></br>##### **WHSDynamicActionsViewController** - handles the logic behind dynamic actions

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `openAddRecordView`
- `didSaveAction: ... isNew`<br/></br>##### **WHSDynamicSignActionsViewController** - handles the logic behind dynamic sign actions

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `saveBarButtonItemDidTapped`
- `initializeDataSource`
- `createJSON`
- `uploadOfflineAttachmentsAndSubmit`
- `submitToApi`
- `saveSignOffIndex`
- `saveActionIndex`
- `createJSONForAction`
- `checkAutoHazardWithRegID`
- `isRequiredDataFilled`<br/></br>##### **WHSDynamicSigneesViewController** - handles the logic behind dynamic signees

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... viewForHeaderInSection`
- `tableView: ... viewForFooterInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `saveBarButtonItemDidTapped`
- `validToSave`
- `didSelectUser`
- `didFinishSigningWithImage`
- `didTapAddSigneeView`
- `didTapRemoveSigneeView`
- `textViewDidChange`
- `showPersonInvolvedTypeView`
- `refreshActionedByFields`
- `showSignatureViewController`
- `initializeDataSource`<br/></br>##### **WHSDynamicTemplatesViewController** - handles the logic behind dynamic templates 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchTemplatesField`
- `saveTemplateDetailsData`
- `checkAutoHazardWithRegID`
- `initializeDataSource`
- `updateDataSource`
- `createJSON`
- `showTemplatesPickerView`
- `showDropdownPickerViewWithMultipleModifier`
- `showTimelinePickerViewWithPickerType: ... indexPath`
- `showDatePickerWithTitle: ... pickerMode: ... initialDate: ... doneBlock: ... cancelBlock: ... showInView: ... isTableGrouped`
- `showYesNoNAPickerView`
- `proceedToFileUpload`
- `openCamera`
- `imagePickerControllerDidCancel`
- `imagePickerController ... didFinishPickingMediaWithInfo`
- `documentPickerWasCancelled`
- `documentPicker: ... didPickDocumentAtURL`
- `showDocumentPicker`
- `setAllowedUTIs`
- `uploadDTFile: ... sessionID: ... filename`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSEditAIInspectionSubTypeViewController** - handles the editing of an AI inspection subtype

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditAIInspectionTypeViewController** - handles the editing of an AI inspection type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditActionCategoryViewController** - handles the editing of an action category view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditAssetSubTypeViewController** - handles the editing of an asset subtype

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditAssetTypeViewController** - handles the editing of an asset type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditAtmosphericMonitoringTypeViewController** - Montrose the editing of an atmospheric monitoring tipe

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditAttachmentsViewController** - handles editing of an attachment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `fetchRecords`
- `connectionDidFinishLoading`
- `connection: ... willSendRequest: ... redirectResponse`
- `initializeDataSource`
- `tableView: ... didSelectRowAtIndexPath`
- `getDocLink`
- `prepareDownloadAttachment`
- `downloadAttachment`
- `openDataAttachment`
- `numberOfPreviewItemsInPreviewController`
- `previewController: ... previewItemAtIndex`
- `showHUD`
- `hideHUD`<br/></br>##### **WHSEditAttendeeViewController** - handles editing of an attendee

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchAttendeeDetailsData`
- `initializeDataSource`<br/></br>##### **WHSEditEmployeeDepartmentViewController** - handles editing a department of an employee

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditEmployeeDivisionViewController** - handles editing of an employee's division

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditGenericViewController** - handles editing a generic

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditInspectionTypeViewController** - handles the editing of an inspection type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`
- `createJSON`<br/></br>##### **WHSEditLicenceViewController** - handles the editing of a license

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditNoiseAssessmentSubTypeViewController** - handles the editing of a noice assessment subtype

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditNoiseAssessmentTypeViewController** - handles the editing a noise assessment type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditNotificationReceiverViewController** - handles editing a notification receiver

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSEditPointsRaisedViewController** - handles editing points raised

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `registerActionDidSaved: ... responseData`
- `registerActionSavingDidFailed: ... responseData`
- `fetchPointRaisedDetailsData`
- `initializeDataSource`
- `showPointRaisedActionsView`<br/></br>##### **WHSEditWorkerViewController** - handles the editing of a worker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `initializeDataSource`<br/></br>##### **WHSEmailReportViewController** - shows the email report screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `initializeDataSource`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `sendBarButtonItemDidTapped`
- `saveAction`
- `createJSON`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`<br/></br>##### **WHSEmergencyProcedureViewController** - displays the emergency procedure screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchEmergencyProceduresListData`
- `initializeDataSource`
- `generateHTML`
- `showWebView`<br/></br>##### **WHSEmployeeAddServiceHistoryViewController** - handles adding a service history of an employee

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveServiceHistoryData`
- `initializeDataSource`
- `createJSON`
- `showRecordTypePickerView`
- `showServiceHistoryTypePickerView`
- `showServicedByPickerView`
- `showDatePickerWithIndexPath`
- `showStatusOrResultPickerView`
- `showSaveSucceededView`
- `showSaveFailedView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `saveFailed`<br/></br>##### **WHSEmployeeAddTestHistoryViewController** - adds an employee's test history

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `switchCellValueDidChanged`
- `acSheet: ... clickedButtonAtIndex`
- `saveTestHistoryData`
- `initializeDataSource`
- `createJSON`
- `showTestTypePickerView`
- `showWorkerPicker`
- `showDatePickerWithIndexPath`
- `showStatusPickerView`
- `showSaveSucceededView`
- `showSaveFailedView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `saveFailed`<br/></br>##### **WHSEmployeeContractorCompanyPickerViewController** - handles the picking of an employee's contractor company

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue: ... sender`<br/></br>##### **WHSEmployeeDepartmentPickerViewController** - handles the picking of an employee department

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddEmployeeDeparmentView`
- `showEditEmployeeDepartmentView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSEmployeeEditServiceHistoryViewController** - handles the editing of an employee's service history

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `registerActionDidSaved: ... responseData`
- `registerActionSavingDidFailed: ... responseData`
- `fetchServiceHistoryDetailsData`
- `initializeDataSource`
- `showServiceHistoryActions`
- `showAttachmentsView`<br/></br>##### **WHSEmployeeEditTestHistoryViewController** - handles the editing of an employee's test history

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `registerActionDidSaved: ... responseData`
- `registerActionSavingDidFailed: ... responseData`
- `fetchTestHistoryDetailsData`
- `initializeDataSource`
- `showTestHistoryActions `
- `showAttachmentsView`<br/></br>##### **WHSEmployeeServiceHistoryViewController** - shows the employee service history screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `serviceHistoryDidSaved: ... responseData`
- `serviceHistorySavingDidFailed: ... responseData`
- `initializeDataSource`
- `showEditServiceHistoryDetailsView`
- `openAddRecordView`<br/></br>##### **WHSEmployeeTestHistoryViewController** - handles the showing of the employee test history screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPat`
- `tableView: ... didSelectRowAtIndexPath`
- `testHistoryDidSaved: ... responseData`
- `testHistorySavingDidFailed: ... responseData`
- `initializeDataSource`
- `showEditTestHistoryDetailsView `
- `openAddRecordView`<br/></br>##### **WHSEnvironmentalAtmosphericMonitoringSearchResultsViewController** - handles the showing of the search results in the environmental atmospheric monitoring section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchSearchResultsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSEnvironmentalAtmosphericMonitoringSearchViewController** - handles the showing of the search results in the environmental atmospheric monitoring section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSEnvironmentalAtmosphericMonitoringViewController** - handles the showing of the environmental atmospheric monitoring screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchAtmosphericMonitoringListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSEnvironmentalConfinedSpacesSearchResultsViewController** - handles the showing of the search results in the environmental confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchSearchResultsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `setCellTitlesForDisplay`
- `showTabView`<br/></br>##### **WHSEnvironmentalConfinedSpacesSearchViewController** - handles the searching in the environmental confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSEnvironmentalConfinedSpacesViewController** - handles the showing of the environmental confined spaces screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `didReceiveMemoryWarning`
- `acSheet: ... clickedButtonAtIndex`
- `prepareForSegue: ... sender`
- `connectionDidFinishLoading`
- `openAddRecordView`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchConfinedSpacesListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`<br/></br>##### **WHSEnvironmentalDetailsViewController** - handles the showing of the details in the environmental section

###### **Methods and Calculated Variables**
- `initializeDataSource`<br/></br>##### **WHSEnvironmentalNoiseControlSearchResultsViewController** - handles the showing of the search results in the environmental noise control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchSearchResultsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSEnvironmentalNoiseControlSearchViewController** - handles the searching in the environmental noise control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSEnvironmentalNoiseControlViewController** - handles the environmental noise control screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchNoiseControlListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSEnvironmentalSearchViewController** - handles the search in the environmental section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showGenericPickerViewWithType`
- `showSearchResultsViewWithDataList`
- `showStatusPickerView`
- `showPersonResponsiblePickerView`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSEnvironmentalViewController** - handles the environmental screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `prepareForSegue`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `showAtmosphericMonitoringView`
- `showNoiseControlView`
- `showConfinedSpaces`
- `showAsbestosView`
- `showCarcinogensView`<br/></br>##### **WHSExposureLimitsAddViewController** - handles the adding of an exposure limit

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `searchResultsDonePicking`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `initializeSearchBarButtonItem`
- `initializeDoneBarButtonItem`
- `showExposureLimitTypePickerView`
- `showSearchResultsViewWithSearchPhrase`
- `searchBarButtonItemDidTapped`
- `doneBarButtonItemDidTapped`<br/></br>##### **WHSExposureLimitsSearchResultsViewController** - handles the search results of the exposure limits section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchSubstanceListData`
- `initializeDataSource`
- `initializeDoneBarButtonItem`
- `doneBarButtonItemDidTapped`<br/></br>##### **WHSExposureLimitsViewController** - handles the exposure limits screen 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `exposureLimitsFinishedAdding`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`
- `updateDataSourceWithRawDataList`
- `removeItemOnDataSourceWithIndexPath`
- `initializeDoneBarButtonItem`
- `initializeDeleteBarButtonItem`
- `showAddExposureLimitsView`
- `openAddRecordView`
- `doneBarButtonItemDidTapped`
- `deleteBarButtonItemDidTapped`<br/></br>##### **WHSFireFightingClassPickerViewController** - handles the picking of a class in the fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddClassView`
- `showEditClassView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSFireFightingRatingPickerViewController** - handles the picking of a rating in the firefighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddRatingView`
- `showEditRatingView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSGenericPickerViewController** - the superclass of a generic picker view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddGenericView`
- `showEditGenericView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSGroupedTableViewController** - handles the showing of a grouped table view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `processDataSource`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection:`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPat`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `preselectedKeysContain`
- `donePickingBarButtonItemDidTapped`<br/></br>##### **WHSHazardsAsbestosAddDetailsViewController** - handles the adding of the details in the hazards of asbestos section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView:`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchLocationAddress`
- `fetchAutoNum`
- `saveDetails`
- `initializeDataSource`
- `clearLocationData`
- `clearRiskAssessmentData`
- `createJSONData`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showPriorityPickerView`
- `showProjectPickerView`
- `showStatusPickerView`
- `showRiskAssessmentPickerView`
- `showPoliciesPickerView`
- `showProceduresPickerView`
- `showLegislationsPickerView`
- `showTrainingPickerView`
- `showInspectionFrequencyPickerView`
- `refreshSelectedRow`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleLocationData`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSHazardsAsbestosAddInspectionHistoryViewController** - handles the adding of inspection history in the hazards asbestos section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking ... dataPicked`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveInspectionHistory`
- `initializeDataSource`
- `showInspectionTypePicker`
- `showTestResultsPickerView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSHazardsAsbestosAddRemovalHistoryViewController** - handles the adding of the removal history in the hazards asbestos section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ...titleForHeaderInSection`
- `tableView: ...cellForRowAtIndexPath`
- `tableView: ...estimatedHeightForRowAtIndexPath`
- `tableView: ...heightForRowAtIndexPath`
- `tableView: ...didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveRemovalHistory`
- `initializeDataSource`
- `activateTextView: ... indexPath`
- `showDatePicker: ... indexPath`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSHazardsAsbestosEditDetailsViewController** - handles the editing of the details in the hazards asbestos section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`
- `createJSONData`<br/></br>##### **WHSHazardsAsbestosEditInspectionHistoryViewController** - handles the editing of the inspection history in the hazards as Bestos section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `registerActionDidSaved: ... responseData`
- `registerActionSavingDidFailed: ... responseData`
- `acSheet: ... clickedButtonAtIndex`
- `fetchInspectionHistoryDetailsData`
- `initializeDataSource`
- `reloadActionsView`
- `showActionsView`
- `showAttachmentsView`<br/></br>##### **WHSHazardsAsbestosEditRemovalHistoryViewController** - handles the editing of the removal history in the Hazards Asbestos section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchRemovalHistoryData`
- `initializeDataSource`
- `showAttachmentsView`<br/></br>##### **WHSHazardsAsbestosInspectionHistoryViewController** - handles the showing of the inspection history in the Hazards Asbestos screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchInspectionHistory`
- `showEditRecordView`
- `openAddRecordView`<br/></br>##### **WHSHazardsAsbestosRemovalHistoryViewController** - handles the removal history of hazards asbestos

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchRemovalHistory`
- `showEditRecordView `
- `openAddRecordView`<br/></br>##### **WHSHazardsAsbestosSearchFormViewController** - handles the search form in hazards asbestos

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsView`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSHazardsAsbestosSearchResultsViewController** - handles the search results in hazards asbestos

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSHazardsAsbestosTabViewController** - handles the hazards asbestos tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showSignOffView`
- `showDetailsView`
- `showInspectionHistoryView`
- `showRemovalHistoryView`
- `showActionsView`<br/></br>##### **WHSHazardsAsbestosViewController** - shows the Hazards Asbestos screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchAsbestosListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSHazardsCarcinogensAddEmployeeExposureViewController** - handles the adding of employee exposure in hazards carcinogens

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveEmployeeExposureData`
- `fetchWorkerDetails`
- `initializeDataSource`
- `updateDataSource`
- `createJSON`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `disabledCellsIndexPaths`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSHazardsCarcinogensAddRecordViewController** - handles the adding of record in hazards carcinogens

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveCarcinogensDetails`
- `fetchAutoNum`
- `initializeDataSource`
- `createJSON`
- `activateTextView: ... indexPath`
- `showProjectPickerView`
- `showStatusPickerView`
- `showProductStoragePickerView`
- `showProductPickerView`
- `showProductListPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isProductExists`
- `appendProducts: ... productNames`
- `existingProductList`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSHazardsCarcinogensEditEmployeeExposureViewController** - handles the editing of employee exposure in hazards carcinogens

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchEmployeeExposureDetailsData`
- `initializeDataSource`<br/></br>##### **WHSHazardsCarcinogensEditRecordViewController** - handles editing of a record in the Hazards Carcinogens section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSHazardsCarcinogensEmployeeExposureViewController** - handles the employee exposure in hazards carcinogens

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchEmployeeExposures`
- `initializeDataSource`
- `openEditRecordView`
- `openAddRecordView`<br/></br>##### **WHSHazardsCarcinogensSearchFormViewController** - handles the search form in hazards carcinogens

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsView`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSHazardsCarcinogensSearchResultsViewController** - handles the search results in hazards carcinogens

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`
<br/></br>##### **WHSHazardsCarcinogensTabViewController** - handles the hazards carcinogens tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showSignOffView`
- `showEditDetailsView`
- `showEmployeeExposureView`
- `showActionsView`<br/></br>##### **WHSHazardsCarcinogensViewController** - controls the hazards carcinogens

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchCarcinogensListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSHazardsDetailsViewController** - handles the showing of the details in the hazards section

###### **Methods and Calculated Variables**
- `initializeDataSource`<br/></br>##### **WHSHazardsSearchFormViewController** - handles the showing of the search form in the Hazards section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showStatusPickerView`<br/></br>##### **WHSHazardsSearchResutlsViewController** - handles the showing of the search results in the Hazards section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `searchRecords`
- `fetchNextPage`<br/></br>##### **WHSHazardsViewController** - handles the showing of the Hazards screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `showAsbestosView`
- `showCarcinogensView`<br/></br>##### **WHSIRSearchResultsViewController** - handles the search results in IR

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `searchRecords`
- `initializeDataSource`
- `showTabView`<br/></br>##### **WHSIRSearchViewController** - handles the IR search

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showDatePickerWithIndexPath`
- `showIncidentTypePickerView`
- `showRiskRatingPickerView`
- `showStatusPickerView`
- `showSearchResultsViewWithDataList`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSIncidentReportingAddNewHazardsViewController** - handles the adding of new hazards in incident reporting

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveHazardData`
- `initializeDataSource`
- `createJSON`
- `showHazardTypePickerView`
- `showHazardSubTypePickerView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `clearHazardData`<br/></br>##### **WHSIncidentReportingAddNewWitnessViewController** - handles the adding of new witness in incident reporting

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... willSendRequest`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchEmployeeDetails`
- `saveWitnessData`
- `initializeDataSource`
- `updateDataSource`
- `createJSON`
- `showWorkerPickerView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `clearWitnessData`<br/></br>##### **WHSIncidentReportingAddRecordViewController** - handles the adding of record in incident reporting

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... willSendRequest`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `dateOnlyFormatFromDateString`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... viewForHeaderInSection`
- `sectionTapped`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... estimatedHeightForHeaderInSection`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchFlexibleForm`
- `fetchAutoNum`
- `fetchProjectDetails`
- `fetchLocationAddress`
- `fetchEmployeeDetails`
- `saveDetailsData`
- `saveIRDetCData`
- `saveIRAddDetData`
- `saveIRDetRPData`
- `saveIRAddDetNFData`
- `initializeDataSourceWithCallback`
- `initializeDataSource`
- `updateEmployeeData`
- `createIRDetJSON`
- `createIRDetCJSON`
- `createIRAddDetJSON`
- `createIRDetRPJSON`
- `createIRAddDetNFJSON`
- `showTypePickerView`
- `showDatePickerWithIndexPath`
- `showDateTimePickerWithIndexPath`
- `showProjectPickerView`
- `showManagementSystemPicker`
- `showPersonPickerView`
- `showConsequenceRankingPicker`
- `showPotentialOutcomePicker`
- `showNotificationSeverityPicker`
- `showEmployeeContractorsCompanyPickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showStatusPickerView`
- `showWorkerPickerView`
- `showImmediateTreatmentPicker`
- `showGenderPickerView`
- `showDivisionPickerView`
- `showDepartmentPickerView`
- `showJobTitlePickerView`
- `showOccupationPickerView`
- `showIndustryPickerView`
- `showEmploymentCategoryPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `clearLocationTypeData`
- `clearDivisionData`
- `isSectionPersonInvolve`
- `insertValuesFromCell: ... intoData: ... usingParam`
- `setValuesForCell: ... fromData: ... usingParam`
- `insertValue: ... forKeyPath: ... inData`
- `insertValue: ... forKeyPath: ... inData`
- `valueFromData: ... forKeyPath: ... withTransForm`<br/></br>##### **WHSIncidentReportingAddTypeViewController** - handles the adding of type in incident reporting

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveAssetType`
- `initializeDataSource`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `createJSON`<br/></br>##### **WHSIncidentReportingAdditionalDetailsViewController** - handles the additional details in incident reporting

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSIncidentReportingDetailsViewController** - handles the details in incident reporting

###### **Methods and Calculated Variables**
- `initializeDataSource`<br/></br>##### **WHSIncidentReportingEditAdditionalDetailsViewController** - handles the editing of additional details in incident reporting

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `initializeDataSourceWithFields`
- `connection: ... willSendRequest`
- `connection: ... didReceiveData`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchFlexibleForm`
- `fetchAdditionalDetailsData`
- `fetchProjectDetails`
- `saveAdditionalDetailsData`
- `initializeDataSource`
- `createJSON`
- `showProjectPickerView`
- `showAssetEquipmentTypePickerView`
- `showAssetEquipmentPickerView`
- `showAssetEquipmentListPickerView`
- `showChemicalStoragePickerView`
- `showChemicalPickerView`
- `showChemicalListPickerView`
- `showWorkerPickerView`
- `showWorkersPickerView`
- `showLossPickerView`
- `showIncidentIdentifierPickerView`
- `showEnvironmentalIncidentCategoryPickerViewWithRow`
- `showDatePickerWithIndexPath`
- `showNatureInjuryPickerView`
- `showMechanismInjuryPickerView`
- `showBodyPartsHarmedPickerView`
- `showDutyStatusPickerView`
- `showTimeStartPickerView`
- `showRotatingShiftManagementPickerView`
- `showShiftLengthPickerView`
- `showProportionWorkedPickerView`
- `showEmployeeSupervisionPickerView`
- `showAgencyIncidentPickerView`
- `getHeaderAndFooterHeightForSection`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `isProductExists`
- `appendProducts: ... productNames`
- `existingProductList`<br/></br>##### **WHSIncidentReportingEditDetailsViewController** - handles the editing of details in incident reporting

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `fetchDetails`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `fetchIRDetCData`
- `fetchIRAddDetData`
- `fetchIRDetRPData`
- `fetchIRAddDetNFData`
- `initializeDataSource`
- `initializeWorkerDetails`
- `initializeFirstReportDetails`
- `initializeIntiialReportDetails`
- `sendFetchRequest: ... delegate: ... dictionaryType`<br/></br>##### **WHSIncidentReportingEditHazardsViewController** - handles the editing of a hazard in the incident reporting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchHazardDetailsData`
- `initializeDataSource`
<br/></br>##### **WHSIncidentReportingEditTypeViewController** - handles the editing of a type in the Incident Reporting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSIncidentReportingEditWitnessViewController** - handles the editing of a witness in the Incident Reporting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchWitnessDetailsData`
- `initializeDataSource`<br/></br>##### **WHSIncidentReportingHazardsViewController** - controls the WHS incident reporting hazards view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `viewWillDisappear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `swipeableTableViewCell: Ã¢ÂÂ¦ didTriggerRightUtilityButtonWithIndex`
- `fetchHazardsData`
- `initializeDataSource`
- `showEditHazardView`
- `cellRightUtitilityButtons`
- `openAddRecordView`<br/></br>##### **WHSIncidentReportingIncidentAssessmentViewController** - handles the WHS incident reporting incident assessment view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchFlexibleForm`
- `fetchIncidentAssessmentDetailsData`
- `fetchRecommendedRiskSignificanceData`
- `fetchIdentifiedHazardsData`
- `saveIncidentAssessmentData`
- `initializeDataSourceWithFields`
- `initializeDataSource`
- `createJSON`
- `showIdentifiedHazardList`
- `showAssetEquipmentTypePickerView`
- `showAssetEquipmentPickerView`
- `showAssetEquipmentListPickerView`
- `showChemicalStoragePickerView`
- `showChemicalPickerView`
- `showChemicalListPickerView`
- `showTrainingTypePickerView`
- `showIncidentFrequencyPickerView`
- `showAdverseEffectsPickerView`
- `showHazardImpactPickerView`
- `showRiskSignificancePickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `isSelectedItemsExists`
- `setSelectedItemWithIDs`
- `changeSelectedItemWithIDs`
- `appendSelectedItemWithIDs`
- `discardSelectedItemWithStringOfIDs`
- `discardSelectedItemWithStringOfIDsChemical`
- `dismissedViewWithRecords`<br/></br>##### **WHSIncidentReportingRecordViewController** - shows the Incident Reporting Record screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchIncidentReports`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`
- `showSearchView`
- `openPDFView`
- `showEmailReport`
- `openAddRecordView`<br/></br>##### **WHSIncidentReportingTabViewController** - handles the incident reporting procedures tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `connectionDidFinishLoading`
- `fetchFlexForm`
- `registerActionDidSaved`
- `registerActionSavingDidFailed`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showEditAdditionalDetailsView`
- `showHazardsView`
- `showWitnessessView`
- `showTreatmentsView`
- `showIncidentAssessmentDetailsView`
- `showActionsView`<br/></br>##### **WHSIncidentReportingTreatmentsDetailsViewController** - handles the WHS incident reporting treatments details view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchTreatmentsDetailsData`
- `fetchFlexibleForm`
- `saveTreatmentData`
- `initializeDataSource`
- `createJSON`
- `clearTimeLostDateData`
- `showAttachmentsView`
- `showTreatmentObtainedPickerView`
- `showUnitPickerView`
- `showDatePickerWithIndexPath`
- `showDateTimePickerWithIndexPath`
- `saveBarButtonItemDidTapped`<br/></br>##### **WHSIncidentReportingTypePickerViewController** - handles the picker view for incident reporting types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddIncidentReportingTypeView`
- `showEditIncidentReportingTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSIncidentReportingWitnessesViewController** - handles the incident reporting witnesses view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `swipeableTableViewCell: Ã¢ÂÂ¦ didTriggerRightUtilityButtonWithIndex`
- `fetchWitnessesData`
- `deleteWitnessData`
- `initializeDataSource`
- `showEditWitnessView`
- `openAddRecordView`<br/></br>##### **WHSInspectionTypePickerViewController** - handles the picker view for inspection types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddInspectionTypeView`
- `showEditInspectionTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSLandingViewController** - handles the Landing screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `buttonHamburgerDidTapped`
- `verifyHamburgerButtonExistence`
- `showActionsMonitorSearchResultsView`
- `fetchDashboardInformations`
- `fetchDynamicMenu`
- `processDashboardData`<br/></br>##### **WHSLegislationsTabViewController** - handles the Legislations tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentView`
- `showSignOffView`
- `showEmailReportView`
- `showEditDetailsView`
- `showActionsView`<br/></br>##### **WHSLicencePickerViewController** - handles the License Picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddLicenceView`
- `showEditLicenceView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSLocationPickerViewController** - handles the picker view for location

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddLocationView`
- `showEditLocationView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSLocationTypePickerViewController** - handles the picker view for location types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddLocationView`
- `openAddRecordView`<br/></br>##### **WHSLoginViewController** - handles the Login screen and login in of a user

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillDisappear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `textFieldShouldReturn`
- `showLoginStatusViewWithTitle: ... message`
- `initializeTextFields`
- `buttonLoginDidTapped`
- `getUserID`
- `validateUserID`
- `verifyUserCredentials: ... password`
- `validateUserCredentials`
- `getResponseMessage`
- `validateUsername`
- `validatePassword`<br/></br>##### **WHSMSDSProductDetailsViewController** - handles the product details in msds

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `prepareForSegue: ... sender`
- `connectionDidFinishLoading`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `mailComposeController: ... didFinishWithResult: ... error`
- `fetchProductDetails`
- `sanitizeJSON`
- `reorderSanitizedJSON`<br/></br>##### **WHSMSDSSearchResultsViewController** - handles the display of search results for MSDS

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `prepareForSegue`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `searchProducts`
<br/></br>##### **WHSMSDSSearchViewController** - handles the searching in msds

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `prepareForSegue: ... sender`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `initializeSearchBarButtonItem`
- `showNotEnoughQueryPhrase`
- `initializeUserInputReceivers`
- `searchBarButtonItemDidTapped`
- `finishedSelectingSearchTypeHandler`
- `finishedSelectingSearchFormatHandler`<br/></br>##### **WHSManifestsReportPDFViewController** - handles the PDF display for manifests reports

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue`<br/></br>##### **WHSMenuViewController** - controls menu

###### **Methods and Calculated Variables**
- `initWithCoder`
- `viewDidLoad`
- `viewWillLayoutSubviews`
- `viewWillAppear`
- `initializeTableViewPlaceholder`
- `showNoPermissionPlaceholderInMenu`
- `postURLConnectionDidFinishLoading: ... json: ... baseKey: ... targetKey`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... viewForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeMenuTableView`
- `initializeMenuTableView`
- `initializeDataSource`
- `initializeDataSourceFromFlexiForm: ... allowedFieldsKey`
- `initializeDataSourceFromAllowedFields: ... allowedFieldsKey`
- `initializeDataSourceFromFlexiForm: ... callback`
- `validateRequiredFields`
- `setTableviewDefaultBackgroundColor`
- `showNotEnoughRecordView`
- `showNotEnoughRecordViewWithTitle: ... message: ... isGoingBack`
- `fetchValidSubMenuItemListWithParentID`
- `requestPathForFlexibleFormWithPageID: ... controlID: ... refKey`
- `fetchFlexibleFormWithPageID: ... controlID: ... refKey`
- `processRecordIDs: ... JSON`
- `formatIDsToArrays`
- `processValuesOnJSONWithKey: ... JSON: ... completionBlock`
- `isNumberOfRecordsEnough: ... count`
- `isNumberOfRecordsEnough: ... array`
- `processPickerFromJSONWithKey: ... JSONDataList`
- `formatPickedItems: ... dataToBeExtractedKey: ... indent`
- `formatPickedItems: ... dataToBeExtractedKey: ... indent: .. indentationString`
- `formatPickedDataset: ... dataToBeExtractedKey: ... indent: ... indentationString`
- `formatPickedPersons: ... indentationString`<br/></br>##### **WHSNoiseAssessmentSubTypePickerViewController** - handles the picker view for noise assessment sub types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddSubTypeView`
- `showEditSubTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSNoiseControlAddAssessmentViewController** - handles adding an assessment in the Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `saveAssessmentDetailsData`
- `initializeDataSource`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSNoiseControlAddControlViewController** - handles the adding of a control in the Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue`<br/></br>##### **WHSNoiseControlAddRecordViewController** - handles the adding for noise control records

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: Ã¢ÂÂ¦ dataPicked`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchAutoNum`
- `fetchLocationAddressData`
- `saveNoiseControlDetailsData`
- `initializeDataSource`
- `clearNoiseAssessmentData`
- `clearLocationData`
- `createJSON`
- `showNoiseAssessmentTypePickerView`
- `showNoiseAssessmentSubTypePickerView`
- `showNoiseAssessmentCategoryPickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showAssetEquipmentTypePickerView`
- `showAssetEquipmentPickerView`
- `showAssetEquipmentListPickerView`
- `showChemicalStoragePickerView`
- `showChemicalPickerView`
- `showChemicalListPickerView`
- `showDatePickerWithIndexPath`
- `showStatusPickerView`
- `showYesNoNotDeterminedPickerView`
- `showAudioMetricPickerView`
- `showLinkRiskAssessmentPickerView`
- `showLinkJSAPickerView`
- `showLinkSWMSPickerView`
- `showRelevantPoliciesPickerView`
- `showRelevantProceduresPickerView`
- `showRelevantLegislationsPickeriew`
- `showRelevantTrainingPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`
- `isSelectedItemsExists`
- `setSelectedItemWithIDs`
- `appendSelectedItemWithIDs`
- `discardSelectedItemWithStringOfIDs`
<br/></br>##### **WHSNoiseControlAssessmentDetailsViewController** - handles the showing of assessment details in the Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `swipeableTableViewCell: Ã¢ÂÂ¦ didTriggerRightUtilityButtonWithIndex`
- `deleteAssessment`
- `initializeDataSource`
- `showEditDetailsView`
- `initializeAddRecordBarButtonItem`
- `showAddAssessmentView`
- `showEditCommentView`
- `cellRightUtitilityButtons`
- `sanitizeAssessments`<br/></br>##### **WHSNoiseControlEditAssessmentCommentViewController** - handles the editing of an assessment in the Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `initializeDataSource`<br/></br>##### **WHSNoiseControlEditMeasurementViewController** - handles the editing of noise control measurement

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: Ã¢ÂÂ¦ dataPicked`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchMeasurementDetailsData`
- `saveMeasurementDetailsData`
- `initializeDataSource`
- `createJSON`
- `showMeasurementLocalityPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
<br/></br>##### **WHSNoiseControlEditRecordViewController** - handles the editing of a record in Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchNoiseControlDetailsData`
- `initializeDataSource`<br/></br>##### **WHSNoiseControlNewControlViewController** - handles the showing of the new control in the Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `showEditRecordView`
- `initializeDataSource`
- `openAddRecordView`<br/></br>##### **WHSNoiseControlTabViewController** - handles the noise control tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showEditMeasurementView`
- `showAssessmentView`
- `showNewControlsView`<br/></br>##### **WHSNonChemicalRiskAssessmentAssessmentViewController** - handles the WHS nonchemical risk assessment assessment view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `fetchAssessmentData`
- `initializeDataSource`
<br/></br>##### **WHSNonChemicalRiskAssessmentDetailsViewController** - handles the WHS nonchemical risk assessment details view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ viewForHeaderInSection`
- `sectionTapped`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSNonChemicalRiskAssessmentNewControlsViewController** - handles the new controls in non chemical risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`<br/></br>##### **WHSNonChemicalRiskAssessmentSearchResultsViewController** - handles the search results in non chemical risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSNonChemicalRiskAssessmentSearchViewController** - handles the search in non chemical risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `showSearchResultsView`<br/></br>##### **WHSNonChemicalRiskAssessmentTabViewController** - handles the non chemical risk assessment tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchTabs`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showNewControlsView`
- `showSignOffView`
- `showDetailsView`
- `showAssessmentView`
- `showHazardsAndConsequencesView`
- `showHazardsView`
- `showConsequencesView`
- `showCurrentControlsView`
- `processTabFlags`<br/></br>##### **WHSNonChemicalRiskAssessmentViewController** - shows the Non Chemical Risk Assessment screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchNonChemicalRiskAssessmentListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showSearchView`
- `showPDFView`
- `showEmailReportView`
- `showTabView`
<br/></br>##### **WHSNonChemicalRiskManagementViewController** - controls the non chemical risk management

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `showHATRiskAssessmentView`
- `showSWMSView`
- `showSWPView`<br/></br>##### **WHSNonChemicalSafeWorkManagementSystemActionViewController** - handles the WHS nonchemical safe work management system action view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchNewControlsData`
- `showAddActionView`
- `showEditActionView`
<br/></br>##### **WHSNonChemicalSafeWorkManagementSystemAddActionViewController** - handles the WHS adding of action for nonchemical safe work management systems

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `sendPOSTRequest`
- `initializeDataSource`
- `showCategoryPickerView`
- `showStatusPickerView`
- `showPriorityPickerView`
- `showSendNotificationToPickerView`
- `showDatePickerWithTitle`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `getRecipientIDs`
- `createPOSTJSON`<br/></br>##### **WHSNonChemicalSafeWorkManagementSystemEditActionViewController** - handles the editing of actions for WHS nonchemical safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchActionDetailsData`
- `initializeDataSource`<br/></br>##### **WHSNonChemicalSafeWorkProceduresAddActionViewController** - handles the adding of action for the WHS nonchemical safe work procedures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `sendPOSTRequest`
- `initializeDataSource`
- `showCategoryPickerView`
- `showControlMeasurePickerView`
- `showStatusPickerView`
- `showPriorityPickerView`
- `showSendNotificationToPickerView`
- `showDatePickerWithTitle`
- `switchValueDidChanged`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `getRecipientIDs`
- `createPOSTJSON`<br/></br>##### **WHSNonChemicalSafeWorkProceduresEditActionViewController** - handles the editing of actions for WHS nonchemical safe work procedures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchActionDetailsData`
- `initializeDataSource`<br/></br>##### **WHSNotificationReceiverPickerViewController** - handles the picker in notification receiver

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddNotificationReceiversView`
- `showEditNotificationReceiversView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSOfflineFormViewController** - shows the workers 

###### **Methods and Calculated Variables**
`viewDidLoad`
`viewWillAppear`
`initializeDataSource`
`accessPermission`
`tableView(...didSelectRowAt)`
`tableView(...heightForRowAt)`<br/></br>##### **WHSOfflineFormsAuditsInspectionViewController** - handles the audits inspection in the offline forms section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `initializeDataSource`
- `tableView(...didSelectRowAt)`<br/></br>##### **WHSOfflineFormsViewController** - handles the offline forms screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `initializeDataSource`
- `showNoFormsDownloaded`
- `downloadAll`
- `tableView(...cellForRowAt)`
- `tableView(...didSelectRowAt)`
- `tableView(...heightForRowAt)`
<br/></br>##### **WHSPAPComplaintsSearchResultsViewController** - Handles the search results for the PAP Complaints section

###### **Methods and Calculated Variables**
- `showTabView`<br/></br>##### **WHSPAPComplaintsSearchViewController** handles the searching for the PAP Complaints section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`
<br/></br>##### **WHSPAPComplaintsTabViewController** - handles the PAP complaints tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentView`
- `showEmailReportView`
- `showSignOffView`
- `showEditDetailsView`
- `showChecklistView`
- `showPointsRaisedView`
- `showActionsView`
<br/></br>##### **WHSPAPDetailsViewController** - handles the PAP details

###### **Methods and Calculated Variables**
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`<br/></br>##### **WHSPAPDrillsSearchResultsViewController** - handles the search results in the PAP Drills section

###### **Methods and Calculated Variables**
- `showTabView`<br/></br>##### **WHSPAPDrillsSearchViewController** - handles the searching in the PAP Drills section

###### **Methods and Calculated Variables**
- `showSearchResultsViewWithDataList`
<br/></br>##### **WHSPAPDrillsTabViewController** - handles the PAP drills tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentView`
- `showSignOffView`
- `showEmailReportView`
- `showEditDetailsView`
- `showChecklistView`
- `showActionsView`<br/></br>##### **WHSPAPLegislationsSearchResultsViewController** - handles the search results in the PAP Legislations section

###### **Methods and Calculated Variables**
- `showTabView`<br/></br>##### **WHSPAPLegislationsSearchViewController** - handles the searching in the PAP Legislations section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSPAPPlansProceduresTabViewController** - handles the PAP plans procedures tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentView`
- `showEmailReportView`
- `showEditDetailsView`
- `showSignOffView`
- `showChecklistView`
- `showEmergencyProcedureView`
- `showActionsView`<br/></br>##### **WHSPAPPlansSearchResultsViewController** - handles the search results in the PAP Plans section 

###### **Methods and Calculated Variables**
- `showTabView`<br/></br>##### **WHSPAPPlansSearchViewController** - handles the searching in the PAP Plans section 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSPAPSearchResultsViewController** - handles the search results in PAP

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSPAPSearchViewController** - handles the searching in pap

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showTypePickerView`
- `showSubTypePickerView`
- `showStatusPickerView`
- `showDatePickerWithIndexPath`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSPAPTrainingSearchResultsViewController** - handles the search results in the AP training section screen

###### **Methods and Calculated Variables**
- `showTabView`<br/></br>##### **WHSPAPTrainingTabViewController** - handles the pap training tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentView`
- `showEmailReportView`
- `showSignOffView`
- `showEditDetailsView`
- `showChecklistView`
- `showAttendeesView`
- `showActionsView`<br/></br>##### **WHSPAPTraningSearchViewController** - handles the searching in the AP training section

###### **Methods and Calculated Variables**
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSPDFAddSigneesViewController** - handles the PDF Add signees screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `didSelectUser`
- `didFinishSigningWithImage`
- `saveBarButtonItemDidTapped`
- `validToSave`
- `textViewDidChange`
- `showSignatureViewController`
- `initializeDataSource`
- `showPersonInvolvedTypeView`
- `refreshActionedByFields`<br/></br>##### **WHSPDFEditSigneeViewController** - handles the editing of the signee on a pdf

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSPDFSigneesViewController** - handles the showing of the PDF Signees screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewWillDisappear`
- `handleBack`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `openAddRecordView`
- `toggleSubmitButton`
- `submitSignatures`
- `submitSignoffWithIndex`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ editActionsForRowAtIndexPath`
- `initializeDataSource`
- `saveOnlineSignature`<br/></br>##### **WHSPDFViewController** - handles the pdf view

###### **Methods and Calculated Variables**
- `initWithCoder`
- `viewDidLoad`
- `viewDidAppear`
- `viewWillDisappear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `webView: Ã¢ÂÂ¦ decidePolicyForNavigationAction`
- `webView: Ã¢ÂÂ¦ didFinishNavigation`
- `mailComposeController: Ã¢ÂÂ¦ didFinishWithResult`
- `initializeNavigationBarButtonItems`
- `showFileNotFoundView`
- `showExperiencedErrorView`
- `showCantEmailView`
- `externalButtonDidTapped`
- `openPDFExternally`
- `emailPDF`
- `moreButtonTapped`
- `signOff`
- `deletePDF`
- `createJSON`
- `logPDF`
- `logPDFdelete`
- `downloadPDF`
- `fetchPDF`
- `directlyFetchPDF`
- `loadPDFFileToWebView`<br/></br>##### **WHSPointsRaisedViewController** - controls the points raised

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `swipeableTableViewCell: ... didTriggerRightUtilityButtonWithIndex`
- `swipeableTableViewCell: ... canSwipeToState`
- `deletePointsData`
- `initializeDataSource`
- `showEditPointsRaisedView`
- `cellRightUtitilityButtons`
- `openAddRecordView`<br/></br>##### **WHSPoliciesAddRecordViewController** - handles the adding of WHS policies records

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `saveDetailsData`
- `fetchAutoNum`
- `initializeDataSource`
- `createJSON`
- `showTypePickerView`
- `showSubTypePickerView`
- `showStatePickerView`
- `showDatePickerWithIndexPath`
- `showStatusPickerView`
- `showWebView`
- `showRelevantLegislationsPickerView`
- `showRelevantTrainingPickerView`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`
- `clearTypeData`<br/></br>##### **WHSPoliciesComplaintsAddRecordViewController** - handles the adding of policies complaints records

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchAutoNum`
- `fetchLocationAddress`
- `saveDetailsData`
- `initializeDataSource`
- `createJSON`
- `showTypePickerView`
- `showSubTypePickerView`
- `showStatePickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showDatePickerWithIndexPath`
- `showDateTimePickerWithIndexPath`
- `showStatusPickerView`
- `showRelevantPoliciesPickerView`
- `showRelevantLegislationsPickerView`
- `showRelevantTrainingPickerView`
- `showCompetenciesPickerView`
- `showInternalExternalPickerView`
- `showWorkerPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`
- `clearTypeData`
- `clearLocationTypeData`
<br/></br>##### **WHSPoliciesComplaintsEditRecordViewController** - handles the editing of policies complaints records

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSPoliciesComplaintsViewController** - handles the policies complaints

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchRecordsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSPoliciesDrillsAddRecordViewController** - handles the adding of policies drills records

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchAutoNum`
- `fetchLocationAddress`
- `saveDetailsData`
- `initializeDataSource`
- `createJSON`
- `showTypePickerView`
- `showSubTypePickerView`
- `showStatePickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showDatePickerWithIndexPath`
- `showDateTimePickerWithIndexPath`
- `showStatusPickerView`
- `showRelevantPoliciesPickerView`
- `showRelevantLegislationsPickerView`
- `showRelevantTrainingPickerView`
- `showCompetenciesPickerView`
- `showInternalExternalPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`
- `clearTypeData`
- `clearLocationTypeData`
<br/></br>##### **WHSPoliciesDrillsEditRecordViewController** - handles the editing of record in policies drills

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSPoliciesDrillsViewController** - controls the policies drills

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchRecordsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSPoliciesEditRecordViewController** - handles the editing of record in policies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSPoliciesLegislationsAddRecordViewController** - handles the adding of policies legislations records

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `saveDetailsData`
- `fetchAutoNum`
- `initializeDataSource`
- `createJSON`
- `showTypePickerView`
- `showSubTypePickerView`
- `showAuthorityPickerView`
- `showStatePickerView`
- `showApplicableStatePickerView`
- `showVerifiedStatePickerView`
- `showDatePickerWithIndexPath`
- `showStatusPickerView`
- `showRelevantPoliciesPickerView`
- `showRelevantTrainingPickerView`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`
- `clearTypeData`<br/></br>##### **WHSPoliciesLegislationsEditRecordViewController** - handles the editing of record in the policies legislations

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPat`
- `fetchDetailsData`
- `initializeDataSource`
- `getApplicableStates`
- `getApplicableStatesIDs`
- `getVerifiedStates`
- `getVerifiedStatesIDs`<br/></br>##### **WHSPoliciesLegislationsViewController** - controls the policies legislations

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchRecordsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSPoliciesPlansAddRecordViewController** - handles the adding of record in policies plans

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveDate`
- `connectionDidFinishLoadin`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchLocationAddress`
- `saveDetailsData `
- `fetchAutoNum`
- `initializeDataSource`
- `createJSON`
- `showTypePickerView`
- `showSubTypePickerView`
- `showStatePickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showDatePickerWithIndexPath`
- `showStatusPickerView`
- `showRelevantPoliciesPickerView`
- `showRelevantLegislationsPickerView`
- `showRelevantTrainingPickerView`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`
- `clearTypeData`
- `clearLocationTypeData`<br/></br>##### **WHSPoliciesPlansEditRecordViewController** - handles the editing of record in policies plans

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSPoliciesPlansViewController** - controls the policies plans

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchRecordsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSPoliciesProceduresViewController** - handles the procedures in policies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `showPoliciesView`
- `showPlansAndProceduresView`
- `showLegislationsView`
- `showTrainingView`
- `showDrillView`
- `showComplaintsView`<br/></br>##### **WHSPoliciesSearchResultsViewController** - handles the display of search results for policies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showTabView`<br/></br>##### **WHSPoliciesSearchViewController** - handles the searching of policies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSPoliciesTabViewController** - handles the policies tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showSignOffView`
- `showEmailReportView`
- `showEditDetailsView`
- `showActionsView`<br/></br>##### **WHSPoliciesTrainingAddRecordViewController** - handles the WHS adding of policies training records

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchAutoNum`
- `fetchLocationAddress`
- `saveDetailsData`
- `initializeDataSource`
- `createJSON`
- `showTypePickerView`
- `showSubTypePickerView`
- `showStatePickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showDatePickerWithIndexPath`
- `showDateTimePickerWithIndexPath`
- `showStatusPickerView`
- `showRelevantPoliciesPickerView`
- `showRelevantLegislationsPickerView`
- `showCompetenciesPickerView`
- `showInternalExternalPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`
- `clearTypeData`
- `clearLocationTypeData`<br/></br>##### **WHSPoliciesTrainingEditRecordViewController** - handles the editing of record in policies training

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`
- `getInternalExternal`<br/></br>##### **WHSPoliciesTrainingViewController** - controls the policies training

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchRecordsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSPoliciesViewController** - controls the policies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchRecordsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSProductDetailsViewController** - handles the display of product details

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSProjectPickerViewController** - handles the project picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddProjectView`
- `openAddRecordView`<br/></br>##### **WHSRecordViewController** - handles showing of the Record screen

###### **Methods and Calculated Variables**
- `initWithCoder`
- `viewDidLoad`
- `viewWillLayoutSubviews`
- `initializeTableViewPlaceholder`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `scrollViewDidEndDragging: ... willDecelerate`
- `searchBarShouldBeginEditing`
- `searchBarTextDidBeginEditing`
- `searchBar: ... textDidChange`
- `searchBarSearchButtonClicked`
- `searchBarCancelButtonClicked`
- `fetchRecords`
- `fetchPDF`
- `fetchNextPage`
- `updateDataSource`
- `initializePDFBarButtonItem`
- `initializePDFBarButtonItem`
- `initializeMoreOptionsBarButtonItem`
- `presentMoreOptionsActionSheet`
- `initializeAddRecord`
- `showNoPermissionPlaceholder`
- `showSearchBar`
- `hideSearchBar`
- `showSearchView`
- `openPDFView`
- `openAddRecordView`
- `moreOptionsBarButtonItemDidTapped`
- `searchItem`<br/></br>##### **WHSRegisterActionDetailsViewController** - handles the action details in register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`
- `fetchActionDetails`<br/></br>##### **WHSRegisterActionManagerViewController** - handles the action manager of the register

###### **Methods and Calculated Variables**
- `tablePickerDidFinishedPicking: ... dataPicked`
- `createInData`
- `transferActionData`<br/></br>##### **WHSRegisterActionsViewController** - handles the actions of the register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `reloadViewFromSavedAction`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `registerActionDidSaved: ... responseData`
- `registerActionSavingDidFailed: ... responseData`
- `fetchActionsData`
- `initializeDataSource`
- `showEditRecordView`
- `openAddRecordView`<br/></br>##### **WHSRegisterAddActionViewController** - handles the adding of action in the register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `saveActionButtonDidTapped`
- `cellSwitchDidValueChanged`<br/></br>##### **WHSRegisterAddActionsViewController** - handles the adding of actions in the register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchFlexibleForm`
- `fetchAutoNum`
- `saveAction`
- `initializeDataSource`
- `showActionTypePicker`
- `showActionCategoryPickerView`
- `showGenericPickerViewWithTitle: ... recordType: ... dataReturnedKey`
- `showWorkerPickerView: ... isNotification`
- `showNotificationReceiverPickerView`
- `showSaveSucceedAlertView`
- `showSaveFailedAlertView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `createJSON`<br/></br>##### **WHSRegisterAddServiceTypeViewController** - handles the adding of service type in the register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveServiceTypeData`
- `initializeDataSource`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSRegisterAddTestTypeViewController** - handles the adding of test type in the register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `saveTestTypeData`
- `initializeDataSource`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSRegisterEditActionDetailsViewController** - handles the editing of action details in the register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `saveActionButtonDidTapped`
- `cellSwitchDidValueChanged`<br/></br>##### **WHSRegisterEditActionsViewController** - handles the editing of actions in register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `fetchDetails`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchActionDetailsData`
- `initializeDataSource`
- `formatNotificationReceivers`<br/></br>##### **WHSRegisterEditServiceTypeViewController** - handles the editing of a service type in the Register section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSRegisterEditTestTypeViewController** - handles the editing of a test type in the Registers section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`<br/></br>##### **WHSRegisterServiceTypePickerViewController** - handles the picking of a service type in Registers section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddServiceTypeView`
- `showEditServiceTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSRegisterTestHistoryDetailsViewController** - handles the viewing of the details of the Register Test History

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `connectionDidFinishLoading`
- `processActionRecordCount`
- `initializeEditDetailsView`
- `showEditDetailsView`<br/></br>##### **WHSRegisterTestHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchTestHistories`
- `showTestHistoryDetailsView`<br/></br>##### **WHSRegisterTestTypePickerViewController** - handles the picking of a Register Test Type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddTestTypeView`
- `showEditTestTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSRegistersSearchViewController** - handles the searching in registers

###### **Methods and Calculated Variables**<br/></br>##### **WHSRegistersViewController** - handles the viewing of the Registers screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `didReceiveMemoryWarning`
- `prepareForSegue`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `showHazardsView`
- `showAssetsView`
- `showSafetyView`
- `showEnvironmentalView`
- `showChemicalsView`<br/></br>##### **WHSReportIncidentViewController** - handles the showing of the Report Incident Screen 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `download`
- `fetchOfflineConnection`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `handleFlexi`
- `connectionDidFinishLoading`
- `dateOnlyFormatFromDateString`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ viewForHeaderInSection`
- `sectionTapped`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchAutoNum`
- `fetchFlexibleForm`
- `fetchFlexibleFormWithPageID`
- `fetchProjectDetails`
- `fetchLocationAddress`
- `fetchNotificationSeverity`
- `fetchEmployeeDetails`
- `saveDetailsData`
- `uploadAttachment`
- `uploadAttachments`
- `initializeDataSource`
- `updateEmployeeData`
- `createJSON`
- `showTypePickerView`
- `showDatePickerWithIndexPath`
- `showDateTimePickerWithIndexPath`
- `showEmployeeContractorsCompanyPickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showPersonInvolvedTypeView`
- `refreshPersonInvolvedFields`
- `showWorkerPickerView`
- `showPersonPickerView`
- `showGenderPickerView`
- `showDivisionPickerView`
- `showDepartmentPickerView`
- `showJobTitlePickerView`
- `showOccupationPickerView`
- `showIndustryPickerView`
- `showEmploymentCategoryPickerView`
- `showContractorListPicker`
- `showPersonInvolvedPicker`
- `showConsequenceRankingPicker`
- `showPotentialOutcomePicker`
- `showNotificationSeverityPicker`
- `showNatureOfInjuryPicker`
- `showBodyPartsHarmedPicker`
- `showMechanismOfInjuryPicker`
- `showImmediateTreatmentPicker`
- `showHazardTypePicker`
- `showUploadOptions`
- `showDocumentPicker`
- `showImagePicker`
- `setAllowedUTIs`
- `documentPicker: Ã¢ÂÂ¦ didPickDocumentAtURL`
- `documentPickerWasCancelled`
- `refreshSelectedRow`
- `imagePickerController: Ã¢ÂÂ¦ didFinishPickingMediaWithInfo`
- `imagePickerControllerDidCancel`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `clearLocationTypeData`
- `clearDepartmentData`
- `cellIndexForField`<br/></br>##### **WHSRichTextEditorViewController** - handles the rich text editor

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue`<br/></br>##### **WHSRiskAssessmentActionDetailsViewController** - handles the action details in the risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `fetchActionDetails`
- `initializeDataSource`<br/></br>##### **WHSRiskAssessmentActionManagerViewController** - handles the action manager in the risk assessment

###### **Methods and Calculated Variables**
- `tablePickerDidFinishedPicking: ... dataPicked`
- `createInData`
- `isValidObjectForIndex`
- `transferActionData`
- `showActionControlMeasurePickerView`<br/></br>##### **WHSRiskAssessmentAddActionViewController** - handles the adding of action in the risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `cellSwitchDidValueChanged`
- `saveActionButtonDidTapped`<br/></br>##### **WHSRiskAssessmentEditActionDetailsViewController** - handles the editing of action details in risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `saveActionButtonDidTapped`
- `cellSwitchDidValueChanged`<br/></br>##### **WHSRiskAssessmentPicturesViewController** - handles the showing of pictures in the Risk Management section

###### **Methods and Calculated Variables**
- `collectionCellIdentifier`
- `initializeCollectionViews`
- `preferredCollectionViewFrame`
- `processPictures`
- `processHeadersAndDetails`<br/></br>##### **WHSRiskAssessmentViewController** - controls the risk assessment

###### **Methods and Calculated Variables**
- `initWithCoder`
- `viewDidLoad`
- `viewWillAppear`
- `viewWillDisappear`
- `prepareForSegue: ... sender`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `connection: ... willSendRequest`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `initializeMoreBarButtonItem`
- `initializePanel`
- `toggleMorePanelView`
- `showPanelView`
- `hidePanelView`
- `initializePanelDataSource`
- `fetchData`
- `fetchAttachmentCount`
- `fetchActionRecordCount`
- `editRecordButtonDidTapped`
- `viewPDFButtonDidTapped`
- `disableMoreButton`
- `disableEditRecord`
- `disableViewPDF`
- `disableAttachments`
- `disableEmailReport`
- `disableActions`<br/></br>##### **WHSRiskManagementAddActionViewController** - handles the adding of action in risk management

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView `
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `sendPOSTRequest`
- `initializeDataSource`
- `showCategoryPickerView`
- `showControlMeasurePickerView`
- `showStatusPickerView`
- `showPriorityPickerView`
- `showSendNotificationToPickerView`
- `showDatePickerWithTitle: ... view`
- `switchValueDidChanged`
- `saveBarButtonItemDidTapped`
- `clearControlMeasureData`
- `isAllRequiredDataFilledUp`
- `getRecipientIDs`
- `createPOSTJSON`<br/></br>##### **WHSRiskManagementEditActionViewController** - handles the editing of action in risk management

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchActionDetailsData`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`<br/></br>##### **WHSRiskManagementViewController** - handles the Risk Management screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `prepareForSegue`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `showChemicalRiskManagementView`
- `showNonChemicalRiskManagementView`
- `initializeDataSource`<br/></br>##### **WHSSafeWorkManagementSystemActionDetailsViewController** - handles the action details of safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`
- `fetchActionDetails`<br/></br>##### **WHSSafeWorkManagementSystemActionManagerViewController** - handles the action manager of safe work management system

###### **Methods and Calculated Variables**
- `tablePickerDidFinishedPicking: ... dataPicked`
- `createInData`
- `transferActionData`
- `showActionTaskPickerView`<br/></br>##### **WHSSafeWorkManagementSystemActivityViewController** - handles the activity in safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... viewForHeaderInSection`
- `sectionTapped`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `fetchActivityData`
- `initializeDataSource`<br/></br>##### **WHSSafeWorkManagementSystemAddActionViewController** -  handles the adding of action in safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `saveActionButtonDidTapped`
- `cellSwitchDidValueChanged`<br/></br>##### **WHSSafeWorkManagementSystemDetailViewController** - handles the detail in safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... viewForHeaderInSection`
- `sectionTapped`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSSafeWorkManagementSystemEditActionDetailsViewController** - handles the editing of action details in safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `saveActionButtonDidTapped`
- `cellSwitchDidValueChanged`<br/></br>##### **WHSSafeWorkManagementSystemSearchResultsViewController** - handles the search results in safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSSafeWorkManagementSystemSearchViewController** - handles the searching in safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `initializeDataSource`
- `showGenericPickerViewWithType`
- `showRecordTypePickerView`
- `showSearchResultsView`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSSafeWorkManagementSystemTabViewController** - handles the safe work management system tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showSignOffView`
- `showDetailsView`
- `showActivityView`
- `showTasksView`
- `showActionsView`<br/></br>##### **WHSSafeWorkManagementSystemTaskViewController** - handles the tasks in safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... viewForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForRowAtIndexPath`
- `fetchTasksData`
- `initializeDataSource`<br/></br>##### **WHSSafeWorkManagementSystemViewController** - controls the safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchSWMSListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showSearchView`
- `showTabView`<br/></br>##### **WHSSafeWorkProceduresActionViewController** - handles the actions in the Safe Work Procedures section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchNewControlsData`
- `showAddActionView`
- `showEditActionView`<br/></br>##### **WHSSafeWorkProceduresChecklistViewController** - handles the checklist in safe work procedures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `fetchChecklistData`
- `initializeDataSource`<br/></br>##### **WHSSafeWorkProceduresDetailViewController** - handles the details in safe work procedures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... viewForHeaderInSection`
- `sectionTapped`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSSafeWorkProceduresListViewController** handles the showing of the list of safe work procedures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `fetchSWPData`
- `initializeDataSource`<br/></br>##### **WHSSafeWorkProceduresSearchResultsViewController** - handles the search results in safe work procedures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSSafeWorkProceduresSearchViewController** - handles the searching in safe work procedures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showStatusPickerView`
- `showDatePicker`
- `showSearchResultsView`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSSafeWorkProceduresTabViewController** - handles the safe work procedures tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showSignOffView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showSWPView`
- `showChecklistView`
- `showActionsView`<br/></br>##### **WHSSafeWorkProceduresViewController** - shows share work procedures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAt`
- `fetchSWPListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showSearchView`
- `showTabView`<br/></br>##### **WHSSafetyAddDetailsViewController** - handles the adding of details in safety

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchLocationAddressData`
- `fetchAutoNum`
- `saveRecordData`
- `initializeDataSource`
- `createJSON`
- `showSubTypePickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showDatePickerWithIndexPath`
- `showFireFightingClassPickerView`
- `showFireFightingRatingPickerView`
- `showStatusPickerView`
- `showCompetenciesPickerView`
- `showTestingFrequencyPickerView`
- `showServicingFrequencyPickerView`
- `showWorkerPickerView`
- `showRelevantPoliciesPickerView`
- `showRelevantProceduresPickerView`
- `showRelevantLegislationsPickeriew`
- `showRelevantTrainingPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `clearSubTypeData`
- `clearLocationData`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSSafetyAddTestHistoryViewController** - handles the adding of test history in safety

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: ... didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath `
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `switchCellValueDidChanged`
- `acSheet: ... clickedButtonAtIndex`
- `fetchAutoNum`
- `saveTestHistoryData`
- `initializeDataSource`
- `createJSON`
- `showTestTypePickerView`
- `showWorkerPicker`
- `showDatePickerWithIndexPath`
- `showStatusPickerView`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSSafetyEditDetailsViewController** - handles the editing of details in safety

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsDat`
- `initializeDataSource`<br/></br>##### **WHSSafetyEditServiceHistoryViewController** - handles the editing of service history in safety

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `registerActionDidSaved: ... responseData`
- `registerActionSavingDidFailed: ... responseData`
- `fetchServiceHistoryDetailsData`
- `initializeDataSource`
- `showServiceHistoryActions`
- `showAttachmentsView`<br/></br>##### **WHSSafetyEditTestHistoryViewController** - handles the editing of test history in safety

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `registerActionDidSaved: ... responseData`
- `registerActionSavingDidFailed: ... responseData`
- `fetchTestHistoryDetailsData`
- `initializeDataSource`
- `showTestHistoryActions`
- `showAttachmentsView`<br/></br>##### **WHSSafetyEmergencyWashingAddDetailsViewController** - handles the adding go details in the safety emergency washing section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetyEmergencyWashingAddTestHistoryViewController** - handles the adding of test history in the safety emergency washing section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetyEmergencyWashingEditDetailsViewController** - handles the editing of the details in the safety emergency washing section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
<br/></br>##### **WHSSafetyEmergencyWashingEditTestHistoryViewController** - handles the editing of the history of safety emergency washing section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetyEmergencyWashingSearchResultsViewController** - handles the search results in the safety emergency washing section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSSafetyEmergencyWashingSearchViewController** - handles searching in safety emergency washing 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSSafetyEmergencyWashingTabViewController** - logic for the safety emergency washing tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`<br/></br>##### **WHSSafetyEmergencyWashingViewController** shows safety emergency washing screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchEmergencyWashingListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openPDFView`
- `openAddRecordView`<br/></br>##### **WHSSafetyFireDetectionAddDetailsViewController** - handles the adding of details in the Safety Fire Detection section section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFireDetectionAddTestHistoryViewController** - handles the adding of a test history in the Safety Fire Detection section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFireDetectionEditDetailsViewController** - handles the editing of the details in the Safety Fire Detection section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFireDetectionEditTestHistoryViewController** - handles the editing of a test history in the Safety Fire Detection section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFireDetectionSearchResultsViewController** - handles the search results in the Safety Fire Detection section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSSafetyFireDetectionSearchViewController** - handles the search function in the Safety Fire Detection section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSSafetyFireDetectionTabViewController** - handles the Safety fore detection screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`<br/></br>##### **WHSSafetyFireDetectionViewController** - handles the display of the Safety Fire Detection screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchFireDetectionListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openPDFView`
- `openAddRecordView`<br/></br>##### **WHSSafetyFireFightingAddDetailsViewController** - shows the add details screen in the safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFireFightingAddTestHistoryViewController** -shows the add test history screen in the safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFireFightingEditDetailsViewController** - shows the edit details screen in the safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFireFightingEditTestHistoryViewController** - shows edit test history screen in safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFireFightingSearchResultsViewController** - shows the search results screen in the safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSSafetyFireFightingSearchViewController** - shows the search screen in safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`
<br/></br>##### **WHSSafetyFireFightingTabViewController** - logic behind safety fire fighting tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`<br/></br>##### **WHSSafetyFireFightingViewController** - shows safety fire fighting scree

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchFireFightingEquipmentListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSSafetyFirstAidAddDetailsViewController** - handles the adding of details in the Safety First Aid section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFirstAidAddTestHistoryViewController** - handles the adding of a test history in the Safety First Aid section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
<br/></br>##### **WHSSafetyFirstAidEditDetailsViewController** - handles the editing  of details in safety first aid

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFirstAidEditTestHistoryViewController** - handles the editing of test history in safety first aid

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSSafetyFirstAidSearchResultsViewController** - handles the search results in safety first aid

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSSafetyFirstAidSearchViewController** - handles searching in safety first aid

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSSafetyFirstAidTabViewController** - handles the safety first aid tab 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`<br/></br>##### **WHSSafetyFirstAidViewController** - controls the safety first aid

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchFirstAidKitListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSSafetyPPEAddDetailsViewController** - handles adding details in Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`

<br/></br>##### **WHSSafetyPPEAddEmployeeViewController** - handles the adding of employee in safety ppe

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: ... dataPicked`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath `
- `tableView: ... didSelectRowAtIndexPath`
- `textView: ... shouldChangeTextInRange: ... replacementText`
- `textViewDidChange`
- `acSheet: ... clickedButtonAtIndex`
- `fetchLocationAddressData`
- `saveEmployeeDetailsData`
- `initializeDataSource`
- `createJSON`
- `showWorkerPicker`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showStatusPickerView`
- `showDatePickerWithIndexPath`
- `saveBarButtonItemDidTapped`
- `clearLocationData`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSSafetyPPEAddTestHistoryViewController** - handles adding test history of Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetyPPEEditDetailsViewController** - handles the editing of details in safety ppe

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`<br/></br>##### **WHSSafetyPPEEditEmployeeViewController** - handles the editing of employee in safety ppe

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `registerActionDidSaved: ... responseData`
- `registerActionSavingDidFailed: ... responseData`
- `testHistoryDidSaved: ... responseData`
- `testHistorySavingDidFailed: ... responseData`
- `serviceHistoryDidSaved: ... responseData`
- `serviceHistorySavingDidFailed: ... responseData`
- `fetchEmployeeDetailsData`
- `initializeDataSource`
- `showEmployeeActionsView`
- `showEmployeeTestHistoryView`
- `showEmployeeServiceHistoryView`<br/></br>##### **WHSSafetyPPEEditTestHistoryViewController** - handles editing the test history of Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetyPPEEmployeeViewController** - handles employee view of Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchEmployees`
- `showEditPPEDetailsView`
- `openAddRecordView`<br/></br>##### **WHSSafetyPPESearchResultsViewController** - handles the search results of Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSSafetyPPESearchViewController** - handles searching of Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSSafetyPPETabViewController** - handles the safety ppe tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: ... clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showEmployeeView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`<br/></br>##### **WHSSafetyPPEViewController** - handles the safety ppe

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchPPEListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSSafetyServiceHistoryViewController** - handles the display of Safety Service History 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchServiceHistories`
- `showEditServiceHistoryDetailsView`
- `openAddRecordView`<br/></br>##### **WHSSafetySpillKitAddDetailsViewController** - shows add details screen in safety spill kit section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetySpillKitAddTestHistoryViewController** - shows ad test history screen in safety spill kit section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetySpillKitEditDetailsViewController** - shows edit details screen of safety spill kit section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`<br/></br>##### **WHSSafetySpillKitEditTestHistoryViewController** - shows edit test history screen in safety spill kit section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
<br/></br>##### **WHSSafetySpillKitSearchResultsViewController** - shows safety spill kit search results

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSSafetySpillKitSearchViewController** - shows safety spill kit search

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSSafetySpillKitTabViewController** - logic for safety spill kit tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`<br/></br>##### **WHSSafetySpillKitViewController** - shows safety spill kit view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchSpillKitListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`<br/></br>##### **WHSSafetyTabViewController** - handles the showing of the Safety view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `initializeDataSource`
- `disableEmployeeView`
- `showDetailsView`
- `showEmployeeView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`
- `showPDFView`
- `showAttachmentView`<br/></br>##### **WHSSafetyTestHistoryViewController** - handles the showing of the history in the Safety Test section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `fetchTestHistories`
- `showTestHistoryDetailsView`
- `showEditTestHistoryDetailsView`
- `openAddRecordView`
<br/></br>##### **WHSSafetyViewController** - controls the safety

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `showFireFightingEquipmentView`
- `showEmergencyWashingView`
- `showFireDetectionView`
- `showFirstAidKitView`
- `showSpillKitView`
- `showPPEView`<br/></br>##### **WHSSearchRecordViewController** - shows search record view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeSearchBarButtonItem`
- `searchBarButtonItemDidTapped`
- `showSearchResultsViewWithDataList`<br/></br>##### **WHSSearchResultsRecordViewController** - logic behind the search results record screen

###### **Methods and Calculated Variables**
- `searchRecords`<br/></br>##### **WHSSearchViewController** - logic behind the search screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `initializeSearchBarButtonItem`
- `showDatePicker`
- `searchBarButtonItemDidTapped`
- `formatPickedItems`<br/></br>##### **WHSSettingViewController** - handles and shows the Settings screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewWillDisappear`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `mailComposeController: ... didFinishWithResult`
- `showCantEmailView`
- `logoutButtonDidTapped`
- `emailButtonDidTapped`
- `callButtonDidTapped`
- `switchValueDidChanged`<br/></br>##### **WHSSideMenuViewController** - the logic behind the Side Manu of the app

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeSideMenuItems`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `selectMenuCell`
- `fetchedMenuDataDidProcessed`
- `initializeDataSource`
- `updateButtonSettingsView`
- `goBackToHome`
- `homeButtonDidTapped`
- `riskManagementButtonDidTapped`
- `registersButtonDidTapped`
- `policiesAndProceduresButtonDidTapped`
- `incidentReportingButtonDidTapped`
- `auditAndInspectionsButtonDidTapped`
- `dynamicTemplatesButtonDidTapped`
- `settingsButtonDidTapped`
- `actionMonitorButtonDidTapped`
- `offlineDocumentsButtonDidTapped`
- `localFormsButtonTapped`<br/></br>##### **WHSSiteRAControlsViewController** - handles the Controls screen of the Site RA section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `fetchControlCategoriesData`
- `fetchCurrentControlsData`
- `saveRecordData`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `textViewDidChange`
- `initializeDataSource`
- `initializeAddRecord`
- `openAddRecordView`<br/></br>##### **WHSSiteRAHazardsAddHazardViewController** - handles the adding of a hazard in the Site RA Hazards section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `saveHazardData`
- `initializeDataSource`
- `createJSON`
- `showHazardTypePickerView`
- `showHazardSubTypePickerView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `clearHazardData`<br/></br>##### **WHSSiteRAHazardsViewController** - handles the Hazards screen in the Site RA section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `initializeAddRecord`
- `openAddRecordView`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `fetchDetailsHazardTemplateID`
- `fetchTemplateName`
- `fetchHazards`
- `saveRecordData`
- `tablePickerDidFinishedPicking`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `switchCellValueDidChanged`
- `createJSON`
- `showHazardTemplatePicker`
- `textFieldDidChange`
- `saveBarButtonItemDidTapped`
- `initializeDataSource`
- `updateTemplateCell`
- `updateHazardSection`<br/></br>##### **WHSSiteRARiskDetailViewController** - handles the risk detail of the Site RA section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ viewForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `textView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `textView: Ã¢ÂÂ¦ heightForFooterInSection`
- `textView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `fetchDetailsData`
- `createJSON`
- `showHazardTypePickerView`
- `showHazardSubTypePickerView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `saveRecordData`
- `initializeDataSource`
- `clearHazardData`<br/></br>##### **WHSSiteRARisksAddControlViewController** - logic for the screen that shows add risk control in site risk assessment view controller

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `tablePickerDidFinishedPicking: Ã¢ÂÂ¦ dataPicked`
- `searchBar: Ã¢ÂÂ¦ textDidChange`
- `searchBarSearchButtonClicked`
- `fetchControlsList`
- `saveRecordData`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `switchCellValueDidChanged`
- `showControlCategories`
- `initializeDataSource`
- `updateControlsList`
- `filterListBySearchText`
- `initializeAddBarButtonItem`
- `showAddActionView`
- `showEditActionView`
- `addBarButtonItemDidTapped`<br/></br>##### **WHSSiteRARisksRatingViewController** - handles the risk rating screen of the Site RA section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `tableView: Ã¢ÂÂ¦ heightForFooterInSection`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `fetchDetailsData`
- `fetchUserCustomRM`
- `refreshRecommendedRisk`
- `saveRecordData`
- `createJSON`
- `showTablePickerWithListKey`
- `showFrequencyOfExposure`
- `showPossibilityOfExposure`
- `showPotentialImpactLevel`
- `showRiskSignificance`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `initializeStaticFields`
- `initializeCustomFields`<br/></br>##### **WHSSiteRARisksTabViewController** - logic for the screen that shows the table view of risks in the site risks assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReport`
- `showActionsView`
- `showDetailsView`
- `showControlsView`
- `showRatingsView`<br/></br>##### **WHSSiteRARisksViewController** - logic behind the screen that shows the risks in the site risk assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchSiteRARisksListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `openAddRecordView`
- `showSearchView`
- `showPDFView`
- `showEmailReportView`
- `showTabView`<br/></br>##### **WHSSiteRiskAsessmentSearchResultsViewController** - handles the search results of the Site Risk Assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `prepareForSegue`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`<br/></br>##### **WHSSiteRiskAssessmentAddRecordViewController** - logic behind the site risk assessment record screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: Ã¢ÂÂ¦ dataPicked`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ titleForHeaderInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchAutoNum`
- `fetchLocationAddressData`
- `fetchWorkerPhone`
- `saveRecordData`
- `initializeDataSource`
- `clearTypeData`
- `clearLocationTypeData`
- `createJSON`
- `showProjectPickerView`
- `showInspectionTypePickerView`
- `showInspectionSubTypePickerView`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showStatusPickerView`
- `showDatePickerWithIndexPath`
- `showWorkerPickerView`
- `showDateTimePickerWithIndexPath`
- `showRelevantPoliciesPickerView`
- `showRelevantLegislationsPickeriew`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `isAllRequiredDataFilledUp`<br/></br>##### **WHSSiteRiskAssessmentEditRecordViewController** - logic for site risk assessment edit record screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`<br/></br>##### **WHSSiteRiskAssessmentSearchViewController** - logic for site risk assessment search screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: Ã¢ÂÂ¦ dataPicked`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showGenericPickerViewWithType`
- `showLocationPickerView`
- `showStatusPickerView`
- `showSearchResultsView`
- `searchBarButtonItemDidTapped`<br/></br>##### **WHSSiteRiskAssessmentTabViewController** - logic for site risk assessment tab view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReport`
- `showActionsView`
- `showDetailsView`
- `showHazardsView`
- `showRisksView`<br/></br>##### **WHSSiteRiskAssessmentViewController** - logic for site risk assessment screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `fetchRiskAssessmentsListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `openAddRecordView`
- `showSearchView`
- `showPDFView`
- `showEmailReportView`
- `showTabView`<br/></br>##### **WHSSplitViewController** - logic behind split screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `supportedInterfaceOrientations`<br/></br>##### **WHSStartAuditViewController** - controls the view for start audit screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `fetchFlexibleFormWithPageID`
- `fetchOfflineConnection`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `fetchAutoNum`
- `fetchLocationAddress`
- `handleFlexi`
- `handleAutoNumData`
- `clearLocationTypeData`
- `tablePickerDidFinishedPicking: Ã¢ÂÂ¦ dataPicked`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `numberOfSectionsInTableView`
- `tableView: Ã¢ÂÂ¦ numberOfRowsInSection`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForHeaderInSection`
- `textView: Ã¢ÂÂ¦ shouldChangeTextInRange`
- `textViewDidChange`
- `showDateTimePickerWithIndexPath`
- `showLocationTypePickerView`
- `showLocationPickerView`
- `showWorkerPickerView`
- `showDivisionPickerView`
- `showDepartmentPickerView`
- `showUploadOptions`
- `showDocumentPicker`
- `showImagePicker`
- `setAllowedUTIs`
- `documentPicker: Ã¢ÂÂ¦ didPickDocumentAtURL`
- `documentPickerWasCancelled`
- `refreshSelectedRow`
- `imagePickerController: Ã¢ÂÂ¦ didFinishPickingMediaWithInfo`
- `imagePickerControllerDidCancel`
- `doneBarButtonItemDidTapped`
- `uploadAttachment`
- `clearDepartmentData`
- `cellIndexForField`<br/></br>##### **WHSStartupViewController** - shows the start up screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `finishedValidatingUserCredentials`
- `prepareForSegue`
- `unwindToWHSStartupView`
- `isAnExistingUserLoggedIn`<br/></br>##### **WHSTabViewController** - controls the tab view of the app

###### **Methods and Calculated Variables**
- `processTabFlags`
- `fetchValidTabs`
- `viewWillAppear`
- `initializeMoreOptionsBarButtonItem`
- `presentMoreOptionsActionSheet`
- `moreOptionsBarButtonItemDidTapped`<br/></br>##### **WHSTablePickerViewController** - logic behind table picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchOffline`
- `tableView: Ã¢ÂÂ¦ cellForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ estimatedHeightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ heightForRowAtIndexPath`
- `tableView: Ã¢ÂÂ¦ didSelectRowAtIndexPath`
- `searchBarShouldBeginEditing`
- `searchBarCancelButtonClicked`
- `initializeDataSource`
- `initializeDonePickingBarButtonItem`
- `initializePickerTitle`
- `updateEditBarButtonItemState`
- `initializeEditRecord`
- `showNoReferenceFetched`
- `donePickingBarButtonItemDidTapped`
- `editBarButtonItemDidTapped`
- `deselectAllRows`<br/></br>##### **WHSTemplatePickerViewController** - logic for template picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddTemplateView`
- `showEditTemplateView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>##### **WHSUtilitiesViewController** - shows the utilities

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `mailComposeController: Ã¢ÂÂ¦ didFinishWithResult`
- `callNumber`
- `sendEmail`
- `sendEmail: Ã¢ÂÂ¦ delegate`
- `openWebsite`<br/></br>##### **WHSViewController** - superclass of view controllers

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewWillDisappear`
- `didReceiveMemoryWarning`
- `supportedInterfaceOrientations`
- `connection: Ã¢ÂÂ¦ willSendRequest`
- `connection: Ã¢ÂÂ¦ didReceiveResponse`
- `connection: Ã¢ÂÂ¦ didReceiveData`
- `connectionDidFinishLoading`
- `connection: Ã¢ÂÂ¦ didFailWithError`
- `clearUserData`
- `getActionsList`
- `parseActionList`
- `hamburgerBarButtonDidTapped`
- `acSheet: Ã¢ÂÂ¦ clickedButtonAtIndex`
- `initializeNavigationBarTintColor`
- `initializeNavigationBarWithTintColor`
- `initializeNavigationTitle`
- `initializeHamburger`
- `showNoInternetConnectionView`
- `showIncompleteDataView`
- `showMessageWithTitle`
- `showMessageWithTitleWithCompletion`
- `addRightBarButtonItem`
- `pushViewControllerWithBackButton`
- `getMimeTypeForPath`
- `goBackToHomeIfNoAccess`
- `alertIfNoAccess`
- `sendRequest`
- `sendPOSTRequest`
- `postURLConnectionDidFinishLoading`
- `attributedStringAfterHTMLTagsRemovalFromString`
- `stringAfterHTMLTagsBruteRemovalFromString`
- `stringAfterRemovingBreaklineTags`
- `stringByStrippingHTML`
- `stringsSeparatedByComma`
- `showProgressHUD`
- `hideProgressHUD`
- `getModuleAccessTypeWithID`
- `getModuleAccessTypeWithMenuItem`
- `moduleStateForAccessTypeString`<br/></br>##### **WHSWebViewController** - controls web views

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `prepareWebView`
- `loadHTMLString: Ã¢ÂÂ¦ baseURL`<br/></br>##### **WHSWorkerTablePickerViewController** - shows the workers 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddWorkerView`
- `showEditWorker`
- `openAddRecordView`
- `editBarButtonItemDidTapped`<br/></br>