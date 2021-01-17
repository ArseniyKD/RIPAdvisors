import React, { useEffect, useState } from "react";

import {
  TextField,
  ITextFieldStyles,
  DetailsList,
  DetailsListLayoutMode,
  Selection,
  IColumn,
  MarqueeSelection,
  Fabric,
  Text,
  IObjectWithKey,
  initializeIcons,
} from "@fluentui/react";

import "./App.css";

initializeIcons();

const columns: IColumn[] = [
  {
    key: "name",
    name: "Name",
    fieldName: "name",
    minWidth: 100,
    maxWidth: 150,
    isResizable: true,
  },
  {
    key: "number",
    name: "Number",
    fieldName: "number",
    minWidth: 100,
    maxWidth: 150,
    isResizable: true,
  },
];

const items = [
  { name: "CMPUT", number: "291" },
  { name: "CMPUT", number: "281" },
  { name: "CMPUT", number: "271" },
  { name: "CMPUT", number: "261" },
  { name: "CMPUT", number: "251" },
  { name: "CMPUT", number: "241" },
  { name: "CMPUT", number: "231" },
  { name: "CMPUT", number: "221" },
  { name: "CMPUT", number: "211" },
  { name: "CMPUT", number: "291" },
  { name: "CMPUT", number: "281" },
  { name: "CMPUT", number: "271" },
  { name: "CMPUT", number: "261" },
  { name: "CMPUT", number: "251" },
  { name: "CMPUT", number: "241" },
  { name: "CMPUT", number: "231" },
  { name: "CMPUT", number: "221" },
  { name: "CMPUT", number: "211" },
  { name: "CMPUT", number: "291" },
  { name: "CMPUT", number: "281" },
  { name: "CMPUT", number: "271" },
  { name: "CMPUT", number: "261" },
  { name: "CMPUT", number: "251" },
  { name: "CMPUT", number: "241" },
  { name: "CMPUT", number: "231" },
  { name: "CMPUT", number: "221" },
  { name: "CMPUT", number: "211" },
];

export interface ICourseItem {
  name: string;
}

function App() {
  const [selectedTakenCourses, setSelectedTakenCourses] = useState<
    Array<IObjectWithKey>
  >([]);
  const [selectedWantCourses, setSelectedWantCourses] = useState<
    Array<IObjectWithKey>
  >([]);

  const takenCourseSelection = new Selection({
    onSelectionChanged: () => {
      if (setSelectedTakenCourses !== undefined) {
        setSelectedTakenCourses(takenCourseSelection.getSelection());
      }
    },
  });

  const wantCourseSelection = new Selection({
    onSelectionChanged: () => {
      if (setSelectedWantCourses !== undefined) {
        setSelectedWantCourses(wantCourseSelection.getSelection());
      }
    },
  });

  return (
    <div className="App">
      <div className="App-title">Insert Title Here</div>
      <div className="taken-title">Taken classes</div>
      <div className="want-title">Classes to take</div>
      <div className="schedule-title">Schedule</div>
      <div className="taken-table-container">
        <TextField
          label="Filter by name:"
          onChange={() => {}}
        />
        <MarqueeSelection selection={takenCourseSelection}>
          <DetailsList
            items={items}
            columns={columns}
            setKey="set"
            layoutMode={DetailsListLayoutMode.justified}
            selection={takenCourseSelection}
            selectionPreservedOnEmptyClick={true}
            ariaLabelForSelectionColumn="Toggle selection"
            ariaLabelForSelectAllCheckbox="Toggle selection for all items"
            checkButtonAriaLabel="Row checkbox"
          />
        </MarqueeSelection>
      </div>
      <div className="want-table-container">
        <TextField
          label="Filter by name:"
          onChange={() => {}}
        />
        <MarqueeSelection selection={wantCourseSelection}>
          <DetailsList
            items={items}
            columns={columns}
            setKey="set"
            layoutMode={DetailsListLayoutMode.justified}
            selection={wantCourseSelection}
            selectionPreservedOnEmptyClick={true}
            ariaLabelForSelectionColumn="Toggle selection"
            ariaLabelForSelectAllCheckbox="Toggle selection for all items"
            checkButtonAriaLabel="Row checkbox"
          />
        </MarqueeSelection>
      </div>
    </div>
  );
}

export default App;
