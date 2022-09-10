
//BASIC UI VARIABLES - this is used to clculate the positions and heights for both the customeCode and tax slider.

//var top of customCodeCOntainer
var element = document.querySelector('.advanced-custom-code-container');
var style = getComputedStyle(element);
var customCodeContainerTop = style.top;
//console.log(customCodeContainerTop);

//size of customCode Container when its on
var element = document.querySelector('.advanced-custom-code-container');
var style = getComputedStyle(element);
var customCodeContainerHeightOn = style.height;
//console.log(customCodeContainerHeightOn);

//size of customCode Container when its off
var customCodeContainerHeightOff = "50px";
//console.log(customCodeContainerHeightOff);

//size of buffer=> the space between customCode Container and Tax Container
var buffer = "20px";
//console.log(buffer);

 //size of tax container when its on
 var element = document.querySelector('.advanced-tax-container');
 var style = getComputedStyle(element);
 var taxContainerHeightOn = style.height;
 //console.log(taxContainerHeightOn);

 //size of tax container when its off
 var taxContainerHeightOff = "50px";
// console.log(taxContainerHeightOff);


//top of the tax container
//orignally we will set it wth everyting collapsed
originalTaxContainerTop = parseInt(customCodeContainerTop)  +parseInt(customCodeContainerHeightOff) +parseInt(buffer);
//full height of the page
originalPageBottom = originalTaxContainerTop +parseInt(taxContainerHeightOff) +parseInt(buffer);
//console.log(originalPageBottom);



var element = document.querySelector('.home-generate-page');
var style = getComputedStyle(element);
var basicHomeContainerHeight = style.height;

var generateWindowElement = document.querySelector('.home-generate-window');
var generateWindowStyle = getComputedStyle(generateWindowElement);
var basicGenerateWindowHeight = generateWindowStyle.height;

var advancedHomeContainerHeight = "1457px";

var advancedWindowHeight = "1566px";

//stops form from refreshing the page when you click submit
$("#advanced").submit(function(e) {
  e.preventDefault();
});

$("#basic").submit(function(e) {
  e.preventDefault();
});



function Check(box){

  if(!box.checked){
    document.getElementById("basic").style.display='inline';
    document.getElementById("advanced").style.display='none';
    document.getElementById('home-generate-page').setAttribute("style","height:"+basicHomeContainerHeight);
    document.getElementById('home-generate-window').setAttribute("style","height:"+basicGenerateWindowHeight);
  }
  else{
    document.getElementById("basic").style.display='none';
    document.getElementById("advanced").style.display='inline';
    document.getElementById('home-generate-page').setAttribute("style","height:"+advancedHomeContainerHeight);
    document.getElementById('home-generate-window').setAttribute("style","height:"+advancedWindowHeight);
  }
}


function CustomCodeCheck(box){
  updatePageHeight();
}


function TaxCheck(box){
  updatePageHeight();
}


