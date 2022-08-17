[Back](../index.md)

# WHS iOS

## Technical Documentation

### GETTING STARTED



### INSTALLATION AND DEVELOPMENT



### PROGRAMMING LANGUAGE



### MINIMUM VERSION



### APPLICATION ID



### DEBUGGING



### THIRD-PARTY LIBRARIES


#### Cocoapods
Most of the third party libraries are installed using CocoaPods. They can be added by searching library names found in https://cocoapods.org/, inserting them in the Podfile and running the pod install command in the Terminal.

#### Swift Package Manager (SPM)
Some of the third party libraries are installed using SPM

##### Important Libraries

### ACTIVITIES AND CONTROLLERS  

#### Core Classes
- **AppDelegate** - manages most of the pre-startup items like Firebase configurations, etc.
  ##### Configured items
  Firebase
    

#### View Controllers
  

##### **WHSAtmosphericMonitoringTypePickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddMonitoringTypeView`
- `showEditMonitoringTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **MyStorageESQAddSuppliersViewController**

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

##### **WHSAssetsAddServiceHistoryViewController**

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

##### **WHSAssetsElectricalSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList

##### **WHSNoiseControlTabViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showEditDetailsView`
- `showEditMeasurementView`
- `showAssessmentView`
- `showNewControlsView`

##### **WHSAssetsSearchRecordResultsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `searchRecords`
- `fetchNextPage`

##### **WHSNoiseControlAddRecordViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: … willSendRequest`
- `connection: … didReceiveResponse`
- `connection: … didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: … dataPicked`
- `numberOfSectionsInTableView`
- `tableView: … numberOfRowsInSection`
- `tableView: … titleForHeaderInSection`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `textViewDidChange`
- `acSheet: … clickedButtonAtIndex`
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


##### **WHSSafetyFireFightingSearchResultsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSNoiseControlEditMeasurementViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: … didReceiveResponse`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: … dataPicked`
- `numberOfSectionsInTableView`
- `tableView: … numberOfRowsInSection`
- `tableView: … titleForHeaderInSection`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `textView: … shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: … clickedButtonAtIndex`
- `fetchMeasurementDetailsData`
- `saveMeasurementDetailsData`
- `initializeDataSource`
- `createJSON`
- `showMeasurementLocalityPickerView`
- `switchCellValueDidChanged`
- `saveBarButtonItemDidTapped`


##### **WHSAISearchViewController**

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

##### **WHSPAPLegislationsSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSSafetyFireFightingTabViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: … clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`

##### **WHSAssetsPlantAddServiceHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`

##### **WHSSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `initializeSearchBarButtonItem`
- `showDatePicker`
- `searchBarButtonItemDidTapped`
- `formatPickedItems`

##### **WHSSiteRiskAssessmentAddRecordViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `connection: … willSendRequest`
- `connection: … didReceiveResponse`
- `connection: … didReceiveData`
- `connectionDidFinishLoading`
- `tablePickerDidFinishedPicking: … dataPicked`
- `numberOfSectionsInTableView`
- `tableView: … numberOfRowsInSection`
- `tableView: … titleForHeaderInSection`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `textView: … shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: … clickedButtonAtIndex`
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

##### **WHSSafetySpillKitSearchResultsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSAssetsVehiclesSearchRecordViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSAssetsElectricalEditDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSSafetyPPEAddTestHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`

##### **WHSAIEditRecordViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **MyStorageManifestViewController**

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



##### **WHSAIAddRecordViewController**

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

##### **WHSActionViewController**

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

##### **WHSAISearchResultsViewController**

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

##### **WHSChemicalQChartViewController**

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

##### **WHSSafetyEmergencyWashingAddDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … titleForHeaderInSection`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForHeaderInSection`
- `tableView: … heightForFooterInSection`
- `tableView: … heightForRowAtIndexPath`

##### **WHSAddAIInspectionSubTypeViewController**

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

##### **WHSChemicalRegisterProductDetailsViewController**

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

##### **WHSSafetyFireFightingSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`


##### **WHSAddNotificationReceiverViewController**

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

##### **WHSSafetyPPESearchResultsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSAssetsClassifiedViewController**

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

##### **WHSHazardsCarcinogensEditRecordViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSAtmosphericMonitoringEditRecordViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `tableView: ... didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSPAPTraningSearchViewController**

###### **Methods and Calculated Variables**
- `showSearchResultsViewWithDataList`

##### **MyStorageEditStoredQuantityViewController**

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


##### **WHSAddCompetenciesViewController**

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

##### **WHSSafetyEmergencyWashingAddTestHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`

##### **MyStorageESQAddUnitSizesViewController**

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

##### **WHSSafeWorkProceduresViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAt`
- `fetchSWPListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showSearchView`
- `showTabView`

##### **MyStorageESQAddBatchViewController**

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

##### **WHSSafetyFireFightingAddDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … titleForHeaderInSection`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForHeaderInSection`
- `tableView: … heightForFooterInSection`
- `tableView: … heightForRowAtIndexPath`

##### **WHSSafetyPPESearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSAssetsLiftingSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSSafetyEmergencyWashingTabViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: … clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`

##### **WHSPAPComplaintsSearchResultsViewController**

###### **Methods and Calculated Variables**
- `showTabView`

##### **WHSCauseHazardsViewController**

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

##### **WHSAssetsLiftingAddDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsAddDetailsViewController**

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

##### **WHSSafetyPPEEditTestHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`

##### **WHSSplitViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `supportedInterfaceOrientations`

##### **WHSActionCategoryPickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddActionCategoryView`
- `showEditActionCategoryView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSNonChemicalRiskAssessmentViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
- `fetchNonChemicalRiskAssessmentListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showSearchView`
- `showPDFView`
- `showEmailReportView`
- `showTabView`


##### **WHSAddInspectionTypeViewController**

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

##### **WHSSafetyEmergencyWashingSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSSearchResultsRecordViewController**

###### **Methods and Calculated Variables**
- `searchRecords`

##### **WHSSiteRiskAssessmentSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tablePickerDidFinishedPicking: … dataPicked`
- `tableView: … numberOfRowsInSection`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `textViewDidChange`
- `initializeDataSource`
- `showGenericPickerViewWithType`
- `showLocationPickerView`
- `showStatusPickerView`
- `showSearchResultsView`
- `searchBarButtonItemDidTapped`

##### **WHSAssetsPlantSearchResultsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSAtmosphericMonitoringAddMonitoringHistoryViewController**

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

##### **WHSSearchRecordViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeSearchBarButtonItem`
- `searchBarButtonItemDidTapped`
- `showSearchResultsViewWithDataList`

##### **WHSHazardsAsbestosViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
- `fetchAsbestosListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`

##### **WHSAttachmentsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `initializeDataSource`
- `openAddRecordView`
- `showEditAttachmentsView`

##### **WHSAddAIInspectionTypeViewController**

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

##### **WHSAIEditPointsRaisedViewController**

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


##### **WHSUtilitiesViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `mailComposeController: … didFinishWithResult`
- `callNumber`
- `sendEmail`
- `sendEmail: … delegate`
- `openWebsite`

##### **WHSPAPLegislationsSearchResultsViewController**

###### **Methods and Calculated Variables**
- `showTabView`

##### **WHSActionsMonitorSearchViewController**

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

##### **WHSAssetsTestHistoryViewController**

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

##### **WHSPAPDrillsSearchResultsViewController**

###### **Methods and Calculated Variables**
- `showTabView`

##### **WHSAssetsSearchRecordViewController**

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

##### **WHSWebViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `prepareWebView`
- `loadHTMLString: … baseURL`

##### **MyStorageESQInputValueViewController**

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

##### **WHSPAPPlansSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSSafetySpillKitEditDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … titleForHeaderInSection`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForHeaderInSection`
- `tableView: … heightForFooterInSection`
- `tableView: … heightForRowAtIndexPath`

##### **MyStorageESQBatchDetailsViewController**

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

##### **WHSSafetySpillKitAddDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … titleForHeaderInSection`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForHeaderInSection`
- `tableView: … heightForFooterInSection`
- `tableView: … heightForRowAtIndexPath`

