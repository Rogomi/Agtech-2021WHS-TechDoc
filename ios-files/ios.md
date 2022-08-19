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
  

##### **AIMandatoryTableViewController** - handles AI Mandatory screen

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


##### **AISelectTemplateViewController** - handles the selection of the Risk Template

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `toggleTopFive`
- `fetchTemplate`
- `numberOfSections(in tableView...)`
- `tableView(...didSelectRowAt)`
- `fetchFields`
- `organizeFields`

##### **DynamicFormTableViewController** - is a dynamic table view that can be used in different forms such as start audit

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


##### **GenericTableViewController** - handles generic table view types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`


##### **MyStorageAddNewWorkerViewController** - handles the adding of new workers in my storage

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
- `validateEnteredName`

##### **MyStorageCompatibilityViewControllerr** - handles the storage compatibility view

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


##### **MyStorageESQAddBatchViewController** - handles the batch adding in my storage edit stored quantity

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
- `showSamplePOST`

##### **MyStorageESQAddPackSizeViewController** - handles the adding of pack size in my storage ESQ

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


##### **MyStorageESQAddSuppliersViewController** - handles the adding of suppliers in my storage

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
- `trimLeadingTrailingWhiteSpace`

##### **MyStorageESQAddUnitSizesViewController** - handles the adding of unit sizes in my storage ESQ

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
- `trimLeadingTrailingWhitespace`

##### **MyStorageESQBatchDetailsViewController** - handles the display of batch details for my storage ESQ

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
- `getID: ... arrayList: ... index`

##### **MyStorageESQInputValueViewController** - handles the input values for my storage ESQ

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
- `textFieldHiddenReceiverTextDidChange`

##### **MyStorageEditStoredQuantityViewController** - handles the editing of stored quantities in my storage

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


##### **MyStorageManifestViewController** - handles the my storage manifest

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



##### **MyStorageSummaryViewController** - handles the summary display of my storage

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
- `fetchSummary`

##### **NewDynamicTemplateViewController** - is a dynamic template used in different views such as the side menu

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
- `tablePickerDidFinishedPicking: ... dataPicked`

##### **SignOffTableViewController** - handles the view of signing off of items

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
- `allowedToSign`

##### **SignatureViewController** - handles the view that allows the user to write signatures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `didReceiveMemoryWarning`
- `positionForBar`
- `supportedInterfaceOrientations`
- `shouldAutorotate`
- `clearSignature`
- `doneSigning`

##### **SubmittedByTableViewController** - handles the view that displays submitted by

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
- `connectionDidFinishLoading`

##### **WHSSafetyAddServiceHistoryViewController** - handles the adding of service history in safety

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
- `isAllRequiredDataFilledUp`

WHS2MenuViewController
viewDidLoad
prepare(for segue: UIStoryboardSegue, sender: Any?)


##### **WHS2RecordViewController** - handles the display of Record screen

###### **Methods and Calculated Variables**
- `viewDidLoad`



##### **WHSAIAddPointsRaisedViewController** - handles the adding of points raised in audit and inspections

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
- `createJSON`

##### **WHSAIAddRecordViewController** - handles the adding of records in audit and inspections

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
- `isAllRequiredDataFilledUp`

##### **WHSAIEditPointsRaisedViewController** - handles the editing of points raised in audit and inspections

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


##### **WHSAIEditRecordViewController** - handles the editing of records in audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSAIInspectionTypePickerViewController** - handles the inspection type picker in audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddInspectionTypeView`
- `showEditInspectionTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSAIPointsRaisedViewController** - handles the display of points raised view in audit and inspections

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
- `openAddRecordView`

##### **WHSAISearchResultsViewController** - handles the search results of audit and inspections

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
- `showTabView`

##### **WHSAISearchViewController** - handles the searching of audit and inspections

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
- `searchBarButtonItemDidTapped`

##### **WHSAISplittedViewController** - handles the split view of audit and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: â¦ heightForRowAtIndexPath`
- `initializeDataSource`
- `tableView: â¦ didSelectRowAtIndexPath`

##### **WHSAITabViewController** - handles the audit and inspections tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showTasksObservedView`
- `showChecklistView`
- `showPointsRaisedView`
- `showActionsView`

##### **WHSActionCategoryPickerViewController** - handles the action category picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddActionCategoryView`
- `showEditActionCategoryView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSActionDetails ManagerViewController** - handles the managing of action details

###### **Methods and Calculated Variables**
- `initializeDataSource`

##### **WHSActionManagerViewController** - handles the manager for actions

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
- `postURLConnectionDidFinished`

##### **WHSActionViewController** - handles the display of the action view

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
- `initializeDataSource`

##### **WHSActionsMonitorRecordViewController** - handles the display of action monitor records

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


##### **WHSActionsMonitorSearchResultsViewController** - handles the search results of actions monitor

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
- `showEditActionView

##### **WHSActionsMonitorSearchViewController** - handles the searching of actions monitor

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
- `searchBarButtonItemDidTapped`

##### **WHSAddAIInspectionSubTypeViewController** - handles the adding of inspection sub types in audit and inspections

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
- `createJSON`

##### **WHSAddAIInspectionTypeViewController** - handles the adding of inspection types in audit and inspections

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

##### **WHSAddActionCategoryViewController** - handles the adding of categories in actions

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
- `createJSON`

##### **WHSAddAssetSubTypeViewController** - handles the adding of asset sub types

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

##### **WHSAddAssetTypeViewController** - handles the adding of asset types

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

##### **WHSAddAtmosphericMonitoringTypeViewController** - handles the adding of atmospheric monitoring types

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
- `isAllRequiredDataFilledUp`

##### **WHSAddAttachmentsViewController** - handles the adding of attachments

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
- `isAllRequiredDataFilledUp`

##### **WHSAddAttendeeViewController** - handles the adding of attendees

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
- `isAllRequiredDataFilledUp`

##### **WHSAddCompetenciesViewController** - handles the adding of competencies

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
- `isAllRequiredDataFilledUp`

##### **WHSAddControlMeasureViewController** - handles the adding of control measures

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
- `isAllRequiredDataFilledUp`

##### **WHSAddDynamicActionsViewController** - handles the adding of dynamic actions

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
- `createJSON`

##### **WHSAddEmployeeDepartmentViewController** - handles the adding of employee departments

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

##### **WHSAddEmployeeDivisionViewController** - handles the adding of employee divisions

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

##### **WHSAddGenericViewController** - handles the adding of generic views

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

##### **WHSAddInspectionTypeViewController** - handles the adding of inspection types

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
- `createJSON`

##### **WHSAddLicenceViewController** - handles the adding of licences

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
- `isAllRequiredDataFilledUp`

##### **WHSAddLocationViewController** - handles the adding of location

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
- `isAllRequiredDataFilledUp`

##### **WHSAddNoiseAssessmentSubTypeViewController** - handles the adding of noise assessment sub types

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


##### **WHSAddNoiseAssessmentTypeViewController** - handles the adding of noise assessment types

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

##### **WHSAddNotificationReceiverViewController** - handles the adding of notification receivers

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
- `createPOSTJSON`

##### **WHSAddPointsRaisedViewController** - handles the adding of points raised

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
- `createJSON`

##### **WHSAddRecordViewController** - implementation that handles the adding of records

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
- `getPreferredIndexPath`

##### **WHSAddWorkerViewController** - handles the adding of workers

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
- `isAllRequiredDataFilledUp`

##### **WHSAiInspectionSubTypePickerViewController** - handles the inspection sub type picker in audits and inspections

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddInspectionSubTypeView`
- `showEditInspectionSubTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSAssetSubTypePickerViewController** - handles the asset sub type picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddView`
- `showEditView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSAssetTypePickerViewController** - handles the picking of asset types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddView`
- `showEditView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSAssetsAddDetailsViewController** - handles the adding of details in assets

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
- `isAllRequiredDataFilledUp`

##### **WHSAssetsAddServiceHistoryViewController** - handles the adding of service history

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
- `isAllRequiredDataFilledUp`

##### **WHSAssetsAddTestHistoryViewController** - handles the adding of test history in assets

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


##### **WHSAssetsClassifiedAddDetailsViewController** - handles the adding of details in classified assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`

##### **WHSAssetsClassifiedEditDetailsViewController** - handles the editing of details in classified assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`

##### **WHSAssetsClassifiedSearchResultsViewController** - handles the search results of classified assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSAssetsClassifiedSearchViewController** - handles the searching of classified assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSAssetsClassifiedTabViewController** - handles the tab functions in classified assets

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
- `showActionsView`

##### **WHSAssetsClassifiedViewController** - handles the display of classified assets

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
- `openAddRecordView`

##### **WHSAssetsEditDetailsViewController** - handles the editing of details in assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSAssetsEditServiceHistoryViewController** - handles the editing of service history in assets

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
- `showAttachmentsView`

##### **WHSAssetsEditTestHistoryViewController** - handles the editing of test history in assets

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
- `showAttachmentsView`

##### **WHSAssetsElectricalAddDetailsViewController** - handles the adding of details in electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsElectricalAddServiceHistoryViewController** - handles the adding of service history in electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsElectricalEditDetailsViewController** - handles the editing of details in electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsElectricalEditServiceHistoryViewController** - handles the editing of service history in electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsElectricalSearchResultsViewController** - handles the search results for electrical assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSAssetsElectricalSearchViewController** - handles the electrical search

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList

##### **WHSAssetsElectricalTabViewController** - handles the electrical assets tab view

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
- `showActionsView`

##### **WHSAssetsElectricalViewController** - handles the display of electrical assets

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
- `openAddRecordView`

##### **WHSAssetsLiftingAddDetailsViewController** - handles the adding of details in lifting assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsLiftingEditDetailsViewController** - handles the editing of details in lifting assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsLiftingSearchResultsViewController** - handles the search results of lifting assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSAssetsLiftingSearchViewController** - handles the search of lifting assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSAssetsLiftingTabViewController** - handles the tab view for lifting assets

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
- `showActionsView`

##### **WHSAssetsLiftingViewController** - handles the display of lifting assets

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
- `openAddRecordView`

##### **WHSAssetsPlantAddDetailsViewController** - handles the adding of details in plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsPlantAddServiceHistoryViewController** - handles the adding of service history in plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`

##### **WHSAssetsPlantEditDetailsViewController** - handles the editing of details in plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsPlantEditServiceHistoryViewController** - handles the editing of service history in plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue: ... sender`

##### **WHSAssetsPlantSearchResultsViewController** - handles the search results of plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSAssetsPlantSearchViewController** - handles the searching of plant assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSAssetsPlantTabViewController** - handles the tab view for plant assets

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
- `showActionsView`

##### **WHSAssetsPlantViewController** - handles the display of plant assets

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
- `openAddRecordView`

##### **WHSAssetsSearchRecordResultsViewController** - handles the search record results for assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`

##### **WHSAssetsSearchRecordViewController** - handles the searching of records for assets

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
- `searchBarButtonItemDidTapped`

##### **WHSAssetsServiceHistoryViewController** - handles the display of service history for assets

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
- `openAddRecordView`

##### **WHSAssetsTestHistoryViewController** - handles the display of test history for assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `testHistoryDidSaved: ...responseData`
- `testHistorySavingDidFailed: ... responseData`
- `fetchTestHistories`
- `showTestHistoryDetailsView`
- `showTestHistoryEditDetailsView`
- `openAddRecordView`

##### **WHSAssetsVehiclesAddDetailsViewController** - handles the adding of details for vehicle assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsVehiclesEditDetailsViewController** - handles the editing of details for vehicle assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsVehiclesSearchRecordResultsViewController** - handles the search record results of vehicle assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSAssetsVehiclesSearchRecordViewController** - handles the searching of vehicle assets

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSAssetsVehiclesTabViewController** - handles the tab view for vehicle assets

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
- `showActionsView`

##### **WHSAssetsVehiclesViewController** - handles the display of vehicle assets

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
- `openAddRecordView`

##### **WHSAssetsViewController** - handles the display of assets

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
- `showClassifiedEquipmentView`

##### **WHSAtmosphericMonitoringAddMonitoringHistoryViewController** - handles the adding of monitoring history for atmospheric monitoring

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
- `isAllRequiredDataFilledUp`

##### **WHSAtmosphericMonitoringAddRecordViewController** - handles the adding of records for atmospheric monitoring

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
- `discardSelectedItemWithStringOfIDs`

##### **WHSAtmosphericMonitoringEditMonitoringHistoryViewController** - handles the editing of monitoring history for atmospheric monitoring

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchMonitoringHistoryDetailsData`
- `initializeDataSource`
- `showMonitoringHistoryActionsView`
- `showAttachmentsView`

##### **WHSAtmosphericMonitoringEditRecordViewController** - handles the editing of records for atmospheric monitoring

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSAtmosphericMonitoringHistoryViewController** - handles the display of monitoring history for atmospheric monitoring

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchMonitoringHistories`
- `showEditMonitoringHistoryViewController`
- `openAddRecordView`

##### **WHSAtmosphericMonitoringTabViewController** - handles the logic of the atmospheric monitoring section

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
- `showRegisterActionsView`

##### **WHSAtmosphericMonitoringTypePickerViewController** - handles the picking of an atmospheric monitoring type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddMonitoringTypeView`
- `showEditMonitoringTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSAttachmentsViewController** - handles the showing of attatchments

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `openAddRecordView`
- `showEditAttachmentsView`

##### **WHSAttendeesSearchResultsViewController** - handles the search results of atendees

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
- `showEditAttendeesDetailsView`

##### **WHSAttendeesSearchViewController** - handles the searching of Atendees

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
- `showSearchResultsViewWithDataList`

##### **WHSAttendeesViewController** - shows the Attendees

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchAttendeesData`
- `initializeDataSource`
- `showEditAttendeesDetailsView`
- `openAddRecordView`

##### **WHSAuditInspectionsDetailsViewController** - handles the showing of details in Audit Inspection

###### **Methods and Calculated Variables**


##### **WHSAuditInspectionsRecordViewController** - handles the recording of Audit Inspections

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
- `openAddRecordView`

##### **WHSAutoHazardViewController** - handles the Auto Hazard view

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
- `saveBarButtonItemDidTapped`

##### **WHSCauseHazardsViewController** - handles the Cause Hazards view

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
- `saveBarButtonItemDidTapped`

##### **WHSChangePasswordViewController** - handles changing of the password

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
- `handleChangePasswordResults`

##### **WHSChecklistViewController** - handles the Checklist view

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
- `showSectionPicker`

##### **WHSChemicalQChartChemicalSafetyViewController** - handles the Chemical Safety view of the ChemicalQ Chart section

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
- `processStorageLegends`

##### **WHSChemicalQChartDetailViewController** - shows the details view of the ChemicalQ Chart section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`

##### **WHSChemicalQChartDetailsViewController** - shows the details of the ChemicalQ Chart

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
- `getImageCellWithDequeuedCell: ... cellData`