function updatePageHeight(){
  //copying over global variables
  var currentTaxContainerTop = originalTaxContainerTop;
  var taxContainerHeight = taxContainerHeightOff;
  var currentPageBottom = parseInt(advancedHomeContainerHeight);
  var currentGenerateBottom = parseInt(advancedWindowHeight);

  //both sections are on(customCode and tax)
  if(!document.getElementById('isCustomCode').checked && !document.getElementById('isTax').checked ){
    //customCode is on
    document.getElementById("customCodeInput").style.display='inline';
    document.getElementById('customCodeContainer').setAttribute("style","height:" + customCodeContainerHeightOn);
    
    //tax is on
    document.getElementById("taxWindow").style.display='inline';
    taxContainerHeight = taxContainerHeightOn;

    //shift the top of the customCode 
    currentTaxContainerTop += parseInt(customCodeContainerHeightOn) - parseInt(customCodeContainerHeightOff);
  }
  //if only customCode is on
  else if(!document.getElementById('isCustomCode').checked ){
    //console.log("on off")

    //customCode on
    document.getElementById("customCodeInput").style.display='inline';
    document.getElementById('customCodeContainer').setAttribute("style","height:" + customCodeContainerHeightOn);

    //tax off
    document.getElementById("taxWindow").style.display='none';
    taxContainerHeight = taxContainerHeightOff;


    //update top and height
    currentTaxContainerTop += parseInt(customCodeContainerHeightOn) - parseInt(customCodeContainerHeightOff);
    currentPageBottom -= parseInt(taxContainerHeightOn) - parseInt(taxContainerHeightOff);
    currentGenerateBottom -= parseInt(taxContainerHeightOn) - parseInt(taxContainerHeightOff);
  }
  else if(!document.getElementById('isTax').checked ){
    //customCode off
    document.getElementById("customCodeInput").style.display='none';
    document.getElementById('customCodeContainer').setAttribute("style","height:"+ customCodeContainerHeightOff);
    //tax on
    document.getElementById("taxWindow").style.display='inline';
    taxContainerHeight = taxContainerHeightOn;

    //console.log("off on")
    currentPageBottom -= parseInt(customCodeContainerHeightOn) - parseInt(customCodeContainerHeightOff);
    currentGenerateBottom -= parseInt(customCodeContainerHeightOn) - parseInt(customCodeContainerHeightOff);
  }
  else{
    //customCode off
    document.getElementById("customCodeInput").style.display='none';
    document.getElementById('customCodeContainer').setAttribute("style","height:"+ customCodeContainerHeightOff);

    //tax off
    document.getElementById("taxWindow").style.display='none';
    taxContainerHeight = taxContainerHeightOff;

    //console.log("off off")
    currentPageBottom -= (parseInt(customCodeContainerHeightOn) - parseInt(customCodeContainerHeightOff)) + (parseInt(taxContainerHeightOn) - parseInt(taxContainerHeightOff));
    currentGenerateBottom -= (parseInt(customCodeContainerHeightOn) - parseInt(customCodeContainerHeightOff)) + (parseInt(taxContainerHeightOn) - parseInt(taxContainerHeightOff));
    //console.log(currentGenerateBottom);
  }

  //set all the attributes
  const attributes = {
    style: "top:"+currentTaxContainerTop.toString()+"px; height: "+ taxContainerHeight.toString()+";",
  };
  //console.log( "height: "+ taxContainerHeight.toString()+"px;");
  setAttributes(document.getElementById('taxContainer'), attributes)
  document.getElementById('home-generate-page').setAttribute("style","height:"+currentPageBottom.toString()+"px" );
  document.getElementById('home-generate-window').setAttribute("style","height:"+currentGenerateBottom.toString()+"px");
  //console.log(currentGenerateBottom);

}

