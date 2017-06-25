$(document).ready(function () {
    var swPlanetsUrl = 'http://swapi.co/api/planets/';
    var nextPageUrl = '';
    var previousPageUrl = '';
    var modalButtonId = '';

    function getPlanetsData(url) {
        var planetsData = '';
        var myButton = "";


        $.getJSON(url, function (data) {
            nextPageUrl = data['next'];
            previousPageUrl = data['previous'];
            for (let i = 0; i < 10; i++) {
                planetsData += '<tr>';
                planetsData += "<td>" + data['results'][i]['name'] + "</td>";
                planetsData += "<td>" + data['results'][i]['diameter'] + "</td>";
                planetsData += "<td>" + data['results'][i]['climate'] + "</td>";
                planetsData += "<td>" + data['results'][i]['gravity'] + "</td>";
                planetsData += "<td>" + data['results'][i]['terrain'] + "</td>";
                planetsData += "<td>" + data['results'][i]['surface_water'] + "</td>";
                planetsData += "<td>" + data['results'][i]['population'] + "</td>";
                var residents = data['results'][i]['residents']
                if (residents.length !== 0) {
                    modalButtonId = "#modal-button-" + i;
                    myButton = "<button id='modal-button-" + i + "' type='button' class='btn btn-outline-primary btn-block' data-toggle='modal' data-target='#exampleModal'>" + residents.length + " residents</button>";
                    planetsData += "<td>" + myButton + "</td>";
                    modalClick(modalButtonId);
                } else {
                    myButton = "No information";
                    planetsData += "<td>" + myButton + "</td>"
                };
                planetsData += "</tr>";
                document.getElementById("planet-table-body").innerHTML = planetsData;

            };
        });
    };


    function createNextButton(url) {
        if (url !== null) {
            var nextButton = document.createElement("button");
            var text = document.createTextNode("Next");
            var appendToElement = document.getElementById('next')
            nextButton.appendChild(text);
            appendToElement.appendChild(nextButton);
            nextButton.setAttribute('id', 'next-button');
            nextButton.setAttribute("class", "center btn btn-outline-primary");
            nextButton.setAttribute("type", "button");
            nextButton.setAttribute('action', url);
        };
    }

    function createPreviousButton(url) {
        if (url !== null) {
            var previousButton = document.createElement("button");
            var text = document.createTextNode("Previous");
            var appendToElement = document.getElementById('previous')
            previousButton.appendChild(text);
            appendToElement.appendChild(previousButton);
            previousButton.setAttribute('id', 'previous-button');
            previousButton.setAttribute("class", "btn btn-outline-primary");
            previousButton.setAttribute("type", "button");
            previousButton.setAttribute('action', url);
        };
    }

    getPlanetsData(swPlanetsUrl);
    createPreviousButton(previousPageUrl);
    createNextButton(nextPageUrl);

    $("#next-button").click(function () {
        getPlanetsData(nextPageUrl);
    });
    $("#previous-button").click(function () {
        getPlanetsData(previousPageUrl);
    });

    function modalClick(id) {
        $(".list-group").on('click', id, function () {
            $("#myModal").modal();
            alert(id);
        });
    }

});