##### **WHSChemicalQChartHazardsViewController** - shows the hazards view in the ChemicalQ Chart section

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
- `initializeCollectionViews`

##### **WHSChemicalQChartOperationalSafetyViewController** - handles the Operational Safety view in the ChemicalQ Chart section

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
- `getCellDataWithKey: ... titleKey: ... detailKey`

##### **WHSChemicalQChartSearchResultsViewController** - handles the search results in the ChemicalQ Chart section

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
- `showTabView`

##### **WHSChemicalQChartSearchViewController** - handles searching in the ChemicalQ Chart section

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
- `searchBarButtonItemDidTapped`

##### **WHSChemicalQChartTabViewController** - logic behind the ChemicalQ Chart tab

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
- `initializeDataSource`

##### **WHSChemicalQChartViewController** - shows the ChemicalQ Chart screen

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
- `showTabView``

##### **WHSChemicalRegisterProductDetailsViewController** - shows the product details in a Chemical Register 

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
- `reorderSanitizedJSON`

##### **WHSChemicalRegisterViewController** - shows the Chemical Register screen

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
- `qChartButtonDidTapped`

##### **WHSChemicalRiskAssessmentConsequencesViewController** - handles the showing of consequences in the Chemical Risk Assessment

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
- `initializeDataSource`

##### **WHSChemicalRiskAssessmentCurrentControlsViewController** - handles the current controls of a Chemical Risk Assessment

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
- `segregateCurrentControlsData`

##### **WHSChemicalRiskAssessmentDetailsViewController** - shows the details of a Chemical Risk Assessment

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
- `initializeDataSource`

##### **WHSChemicalRiskAssessmentHazardsConsequencesViewController** - handles the showing of the  hazards consequences screen in the chemical risk assessment section

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
- `initializeDataSource`

##### **WHSChemicalRiskAssessmentHazardsViewController** - handles the showing of the hazards screen in the chemical risk assessment section

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
- `initializeDataSource`

##### **WHSChemicalRiskAssessmentNewControlsViewController** - handles the showing of the new controls screen in the chemical risk assessment section

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
- `addBarButtonItemDidTapped`

##### **WHSChemicalRiskAssessmentProductExposureLimitsViewController** - handles the showing of the product exposure limits in the chemical risk assessment screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`

##### **WHSChemicalRiskAssessmentProductViewController** - handles the showing of a product in the chemical risk assessment section

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
- `showExposureLimitsView`

##### **WHSChemicalRiskAssessmentSearchResultsViewController** - handles the showing of the search results in the chemical risk assessment section

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
- `showTabView`

##### **WHSChemicalRiskAssessmentSearchViewController** - handles the search in the chemical risk assessment section

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
- `searchBarButtonItemDidTapped`

##### **WHSChemicalRiskAssessmentTabViewController** - handles the logic behind chemical risk assessment tab

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
- `processTabFlags`

##### **WHSChemicalRiskAssessmentViewController** - handles the showing of the chemical risk assessment screen

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
- `showTabView`

##### **WHSChemicalRiskManagementViewController** - handles the showing of the chemical risk management screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `showRiskAssessmentView`
- `showQChartView`

##### **WHSChemicalsViewController** - handles the showing of the chemicals screen

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
- `getStorageValueWithKey: ... index`

##### **WHSCompatibilityLegendsViewController** - handles the showing of the compatibility legends

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `cancelButtonDidTapped`
- `initializeHeaderDetails`
- `initializeLegendsDataSource`

##### **WHSCompatibilityPDFViewController** handles the showing of the compatibility PDF

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue: ... sender`

##### **WHSCompatibilityProductDetailsViewController** - how does the showing of the product details in the compatibility section

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
- `fetchCompatibilityDetails`

##### **WHSCompatibilityReportPDFViewController** - handles the showing of the compatibility report PDF

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue: ... sender`

##### **WHSCompetenciesPickerViewController** - handles the picking of competencies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddCompetenciesView`
- `showEditCompetenciesView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSConfinedSpacesActionViewController** - how was the showing of an action in the confined spaces section 

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
- `initializeDataSource`

##### **WHSConfinedSpacesAddActionViewController** - handles the adding of an action in the  confined spaces section

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
- `initializeDataSource`

##### **WHSConfinedSpacesAddEntryViewController** - handles the adding of an entry in the confined spaces section

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
- `initializeDataSource`

##### **WHSConfinedSpacesAddRecordViewController** - handles the adding of a record in the confined spaces section

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
- `initializeDataSource`

##### **WHSConfinedSpacesEditActionViewController** - handles the editing of an action in that confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchCSActionDetailsData`
- `initializeDataSource`
- `formatNotificationReceivers`

##### **WHSConfinedSpacesEditEntryViewController** - handles the editing of an entry in the confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`

##### **WHSConfinedSpacesEditRecordViewController** - handles the editing of a record in the confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchConfinedSpacesDetailsData`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `presentDropdownList`

##### **WHSConfinedSpacesEntriesViewController** - handles the showing of the entries in the confined spaces section

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
- `initializeDataSource`

##### **WHSConfinedSpacesMonitoringHistoryViewController** - handles the showing of the history in the confined spaces monitoring section

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
- `showMonitoringTabView`

##### **WHSConfinedSpacesPermitDetailsViewController** - shows the details of a confined spaces permit

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchConfinedSpacesDetailsData`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `returnNullIfNull`
- `initializeDataSource`
- `showEntriesView`
- `showAttachmentsView`
- `showPDFView`

##### **WHSConfinedSpacesPermitsViewController** - shows the permits for confined spaces

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchPermitsData`
- `initializeDataSource`
- `showPermitsView`

##### **WHSConfinedSpacesTabViewController** - logic behind the Confined Spaces tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showAttachmentsView`
- `showEmailReportView`
- `showAssessmentView`
- `showEditDetailsView`
- `showPermitsEntriesView`
- `showMonitoringHistoryView`
- `showActionsView`

##### **WHSControlMeasureTablePickerViewController** - handles the table picker view of the Control Measure section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `detailsView: â¦ savedData`
- `showAddControlMeasureView`
- `openAddRecordView`

##### **WHSDetailsViewController** - handles the logic behind the details screen

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
- `indexForField: ... inSection`

##### **WHSDynamicActionsViewController** - handles the logic behind dynamic actions

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `openAddRecordView`
- `didSaveAction: ... isNew`

##### **WHSDynamicSignActionsViewController** - handles the logic behind dynamic sign actions

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
- `isRequiredDataFilled`

##### **WHSDynamicSigneesViewController** - handles the logic behind dynamic signees

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
- `initializeDataSource`

##### **WHSDynamicTemplatesViewController** - handles the logic behind dynamic templates 

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
- `isAllRequiredDataFilledUp`

##### **WHSEditAIInspectionSubTypeViewController** - handles the editing of an AI inspection subtype

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditAIInspectionTypeViewController** - handles the editing of an AI inspection type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditActionCategoryViewController** - handles the editing of an action category view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditAssetSubTypeViewController** - handles the editing of an asset subtype

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditAssetTypeViewController** - handles the editing of an asset type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditAtmosphericMonitoringTypeViewController** - Montrose the editing of an atmospheric monitoring tipe

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditAttachmentsViewController** - handles editing of an attachment

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
- `hideHUD`

##### **WHSEditAttendeeViewController** - handles editing of an attendee

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchAttendeeDetailsData`
- `initializeDataSource`

##### **WHSEditEmployeeDepartmentViewController** - handles editing a department of an employee

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditEmployeeDivisionViewController** - handles editing of an employee's division

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditGenericViewController** - handles editing a generic

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditInspectionTypeViewController** - handles the editing of an inspection type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`
- `createJSON`

##### **WHSEditLicenceViewController** - handles the editing of a license

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditNoiseAssessmentSubTypeViewController** - handles the editing of a noice assessment subtype

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditNoiseAssessmentTypeViewController** - handles the editing a noise assessment type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditNotificationReceiverViewController** - handles editing a notification receiver

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSEditPointsRaisedViewController** - handles editing points raised

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
- `showPointRaisedActionsView`

##### **WHSEditWorkerViewController** - handles the editing of a worker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `initializeDataSource`

##### **WHSEmailReportViewController** - shows the email report screen

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
- `connectionDidFinishLoading`

##### **WHSEmergencyProcedureViewController** - displays the emergency procedure screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchEmergencyProceduresListData`
- `initializeDataSource`
- `generateHTML`
- `showWebView`

##### **WHSEmployeeAddServiceHistoryViewController** - handles adding a service history of an employee

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
- `saveFailed`

##### **WHSEmployeeAddTestHistoryViewController** - adds an employee's test history

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
- `saveFailed`

##### **WHSEmployeeContractorCompanyPickerViewController** - handles the picking of an employee's contractor company

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue: ... sender`

##### **WHSEmployeeDepartmentPickerViewController** - handles the picking of an employee department

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddEmployeeDeparmentView`
- `showEditEmployeeDepartmentView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSEmployeeEditServiceHistoryViewController** - handles the editing of an employee's service history

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
- `showAttachmentsView`

##### **WHSEmployeeEditTestHistoryViewController** - handles the editing of an employee's test history

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
- `showAttachmentsView`

##### **WHSEmployeeServiceHistoryViewController** - shows the employee service history screen

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
- `openAddRecordView`

##### **WHSEmployeeTestHistoryViewController** - handles the showing of the employee test history screen

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
- `openAddRecordView`

##### **WHSEnvironmentalAtmosphericMonitoringSearchResultsViewController** - handles the showing of the search results in the environmental atmospheric monitoring section

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
- `showTabView`

##### **WHSEnvironmentalAtmosphericMonitoringSearchViewController** - handles the showing of the search results in the environmental atmospheric monitoring section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSEnvironmentalAtmosphericMonitoringViewController** - handles the showing of the environmental atmospheric monitoring screen

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
- `openAddRecordView`

##### **WHSEnvironmentalConfinedSpacesSearchResultsViewController** - handles the showing of the search results in the environmental confined spaces section

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
- `showTabView`

##### **WHSEnvironmentalConfinedSpacesSearchViewController** - handles the searching in the environmental confined spaces section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSEnvironmentalConfinedSpacesViewController** - handles the showing of the environmental confined spaces screen

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
- `showTabView`

##### **WHSEnvironmentalDetailsViewController** - handles the showing of the details in the environmental section

###### **Methods and Calculated Variables**
- `initializeDataSource`

##### **WHSEnvironmentalNoiseControlSearchResultsViewController** - handles the showing of the search results in the environmental noise control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchSearchResultsData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSEnvironmentalNoiseControlSearchViewController** - handles the searching in the environmental noise control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSEnvironmentalNoiseControlViewController** - handles the environmental noise control screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `fetchNoiseControlListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`

##### **WHSEnvironmentalSearchViewController** - handles the search in the environmental section

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
- `searchBarButtonItemDidTapped`

##### **WHSEnvironmentalViewController** - handles the environmental screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `prepareForSegue`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `showAtmosphericMonitoringView`
- `showNoiseControlView`
- `showConfinedSpaces`
- `showAsbestosView`
- `showCarcinogensView`

##### **WHSExposureLimitsAddViewController** - handles the adding of an exposure limit

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
- `doneBarButtonItemDidTapped`

##### **WHSExposureLimitsSearchResultsViewController** - handles the search results of the exposure limits section

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
- `doneBarButtonItemDidTapped`

##### **WHSExposureLimitsViewController** - handles the exposure limits screen 

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
- `deleteBarButtonItemDidTapped`

##### **WHSFireFightingClassPickerViewController** - handles the picking of a class in the fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddClassView`
- `showEditClassView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSFireFightingRatingPickerViewController** - handles the picking of a rating in the firefighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddRatingView`
- `showEditRatingView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSGenericPickerViewController** - the superclass of a generic picker view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddGenericView`
- `showEditGenericView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSGroupedTableViewController** - handles the showing of a grouped table view

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
- `donePickingBarButtonItemDidTapped`

##### **WHSHazardsAsbestosAddDetailsViewController** - handles the adding of the details in the hazards of asbestos section

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
- `isAllRequiredDataFilledUp`

##### **WHSHazardsAsbestosAddInspectionHistoryViewController** - handles the adding of inspection history in the hazards asbestos section

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
- `createJSON`

##### **WHSHazardsAsbestosAddRemovalHistoryViewController** - handles the adding of the removal history in the hazards asbestos section

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
- `createJSON`

##### **WHSHazardsAsbestosEditDetailsViewController** - handles the editing of the details in the hazards asbestos section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`
- `createJSONData`

##### **WHSHazardsAsbestosEditInspectionHistoryViewController** - handles the editing of the inspection history in the hazards as Bestos section

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
- `showAttachmentsView`

##### **WHSHazardsAsbestosEditRemovalHistoryViewController** - handles the editing of the removal history in the Hazards Asbestos section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `acSheet: ... clickedButtonAtIndex`
- `fetchRemovalHistoryData`
- `initializeDataSource`
- `showAttachmentsView`

##### **WHSHazardsAsbestosInspectionHistoryViewController** - handles the showing of the inspection history in the Hazards Asbestos screen

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
- `openAddRecordView`

##### **WHSHazardsAsbestosRemovalHistoryViewController** - handles the removal history of hazards asbestos

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
- `openAddRecordView`

##### **WHSHazardsAsbestosSearchFormViewController** - handles the search form in hazards asbestos

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsView`
- `searchBarButtonItemDidTapped`

##### **WHSHazardsAsbestosSearchResultsViewController** - handles the search results in hazards asbestos

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSHazardsAsbestosTabViewController** - handles the hazards asbestos tab

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
- `showActionsView`

##### **WHSHazardsAsbestosViewController** - shows the Hazards Asbestos screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `fetchAsbestosListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`

##### **WHSHazardsCarcinogensAddEmployeeExposureViewController** - handles the adding of employee exposure in hazards carcinogens

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
- `isAllRequiredDataFilledUp`

##### **WHSHazardsCarcinogensAddRecordViewController** - handles the adding of record in hazards carcinogens

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
- `isAllRequiredDataFilledUp`

##### **WHSHazardsCarcinogensEditEmployeeExposureViewController** - handles the editing of employee exposure in hazards carcinogens

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchEmployeeExposureDetailsData`
- `initializeDataSource`

##### **WHSHazardsCarcinogensEditRecordViewController** - handles editing of a record in the Hazards Carcinogens section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSHazardsCarcinogensEmployeeExposureViewController** - handles the employee exposure in hazards carcinogens

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
- `openAddRecordView`

##### **WHSHazardsCarcinogensSearchFormViewController** - handles the search form in hazards carcinogens

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsView`
- `searchBarButtonItemDidTapped`

##### **WHSHazardsCarcinogensSearchResultsViewController** - handles the search results in hazards carcinogens

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`


##### **WHSHazardsCarcinogensTabViewController** - handles the hazards carcinogens tab

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
- `showActionsView`

##### **WHSHazardsCarcinogensViewController** - controls the hazards carcinogens

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
- `openAddRecordView`