function setAttributes(element, attributes) {
  Object.keys(attributes).forEach(attr => {
    element.setAttribute(attr, attributes[attr]);
  });
}
        var arrHead = new Array();
        arrHead = ['', 'Emp. Name', 'Designation', 'Age']; // table headers.

    // first create a TABLE structure by adding few headers.

        var empTable = document.createElement('table');
        empTable.setAttribute('id', 'empTable');  // table id.

        var tr = empTable.insertRow(-1);
        tr.style.borderWidth = "0px";
        tr.style.borderStyle= "hidden";
        empTable.style.borderSpacing = "0 10px";
        empTable.style.overflow = "auto";
        empTable.style.height = "135px"; 
        empTable.style.display = "block";
        var div = document.getElementById('cont');
        div.appendChild(empTable);    // add table to a container.




    // function to add new row.
    function addRow() {
        var empTab = document.getElementById('empTable');

        var rowCnt = empTab.rows.length;    // get the number of rows.
        var tr = empTab.insertRow(rowCnt); 
        tr.setAttribute("style"," border-width: 0px;");
        tr.setAttribute("style"," border-style: hidden;");// table row.
        tr = empTab.insertRow(rowCnt);

        for (var c = 0; c < arrHead.length; c++) {
            var td = document.createElement('td'); 
                     // TABLE DEFINITION.
            td = tr.insertCell(c);

            if (c == 0) {   // if its the first column of the table.
                // add a button control.
                var button = document.createElement('input');

                // set the attributes.
                button.setAttribute('type', 'button');
                button.setAttribute('value', 'Remove');
                button.setAttribute('calss','advanced-delete-btn button');
                // add button's "onclick" event.

                var styles = {
                  "flex": "0",
                  "left": "6px",
                  "color": "transparent",
                  "width": "20px",

                  //"bottom": "9px",
                  "height": "20px",
                  "position": "absolute",
                  "font-size": "0.1px",
                  //"padding-top": "0px",
                  "border-width": "0px",
                  //"padding-left": "0px",
                  "border-radius": "var(--dl-radius-radius-round)",
                  //"padding-right": "0px",
                  //"padding-bottom": "0px"
              };

              Object.assign(button.style, styles);




                button.setAttribute('onclick', 'removeRow(this)');
                td.setAttribute("style"," border-style: hidden;");
                td.appendChild(button);
            }
            else if(c==1)  {

                // the 2nd, 3rd and 4th column, will have textbox.
                var ele = document.createElement('input');
                ele.setAttribute('type', 'text');
                ele.setAttribute('value', '');
                ele.setAttribute('required', 'true');
                ele.setAttribute('placeholder', 'Name');

                var styles = {
                    //"top": "6px",
                    "left": "29px",
                    "color": "#FFFFFF",
                    "width": "75px",
                    "height": "20px",
                    "margin": "auto",
                    //"padding": "0px",
                    "position": "absolute",
                    "font-size": "20px",
                    "align-self": "center",
                    "text-align": "center",
                    "font-family": "Open Sans",
                    "font-weight": "800",
                    "line-height": "1.15",
                    "border-style": "hidden",
                   "border-width": "0px",
                    "border-radius": "30px",
                    "padding-right": "12px",
                    "text-transform": "none",
                    "text-decoration": "none",
                    "background-color": "#ffffff40",
                };

                Object.assign(ele.style, styles);
                
                td.setAttribute("style"," border-width: 0px;");
                td.setAttribute("style"," border-style: hidden;");
                
                td.appendChild(ele);
            }
            else if(c==2)  {

                // the 2nd, 3rd and 4th column, will have textbox.
                var ele = document.createElement('input');
                ele.setAttribute('type', 'text');
                ele.setAttribute('value', '');
                ele.setAttribute('required', 'true');
                ele.setAttribute('placeholder', 'Address');

                var styles = {
                    //"top": "6px",
                    "left": "110px",
                    "color": "#FFFFFF",
                    "width": "131px",
                    "height": "20px",
                    "margin": "auto",
                    //"padding": "0px",
                    "position": "absolute",
                    "font-size": "20px",
                    "align-self": "center",
                    "text-align": "center",
                    "font-family": "Open Sans",
                    "font-weight": "800",
                    "line-height": "1.15",
                    "border-style": "hidden",
                    "border-width": "0px",
                    "border-radius": "30px",
                    "padding-right": "12px",
                    "text-transform": "none",
                    "text-decoration": "none",
                    "background-color": "#ffffff40",
                };

                Object.assign(ele.style, styles);

                td.setAttribute("style"," border-width: 0px;");
                td.setAttribute("style"," border-style: hidden;");

                td.appendChild(ele);
            }
            else if(c==3)  {

                // the 2nd, 3rd and 4th column, will have textbox.
                var ele = document.createElement('input');
                ele.setAttribute('type', 'text');
                ele.setAttribute('value', '');
                ele.setAttribute('required', 'true');
                ele.setAttribute('placeholder', 'Percent');


                var styles = {
                    //"top": "5px",
                    "color": "#FFFFFF",
                    "right": "8px",
                    "width": "46px",
                    "height": "20px",
                    "margin": "auto",
                    //"padding": "0px",
                    "position": "absolute",
                    "font-size": "20px",
                    "align-self": "center",
                    "text-align": "center",
                    "font-family": "Open Sans",
                    "font-weight": "800",
                    "line-height": "1.15",
                    "border-style": "hidden",
                    "border-width": "0px",
                    "border-radius": "30px",
                    "padding-right": "12px",
                    "text-transform": "none",
                    "text-decoration": "none",
                    "background-color": "#ffffff40",
                };

                Object.assign(ele.style, styles);

                td.setAttribute("style"," border-width: 0px;");
                td.setAttribute("style"," border-style: hidden;");

                td.appendChild(ele);
                }
        }
    }


    function setAttributes(element, attributes) {
  Object.keys(attributes).forEach(attr => {
    element.setAttribute(attr, attributes[attr]);
  });
}

    // function to delete a row.
    function removeRow(oButton) {
        var empTab = document.getElementById('empTable');
        empTab.deleteRow(oButton.parentNode.parentNode.rowIndex); // buttton -> td -> tr
    }

    // function to extract and submit table data.
    function submit() {
        var myTab = document.getElementById('empTable');
        var arrValues = new Array();

        // loop through each row of the table.
        for (row = 1; row < myTab.rows.length - 1; row++) {
            // loop through each cell in a row.
            for (c = 0; c < myTab.rows[row].cells.length; c++) {
                var element = myTab.rows.item(row).cells[c];
                if (element.childNodes[0].getAttribute('type') == 'text') {
                    arrValues.push("'" + element.childNodes[0].value + "'");
                }
            }
        }
        
        // finally, show the result in the console.
        console.log(arrValues);
    }

    window.formFinished = async () => {
      if($('#contractLevel').attr('checked')){
        var result = $("#advanced input[required]").filter(function () {
          return $.trim($(this).val()).length == 0
        }).length == 0;
        
        return result;
          
    
      }
      else{
        var result = $("#basic input[required]").filter(function () {
          return $.trim($(this).val()).length == 0
        }).length == 0;
        return result; 
      }
    
    }

    
      

    