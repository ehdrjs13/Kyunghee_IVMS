function onEdit(e) {
    var sheet = e.source.getSheetByName("Sheet1"); 
    var editedRow = e.range.getRow();
  
    if (e.range.getColumn() == 1 || e.range.getColumn() == 2 || e.range.getColumn() == 3) {
      var name = sheet.getRange(editedRow, 1).getValue();  
      var school = sheet.getRange(editedRow, 2).getValue();  
      var email = sheet.getRange(editedRow, 3).getValue(); 
      

      var url = `https://url.com:8000/newusr?name=${encodeURIComponent(name)}&school=${encodeURIComponent(school)}&email=${encodeURIComponent(email)}`;
  
      try {
        var response = UrlFetchApp.fetch(url);  
        Logger.log("Response: " + response.getContentText());
      } catch (error) {
        Logger.log("Error: " + error.message);  
      }
    }
  }
  