##### **WHSHazardsDetailsViewController** - handles the showing of the details in the hazards section

###### **Methods and Calculated Variables**
- `initializeDataSource`

##### **WHSHazardsSearchFormViewController** - handles the showing of the search form in the Hazards section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showStatusPickerView`

##### **WHSHazardsSearchResutlsViewController** - handles the showing of the search results in the Hazards section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `searchRecords`
- `fetchNextPage`

##### **WHSHazardsViewController** - handles the showing of the Hazards screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `showAsbestosView`
- `showCarcinogensView`

##### **WHSIRSearchResultsViewController** - handles the search results in IR

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
- `showTabView`

##### **WHSIRSearchViewController** - handles the IR search

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
- `searchBarButtonItemDidTapped`

##### **WHSIncidentReportingAddNewHazardsViewController** - handles the adding of new hazards in incident reporting

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
- `clearHazardData`

##### **WHSIncidentReportingAddNewWitnessViewController** - handles the adding of new witness in incident reporting

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
- `clearWitnessData`

##### **WHSIncidentReportingAddRecordViewController** - handles the adding of record in incident reporting

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
- `valueFromData: ... forKeyPath: ... withTransForm`

##### **WHSIncidentReportingAddTypeViewController** - handles the adding of type in incident reporting

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

##### **WHSIncidentReportingAdditionalDetailsViewController** - handles the additional details in incident reporting

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSIncidentReportingDetailsViewController** - handles the details in incident reporting

###### **Methods and Calculated Variables**
- `initializeDataSource`

##### **WHSIncidentReportingEditAdditionalDetailsViewController** - handles the editing of additional details in incident reporting

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
- `existingProductList`

##### **WHSIncidentReportingEditDetailsViewController** - handles the editing of details in incident reporting

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
- `sendFetchRequest: ... delegate: ... dictionaryType`

##### **WHSIncidentReportingEditHazardsViewController** - handles the editing of a hazard in the incident reporting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchHazardDetailsData`
- `initializeDataSource`


##### **WHSIncidentReportingEditTypeViewController** - handles the editing of a type in the Incident Reporting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSIncidentReportingEditWitnessViewController** - handles the editing of a witness in the Incident Reporting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchWitnessDetailsData`
- `initializeDataSource`

##### **WHSIncidentReportingRecordViewController** - shows the Incident Reporting Record screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `acSheet: â¦ clickedButtonAtIndex`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchIncidentReports`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`
- `showSearchView`
- `openPDFView`
- `showEmailReport`
- `openAddRecordView`

##### **WHSIncidentReportingTypePickerViewController** - handles the picker view for incident reporting types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddIncidentReportingTypeView`
- `showEditIncidentReportingTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSInspectionTypePickerViewController** - handles the picker view for inspection types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddInspectionTypeView`
- `showEditInspectionTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSLandingViewController** - handles the Landing screen

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
- `processDashboardData`

##### **WHSLegislationsTabViewController** - handles the Legislations tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: â¦ didSelectRowAtIndexPath`
- `tableView: â¦ clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentView`
- `showSignOffView`
- `showEmailReportView`
- `showEditDetailsView`
- `showActionsView`

##### **WHSLicencePickerViewController** - handles the License Picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddLicenceView`
- `showEditLicenceView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSLocationPickerViewController** - handles the picker view for location

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddLocationView`
- `showEditLocationView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSLocationTypePickerViewController** - handles the picker view for location types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddLocationView`
- `openAddRecordView`

##### **WHSLoginViewController** - handles the Login screen and login in of a user

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
- `validatePassword`

##### **WHSMSDSProductDetailsViewController** - handles the product details in msds

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
- `reorderSanitizedJSON`

##### **WHSMSDSSearchResultsViewController** - handles the display of search results for MSDS

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `prepareForSegue`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `searchProducts`


##### **WHSMSDSSearchViewController** - handles the searching in msds

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
- `finishedSelectingSearchFormatHandler`

##### **WHSManifestsReportPDFViewController** - handles the PDF display for manifests reports

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue`

##### **WHSMenuViewController** - controls menu

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
- `formatPickedPersons: ... indentationString`

##### **WHSNoiseAssessmentSubTypePickerViewController** - handles the picker view for noise assessment sub types

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddSubTypeView`
- `showEditSubTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSNoiseControlAddAssessmentViewController** - handles adding an assessment in the Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: â¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `textView: â¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: â¦ clickedButtonAtIndex`
- `saveAssessmentDetailsData`
- `initializeDataSource`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`

##### **WHSNoiseControlAddControlViewController** - handles the adding of a control in the Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue`

##### **WHSNoiseControlAddRecordViewController** - handles the adding for noise control records

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: â¦ willSendRequest`
- `connection: â¦ didReceiveResponse`
- `connection: â¦ didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: â¦ dataPicked`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: â¦ clickedButtonAtIndex`
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


##### **WHSNoiseControlAssessmentDetailsViewController** - handles the showing of assessment details in the Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `swipeableTableViewCell: â¦ didTriggerRightUtilityButtonWithIndex`
- `deleteAssessment`
- `initializeDataSource`
- `showEditDetailsView`
- `initializeAddRecordBarButtonItem`
- `showAddAssessmentView`
- `showEditCommentView`
- `cellRightUtitilityButtons`
- `sanitizeAssessments`

##### **WHSNoiseControlEditAssessmentCommentViewController** - handles the editing of an assessment in the Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `initializeDataSource`

##### **WHSNoiseControlEditMeasurementViewController** - handles the editing of noise control measurement

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: â¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: â¦ dataPicked`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `textView: â¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: â¦ clickedButtonAtIndex`
- `fetchMeasurementDetailsData`
- `saveMeasurementDetailsData`
- `initializeDataSource`
- `createJSON`
- `showMeasurementLocalityPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`


##### **WHSNoiseControlEditRecordViewController** - handles the editing of a record in Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchNoiseControlDetailsData`
- `initializeDataSource`

##### **WHSNoiseControlNewControlViewController** - handles the showing of the new control in the Noise Control section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `showEditRecordView`
- `initializeDataSource`
- `openAddRecordView`

##### **WHSNoiseControlTabViewController** - handles the noise control tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showEditMeasurementView`
- `showAssessmentView`
- `showNewControlsView`

##### **WHSNonChemicalRiskAssessmentNewControlsViewController** - handles the new controls in non chemical risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`

##### **WHSNonChemicalRiskAssessmentSearchResultsViewController** - handles the search results in non chemical risk assessment

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
- `showTabView`

##### **WHSNonChemicalRiskAssessmentSearchViewController** - handles the search in non chemical risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `showSearchResultsView`

##### **WHSNonChemicalRiskAssessmentTabViewController** - handles the non chemical risk assessment tab

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
- `processTabFlags`

##### **WHSNonChemicalRiskAssessmentViewController** - shows the Non Chemical Risk Assessment screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `fetchNonChemicalRiskAssessmentListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showSearchView`
- `showPDFView`
- `showEmailReportView`
- `showTabView`


##### **WHSNonChemicalRiskManagementViewController** - controls the non chemical risk management

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `showHATRiskAssessmentView`
- `showSWMSView`
- `showSWPView`

##### **WHSNotificationReceiverPickerViewController** - handles the picker in notification receiver

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddNotificationReceiversView`
- `showEditNotificationReceiversView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSOfflineFormViewController** - shows the workers 

###### **Methods and Calculated Variables**
`viewDidLoad`
`viewWillAppear`
`initializeDataSource`
`accessPermission`
`tableView(...didSelectRowAt)`
`tableView(...heightForRowAt)`

##### **WHSOfflineFormsAuditsInspectionViewController** - handles the audits inspection in the offline forms section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `initializeDataSource`
- `tableView(...didSelectRowAt)`

##### **WHSOfflineFormsViewController** - handles the offline forms screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `initializeDataSource`
- `showNoFormsDownloaded`
- `downloadAll`
- `tableView(...cellForRowAt)`
- `tableView(...didSelectRowAt)`
- `tableView(...heightForRowAt)`


##### **WHSPAPComplaintsSearchResultsViewController** - Handles the search results for the PAP Complaints section

###### **Methods and Calculated Variables**
- `showTabView`

##### **WHSPAPComplaintsSearchViewController** handles the searching for the PAP Complaints section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`


##### **WHSPAPComplaintsTabViewController** - handles the PAP complaints tab

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


##### **WHSPAPDetailsViewController** - handles the PAP details

###### **Methods and Calculated Variables**
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`

##### **WHSPAPDrillsSearchResultsViewController** - handles the search results in the PAP Drills section

###### **Methods and Calculated Variables**
- `showTabView`

##### **WHSPAPDrillsSearchViewController** - handles the searching in the PAP Drills section

###### **Methods and Calculated Variables**
- `showSearchResultsViewWithDataList`


##### **WHSPAPDrillsTabViewController** - handles the PAP drills tab

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
- `showActionsView`

##### **WHSPAPLegislationsSearchResultsViewController** - handles the search results in the PAP Legislations section

###### **Methods and Calculated Variables**
- `showTabView`

##### **WHSPAPLegislationsSearchViewController** - handles the searching in the PAP Legislations section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSPAPPlansProceduresTabViewController** - handles the PAP plans procedures tab

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
- `showActionsView`

##### **WHSPAPPlansSearchResultsViewController** - handles the search results in the PAP Plans section 

###### **Methods and Calculated Variables**
- `showTabView`

##### **WHSPAPPlansSearchViewController** - handles the searching in the PAP Plans section 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSPAPSearchResultsViewController** - handles the search results in PAP

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
- `showTabView`

##### **WHSPAPSearchViewController** - handles the searching in pap

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
- `searchBarButtonItemDidTapped`

##### **WHSPAPTrainingSearchResultsViewController** - handles the search results in the AP training section screen

###### **Methods and Calculated Variables**
- `showTabView`

##### **WHSPAPTrainingTabViewController** - handles the pap training tab

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
- `showActionsView`

##### **WHSPAPTraningSearchViewController** - handles the searching in the AP training section

###### **Methods and Calculated Variables**
- `showSearchResultsViewWithDataList`

##### **WHSPDFAddSigneesViewController** - handles the PDF Add signees screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `didSelectUser`
- `didFinishSigningWithImage`
- `saveBarButtonItemDidTapped`
- `validToSave`
- `textViewDidChange`
- `showSignatureViewController`
- `initializeDataSource`
- `showPersonInvolvedTypeView`
- `refreshActionedByFields`

##### **WHSPDFEditSigneeViewController** - handles the editing of the signee on a pdf

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSPDFSigneesViewController** - handles the showing of the PDF Signees screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewWillDisappear`
- `handleBack`
- `connection: â¦ willSendRequest`
- `connection: â¦ didReceiveData`
- `connection: â¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `openAddRecordView`
- `toggleSubmitButton`
- `submitSignatures`
- `submitSignoffWithIndex`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `tableView: â¦ editActionsForRowAtIndexPath`
- `initializeDataSource`
- `saveOnlineSignature`

##### **WHSPointsRaisedViewController** - controls the points raised

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
- `openAddRecordView`

##### **WHSPoliciesDrillsEditRecordViewController** - handles the editing of record in policies drills

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSPoliciesDrillsViewController** - controls the policies drills

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
- `openAddRecordView`

##### **WHSPoliciesEditRecordViewController** - handles the editing of record in policies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSPoliciesLegislationsEditRecordViewController** - handles the editing of record in the policies legislations

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
- `getVerifiedStatesIDs`

##### **WHSPoliciesLegislationsViewController** - controls the policies legislations

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
- `openAddRecordView`

##### **WHSPoliciesPlansAddRecordViewController** - handles the adding of record in policies plans

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
- `clearLocationTypeData`

##### **WHSPoliciesPlansEditRecordViewController** - handles the editing of record in policies plans

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSPoliciesPlansViewController** - controls the policies plans

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
- `openAddRecordView`

##### **WHSPoliciesProceduresViewController** - handles the procedures in policies

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
- `showComplaintsView`

##### **WHSPoliciesSearchResultsViewController** - handles the display of search results for policies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showTabView`

##### **WHSPoliciesSearchViewController** - handles the searching of policies

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSPoliciesTabViewController** - handles the policies tab

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
- `showActionsView`

##### **WHSPoliciesTrainingEditRecordViewController** - handles the editing of record in policies training

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`
- `getInternalExternal`

##### **WHSPoliciesTrainingViewController** - controls the policies training

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
- `openAddRecordView`

##### **WHSPoliciesViewController** - controls the policies

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
- `openAddRecordView`

##### **WHSProductDetailsViewController** - handles the display of product details

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSProjectPickerViewController** - handles the project picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddProjectView`
- `openAddRecordView`

##### **WHSRecordViewController** - handles showing of the Record screen

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
- `searchItem`

##### **WHSRegisterActionDetailsViewController** - handles the action details in register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`
- `fetchActionDetails`

##### **WHSRegisterActionManagerViewController** - handles the action manager of the register

###### **Methods and Calculated Variables**
- `tablePickerDidFinishedPicking: ... dataPicked`
- `createInData`
- `transferActionData`

##### **WHSRegisterActionsViewController** - handles the actions of the register

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
- `openAddRecordView`

##### **WHSRegisterAddActionViewController** - handles the adding of action in the register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `saveActionButtonDidTapped`
- `cellSwitchDidValueChanged`

##### **WHSRegisterAddActionsViewController** - handles the adding of actions in the register

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
- `createJSON`

##### **WHSRegisterAddServiceTypeViewController** - handles the adding of service type in the register

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
- `isAllRequiredDataFilledUp`

##### **WHSRegisterAddTestTypeViewController** - handles the adding of test type in the register

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
- `isAllRequiredDataFilledUp`

##### **WHSRegisterEditActionDetailsViewController** - handles the editing of action details in the register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `saveActionButtonDidTapped`
- `cellSwitchDidValueChanged`

##### **WHSRegisterEditActionsViewController** - handles the editing of actions in register

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `fetchDetails`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchActionDetailsData`
- `initializeDataSource`
- `formatNotificationReceivers`

##### **WHSRegisterEditServiceTypeViewController** - handles the editing of a service type in the Register section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSRegisterEditTestTypeViewController** - handles the editing of a test type in the Registers section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **WHSRegisterServiceTypePickerViewController** - handles the picking of a service type in Registers section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddServiceTypeView`
- `showEditServiceTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSRegisterTestHistoryDetailsViewController** - handles the viewing of the details of the Register Test History

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `connectionDidFinishLoading`
- `processActionRecordCount`
- `initializeEditDetailsView`
- `showEditDetailsView`

##### **WHSRegisterTestHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `connectionDidFinishLoading`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchTestHistories`
- `showTestHistoryDetailsView`

##### **WHSRegisterTestTypePickerViewController** - handles the picking of a Register Test Type

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddTestTypeView`
- `showEditTestTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSRegistersSearchViewController** - handles the searching in registers

###### **Methods and Calculated Variables**

