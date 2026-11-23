function calculateBMI() {

    let weight = document.getElementById("weight").value;
    let height = document.getElementById("height").value;


    if (weight == "" || height == "") {

        document.getElementById("result").innerHTML =
            "Please enter weight and height";

        return;
    }
    // Convert height from cm to meter
    height = height / 100;


    // BMI Formula
    let bmi = weight / (height * height);


    let category;
    let tip;


    if (bmi < 18.5) {

        category = "Underweight";

        tip = "Tip: Eat a balanced diet with healthy calories and protein-rich foods.";

    }

    else if (bmi < 25) {

        category = "Normal Weight";

        tip = "Tip: Great! Maintain your healthy lifestyle with a balanced diet and regular activity.";

    }

    else if (bmi < 30) {

        category = "Overweight";

        tip = "Tip: Try regular walking, exercise, and reduce unhealthy snacks.";

    }
    else {
        category = "Obese";
        tip = "Tip: Focus on a balanced diet, daily activity, and healthy eating habits.";

    }
    document.getElementById("result").innerHTML =
        "BMI: " + bmi.toFixed(2) + "<br>" +
        "Category: " + category + "<br><br>" +
        tip;
}
function resetBMI() {

    document.getElementById("weight").value = "";

    document.getElementById("height").value = "";

    document.getElementById("result").innerHTML =
        "Your BMI will appear here";

}