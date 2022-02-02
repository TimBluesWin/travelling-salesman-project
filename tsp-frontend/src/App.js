import React, { Component } from "react";
import Swal from 'sweetalert2'

const selectedPoint = ""
var performed = false

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pointList: [],
      randomList: [],
      orList: [],
      orListOpt: [],
      cheapList: [],
      christList: [],
      pointTotal: 0,
      randomTotal: 0,
      orTotal: 0,
      orOptTotal: 0,
      cheapTotal: 0,
      christTotal: 0,
    };
  }

  componentDidMount() {
    var url = "http://127.0.0.1:8000/api/points/";
    fetch(url)
      .then(response => {
        return response.json();
      })
      .then(d => {
        this.setState({ pointList: d });
        console.log("state", this.state.pointList)
      })
      .catch(error => console.log(error))
  }

  getResults() {
    var url = "http://127.0.0.1:8000/api/nneighbour/?q=" + this.selectedPoint;
    fetch(url)
      .then(response => {
        return response.json();
      })
      .then(d => {
        this.setState({ pointList: d["tour"], pointTotal: d["distance"] });
        console.log("state", this.state.pointList["tour"])
      })
      .catch(error => console.log(error))
  }

  getRandom() {
    var url = "http://127.0.0.1:8000/api/rinsertion/?q=" + this.selectedPoint;
    fetch(url)
      .then(response => {
        return response.json();
      })
      .then(d => {
        this.setState({ randomList: d["tour"], randomTotal: d["distance"] });
        console.log("state", this.state.randomList["tour"])
      })
      .catch(error => console.log(error))

  }

  getOr() {
    var url = "http://127.0.0.1:8000/api/googleor/?q=" + this.selectedPoint + "&optimize=0";
    fetch(url)
      .then(response => {
        return response.json();
      })
      .then(d => {
        this.setState({ orList: d["tour"], orTotal: d["distance"] });
        console.log("state", this.state.orList["tour"])
      })
      .catch(error => console.log(error))

  }

  getOrOpt() {
    var url = "http://127.0.0.1:8000/api/googleor/?q=" + this.selectedPoint + "&optimize=1";
    fetch(url)
      .then(response => {
        return response.json();
      })
      .then(d => {
        this.setState({ orListOpt: d["tour"], orOptTotal: d["distance"] });
        console.log("state", this.state.orListOpt["tour"])
      })
      .catch(error => console.log(error))

  }

  getCheapest() {
    var url = "http://127.0.0.1:8000/api/cheapestinsertion/?q=" + this.selectedPoint;
    fetch(url)
      .then(response => {
        return response.json();
      })
      .then(d => {
        this.setState({ cheapList: d["tour"], cheapTotal: d["distance"] });
        console.log("state", this.state.cheapList["tour"])
      })
      .catch(error => console.log(error))

  }

  getChristophides() {
    var url = "http://127.0.0.1:8000/api/christofidesalgorithm/?q=" + this.selectedPoint;
    fetch(url)
      .then(response => {
        return response.json();
      })
      .then(d => {
        this.setState({ christList: d["tour"], christTotal: d["distance"] });
        console.log("state", this.state.christList["tour"])
      })
      .catch(error => console.log(error))

  }

  removeElements() {
    if (this.performed) {
      document.getElementById("cardRandom1").style.display = "block";
      document.getElementById("cardRandom2").style.display = "block";
      document.getElementById("cardRandom3").style.display = "block";
      document.getElementById("cardRandom4").style.display = "block";
      document.getElementById("cardRandom5").style.display = "block";
      document.getElementById("navTitle").innerHTML = "Nearest neighbour:";
      document.getElementById("infoText").innerHTML = "Check every different solution!";
      document.getElementById("infoText").style.textAlign = "center";
      var buttonElements = document.getElementsByName("selectButton");

      for (var i = 0, max = buttonElements.length; i < max; i++) {
        buttonElements[i].style.visibility = "hidden";
      }
    }
  }

  handleSelect = (item, name) => {
    this.selectedPoint = JSON.stringify(item);
    Swal.fire({
      title: 'Great selection!',
      text: 'You have selected: ' + JSON.stringify(name),
      icon: 'success',
      confirmButtonText: "Let's go!"
    }).then((result) => {
      if (result.isConfirmed) {
        this.performed = true
        this.getOrOpt();
        this.getResults();
        this.getRandom();
        this.getOr();
        this.getCheapest();
        this.getChristophides();
      }
    })
  };

  renderRandom = () => {

    return this.state.randomList.map(((randomList, index) => (
      <li
        key={`${randomList.id}${index}`}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span>
          {randomList.name}
        </span>
        <span>
          {randomList.distance}
        </span>
      </li>
    )), this.removeElements());
  };
  renderOr = () => {

    return this.state.orList.map(((orList, index) => (
      <li
        key={`${orList.id}${index}`}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span>
          {orList.name}
        </span>
        <span>
          {orList.distance}
        </span>
      </li>
    )), this.removeElements());
  };
  renderOrOpt = () => {

    return this.state.orListOpt.map(((orListOpt, index) => (
      <li
        key={`${orListOpt.id}${index}`}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span>
          {orListOpt.name}
        </span>
        <span>
          {orListOpt.distance}
        </span>
      </li>
    )), this.removeElements());
  };
  renderCheapest = () => {

    return this.state.cheapList.map(((cheapList, index) => (
      <li
        key={`${cheapList.id}${index}`}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span>
          {cheapList.name}
        </span>
        <span>
          {cheapList.distance}
        </span>
      </li>
    )), this.removeElements());
  };
  renderChristophides = () => {

    return this.state.christList.map(((christList, index) => (
      <li
        key={`${christList.id}${index}`}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span>
          {christList.name}
        </span>
        <span>
          {christList.distance}
        </span>
      </li>
    )), this.removeElements());
  };

  renderItems = () => {

    if (!this.performed) {
      return this.state.pointList.map(((pointList, index) => (
        <li
          key={`${pointList.id}${index}`}
          className="list-group-item d-flex justify-content-between align-items-center"
        >
          <span>
            {pointList.name}
          </span>
          <span >
            <button name="selectButton"
              className="btn btn-new"
              style={{ backgroundColor: '#7066e0', color: 'white' }}
              onClick={() => this.handleSelect(pointList.id, pointList.name)}
            >
              Select!
            </button>
          </span>
        </li>
      )), this.removeElements());
    } else {
      return this.state.pointList.map(((pointList, index) => (
        <li
          key={`${pointList.id}${index}`}
          className="list-group-item d-flex justify-content-between align-items-center"
        >
          <span>
            {pointList.name}
          </span>
          <span>
            {pointList.distance}
          </span>
        </li>
      )), this.removeElements());
    }
  };

  render() {
    return (
      <main className="container">
        <h1 class="text-white display-1 text-center">TSP in Innsbruck</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
              <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                  <li class="nav-item active">
                    <a class="nav-link" href="#">Home</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">About TSP</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="#">About us</a>
                  </li>
                </ul>
              </div>
            </nav>
            <br></br>
            <div className="card p-3">
              <span id="infoText">
                <p class="text-center" >Plan your shortest path!</p>
                <p class="text-center" >Simply select a point of interest and find the way to visit them all.</p>
              </span>
              <div className="mb-4">
              </div>
              <div className="nav nav-tabs">
                <span
                  className="nav-link active nav-link"
                  id="navTitle"
                >
                  Possible starting points
                </span>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
                <p><b>Total: {this.state.pointTotal} m</b></p>
              </ul>
            </div>
            <br></br>
            <div className="card p-3" id="cardRandom1" style={{ display: 'none' }}>
              <div className="nav nav-tabs">
                <span
                  className="nav-link active nav-link"
                  id="navTitle"
                >
                  Random insertion:
                </span>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderRandom()}
                <p><b>Total: {this.state.randomTotal} m</b></p>
              </ul>
            </div>
            <br></br>
            <div className="card p-3" id="cardRandom2" style={{ display: 'none' }}>
              <div className="nav nav-tabs">
                <span
                  className="nav-link active nav-link"
                  id="navTitle"
                >
                  Google OR (Not optimized):
                </span>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderOr()}
                <p><b>Total: {this.state.orTotal} m</b></p>
              </ul>
            </div>
            <br></br>
            <div className="card p-3" id="cardRandom5" style={{ display: 'none' }}>
              <div className="nav nav-tabs">
                <span
                  className="nav-link active nav-link"
                  id="navTitle"
                >
                  Google OR (Optimized):
                </span>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderOrOpt()}
                <p><b>Total: {this.state.orOptTotal} m</b></p>
              </ul>
            </div>
            <br></br>
            <div className="card p-3" id="cardRandom3" style={{ display: 'none' }}>
              <div className="nav nav-tabs">
                <span
                  className="nav-link active nav-link"
                  id="navTitle"
                >
                  Cheapest insertion:
                </span>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderCheapest()}
                <p><b>Total: {this.state.cheapTotal} m</b></p>
              </ul>
            </div>
            <br></br>
            <div className="card p-3" id="cardRandom4" style={{ display: 'none' }}>
              <div className="nav nav-tabs">
                <span
                  className="nav-link active nav-link"
                  id="navTitle"
                >
                  Christophides algorithm:
                </span>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderChristophides()}
                <p><b>Total: {this.state.christTotal} m</b></p>
              </ul>
            </div>
            <br></br>
          </div>
        </div>
      </main>
    );
  }
}
export default App;