##### **WHSAssetSubTypePickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddView`
- `showEditView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSActionsMonitorSearchResultsViewController**

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

##### **WHSPAPComplaintsSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`


##### **WHSLegislationsTabViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: … didSelectRowAtIndexPath`
- `tableView: … clickedButtonAtIndex`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentView`
- `showSignOffView`
- `showEmailReportView`
- `showEditDetailsView`
- `showActionsView`

##### **WHSAssetTypePickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddView`
- `showEditView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **SignatureViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `didReceiveMemoryWarning`
- `positionForBar`
- `supportedInterfaceOrientations`
- `shouldAutorotate`
- `clearSignature`
- `doneSigning`

##### **WHSStartAuditViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `fetchFlexibleFormWithPageID`
- `fetchOfflineConnection`
- `connection: … willSendRequest`
- `connection: … didReceiveResponse`
- `connection: … didReceiveData`
- `connectionDidFinishLoading`
- `fetchAutoNum`
- `fetchLocationAddress`
- `handleFlexi`
- `handleAutoNumData`
- `clearLocationTypeData`
- `tablePickerDidFinishedPicking: … dataPicked`
- `tableView: … heightForRowAtIndexPath`
- `numberOfSectionsInTableView`
- `tableView: … numberOfRowsInSection`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForHeaderInSection`
- `textView: … shouldChangeTextInRange`
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
- `documentPicker: … didPickDocumentAtURL`
- `documentPickerWasCancelled`
- `refreshSelectedRow`
- `imagePickerController: … didFinishPickingMediaWithInfo`
- `imagePickerControllerDidCancel`
- `doneBarButtonItemDidTapped`
- `uploadAttachment`
- `clearDepartmentData`
- `cellIndexForField`

##### **WHSAddLocationViewController**

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

##### **WHSAddEmployeeDepartmentViewController**

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

##### **GenericTableViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `numberOfSectionsInTableView`
- `tableView: ... numberOfRowsInSection`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`


##### **WHSAddAtmosphericMonitoringTypeViewController**

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

##### **WHSSiteRiskAssessmentViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
- `fetchRiskAssessmentsListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `openAddRecordView`
- `showSearchView`
- `showPDFView`
- `showEmailReportView`
- `showTabView`

##### **MyStorageESQAddPackSizeViewController**

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


##### **WHSAddActionCategoryViewController**

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

##### **WHSChecklistViewController**

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

##### **WHSAddNoiseAssessmentSubTypeViewController**

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


##### **WHSAssetsElectricalAddServiceHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsClassifiedSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSConfinedSpacesPermitsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: … numberOfRowsInSection`
- `tableView: … titleForHeaderInSection`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `fetchPermitsData`
- `initializeDataSource`
- `showPermitsView`

##### **WHSAssetsVehiclesTabViewController**

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

##### **WHSAddRecordViewController**

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

##### **WHSAssetsClassifiedAddDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`

##### **WHSChemicalRiskAssessmentConsequencesViewController**

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

##### **WHSNoiseControlAddControlViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue`

##### **WHSPoliciesSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewWillDisappear`
- `didReceiveMemoryWarning`
- `supportedInterfaceOrientations`
- `connection: … willSendRequest`
- `connection: … didReceiveResponse`
- `connection: … didReceiveData`
- `connectionDidFinishLoading`
- `connection: … didFailWithError`
- `clearUserData`
- `getActionsList`
- `parseActionList`
- `hamburgerBarButtonDidTapped`
- `acSheet: … clickedButtonAtIndex`
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

##### **WHSChemicalRiskAssessmentCurrentControlsViewController**

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

##### **WHSAssetsClassifiedEditDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`

##### **WHSAddAttendeeViewController**

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

##### **WHSAssetsVehiclesSearchRecordResultsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSAssetsElectricalEditServiceHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAtmosphericMonitoringAddRecordViewController**

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

##### **WHSActionsMonitorRecordViewController**

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


##### **SubmittedByTableViewController**

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

##### **WHSAttendeesSearchViewController**

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

##### **WHSConfinedSpacesPermitDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchConfinedSpacesDetailsData`
- `numberOfSectionsInTableView`
- `tableView: … numberOfRowsInSection`
- `tableView: … titleForHeaderInSection`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
- `returnNullIfNull`
- `initializeDataSource`
- `showEntriesView`
- `showAttachmentsView`
- `showPDFView`