##### **WHSRegistersViewController** - handles the viewing of the Registers screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `didReceiveMemoryWarning`
- `prepareForSegue`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `showHazardsView`
- `showAssetsView`
- `showSafetyView`
- `showEnvironmentalView`
- `showChemicalsView`

##### **WHSReportIncidentViewController** - handles the showing of the Report Incident Screen 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `download`
- `fetchOfflineConnection`
- `connection: â¦ willSendRequest`
- `connection: â¦ didReceiveResponse`
- `connection: â¦ didReceiveData`
- `handleFlexi`
- `connectionDidFinishLoading`
- `dateOnlyFormatFromDateString`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ viewForHeaderInSection`
- `sectionTapped`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForHeaderInSection`
- `tableView: â¦ heightForFooterInSection`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `textView: â¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: â¦ clickedButtonAtIndex`
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
- `documentPicker: â¦ didPickDocumentAtURL`
- `documentPickerWasCancelled`
- `refreshSelectedRow`
- `imagePickerController: â¦ didFinishPickingMediaWithInfo`
- `imagePickerControllerDidCancel`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`
- `handleAutoNumData`
- `clearLocationTypeData`
- `clearDepartmentData`
- `cellIndexForField`

##### **WHSRichTextEditorViewController** - handles the rich text editor

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue`

##### **WHSRiskAssessmentActionDetailsViewController** - handles the action details in the risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `fetchActionDetails`
- `initializeDataSource`

##### **WHSRiskAssessmentActionManagerViewController** - handles the action manager in the risk assessment

###### **Methods and Calculated Variables**
- `tablePickerDidFinishedPicking: ... dataPicked`
- `createInData`
- `isValidObjectForIndex`
- `transferActionData`
- `showActionControlMeasurePickerView`

##### **WHSRiskAssessmentAddActionViewController** - handles the adding of action in the risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `cellSwitchDidValueChanged`
- `saveActionButtonDidTapped`

##### **WHSRiskAssessmentEditActionDetailsViewController** - handles the editing of action details in risk assessment

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `saveActionButtonDidTapped`
- `cellSwitchDidValueChanged`

##### **WHSRiskAssessmentPicturesViewController** - handles the showing of pictures in the Risk Management section

###### **Methods and Calculated Variables**
- `collectionCellIdentifier`
- `initializeCollectionViews`
- `preferredCollectionViewFrame`
- `processPictures`
- `processHeadersAndDetails`

##### **WHSRiskAssessmentViewController** - controls the risk assessment

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
- `disableActions`

##### **WHSRiskManagementAddActionViewController** - handles the adding of action in risk management

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
- `createPOSTJSON`

##### **WHSRiskManagementEditActionViewController** - handles the editing of action in risk management

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchActionDetailsData`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`

##### **WHSRiskManagementViewController** - handles the Risk Management screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `prepareForSegue`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `showChemicalRiskManagementView`
- `showNonChemicalRiskManagementView`
- `initializeDataSource`

##### **WHSSafeWorkManagementSystemActionDetailsViewController** - handles the action details of safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`
- `fetchActionDetails`

##### **WHSSafeWorkManagementSystemActionManagerViewController** - handles the action manager of safe work management system

###### **Methods and Calculated Variables**
- `tablePickerDidFinishedPicking: ... dataPicked`
- `createInData`
- `transferActionData`
- `showActionTaskPickerView`

##### **WHSSafeWorkManagementSystemActivityViewController** - handles the activity in safe work management system

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
- `initializeDataSource`

##### **WHSSafeWorkManagementSystemAddActionViewController** -  handles the adding of action in safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `saveActionButtonDidTapped`
- `cellSwitchDidValueChanged`

##### **WHSSafeWorkManagementSystemDetailViewController** - handles the detail in safe work management system

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
- `initializeDataSource`

##### **WHSSafeWorkManagementSystemEditActionDetailsViewController** - handles the editing of action details in safe work management system

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `saveActionButtonDidTapped`
- `cellSwitchDidValueChanged`

##### **WHSSafeWorkManagementSystemSearchResultsViewController** - handles the search results in safe work management system

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
- `showTabView`

##### **WHSSafeWorkManagementSystemSearchViewController** - handles the searching in safe work management system

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
- `searchBarButtonItemDidTapped`

##### **WHSSafeWorkManagementSystemTabViewController** - handles the safe work management system tab

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
- `showActionsView`

##### **WHSSafeWorkManagementSystemTaskViewController** - handles the tasks in safe work management system

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
- `initializeDataSource`

##### **WHSSafeWorkManagementSystemViewController** - controls the safe work management system

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
- `showTabView`

##### **WHSSafeWorkProceduresActionViewController** - handles the actions in the Safe Work Procedures section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchNewControlsData`
- `showAddActionView`
- `showEditActionView`

##### **WHSSafeWorkProceduresChecklistViewController** - handles the checklist in safe work procedures

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
- `initializeDataSource`

##### **WHSSafeWorkProceduresDetailViewController** - handles the details in safe work procedures

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
- `initializeDataSource`

##### **WHSSafeWorkProceduresListViewController** handles the showing of the list of safe work procedures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `fetchSWPData`
- `initializeDataSource`

##### **WHSSafeWorkProceduresSearchResultsViewController** - handles the search results in safe work procedures

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
- `showTabView`

##### **WHSSafeWorkProceduresSearchViewController** - handles the searching in safe work procedures

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
- `searchBarButtonItemDidTapped`

##### **WHSSafeWorkProceduresTabViewController** - handles the safe work procedures tab

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
- `showActionsView`

##### **WHSSafeWorkProceduresViewController** - shows share work procedures

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAt`
- `fetchSWPListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showSearchView`
- `showTabView`

##### **WHSSafetyAddDetailsViewController** - handles the adding of details in safety

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
- `isAllRequiredDataFilledUp`

##### **WHSSafetyAddTestHistoryViewController** - handles the adding of test history in safety

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
- `isAllRequiredDataFilledUp`

##### **WHSSafetyEditDetailsViewController** - handles the editing of details in safety

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsDat`
- `initializeDataSource`

##### **WHSSafetyEditServiceHistoryViewController** - handles the editing of service history in safety

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
- `showAttachmentsView`

##### **WHSSafetyEditTestHistoryViewController** - handles the editing of test history in safety

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
- `showAttachmentsView`

##### **WHSSafetyEmergencyWashingAddDetailsViewController** - handles the adding go details in the safety emergency washing section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForHeaderInSection`
- `tableView: â¦ heightForFooterInSection`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetyEmergencyWashingAddTestHistoryViewController** - handles the adding of test history in the safety emergency washing section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetyEmergencyWashingEditDetailsViewController** - handles the editing of the details in the safety emergency washing section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForHeaderInSection`
- `tableView: â¦ heightForFooterInSection`
- `tableView: â¦ heightForRowAtIndexPath`


##### **WHSSafetyEmergencyWashingEditTestHistoryViewController** - handles the editing of the history of safety emergency washing section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetyEmergencyWashingSearchResultsViewController** - handles the search results in the safety emergency washing section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSSafetyEmergencyWashingSearchViewController** - handles searching in safety emergency washing 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSSafetyEmergencyWashingTabViewController** - logic for the safety emergency washing tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: â¦ clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`

##### **WHSSafetyEmergencyWashingViewController** shows safety emergency washing screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `fetchEmergencyWashingListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openPDFView`
- `openAddRecordView`

##### **WHSSafetyFireDetectionAddDetailsViewController** - handles the adding of details in the Safety Fire Detection section section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSSafetyFireDetectionAddTestHistoryViewController** - handles the adding of a test history in the Safety Fire Detection section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSSafetyFireDetectionEditDetailsViewController** - handles the editing of the details in the Safety Fire Detection section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSSafetyFireDetectionEditTestHistoryViewController** - handles the editing of a test history in the Safety Fire Detection section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSSafetyFireDetectionSearchResultsViewController** - handles the search results in the Safety Fire Detection section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSSafetyFireDetectionSearchViewController** - handles the search function in the Safety Fire Detection section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSSafetyFireDetectionTabViewController** - handles the Safety fore detection screen

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
- `showActionsView`

##### **WHSSafetyFireDetectionViewController** - handles the display of the Safety Fire Detection screen

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
- `openAddRecordView`

##### **WHSSafetyFireFightingAddDetailsViewController** - shows the add details screen in the safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForHeaderInSection`
- `tableView: â¦ heightForFooterInSection`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetyFireFightingAddTestHistoryViewController** -shows the add test history screen in the safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetyFireFightingEditDetailsViewController** - shows the edit details screen in the safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForHeaderInSection`
- `tableView: â¦ heightForFooterInSection`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetyFireFightingEditTestHistoryViewController** - shows edit test history screen in safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetyFireFightingSearchResultsViewController** - shows the search results screen in the safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSSafetyFireFightingSearchViewController** - shows the search screen in safety fire fighting section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`


##### **WHSSafetyFireFightingTabViewController** - logic behind safety fire fighting tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: â¦ clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`

##### **WHSSafetyFireFightingViewController** - shows safety fire fighting scree

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `fetchFireFightingEquipmentListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`

##### **WHSSafetyFirstAidAddDetailsViewController** - handles the adding of details in the Safety First Aid section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSSafetyFirstAidAddTestHistoryViewController** - handles the adding of a test history in the Safety First Aid section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`


##### **WHSSafetyFirstAidEditDetailsViewController** - handles the editing  of details in safety first aid

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSSafetyFirstAidEditTestHistoryViewController** - handles the editing of test history in safety first aid

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSSafetyFirstAidSearchResultsViewController** - handles the search results in safety first aid

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSSafetyFirstAidSearchViewController** - handles searching in safety first aid

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSSafetyFirstAidTabViewController** - handles the safety first aid tab 

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
- `showActionsView`

##### **WHSSafetyFirstAidViewController** - controls the safety first aid

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
- `openAddRecordView`

##### **WHSSafetyPPEAddDetailsViewController** - handles adding details in Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForHeaderInSection`
- `tableView: â¦ heightForFooterInSection`
- `tableView: â¦ heightForRowAtIndexPath`



##### **WHSSafetyPPEAddEmployeeViewController** - handles the adding of employee in safety ppe

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
- `isAllRequiredDataFilledUp`

##### **WHSSafetyPPEAddTestHistoryViewController** - handles adding test history of Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetyPPEEditDetailsViewController** - handles the editing of details in safety ppe

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSSafetyPPEEditEmployeeViewController** - handles the editing of employee in safety ppe

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
- `showEmployeeServiceHistoryView`

##### **WHSSafetyPPEEditTestHistoryViewController** - handles editing the test history of Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetyPPEEmployeeViewController** - handles employee view of Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchEmployees`
- `showEditPPEDetailsView`
- `openAddRecordView`

##### **WHSSafetyPPESearchResultsViewController** - handles the search results of Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSSafetyPPESearchViewController** - handles searching of Safety PPEs

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSSafetyPPETabViewController** - handles the safety ppe tab

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
- `showActionsView`

##### **WHSSafetyPPEViewController** - handles the safety ppe

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
- `openAddRecordView`

##### **WHSSafetyServiceHistoryViewController** - handles the display of Safety Service History 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchServiceHistories`
- `showEditServiceHistoryDetailsView`
- `openAddRecordView`

##### **WHSSafetySpillKitAddDetailsViewController** - shows add details screen in safety spill kit section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForHeaderInSection`
- `tableView: â¦ heightForFooterInSection`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetySpillKitAddTestHistoryViewController** - shows ad test history screen in safety spill kit section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetySpillKitEditDetailsViewController** - shows edit details screen of safety spill kit section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForHeaderInSection`
- `tableView: â¦ heightForFooterInSection`
- `tableView: â¦ heightForRowAtIndexPath`

##### **WHSSafetySpillKitEditTestHistoryViewController** - shows edit test history screen in safety spill kit section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`


##### **WHSSafetySpillKitSearchResultsViewController** - shows safety spill kit search results

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSSafetySpillKitSearchViewController** - shows safety spill kit search

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSSafetySpillKitTabViewController** - logic for safety spill kit tab

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: â¦ clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`

##### **WHSSafetySpillKitViewController** - shows safety spill kit view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `fetchSpillKitListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`

##### **WHSSafetyTabViewController** - handles the showing of the Safety view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `initializeDataSource`
- `disableEmployeeView`
- `showDetailsView`
- `showEmployeeView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`
- `showPDFView`
- `showAttachmentView`

##### **WHSSafetyTestHistoryViewController** - handles the showing of the history in the Safety Test section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `fetchTestHistories`
- `showTestHistoryDetailsView`
- `showEditTestHistoryDetailsView`
- `openAddRecordView`


##### **WHSSafetyViewController** - controls the safety

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
- `showPPEView`

##### **WHSSearchRecordViewController** - shows search record view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeSearchBarButtonItem`
- `searchBarButtonItemDidTapped`
- `showSearchResultsViewWithDataList`

##### **WHSSearchResultsRecordViewController** - logic behind the search results record screen

###### **Methods and Calculated Variables**
- `searchRecords`

##### **WHSSearchViewController** - logic behind the search screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `initializeSearchBarButtonItem`
- `showDatePicker`
- `searchBarButtonItemDidTapped`
- `formatPickedItems`

##### **WHSSettingViewController** - handles and shows the Settings screen

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
- `switchValueDidChanged`

##### **WHSSideMenuViewController** - the logic behind the Side Manu of the app

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeSideMenuItems`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
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
- `localFormsButtonTapped`

##### **WHSSiteRAControlsViewController** - handles the Controls screen of the Site RA section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connection: â¦ willSendRequest`
- `connection: â¦ didReceiveData`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `fetchControlCategoriesData`
- `fetchCurrentControlsData`
- `saveRecordData`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `acSheet: â¦ clickedButtonAtIndex`
- `textViewDidChange`
- `initializeDataSource`
- `initializeAddRecord`
- `openAddRecordView`

##### **WHSSiteRAHazardsAddHazardViewController** - handles the adding of a hazard in the Site RA Hazards section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: â¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: â¦ clickedButtonAtIndex`
- `saveHazardData`
- `initializeDataSource`
- `createJSON`
- `showHazardTypePickerView`
- `showHazardSubTypePickerView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `clearHazardData`

##### **WHSSiteRAHazardsViewController** - handles the Hazards screen in the Site RA section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `initializeAddRecord`
- `openAddRecordView`
- `connection: â¦ willSendRequest`
- `connection: â¦ didReceiveResponse`
- `connection: â¦ didReceiveData`
- `connectionDidFinishLoading`
- `fetchDetailsHazardTemplateID`
- `fetchTemplateName`
- `fetchHazards`
- `saveRecordData`
- `tablePickerDidFinishedPicking`
- `acSheet: â¦ clickedButtonAtIndex`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `switchCellValueDidChanged`
- `createJSON`
- `showHazardTemplatePicker`
- `textFieldDidChange`
- `saveBarButtonItemDidTapped`
- `initializeDataSource`
- `updateTemplateCell`
- `updateHazardSection`

##### **WHSSiteRARiskDetailViewController** - handles the risk detail of the Site RA section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: â¦ didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ viewForHeaderInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `textView: â¦ shouldChangeTextInRange`
- `textViewDidChange`
- `textView: â¦ heightForHeaderInSection`
- `textView: â¦ heightForFooterInSection`
- `textView: â¦ estimatedHeightForRowAtIndexPath`
- `textView: â¦ heightForRowAtIndexPath`
- `fetchDetailsData`
- `createJSON`
- `showHazardTypePickerView`
- `showHazardSubTypePickerView`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`
- `acSheet: â¦ clickedButtonAtIndex`
- `saveRecordData`
- `initializeDataSource`
- `clearHazardData`

