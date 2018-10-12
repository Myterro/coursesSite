"use strict";

var currentId;

function getCurrentId(){
    currentId = document.activeElement.id;
}

function validateForm(){
    var formValue = document.getElementById(currentId).value;
    var regex = selectRegex(currentId);
    validation(formValue, regex[0], regex[1]);
}

function selectRegex(currentId){
    var regex = (currentId == "id_username") ? [/^[a-zA-Z0-9]*$/, "Only a-z A-Z 0-9."] :
                (currentId == "id_email") ? [/.+\@.+\..+/, "Enter a valid email address."] :
                (["id_password1", "id_password2"].includes(currentId)) ? [/.{8,}/, "Password is too short (>= 8 chars)."] :
                (["id_author_name", "id_category_name", "id_course_name"].includes(currentId)) ? [/^[a-zA-Z]*$/, "Only a-z A-Z."] :
                (currentId == "id_author_age") ? [/^[8-9]$|^[1-9][0-9]$/, "Only value from 8-99."] :
                (["id_author_photo", "id_course_cover"].includes(currentId)) ? [/\.(gif|jpg|jpeg|tiff|png)$/, "Upload a valid image"] :
                (currentId == "id_course_price") ? [/^[0-9]$|^[1-9][0-9]+$/, "Only numbers."] :
                (["id_category", "id_author"].includes(currentId)) ? [/.+/, "Select option."] : null;

    if (currentId == "id_pub_date") {
        var date = new Date(document.getElementById(currentId).value).getTime();
        var currentDate = new Date();
        if (isNaN(date)){
            document.getElementById(currentId).value = currentDate.toISOString().split('T')[0];
        } else if (currentDate.getTime() >= date) {
            document.getElementById(currentId).value = currentDate.toISOString().split('T')[0];
        } else {
            reg = /(20\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))/;
        }
        errMsg = "Enter a valid date.";
        return [reg, errMsg];
    }

    return regex;
}

function validation(formValue, reg, errMsg){
    if (reg.test(formValue) == false){
        document.getElementById(currentId + "_error").innerHTML = errMsg;
        document.getElementById("submitButton").disabled = true;
    }
    else {
        document.getElementById(currentId + "_error").innerHTML = "";
        document.getElementById("submitButton").disabled = false;
    }
}