##### **WHSAtmosphericMonitoringEditMonitoringHistoryViewController**

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

##### **WHSAssetsElectricalSearchResultsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSChemicalQChartSearchViewController**

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

##### **SignOffTableViewController**

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

##### **WHSAssetsEditTestHistoryViewController**

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

##### **WHSSiteRARisksTabViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: … didSelectRowAtIndexPath`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReport`
- `showActionsView`
- `showDetailsView`
- `showControlsView`
- `showRatingsView`

##### **WHSPAPTrainingSearchResultsViewController**

###### **Methods and Calculated Variables**
- `showTabView`

##### **WHSWorkerTablePickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddWorkerView`
- `showEditWorker`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSPAPPlansSearchResultsViewController**

###### **Methods and Calculated Variables**
- `showTabView`

##### **WHSAssetsLiftingEditDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsServiceHistoryViewController**

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

##### **WHSAssetsClassifiedSearchResultsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSPAPDrillsSearchViewController**

###### **Methods and Calculated Variables**
- `showSearchResultsViewWithDataList`


##### **WHSControlMeasureTablePickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `detailsView: … savedData`
- `showAddControlMeasureView`
- `openAddRecordView`

##### **WHSStartupViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `finishedValidatingUserCredentials`
- `prepareForSegue`
- `unwindToWHSStartupView`
- `isAnExistingUserLoggedIn`

##### **WHSAiInspectionSubTypePickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddInspectionSubTypeView`
- `showEditInspectionSubTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSSafetySpillKitViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
- `fetchSpillKitListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`

##### **WHSAIAddPointsRaisedViewController**

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

##### **WHSAIPointsRaisedViewController**

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

##### **WHSSafetyEmergencyWashingEditDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … titleForHeaderInSection`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForHeaderInSection`
- `tableView: … heightForFooterInSection`
- `tableView: … heightForRowAtIndexPath`


##### **WHSSafetySpillKitTabViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `acSheet: … clickedButtonAtIndex`
- `showSignOffView`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReportView`
- `showDetailsView`
- `showTestHistoryView`
- `showServiceHistoryView`
- `showActionsView`

##### **WHSActionDetails ManagerViewController**

###### **Methods and Calculated Variables**
- `initializeDataSource`

##### **WHSAttendeesSearchResultsViewController**

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

##### **WHSSiteRARisksViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
- `fetchSiteRARisksListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `openAddRecordView`
- `showSearchView`
- `showPDFView`
- `showEmailReportView`
- `showTabView`

##### **WHSAtmosphericMonitoringTabViewController**

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

##### **WHSAssetsLiftingTabViewController**

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

##### **WHSAssetsPlantTabViewController**

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

##### **WHSTemplatePickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddTemplateView`
- `showEditTemplateView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSSafetyEmergencyWashingSearchResultsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSAddNoiseAssessmentTypeViewController**

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

##### **WHSSafetyFireFightingAddTestHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`

##### **WHSAtmosphericMonitoringHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `fetchMonitoringHistories`
- `showEditMonitoringHistoryViewController`
- `openAddRecordView`

##### **WHSAssetsPlantSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSAssetsPlantAddDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSChangePasswordViewController**

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

##### **WHSAddControlMeasureViewController**

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

##### **WHSSafetyFireFightingEditTestHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`

##### **WHSProjectPickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddProjectView`
- `openAddRecordView`

##### **WHSAuditInspectionsRecordViewController**

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

##### **WHSAssetsAddTestHistoryViewController**

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


##### **WHSNoiseControlNewControlViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `numberOfSectionsInTableView`
- `tableView: … numberOfRowsInSection`
- `tableView: … titleForHeaderInSection`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `showEditRecordView`
- `initializeDataSource`
- `openAddRecordView`

##### **WHSChemicalQChartSearchResultsViewController**

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

##### **WHSSafetySpillKitEditTestHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`


##### **WHSAddAssetTypeViewController**

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

##### **NewDynamicTemplateViewController**

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

##### **WHSSafetyPPEEmployeeViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `fetchEmployees`
- `showEditPPEDetailsView`
- `openAddRecordView`

##### **WHSAssetsEditDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: ... willSendRequest: ... redirectResponse`
- `connection: ... didReceiveData`
- `connectionDidFinishLoading`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSAddAssetSubTypeViewController**

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

##### **WHSNoiseControlEditAssessmentCommentViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `initializeDataSource`

##### **WHSAddAttachmentsViewController**

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

##### **WHSAssetsLiftingSearchResultsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... didSelectRowAtIndexPath`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`

##### **WHSChemicalQChartChemicalSafetyViewController**

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

##### **WHSAssetsElectricalTabViewController**

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

##### **WHSAssetsPlantEditDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **MyStorageAddNewWorkerViewController**

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

##### **WHSAssetsEditServiceHistoryViewController**

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

##### **WHSAISplittedViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: … heightForRowAtIndexPath`
- `initializeDataSource`
- `tableView: … didSelectRowAtIndexPath`

##### **WHSNoiseControlEditRecordViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAtIndexPath`
- `fetchNoiseControlDetailsData`
- `initializeDataSource`

##### **WHSAssetsVehiclesAddDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAssetsPlantViewController**

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

##### **WHSAIInspectionTypePickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddInspectionTypeView`
- `showEditInspectionTypeView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **WHSActionManagerViewController**

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

##### **WHSChemicalQChartDetailViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: ... cellForRowAtIndexPath`
- `tableView: ... heightForRowAtIndexPath`
- `initializeDataSource`

##### **WHSLicencePickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showAddLicenceView`
- `showEditLicenceView`
- `openAddRecordView`
- `editBarButtonItemDidTapped`

##### **MyStorageCompatibilityViewControllerr**

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


##### **WHSSafetyPPEAddDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … titleForHeaderInSection`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForHeaderInSection`
- `tableView: … heightForFooterInSection`
- `tableView: … heightForRowAtIndexPath`



##### **WHSSiteRARisksAddControlViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: … willSendRequest`
- `connection: … didReceiveResponse`
- `connection: … didReceiveData`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: … numberOfRowsInSection`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … titleForHeaderInSection`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `tablePickerDidFinishedPicking: … dataPicked`
- `searchBar: … textDidChange`
- `searchBarSearchButtonClicked`
- `fetchControlsList`
- `saveRecordData`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `acSheet: … clickedButtonAtIndex`
- `switchCellValueDidChanged`
- `showControlCategories`
- `initializeDataSource`
- `updateControlsList`
- `filterListBySearchText`
- `initializeAddBarButtonItem`
- `showAddActionView`
- `showEditActionView`
- `addBarButtonItemDidTapped`

##### **WHSAddDynamicActionsViewController**

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

##### **WHSAttendeesViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `fetchAttendeesData`
- `initializeDataSource`
- `showEditAttendeesDetailsView`
- `openAddRecordView`

##### **WHSConfinedSpacesTabViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showAttachmentsView`
- `showEmailReportView`
- `showAssessmentView`
- `showEditDetailsView`
- `showPermitsEntriesView`
- `showMonitoringHistoryView`
- `showActionsView`

##### **WHSSafetyFireFightingViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
- `fetchFireFightingEquipmentListData`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showPDFView`
- `showEmailReportView`
- `showSearchView`
- `showTabView`
- `openAddRecordView`

##### **WHSAutoHazardViewController**

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

##### **WHSAssetsViewController**

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

##### **WHSAITabViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
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

##### **WHSAssetsElectricalViewController**

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

##### **WHSAssetsElectricalAddDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSAddEmployeeDivisionViewController**

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

##### **WHSSafetyEmergencyWashingEditTestHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`

##### **WHSAssetsVehiclesEditDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: ... titleForHeaderInSection`
- `tableView: ... didSelectRowAtIndexPath`
- `tableView: ... estimatedHeightForRowAtIndexPath`
- `tableView: ... heightForHeaderInSection`
- `tableView: ... heightForFooterInSection`
- `tableView: ... heightForRowAtIndexPath`

##### **WHSTablePickerViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `fetchOffline`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
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

##### **WHSAddLicenceViewController**

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