##### **WHSSiteRARisksAddControlViewController** - logic for the screen that shows add risk control in site risk assessment view controller

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: â¦ willSendRequest`
- `connection: â¦ didReceiveResponse`
- `connection: â¦ didReceiveData`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `tablePickerDidFinishedPicking: â¦ dataPicked`
- `searchBar: â¦ textDidChange`
- `searchBarSearchButtonClicked`
- `fetchControlsList`
- `saveRecordData`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `acSheet: â¦ clickedButtonAtIndex`
- `switchCellValueDidChanged`
- `showControlCategories`
- `initializeDataSource`
- `updateControlsList`
- `filterListBySearchText`
- `initializeAddBarButtonItem`
- `showAddActionView`
- `showEditActionView`
- `addBarButtonItemDidTapped`

##### **WHSSiteRARisksRatingViewController** - handles the risk rating screen of the Site RA section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: â¦ willSendRequest`
- `connection: â¦ didReceiveResponse`
- `connection: â¦ didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `textView: â¦ shouldChangeTextInRange`
- `textViewDidChange`
- `tableView: â¦ heightForFooterInSection`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
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
- `acSheet: â¦ clickedButtonAtIndex`
- `initializeStaticFields`
- `initializeCustomFields`

##### **WHSSiteRARisksTabViewController** - logic for the screen that shows the table view of risks in the site risks assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: â¦ didSelectRowAtIndexPath`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReport`
- `showActionsView`
- `showDetailsView`
- `showControlsView`
- `showRatingsView`

##### **WHSSiteRARisksViewController** - logic behind the screen that shows the risks in the site risk assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `fetchSiteRARisksListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `openAddRecordView`
- `showSearchView`
- `showPDFView`
- `showEmailReportView`
- `showTabView`

##### **WHSSiteRiskAsessmentSearchResultsViewController** - handles the search results of the Site Risk Assessment section

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `prepareForSegue`
- `connectionDidFinishLoading`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSSiteRiskAssessmentAddRecordViewController** - logic behind the site risk assessment record screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: â¦ willSendRequest`
- `connection: â¦ didReceiveResponse`
- `connection: â¦ didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: â¦ dataPicked`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ titleForHeaderInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `textView: â¦ shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: â¦ clickedButtonAtIndex`
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
- `isAllRequiredDataFilledUp`

##### **WHSSiteRiskAssessmentEditRecordViewController** - logic for site risk assessment edit record screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSSiteRiskAssessmentSearchViewController** - logic for site risk assessment search screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: â¦ dataPicked`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showGenericPickerViewWithType`
- `showLocationPickerView`
- `showStatusPickerView`
- `showSearchResultsView`
- `searchBarButtonItemDidTapped`

##### **WHSSiteRiskAssessmentTabViewController** - logic for site risk assessment tab view

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReport`
- `showActionsView`
- `showDetailsView`
- `showHazardsView`
- `showRisksView`

##### **WHSSiteRiskAssessmentViewController** - logic for site risk assessment screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: â¦ didSelectRowAtIndexPath`
- `acSheet: â¦ clickedButtonAtIndex`
- `fetchRiskAssessmentsListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `openAddRecordView`
- `showSearchView`
- `showPDFView`
- `showEmailReportView`
- `showTabView`

##### **WHSSplitViewController** - logic behind split screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `supportedInterfaceOrientations`

##### **WHSStartAuditViewController** - controls the view for start audit screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `fetchFlexibleFormWithPageID`
- `fetchOfflineConnection`
- `connection: â¦ willSendRequest`
- `connection: â¦ didReceiveResponse`
- `connection: â¦ didReceiveData`
- `connectionDidFinishLoading`
- `fetchAutoNum`
- `fetchLocationAddress`
- `handleFlexi`
- `handleAutoNumData`
- `clearLocationTypeData`
- `tablePickerDidFinishedPicking: â¦ dataPicked`
- `tableView: â¦ heightForRowAtIndexPath`
- `numberOfSectionsInTableView`
- `tableView: â¦ numberOfRowsInSection`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForHeaderInSection`
- `textView: â¦ shouldChangeTextInRange`
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
- `documentPicker: â¦ didPickDocumentAtURL`
- `documentPickerWasCancelled`
- `refreshSelectedRow`
- `imagePickerController: â¦ didFinishPickingMediaWithInfo`
- `imagePickerControllerDidCancel`
- `doneBarButtonItemDidTapped`
- `uploadAttachment`
- `clearDepartmentData`
- `cellIndexForField`

##### **WHSStartupViewController** - shows the start up screen

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `finishedValidatingUserCredentials`
- `prepareForSegue`
- `unwindToWHSStartupView`
- `isAnExistingUserLoggedIn`

##### **WHSTabViewController** - controls the tab view of the app

###### **Methods and Calculated Variables**
- `processTabFlags`
- `fetchValidTabs`
- `viewWillAppear`
- `initializeMoreOptionsBarButtonItem`
- `presentMoreOptionsActionSheet`
- `moreOptionsBarButtonItemDidTapped`

##### **WHSTablePickerViewController** - logic behind table picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchOffline`
- `tableView: â¦ cellForRowAtIndexPath`
- `tableView: â¦ estimatedHeightForRowAtIndexPath`
- `tableView: â¦ heightForRowAtIndexPath`
- `tableView: â¦ didSelectRowAtIndexPath`
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
- `deselectAllRows`

##### **WHSTemplatePickerViewController** - logic for template picker

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddTemplateView`
- `showEditTemplateView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSUtilitiesViewController** - shows the utilities

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `mailComposeController: â¦ didFinishWithResult`
- `callNumber`
- `sendEmail`
- `sendEmail: â¦ delegate`
- `openWebsite`

##### **WHSViewController** - superclass of view controllers

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewWillDisappear`
- `didReceiveMemoryWarning`
- `supportedInterfaceOrientations`
- `connection: â¦ willSendRequest`
- `connection: â¦ didReceiveResponse`
- `connection: â¦ didReceiveData`
- `connectionDidFinishLoading`
- `connection: â¦ didFailWithError`
- `clearUserData`
- `getActionsList`
- `parseActionList`
- `hamburgerBarButtonDidTapped`
- `acSheet: â¦ clickedButtonAtIndex`
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
- `moduleStateForAccessTypeString`

##### **WHSWebViewController** - controls web views

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `prepareWebView`
- `loadHTMLString: â¦ baseURL`

##### **WHSWorkerTablePickerViewController** - shows the workers 

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddWorkerView`
- `showEditWorker`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

   Bud1  Ø      Ø   0  Ð                                              
    H S A d d G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          @                                              @                                                @                                                @                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              %   # - D y n a m i c F o r m T a b l e V i e w C o n t r o l l e r . t x tIlocblob      A   .ÿÿÿÿÿÿ      - G e n e r i c T a b l e V i e w C o n t r o l l e r . t x tIlocblob      ¯   .ÿÿÿÿÿÿ     ( - M y S t o r a g e A d d N e w W o r k e r V i e w C o n t r o l l e r . t x tIlocblob        .ÿÿÿÿÿÿ     ) - M y S t o r a g e C o m p a t i b i l i t y V i e w C o n t r o l l e r . t x tIlocblob        .ÿÿÿÿÿÿ     . - M y S t o r a g e E d i t S t o r e d Q u a n t i t y V i e w C o n t r o l l e r . t x tIlocblob     ù   .ÿÿÿÿÿÿ     ' - M y S t o r a g e E S Q A d d B a t c h V i e w C o n t r o l l e r . t x tIlocblob     g   .ÿÿÿÿÿÿ     * - M y S t o r a g e E S Q A d d P a c k S i z e V i e w C o n t r o l l e r . t x tIlocblob      A   ÿÿÿÿÿÿ     + - M y S t o r a g e E S Q A d d S u p p l i e r s V i e w C o n t r o l l e r . t x tIlocblob      ¯   ÿÿÿÿÿÿ     + - M y S t o r a g e E S Q A d d U n i t S i z e s V i e w C o n t r o l l e r . t x tIlocblob        ÿÿÿÿÿÿ     + - M y S t o r a g e E S Q B a t c h D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob        ÿÿÿÿÿÿ     ) - M y S t o r a g e E S Q I n p u t V a l u e V i e w C o n t r o l l e r . t x tIlocblob     ù   ÿÿÿÿÿÿ     $ - M y S t o r a g e M a n i f e s t V i e w C o n t r o l l e r . t x tIlocblob     g   ÿÿÿÿÿÿ     # - M y S t o r a g e S u m m a r y V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     % - N e w D y n a m i c T e m p l a t e V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ      - S i g n a t u r e V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ      - S i g n O f f T a b l e V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     # - S u b m i t t e d B y T a b l e V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     * - W H S A c t i o n C a t e g o r y P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     + - W H S A c t i o n D e t a i l s   M a n a g e r V i e w C o n t r o l l e r . t x tIlocblob      A  ~ÿÿÿÿÿÿ     # - W H S A c t i o n M a n a g e r V i e w C o n t r o l l e r . t x tIlocblob      ¯  ~ÿÿÿÿÿÿ     * - W H S A c t i o n s M o n i t o r R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ     1 - W H S A c t i o n s M o n i t o r S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ     * - W H S A c t i o n s M o n i t o r S e a r c h V i e w C o n t r o l l e r . t x tIlocblob     ù  ~ÿÿÿÿÿÿ      - W H S A c t i o n V i e w C o n t r o l l e r . t x tIlocblob     g  ~ÿÿÿÿÿÿ     ' - W H S A d d A c t i o n C a t e g o r y V i e w C o n t r o l l e r . t x tIlocblob      A  îÿÿÿÿÿÿ     , - W H S A d d A I I n s p e c t i o n S u b T y p e V i e w C o n t r o l l e r . t x tIlocblob      ¯  îÿÿÿÿÿÿ     ) - W H S A d d A I I n s p e c t i o n T y p e V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ     % - W H S A d d A s s e t S u b T y p e V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ     " - W H S A d d A s s e t T y p e V i e w C o n t r o l l e r . t x tIlocblob     ù  îÿÿÿÿÿÿ     2 - W H S A d d A t m o s p h e r i c M o n i t o r i n g T y p e V i e w C o n t r o l l e r . t x tIlocblob     g  îÿÿÿÿÿÿ     $ - W H S A d d A t t a c h m e n t s V i e w C o n t r o l l e r . t x tIlocblob      A  ^ÿÿÿÿÿÿ     ! - W H S A d d A t t e n d e e V i e w C o n t r o l l e r . t x tIlocblob      ¯  ^ÿÿÿÿÿÿ     % - W H S A d d C o m p e t e n c i e s V i e w C o n t r o l l e r . t x tIlocblob       ^ÿÿÿÿÿÿ     ' - W H S A d d C o n t r o l M e a s u r e V i e w C o n t r o l l e r . t x tIlocblob       ^ÿÿÿÿÿÿ     ' - W H S A d d D y n a m i c A c t i o n s V i e w C o n t r o l l e r . t x tIlocblob     ù  ^ÿÿÿÿÿÿ     + - W H S A d d E m p l o y e e D e p a r t m e n t V i e w C o n t r o l l e r . t x tIlocblob     g  ^ÿÿÿÿÿÿ     ) - W H S A d d E m p l o y e e D i v i s i o n V i e w C o n t r o l l e r . t x tIlocblob      A  Îÿÿÿÿÿÿ                                 #   ' - W H S A d d I n s p e c t i o n T y p e V i e w C o n t r o l l e r . t x tIlocblob       Îÿÿÿÿÿÿ       - W H S A d d L i c e n c e V i e w C o n t r o l l e r . t x tIlocblob       Îÿÿÿÿÿÿ     ! - W H S A d d L o c a t i o n V i e w C o n t r o l l e r . t x tIlocblob     ù  Îÿÿÿÿÿÿ     / - W H S A d d N o i s e A s s e s s m e n t S u b T y p e V i e w C o n t r o l l e r . t x tIlocblob     g  Îÿÿÿÿÿÿ     , - W H S A d d N o i s e A s s e s s m e n t T y p e V i e w C o n t r o l l e r . t x tIlocblob      A  >ÿÿÿÿÿÿ     - - W H S A d d N o t i f i c a t i o n R e c e i v e r V i e w C o n t r o l l e r . t x tIlocblob      ¯  >ÿÿÿÿÿÿ     % - W H S A d d P o i n t s R a i s e d V i e w C o n t r o l l e r . t x tIlocblob       >ÿÿÿÿÿÿ      - W H S A d d R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       >ÿÿÿÿÿÿ      - W H S A d d W o r k e r V i e w C o n t r o l l e r . t x tIlocblob     ù  >ÿÿÿÿÿÿ     ' - W H S A I A d d P o i n t s R a i s e d V i e w C o n t r o l l e r . t x tIlocblob     g  >ÿÿÿÿÿÿ     ! - W H S A I A d d R e c o r d V i e w C o n t r o l l e r . t x tIlocblob      A  ®ÿÿÿÿÿÿ     ( - W H S A I E d i t P o i n t s R a i s e d V i e w C o n t r o l l e r . t x tIlocblob      ¯  ®ÿÿÿÿÿÿ     " - W H S A I E d i t R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       ®ÿÿÿÿÿÿ     / - W H S A i I n s p e c t i o n S u b T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob       ®ÿÿÿÿÿÿ     , - W H S A I I n s p e c t i o n T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     ù  ®ÿÿÿÿÿÿ     $ - W H S A I P o i n t s R a i s e d V i e w C o n t r o l l e r . t x tIlocblob     g  ®ÿÿÿÿÿÿ     % - W H S A I S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ      - W H S A I S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ       - W H S A I S p l i t t e d V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ      - W H S A I T a b V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     & - W H S A s s e t s A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     - - W H S A s s e t s A d d S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     * - W H S A s s e t s A d d T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     0 - W H S A s s e t s C l a s s i f i e d A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     1 - W H S A s s e t s C l a s s i f i e d E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     3 - W H S A s s e t s C l a s s i f i e d S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     , - W H S A s s e t s C l a s s i f i e d S e a r c h V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     ) - W H S A s s e t s C l a s s i f i e d T a b V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     & - W H S A s s e t s C l a s s i f i e d V i e w C o n t r o l l e r . t x tIlocblob      A  þÿÿÿÿÿÿ     ' - W H S A s s e t s E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      ¯  þÿÿÿÿÿÿ     . - W H S A s s e t s E d i t S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       þÿÿÿÿÿÿ     + - W H S A s s e t s E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       þÿÿÿÿÿÿ     0 - W H S A s s e t s E l e c t r i c a l A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ù  þÿÿÿÿÿÿ     7 - W H S A s s e t s E l e c t r i c a l A d d S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  þÿÿÿÿÿÿ     1 - W H S A s s e t s E l e c t r i c a l E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      A  nÿÿÿÿÿÿ       ) - W H S A d d E m p l o y e e D i v i s i o n V i e w C o n t r o l l e r . t x tIlocblob      A  Îÿÿÿÿÿÿ                                 #    - W H S S e t t i n g V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ      - W H S S i d e M e n u V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     $ - W H S S i t e R A C o n t r o l s V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     , - W H S S i t e R A H a z a r d s A d d H a z a r d V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     # - W H S S i t e R A H a z a r d s V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     & - W H S S i t e R A R i s k D e t a i l V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     + - W H S S i t e R A R i s k s A d d C o n t r o l V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     ' - W H S S i t e R A R i s k s R a t i n g V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     $ - W H S S i t e R A R i s k s T a b V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     ! - W H S S i t e R A R i s k s V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     4 - W H S S i t e R i s k A s e s s m e n t S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     1 - W H S S i t e R i s k A s s e s s m e n t A d d R e c o r d V i e w C o n t r o l l e r . t x tIlocblob      A  þÿÿÿÿÿÿ     2 - W H S S i t e R i s k A s s e s s m e n t E d i t R e c o r d V i e w C o n t r o l l e r . t x tIlocblob      ¯  þÿÿÿÿÿÿ     . - W H S S i t e R i s k A s s e s s m e n t S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       þÿÿÿÿÿÿ     + - W H S S i t e R i s k A s s e s s m e n t T a b V i e w C o n t r o l l e r . t x tIlocblob       þÿÿÿÿÿÿ     ( - W H S S i t e R i s k A s s e s s m e n t V i e w C o n t r o l l e r . t x tIlocblob     ù  þÿÿÿÿÿÿ      - W H S S p l i t V i e w C o n t r o l l e r . t x tIlocblob     g  þÿÿÿÿÿÿ       - W H S S t a r t A u d i t V i e w C o n t r o l l e r . t x tIlocblob      A  nÿÿÿÿÿÿ      - W H S S t a r t u p V i e w C o n t r o l l e r . t x tIlocblob      ¯  nÿÿÿÿÿÿ     ! - W H S T a b l e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob       nÿÿÿÿÿÿ      - W H S T a b V i e w C o n t r o l l e r . t x tIlocblob       nÿÿÿÿÿÿ     $ - W H S T e m p l a t e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     ù  nÿÿÿÿÿÿ      - W H S U t i l i t i e s V i e w C o n t r o l l e r . t x tIlocblob     g  nÿÿÿÿÿÿ      - W H S V i e w C o n t r o l l e r . t x tIlocblob      A  Þÿÿÿÿÿÿ      - W H S W e b V i e w C o n t r o l l e r . t x tIlocblob      ¯  Þÿÿÿÿÿÿ     ' - W H S W o r k e r T a b l e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob       Þÿÿÿÿÿÿ     0 W H S I n c i d e n t R e p o r t i n g T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     ) W H S I n s p e c t i o n T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     Õ  ~ÿÿÿÿÿÿ     # W H S L o c a t i o n P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     C  ~ÿÿÿÿÿÿ     ' W H S L o c a t i o n T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     ±  ~ÿÿÿÿÿÿ     ' W H S M a n i f e s t s R e p o r t P D F V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ     & W H S M S D S S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     Õ  îÿÿÿÿÿÿ     1 W H S N o i s e A s s e s s m e n t S u b T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     C  îÿÿÿÿÿÿ     * W H S P o l i c i e s S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     ±  îÿÿÿÿÿÿ     # W H S P r o d u c t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ   c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  þÿÿÿÿÿÿ     1 - W H S A s s e t s E l e c t r i c a l E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      A  nÿÿÿÿÿÿ       ) - W H S A d d E m p l o y e e D i v i s i o n V i e w C o n t r o l l e r . t x tIlocblob      A  Îÿÿÿÿÿÿ                                 "   3 - W H S A s s e t s E l e c t r i c a l S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       nÿÿÿÿÿÿ     , - W H S A s s e t s E l e c t r i c a l S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       nÿÿÿÿÿÿ     ) - W H S A s s e t s E l e c t r i c a l T a b V i e w C o n t r o l l e r . t x tIlocblob     ù  nÿÿÿÿÿÿ     & - W H S A s s e t s E l e c t r i c a l V i e w C o n t r o l l e r . t x tIlocblob     g  nÿÿÿÿÿÿ     - - W H S A s s e t s L i f t i n g A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      A  Þÿÿÿÿÿÿ     . - W H S A s s e t s L i f t i n g E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      ¯  Þÿÿÿÿÿÿ     0 - W H S A s s e t s L i f t i n g S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       Þÿÿÿÿÿÿ     ) - W H S A s s e t s L i f t i n g S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       Þÿÿÿÿÿÿ     & - W H S A s s e t s L i f t i n g T a b V i e w C o n t r o l l e r . t x tIlocblob     ù  Þÿÿÿÿÿÿ     # - W H S A s s e t s L i f t i n g V i e w C o n t r o l l e r . t x tIlocblob     g  Þÿÿÿÿÿÿ     + - W H S A s s e t s P l a n t A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      A  Nÿÿÿÿÿÿ     2 - W H S A s s e t s P l a n t A d d S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      ¯  Nÿÿÿÿÿÿ     , - W H S A s s e t s P l a n t E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       Nÿÿÿÿÿÿ     3 - W H S A s s e t s P l a n t E d i t S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       Nÿÿÿÿÿÿ     . - W H S A s s e t s P l a n t S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     ù  Nÿÿÿÿÿÿ     ' - W H S A s s e t s P l a n t S e a r c h V i e w C o n t r o l l e r . t x tIlocblob     g  Nÿÿÿÿÿÿ     $ - W H S A s s e t s P l a n t T a b V i e w C o n t r o l l e r . t x tIlocblob      A  ¾ÿÿÿÿÿÿ     ! - W H S A s s e t s P l a n t V i e w C o n t r o l l e r . t x tIlocblob      ¯  ¾ÿÿÿÿÿÿ     / - W H S A s s e t s S e a r c h R e c o r d R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       ¾ÿÿÿÿÿÿ     ( - W H S A s s e t s S e a r c h R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       ¾ÿÿÿÿÿÿ     * - W H S A s s e t s S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     ù  ¾ÿÿÿÿÿÿ     ' - W H S A s s e t s T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  ¾ÿÿÿÿÿÿ     ( - W H S A s s e t S u b T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob      A  .ÿÿÿÿÿÿ     . - W H S A s s e t s V e h i c l e s A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      ¯  .ÿÿÿÿÿÿ     / - W H S A s s e t s V e h i c l e s E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       .ÿÿÿÿÿÿ     7 - W H S A s s e t s V e h i c l e s S e a r c h R e c o r d R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       .ÿÿÿÿÿÿ     0 - W H S A s s e t s V e h i c l e s S e a r c h R e c o r d V i e w C o n t r o l l e r . t x tIlocblob     ù  .ÿÿÿÿÿÿ     ' - W H S A s s e t s V e h i c l e s T a b V i e w C o n t r o l l e r . t x tIlocblob     g  .ÿÿÿÿÿÿ     $ - W H S A s s e t s V e h i c l e s V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ      - W H S A s s e t s V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     % - W H S A s s e t T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     ? - W H S A t m o s p h e r i c M o n i t o r i n g A d d M o n i t o r i n g H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     4 - W H S A t m o s p h e r i c M o n i t o r i n g A d d R e c o r d V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     @ - W H S A t m o s p h e r i c M o n i t o r i n g E d i t M o n i t o r i n g H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ                         !   2 - W H S A t m o s p h e r i c M o n i t o r i n g H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     . - W H S A t m o s p h e r i c M o n i t o r i n g T a b V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     5 - W H S A t m o s p h e r i c M o n i t o r i n g T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     ! - W H S A t t a c h m e n t s V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     , - W H S A t t e n d e e s S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     % - W H S A t t e n d e e s S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      A  ~ÿÿÿÿÿÿ      - W H S A t t e n d e e s V i e w C o n t r o l l e r . t x tIlocblob      ¯  ~ÿÿÿÿÿÿ     - - W H S A u d i t I n s p e c t i o n s D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ     , - W H S A u d i t I n s p e c t i o n s R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ       - W H S A u t o H a z a r d V i e w C o n t r o l l e r . t x tIlocblob     ù  ~ÿÿÿÿÿÿ     " - W H S C a u s e H a z a r d s V i e w C o n t r o l l e r . t x tIlocblob     g  ~ÿÿÿÿÿÿ     $ - W H S C h a n g e P a s s w o r d V i e w C o n t r o l l e r . t x tIlocblob      A  îÿÿÿÿÿÿ      - W H S C h e c k l i s t V i e w C o n t r o l l e r . t x tIlocblob      ¯  îÿÿÿÿÿÿ     2 - W H S C h e m i c a l Q C h a r t C h e m i c a l S a f e t y V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ     + - W H S C h e m i c a l Q C h a r t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ     * - W H S C h e m i c a l Q C h a r t D e t a i l V i e w C o n t r o l l e r . t x tIlocblob     ù  îÿÿÿÿÿÿ     + - W H S C h e m i c a l Q C h a r t H a z a r d s V i e w C o n t r o l l e r . t x tIlocblob     g  îÿÿÿÿÿÿ     5 - W H S C h e m i c a l Q C h a r t O p e r a t i o n a l S a f e t y V i e w C o n t r o l l e r . t x tIlocblob      A  	^ÿÿÿÿÿÿ     1 - W H S C h e m i c a l Q C h a r t S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      ¯  	^ÿÿÿÿÿÿ     * - W H S C h e m i c a l Q C h a r t S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       	^ÿÿÿÿÿÿ     ' - W H S C h e m i c a l Q C h a r t T a b V i e w C o n t r o l l e r . t x tIlocblob       	^ÿÿÿÿÿÿ     $ - W H S C h e m i c a l Q C h a r t V i e w C o n t r o l l e r . t x tIlocblob     ù  	^ÿÿÿÿÿÿ     4 - W H S C h e m i c a l R e g i s t e r P r o d u c t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     g  	^ÿÿÿÿÿÿ     & - W H S C h e m i c a l R e g i s t e r V i e w C o n t r o l l e r . t x tIlocblob      A  	Îÿÿÿÿÿÿ     8 - W H S C h e m i c a l R i s k A s s e s s m e n t C o n s e q u e n c e s V i e w C o n t r o l l e r . t x tIlocblob      ¯  	Îÿÿÿÿÿÿ     ; - W H S C h e m i c a l R i s k A s s e s s m e n t C u r r e n t C o n t r o l s V i e w C o n t r o l l e r . t x tIlocblob       	Îÿÿÿÿÿÿ     2 - W H S C h e m i c a l R i s k A s s e s s m e n t D e t a i l V i e w C o n t r o l l e r . t x tIlocblob       	Îÿÿÿÿÿÿ     ? - W H S C h e m i c a l R i s k A s s e s s m e n t H a z a r d s C o n s e q u e n c e s V i e w C o n t r o l l e r . t x tIlocblob     ù  	Îÿÿÿÿÿÿ     3 - W H S C h e m i c a l R i s k A s s e s s m e n t H a z a r d s V i e w C o n t r o l l e r . t x tIlocblob     g  	Îÿÿÿÿÿÿ     7 - W H S C h e m i c a l R i s k A s s e s s m e n t N e w C o n t r o l s V i e w C o n t r o l l e r . t x tIlocblob      A  