##### **WHSSiteRiskAssessmentEditRecordViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAtIndexPath`
- `fetchDetailsData`
- `initializeDataSource`

##### **WHSAddWorkerViewController**

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

##### **WHSAssetsLiftingViewController**

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

##### **WHSChemicalQChartHazardsViewController**

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

##### **WHSAddGenericViewController**

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

##### **WHSAssetsVehiclesViewController**

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

##### **WHSChemicalRiskAssessmentDetailsViewController**

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

##### **WHSChemicalRegisterViewController**

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

##### **WHSNoiseControlAssessmentDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `swipeableTableViewCell: … didTriggerRightUtilityButtonWithIndex`
- `deleteAssessment`
- `initializeDataSource`
- `showEditDetailsView`
- `initializeAddRecordBarButtonItem`
- `showAddAssessmentView`
- `showEditCommentView`
- `cellRightUtitilityButtons`
- `sanitizeAssessments`

##### **WHSChemicalQChartDetailsViewController**

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

##### **WHSSafetyEmergencyWashingViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
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

##### **WHSSafetySpillKitSearchViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `showSearchResultsViewWithDataList`

##### **WHSNoiseControlAddAssessmentViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewDidAppear`
- `connection: … didReceiveResponse`
- `connectionDidFinishLoading`
- `numberOfSectionsInTableView`
- `tableView: … numberOfRowsInSection`
- `tableView: … titleForHeaderInSection`
- `tableView: … cellForRowAtIndexPath`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`
- `tableView: … didSelectRowAtIndexPath`
- `textView: … shouldChangeTextInRange`
- `textViewDidChange`
- `acSheet: … clickedButtonAtIndex`
- `saveAssessmentDetailsData`
- `initializeDataSource`
- `createJSON`
- `saveBarButtonItemDidTapped`
- `isAllRequiredDataFilledUp`

##### **WHSSafetySpillKitAddTestHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForRowAtIndexPath`

##### **DynamicFormTableViewController**

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


##### **WHSAuditInspectionsDetailsViewController**

###### **Methods and Calculated Variables**


##### **WHSPDFEditSigneeViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `initializeDataSource`

##### **MyStorageSummaryViewController**

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

##### **WHSSafetyFireFightingEditDetailsViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `tableView: … titleForHeaderInSection`
- `tableView: … estimatedHeightForRowAtIndexPath`
- `tableView: … heightForHeaderInSection`
- `tableView: … heightForFooterInSection`
- `tableView: … heightForRowAtIndexPath`

##### **WHSAssetsPlantEditServiceHistoryViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `didReceiveMemoryWarning`
- `prepareForSegue: ... sender`

##### **WHSTabViewController**

###### **Methods and Calculated Variables**
- `processTabFlags`
- `fetchValidTabs`
- `viewWillAppear`
- `initializeMoreOptionsBarButtonItem`
- `presentMoreOptionsActionSheet`
- `moreOptionsBarButtonItemDidTapped`

##### **WHSAssetsClassifiedTabViewController**

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

##### **WHSAddPointsRaisedViewController**

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

##### **WHSSiteRiskAssessmentTabViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `tableView: … didSelectRowAtIndexPath`
- `acSheet: … clickedButtonAtIndex`
- `showSignOffView`
- `initializeDataSource`
- `showPDFView`
- `showAttachmentsView`
- `showEmailReport`
- `showActionsView`
- `showDetailsView`
- `showHazardsView`
- `showRisksView`

##### **WHSChemicalQChartTabViewController**

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

##### **WHSIncidentReportingRecordViewController**

###### **Methods and Calculated Variables**
- `viewDidLoad`
- `viewWillAppear`
- `viewDidAppear`
- `connectionDidFinishLoading`
- `acSheet: … clickedButtonAtIndex`
- `tableView: … didSelectRowAtIndexPath`
- `fetchIncidentReports`
- `fetchNextPage`
- `initializeDataSource`
- `updateDataSource`
- `showTabView`
- `showSearchView`
- `openPDFView`
- `showEmailReport`
- `openAddRecordView`

##### **WHSChemicalQChartOperationalSafetyViewController**

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

after uwu