>ÿÿÿÿÿÿ     A - W H S C h e m i c a l R i s k A s s e s s m e n t P r o d u c t E x p o s u r e L i m i t s V i e w C o n t r o l l e r . t x tIlocblob      ¯  
>ÿÿÿÿÿÿ     3 - W H S C h e m i c a l R i s k A s s e s s m e n t P r o d u c t V i e w C o n t r o l l e r . t x tIlocblob       
>ÿÿÿÿÿÿ     9 - W H S C h e m i c a l R i s k A s s e s s m e n t S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       
>ÿÿÿÿÿÿ                     "   / - W H S C h e m i c a l R i s k A s s e s s m e n t T a b V i e w C o n t r o l l e r . t x tIlocblob     g  
>ÿÿÿÿÿÿ     , - W H S C h e m i c a l R i s k A s s e s s m e n t V i e w C o n t r o l l e r . t x tIlocblob      A  
®ÿÿÿÿÿÿ     , - W H S C h e m i c a l R i s k M a n a g e m e n t V i e w C o n t r o l l e r . t x tIlocblob      ¯  
®ÿÿÿÿÿÿ      - W H S C h e m i c a l s V i e w C o n t r o l l e r . t x tIlocblob       
®ÿÿÿÿÿÿ     * - W H S C o m p a t i b i l i t y L e g e n d s V i e w C o n t r o l l e r . t x tIlocblob       
®ÿÿÿÿÿÿ     & - W H S C o m p a t i b i l i t y P D F V i e w C o n t r o l l e r . t x tIlocblob     ù  
®ÿÿÿÿÿÿ     1 - W H S C o m p a t i b i l i t y P r o d u c t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     g  
®ÿÿÿÿÿÿ     , - W H S C o m p a t i b i l i t y R e p o r t P D F V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     ( - W H S C o m p e t e n c i e s P i c k e r V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     * - W H S C o n f i n e d S p a c e s A c t i o n V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     - - W H S C o n f i n e d S p a c e s A d d A c t i o n V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     , - W H S C o n f i n e d S p a c e s A d d E n t r y V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     - - W H S C o n f i n e d S p a c e s A d d R e c o r d V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     . - W H S C o n f i n e d S p a c e s E d i t A c t i o n V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     - - W H S C o n f i n e d S p a c e s E d i t E n t r y V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     . - W H S C o n f i n e d S p a c e s E d i t R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     + - W H S C o n f i n e d S p a c e s E n t r i e s V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     5 - W H S C o n f i n e d S p a c e s M o n i t o r i n g H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     1 - W H S C o n f i n e d S p a c e s P e r m i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     + - W H S C o n f i n e d S p a c e s P e r m i t s V i e w C o n t r o l l e r . t x tIlocblob      A  þÿÿÿÿÿÿ     ' - W H S C o n f i n e d S p a c e s T a b V i e w C o n t r o l l e r . t x tIlocblob      ¯  þÿÿÿÿÿÿ     / - W H S C o n t r o l M e a s u r e T a b l e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob       þÿÿÿÿÿÿ      - W H S D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       þÿÿÿÿÿÿ     $ - W H S D y n a m i c A c t i o n s V i e w C o n t r o l l e r . t x tIlocblob     ù  þÿÿÿÿÿÿ     ( - W H S D y n a m i c S i g n A c t i o n s V i e w C o n t r o l l e r . t x tIlocblob     g  þÿÿÿÿÿÿ     $ - W H S D y n a m i c S i g n e e s V i e w C o n t r o l l e r . t x tIlocblob      A  nÿÿÿÿÿÿ     & - W H S D y n a m i c T e m p l a t e s V i e w C o n t r o l l e r . t x tIlocblob      ¯  nÿÿÿÿÿÿ     ( - W H S E d i t A c t i o n C a t e g o r y V i e w C o n t r o l l e r . t x tIlocblob       nÿÿÿÿÿÿ     - - W H S E d i t A I I n s p e c t i o n S u b T y p e V i e w C o n t r o l l e r . t x tIlocblob       nÿÿÿÿÿÿ     * - W H S E d i t A I I n s p e c t i o n T y p e V i e w C o n t r o l l e r . t x tIlocblob     ù  nÿÿÿÿÿÿ     & - W H S E d i t A s s e t S u b T y p e V i e w C o n t r o l l e r . t x tIlocblob     g  nÿÿÿÿÿÿ     # - W H S E d i t A s s e t T y p e V i e w C o n t r o l l e r . t x tIlocblob      A  Þÿÿÿÿÿÿ     3 - W H S E d i t A t m o s p h e r i c M o n i t o r i n g T y p e V i e w C o n t r o l l e r . t x tIlocblob      ¯  Þÿÿÿÿÿÿ     % - W H S E d i t A t t a c h m e n t s V i e w C o n t r o l l e r . t x tIlocblob       Þÿÿÿÿÿÿ   a l R i s k A s s e s s m e n t S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       
>ÿÿÿÿÿÿ                     !   , - W H S E d i t E m p l o y e e D e p a r t m e n t V i e w C o n t r o l l e r . t x tIlocblob     ù  Þÿÿÿÿÿÿ     * - W H S E d i t E m p l o y e e D i v i s i o n V i e w C o n t r o l l e r . t x tIlocblob     g  Þÿÿÿÿÿÿ     ! - W H S E d i t G e n e r i c V i e w C o n t r o l l e r . t x tIlocblob      A  
Nÿÿÿÿÿÿ     ( - W H S E d i t I n s p e c t i o n T y p e V i e w C o n t r o l l e r . t x tIlocblob      ¯  
Nÿÿÿÿÿÿ     ! - W H S E d i t L i c e n c e V i e w C o n t r o l l e r . t x tIlocblob       
Nÿÿÿÿÿÿ     0 - W H S E d i t N o i s e A s s e s s m e n t S u b T y p e V i e w C o n t r o l l e r . t x tIlocblob       
Nÿÿÿÿÿÿ     - - W H S E d i t N o i s e A s s e s s m e n t T y p e V i e w C o n t r o l l e r . t x tIlocblob     ù  
Nÿÿÿÿÿÿ     . - W H S E d i t N o t i f i c a t i o n R e c e i v e r V i e w C o n t r o l l e r . t x tIlocblob     g  
Nÿÿÿÿÿÿ     & - W H S E d i t P o i n t s R a i s e d V i e w C o n t r o l l e r . t x tIlocblob      A  
¾ÿÿÿÿÿÿ       - W H S E d i t W o r k e r V i e w C o n t r o l l e r . t x tIlocblob      ¯  
¾ÿÿÿÿÿÿ     ! - W H S E m a i l R e p o r t V i e w C o n t r o l l e r . t x tIlocblob       
¾ÿÿÿÿÿÿ     ( - W H S E m e r g e n c y P r o c e d u r e V i e w C o n t r o l l e r . t x tIlocblob       
¾ÿÿÿÿÿÿ     / - W H S E m p l o y e e A d d S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     ù  
¾ÿÿÿÿÿÿ     , - W H S E m p l o y e e A d d T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  
¾ÿÿÿÿÿÿ     5 - W H S E m p l o y e e C o n t r a c t o r C o m p a n y P i c k e r V i e w C o n t r o l l e r . t x tIlocblob      A  .ÿÿÿÿÿÿ     . - W H S E m p l o y e e D e p a r t m e n t P i c k e r V i e w C o n t r o l l e r . t x tIlocblob      ¯  .ÿÿÿÿÿÿ     0 - W H S E m p l o y e e E d i t S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       .ÿÿÿÿÿÿ     - - W H S E m p l o y e e E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       .ÿÿÿÿÿÿ     , - W H S E m p l o y e e S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     ù  .ÿÿÿÿÿÿ     ) - W H S E m p l o y e e T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  .ÿÿÿÿÿÿ     E - W H S E n v i r o n m e n t a l A t m o s p h e r i c M o n i t o r i n g S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     > - W H S E n v i r o n m e n t a l A t m o s p h e r i c M o n i t o r i n g S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     8 - W H S E n v i r o n m e n t a l A t m o s p h e r i c M o n i t o r i n g V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     > - W H S E n v i r o n m e n t a l C o n f i n e d S p a c e s S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     7 - W H S E n v i r o n m e n t a l C o n f i n e d S p a c e s S e a r c h V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     1 - W H S E n v i r o n m e n t a l C o n f i n e d S p a c e s V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     * - W H S E n v i r o n m e n t a l D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     < - W H S E n v i r o n m e n t a l N o i s e C o n t r o l S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     5 - W H S E n v i r o n m e n t a l N o i s e C o n t r o l S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     / - W H S E n v i r o n m e n t a l N o i s e C o n t r o l V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     ) - W H S E n v i r o n m e n t a l S e a r c h V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     # - W H S E n v i r o n m e n t a l V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     ' - W H S E x p o s u r e L i m i t s A d d V i e w C o n t r o l l e r . t x tIlocblob      A  ~ÿÿÿÿÿÿ                     $ - W H S E x p o s u r e L i m i t s V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ     - - W H S F i r e F i g h t i n g C l a s s P i c k e r V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ     . - W H S F i r e F i g h t i n g R a t i n g P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     ù  ~ÿÿÿÿÿÿ     # - W H S G e n e r i c P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     g  ~ÿÿÿÿÿÿ     " - W H S G r o u p e d T a b l e V i e w C o n t r o l l e r . t x tIlocblob      A  îÿÿÿÿÿÿ     / - W H S H a z a r d s A s b e s t o s A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      ¯  îÿÿÿÿÿÿ     9 - W H S H a z a r d s A s b e s t o s A d d I n s p e c t i o n H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ     6 - W H S H a z a r d s A s b e s t o s A d d R e m o v a l H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ     0 - W H S H a z a r d s A s b e s t o s E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ù  îÿÿÿÿÿÿ     : - W H S H a z a r d s A s b e s t o s E d i t I n s p e c t i o n H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  îÿÿÿÿÿÿ     7 - W H S H a z a r d s A s b e s t o s E d i t R e m o v a l H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      A  ^ÿÿÿÿÿÿ     6 - W H S H a z a r d s A s b e s t o s I n s p e c t i o n H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      ¯  ^ÿÿÿÿÿÿ     3 - W H S H a z a r d s A s b e s t o s R e m o v a l H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       ^ÿÿÿÿÿÿ     / - W H S H a z a r d s A s b e s t o s S e a r c h F o r m V i e w C o n t r o l l e r . t x tIlocblob       ^ÿÿÿÿÿÿ     2 - W H S H a z a r d s A s b e s t o s S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     ù  ^ÿÿÿÿÿÿ     ( - W H S H a z a r d s A s b e s t o s T a b V i e w C o n t r o l l e r . t x tIlocblob     g  ^ÿÿÿÿÿÿ     % - W H S H a z a r d s A s b e s t o s V i e w C o n t r o l l e r . t x tIlocblob      A  Îÿÿÿÿÿÿ     ; - W H S H a z a r d s C a r c i n o g e n s A d d E m p l o y e e E x p o s u r e V i e w C o n t r o l l e r . t x tIlocblob      ¯  Îÿÿÿÿÿÿ     1 - W H S H a z a r d s C a r c i n o g e n s A d d R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       Îÿÿÿÿÿÿ     < - W H S H a z a r d s C a r c i n o g e n s E d i t E m p l o y e e E x p o s u r e V i e w C o n t r o l l e r . t x tIlocblob       Îÿÿÿÿÿÿ     2 - W H S H a z a r d s C a r c i n o g e n s E d i t R e c o r d V i e w C o n t r o l l e r . t x tIlocblob     ù  Îÿÿÿÿÿÿ     8 - W H S H a z a r d s C a r c i n o g e n s E m p l o y e e E x p o s u r e V i e w C o n t r o l l e r . t x tIlocblob     g  Îÿÿÿÿÿÿ     2 - W H S H a z a r d s C a r c i n o g e n s S e a r c h F o r m V i e w C o n t r o l l e r . t x tIlocblob      A  >ÿÿÿÿÿÿ     5 - W H S H a z a r d s C a r c i n o g e n s S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       Ëÿÿÿÿÿÿÿÿ   + - W H S H a z a r d s C a r c i n o g e n s T a b V i e w C o n t r o l l e r . t x tIlocblob     o  Ëÿÿÿÿÿÿÿÿ   ( - W H S H a z a r d s C a r c i n o g e n s V i e w C o n t r o l l e r . t x tIlocblob     Ý  Ëÿÿÿÿÿÿÿÿ   $ - W H S H a z a r d s D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      ¯  >ÿÿÿÿÿÿ     ' - W H S H a z a r d s S e a r c h F o r m V i e w C o n t r o l l e r . t x tIlocblob       >ÿÿÿÿÿÿ     * - W H S H a z a r d s S e a r c h R e s u t l s V i e w C o n t r o l l e r . t x tIlocblob       >ÿÿÿÿÿÿ      - W H S H a z a r d s V i e w C o n t r o l l e r . t x tIlocblob     ù  >ÿÿÿÿÿÿ     8 - W H S I n c i d e n t R e p o r t i n g A d d i t i o n a l D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     K  Ëÿÿÿÿÿÿÿÿ   4 - W H S I n c i d e n t R e p o r t i n g A d d N e w H a z a r d s V i e w C o n t r o l l e r . t x tIlocblob     ¹  Ëÿÿÿÿÿÿÿÿ e r . t x tIlocblob      A  ~ÿÿÿÿÿÿ                 !   0 - W H S I n c i d e n t R e p o r t i n g A d d R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       ;ÿÿÿÿÿÿÿÿ   . - W H S I n c i d e n t R e p o r t i n g A d d T y p e V i e w C o n t r o l l e r . t x tIlocblob     o  ;ÿÿÿÿÿÿÿÿ   . - W H S I n c i d e n t R e p o r t i n g D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     Ý  ;ÿÿÿÿÿÿÿÿ   < - W H S I n c i d e n t R e p o r t i n g E d i t A d d i t i o n a l D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     K  ;ÿÿÿÿÿÿÿÿ   2 - W H S I n c i d e n t R e p o r t i n g E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ¹  ;ÿÿÿÿÿÿÿÿ   2 - W H S I n c i d e n t R e p o r t i n g E d i t H a z a r d s V i e w C o n t r o l l e r . t x tIlocblob     g  >ÿÿÿÿÿÿ     / - W H S I n c i d e n t R e p o r t i n g E d i t T y p e V i e w C o n t r o l l e r . t x tIlocblob      A  ®ÿÿÿÿÿÿ     2 - W H S I n c i d e n t R e p o r t i n g E d i t W i t n e s s V i e w C o n t r o l l e r . t x tIlocblob      ¯  ®ÿÿÿÿÿÿ     - - W H S I n c i d e n t R e p o r t i n g R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       ®ÿÿÿÿÿÿ      - W H S L a n d i n g V i e w C o n t r o l l e r . t x tIlocblob       ®ÿÿÿÿÿÿ     % - W H S L e g i s l a t i o n s T a b V i e w C o n t r o l l e r . t x tIlocblob     ù  ®ÿÿÿÿÿÿ     # - W H S L i c e n c e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     g  ®ÿÿÿÿÿÿ      - W H S L o g i n V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     / - W H S N o i s e C o n t r o l A d d A s s e s s m e n t V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     , - W H S N o i s e C o n t r o l A d d C o n t r o l V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     + - W H S N o i s e C o n t r o l A d d R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     3 - W H S N o i s e C o n t r o l A s s e s s m e n t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     7 - W H S N o i s e C o n t r o l E d i t A s s e s s m e n t C o m m e n t V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     1 - W H S N o i s e C o n t r o l E d i t M e a s u r e m e n t V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     , - W H S N o i s e C o n t r o l E d i t R e c o r d V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     , - W H S N o i s e C o n t r o l N e w C o n t r o l V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     % - W H S N o i s e C o n t r o l T a b V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     : - W H S N o n C h e m i c a l R i s k A s s e s s m e n t N e w C o n t r o l s V i e w C o n t r o l l e r . t x tIlocblob     '  ;ÿÿÿÿÿÿÿÿ   < - W H S N o n C h e m i c a l R i s k A s s e s s m e n t S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       «ÿÿÿÿÿÿÿÿ   5 - W H S N o n C h e m i c a l R i s k A s s e s s m e n t S e a r c h V i e w C o n t r o l l e r . t x tIlocblob     o  «ÿÿÿÿÿÿÿÿ   2 - W H S N o n C h e m i c a l R i s k A s s e s s m e n t T a b V i e w C o n t r o l l e r . t x tIlocblob     Ý  «ÿÿÿÿÿÿÿÿ   / - W H S N o n C h e m i c a l R i s k A s s e s s m e n t V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     / - W H S N o n C h e m i c a l R i s k M a n a g e m e n t V i e w C o n t r o l l e r . t x tIlocblob     K  «ÿÿÿÿÿÿÿÿ   0 - W H S P A P C o m p l a i n t s S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     ) - W H S P A P C o m p l a i n t s S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      A  þÿÿÿÿÿÿ     & - W H S P A P C o m p l a i n t s T a b V i e w C o n t r o l l e r . t x tIlocblob     ¹  «ÿÿÿÿÿÿÿÿ     - W H S P A P D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     '  «ÿÿÿÿÿÿÿÿ   , - W H S P A P D r i l l s S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      ¯  þÿÿÿÿÿÿ        A  ~ÿÿÿÿÿÿ                 $   " - W H S P A P D r i l l s T a b V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿÿÿ   2 - W H S P A P L e g i s l a t i o n s S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       þÿÿÿÿÿÿ     + - W H S P A P L e g i s l a t i o n s S e a r c h V i e w C o n t r o l l e r . t x tIlocblob     ù  þÿÿÿÿÿÿ     + - W H S P A P P l a n s P r o c e d u r e s T a b V i e w C o n t r o l l e r . t x tIlocblob     Õ   .ÿÿÿÿÿÿ     + - W H S P A P P l a n s S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     g  þÿÿÿÿÿÿ     $ - W H S P A P P l a n s S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      A  nÿÿÿÿÿÿ     & - W H S P A P S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     C   .ÿÿÿÿÿÿ     . - W H S P A P T r a i n i n g S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      ¯  nÿÿÿÿÿÿ     & - W H S P A P T r a n i n g S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       nÿÿÿÿÿÿ     # - W H S P D F A d d S i g n e e s V i e w C o n t r o l l e r . t x tIlocblob       nÿÿÿÿÿÿ     # - W H S P D F E d i t S i g n e e V i e w C o n t r o l l e r . t x tIlocblob     ù  nÿÿÿÿÿÿ       - W H S P D F S i g n e e s V i e w C o n t r o l l e r . t x tIlocblob     g  nÿÿÿÿÿÿ     $ - W H S P o l i c i e s S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      A  Þÿÿÿÿÿÿ     & - W H S P o l i c i e s T r a i n i n g V i e w C o n t r o l l e r . t x tIlocblob     ±   .ÿÿÿÿÿÿ      - W H S P o l i c i e s V i e w C o n t r o l l e r . t x tIlocblob        .ÿÿÿÿÿÿ     # - W H S P r o j e c t P i c k e r V i e w C o n t r o l l e r . t x tIlocblob      ¯  Þÿÿÿÿÿÿ      - W H S R e c o r d V i e w C o n t r o l l e r . t x tIlocblob       Þÿÿÿÿÿÿ     + - W H S R e g i s t e r A c t i o n D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     Õ   ÿÿÿÿÿÿ     + - W H S R e g i s t e r A c t i o n M a n a g e r V i e w C o n t r o l l e r . t x tIlocblob     C   ÿÿÿÿÿÿ     % - W H S R e g i s t e r A c t i o n s V i e w C o n t r o l l e r . t x tIlocblob     ±   ÿÿÿÿÿÿ     ( - W H S R e g i s t e r A d d A c t i o n s V i e w C o n t r o l l e r . t x tIlocblob        ÿÿÿÿÿÿ     ' - W H S R e g i s t e r A d d A c t i o n V i e w C o n t r o l l e r . t x tIlocblob     Õ  ÿÿÿÿÿÿ     , - W H S R e g i s t e r A d d S e r v i c e T y p e V i e w C o n t r o l l e r . t x tIlocblob     C  ÿÿÿÿÿÿ     ) - W H S R e g i s t e r A d d T e s t T y p e V i e w C o n t r o l l e r . t x tIlocblob     ±  ÿÿÿÿÿÿ     - - W H S R e g i s t e r E d i t S e r v i c e T y p e V i e w C o n t r o l l e r . t x tIlocblob       Þÿÿÿÿÿÿ     * - W H S R e g i s t e r E d i t T e s t T y p e V i e w C o n t r o l l e r . t x tIlocblob     ù  Þÿÿÿÿÿÿ     / - W H S R e g i s t e r S e r v i c e T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob     g  Þÿÿÿÿÿÿ      - W H S R e g i s t e r s V i e w C o n t r o l l e r . t x tIlocblob      A  Nÿÿÿÿÿÿ     0 - W H S R e g i s t e r T e s t H i s t o r y D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      ¯  Nÿÿÿÿÿÿ     ) - W H S R e g i s t e r T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       Nÿÿÿÿÿÿ     , - W H S R e g i s t e r T e s t T y p e P i c k e r V i e w C o n t r o l l e r . t x tIlocblob       Nÿÿÿÿÿÿ     $ - W H S R e p o r t I n c i d e n t V i e w C o n t r o l l e r . t x tIlocblob     ù  Nÿÿÿÿÿÿ     $ - W H S R i c h T e x t E d i t o r V i e w C o n t r o l l e r . t x tIlocblob     g  Nÿÿÿÿÿÿ     , - W H S R i s k A s s e s s m e n t P i c t u r e s V i e w C o n t r o l l e r . t x tIlocblob      A  ¾ÿÿÿÿÿÿ     $ - W H S R i s k M a n a g e m e n t V i e w C o n t r o l l e r . t x tIlocblob      ¯  ¾ÿÿÿÿÿÿ     6 - W H S S a f e t y E m e r g e n c y W a s h i n g A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       ¾ÿÿÿÿÿÿ   o l l e r . t x tIlocblob      ¯  þÿÿÿÿÿÿ        A  ~ÿÿÿÿÿÿ                    7 - W H S S a f e t y E m e r g e n c y W a s h i n g E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ù  ¾ÿÿÿÿÿÿ     ; - W H S S a f e t y E m e r g e n c y W a s h i n g E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  ¾ÿÿÿÿÿÿ     9 - W H S S a f e t y E m e r g e n c y W a s h i n g S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      A  .ÿÿÿÿÿÿ     2 - W H S S a f e t y E m e r g e n c y W a s h i n g S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      ¯  .ÿÿÿÿÿÿ     / - W H S S a f e t y E m e r g e n c y W a s h i n g T a b V i e w C o n t r o l l e r . t x tIlocblob       .ÿÿÿÿÿÿ     , - W H S S a f e t y E m e r g e n c y W a s h i n g V i e w C o n t r o l l e r . t x tIlocblob       .ÿÿÿÿÿÿ     3 - W H S S a f e t y F i r e D e t e c t i o n A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ù  .ÿÿÿÿÿÿ     7 - W H S S a f e t y F i r e D e t e c t i o n A d d T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  .ÿÿÿÿÿÿ     4 - W H S S a f e t y F i r e D e t e c t i o n E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     8 - W H S S a f e t y F i r e D e t e c t i o n E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     6 - W H S S a f e t y F i r e D e t e c t i o n S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     / - W H S S a f e t y F i r e D e t e c t i o n S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     , - W H S S a f e t y F i r e D e t e c t i o n T a b V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     ) - W H S S a f e t y F i r e D e t e c t i o n V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     2 - W H S S a f e t y F i r e F i g h t i n g A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ     6 - W H S S a f e t y F i r e F i g h t i n g A d d T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      ¯  ÿÿÿÿÿÿ     3 - W H S S a f e t y F i r e F i g h t i n g E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     7 - W H S S a f e t y F i r e F i g h t i n g E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       ÿÿÿÿÿÿ     5 - W H S S a f e t y F i r e F i g h t i n g S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     ù  ÿÿÿÿÿÿ     . - W H S S a f e t y F i r e F i g h t i n g S e a r c h V i e w C o n t r o l l e r . t x tIlocblob     g  ÿÿÿÿÿÿ     + - W H S S a f e t y F i r e F i g h t i n g T a b V i e w C o n t r o l l e r . t x tIlocblob      A  ~ÿÿÿÿÿÿ     ( - W H S S a f e t y F i r e F i g h t i n g V i e w C o n t r o l l e r . t x tIlocblob      ¯  ~ÿÿÿÿÿÿ     . - W H S S a f e t y F i r s t A i d A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ     2 - W H S S a f e t y F i r s t A i d A d d T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ     / - W H S S a f e t y F i r s t A i d E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ù  ~ÿÿÿÿÿÿ     3 - W H S S a f e t y F i r s t A i d E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  ~ÿÿÿÿÿÿ     1 - W H S S a f e t y F i r s t A i d S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      A  îÿÿÿÿÿÿ     * - W H S S a f e t y F i r s t A i d S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      ¯  îÿÿÿÿÿÿ     ' - W H S S a f e t y F i r s t A i d T a b V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ     $ - W H S S a f e t y F i r s t A i d V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ     ) - W H S S a f e t y P P E A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ù  îÿÿÿÿÿÿ    ¾ÿÿÿÿÿÿ   o l l e r . t x tIlocblob      ¯  þÿÿÿÿÿÿ        A  ~ÿÿÿÿÿÿ                    - - W H S S a f e t y P P E A d d T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      A  ^ÿÿÿÿÿÿ     * - W H S S a f e t y P P E E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob      ¯  ^ÿÿÿÿÿÿ     + - W H S S a f e t y P P E E d i t E m p l o y e e V i e w C o n t r o l l e r . t x tIlocblob       ^ÿÿÿÿÿÿ     . - W H S S a f e t y P P E E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       ^ÿÿÿÿÿÿ     ' - W H S S a f e t y P P E E m p l o y e e V i e w C o n t r o l l e r . t x tIlocblob     ù  ^ÿÿÿÿÿÿ     , - W H S S a f e t y P P E S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob     g  ^ÿÿÿÿÿÿ     % - W H S S a f e t y P P E S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      A  Îÿÿÿÿÿÿ     " - W H S S a f e t y P P E T a b V i e w C o n t r o l l e r . t x tIlocblob      ¯  Îÿÿÿÿÿÿ     * - W H S S a f e t y S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       Îÿÿÿÿÿÿ     . - W H S S a f e t y S p i l l K i t A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       Îÿÿÿÿÿÿ     2 - W H S S a f e t y S p i l l K i t A d d T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     ù  Îÿÿÿÿÿÿ     / - W H S S a f e t y S p i l l K i t E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     g  Îÿÿÿÿÿÿ     3 - W H S S a f e t y S p i l l K i t E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      A  >ÿÿÿÿÿÿ     1 - W H S S a f e t y S p i l l K i t S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      ¯  >ÿÿÿÿÿÿ     * - W H S S a f e t y S p i l l K i t S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       >ÿÿÿÿÿÿ     ' - W H S S a f e t y S p i l l K i t T a b V i e w C o n t r o l l e r . t x tIlocblob       >ÿÿÿÿÿÿ     $ - W H S S a f e t y S p i l l K i t V i e w C o n t r o l l e r . t x tIlocblob     ù  >ÿÿÿÿÿÿ      - W H S S a f e t y T a b V i e w C o n t r o l l e r . t x tIlocblob     g  >ÿÿÿÿÿÿ     ' - W H S S a f e t y T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      A  ®ÿÿÿÿÿÿ     . - W H S S a f e W o r k P r o c e d u r e s A c t i o n V i e w C o n t r o l l e r . t x tIlocblob      ¯  ®ÿÿÿÿÿÿ     , - W H S S a f e W o r k P r o c e d u r e s L i s t V i e w C o n t r o l l e r . t x tIlocblob       ®ÿÿÿÿÿÿ     ( - W H S S a f e W o r k P r o c e d u r e s V i e w C o n t r o l l e r . t x tIlocblob       ®ÿÿÿÿÿÿ     " - W H S S e a r c h R e c o r d V i e w C o n t r o l l e r . t x tIlocblob     ù  ®ÿÿÿÿÿÿ     ) - W H S S e a r c h R e s u l t s R e c o r d V i e w C o n t r o l l e r . t x tIlocblob     g  ®ÿÿÿÿÿÿ      A  ~ÿÿÿÿÿÿ     ( - W H S S a f e t y F i r e F i g h t i n g V i e w C o n t r o l l e r . t x tIlocblob      ¯  ~ÿÿÿÿÿÿ     . - W H S S a f e t y F i r s t A i d A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ     2 - W H S S a f e t y F i r s t A i d A d d T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       ~ÿÿÿÿÿÿ     / - W H S S a f e t y F i r s t A i d E d i t D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ù  ~ÿÿÿÿÿÿ     3 - W H S S a f e t y F i r s t A i d E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob     g  ~ÿÿÿÿÿÿ     1 - W H S S a f e t y F i r s t A i d S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      A  îÿÿÿÿÿÿ     * - W H S S a f e t y F i r s t A i d S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      ¯  îÿÿÿÿÿÿ     ' - W H S S a f e t y F i r s t A i d T a b V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ     $ - W H S S a f e t y F i r s t A i d V i e w C o n t r o l l e r . t x tIlocblob       îÿÿÿÿÿÿ     ) - W H S S a f e t y P P E A d d D e t a i l s V i e w C o n t r o l l e r . t x tIlocblob     ù  îÿÿÿÿÿÿ    ¾ÿÿÿÿÿÿ   o l l e r . t x tIlocblob      ¯  þÿÿÿÿÿÿ        A  ~ÿÿÿÿÿÿ                        - W H S A d d G e n e r i c V i e w C o n t r o l l e r . t x tIlocblob      ¯  Îÿÿÿÿÿÿ        8 - W H S A s s e t s E l e c t r i c a l E d i t S e r v i c e H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      ¯  nÿÿÿÿÿÿ        5 - W H S A t m o s p h e r i c M o n i t o r i n g E d i t R e c o r d V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ        2 - W H S C h e m i c a l R i s k A s s e s s m e n t S e a r c h V i e w C o n t r o l l e r . t x tIlocblob     ù  
>ÿÿÿÿÿÿ        " - W H S E d i t A t t e n d e e V i e w C o n t r o l l e r . t x tIlocblob       Þÿÿÿÿÿÿ     	   1 - W H S E x p o s u r e L i m i t s S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      ¯  ~ÿÿÿÿÿÿ     
   4 - W H S I n c i d e n t R e p o r t i n g A d d N e w W i t n e s s V i e w C o n t r o l l e r . t x tIlocblob     '  Ëÿÿÿÿÿÿÿÿ      % - W H S P A P D r i l l s S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       þÿÿÿÿÿÿ        : - W H S S a f e t y E m e r g e n c y W a s h i n g A d d T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob       ¾ÿÿÿÿÿÿ     
   * - W H S S a f e t y P P E A d d E m p l o y e e V i e w C o n t r o l l e r . t x tIlocblob     g  îÿÿÿÿÿÿ         - W H S S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ   . t x tIlocblob     g  Îÿÿÿÿÿÿ     3 - W H S S a f e t y S p i l l K i t E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      A  >ÿÿÿÿÿÿ     1 - W H S S a f e t y S p i l l K i t S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      ¯  >ÿÿÿÿÿÿ     * - W H S S a f e t y S p i l l K i t S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       >ÿÿÿÿÿÿ     ' - W H S S a f e t y S p i l l K i t T a b V i e w C o n t r o l l e r . t x tIlocblob       >ÿÿÿÿÿÿ     $ - W H S S a f e t y S p i l l K i t V i e w C o n t r o l l e r . t x tIlocblob     ù  >ÿÿÿÿÿÿ      - W H S S a f e t y T a b V         Ø   E  0  Ð       @  P  `  p         °  À                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       DSDB                                 `                                           à                                                  @                                                @       tIlocblob     g  îÿÿÿÿÿÿ         - W H S S e a r c h V i e w C o n t r o l l e r . t x tIlocblob      A  ÿÿÿÿÿÿ   . t x tIlocblob     g  Îÿÿÿÿÿÿ     3 - W H S S a f e t y S p i l l K i t E d i t T e s t H i s t o r y V i e w C o n t r o l l e r . t x tIlocblob      A  >ÿÿÿÿÿÿ     1 - W H S S a f e t y S p i l l K i t S e a r c h R e s u l t s V i e w C o n t r o l l e r . t x tIlocblob      ¯  >ÿÿÿÿÿÿ     * - W H S S a f e t y S p i l l K i t S e a r c h V i e w C o n t r o l l e r . t x tIlocblob       >ÿÿÿÿÿÿ     ' - W H S S a f e t y S p i l l K i t T a b V i e w C o n t r o l l e r . t x tIlocblob       >ÿÿÿÿÿÿ     $ - W H S S a f e t y S p i l l K i t V i e w C o n t r o l l e r . t x tIlocblob     ù  >ÿÿÿÿÿÿ      - W H S S a f e t y T a b V

after uwu