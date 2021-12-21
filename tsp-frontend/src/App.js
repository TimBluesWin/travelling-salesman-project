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
        this.setState({ pointList: d });
        console.log("state", this.state.pointList)
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
          this.setState({ randomList: d });
          console.log("state", this.state.randomList)
        })
        .catch(error => console.log(error))
    
  }

  removeElements() {
    if (this.performed) {
      document.getElementById("cardRandom").style.display = "block";
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
        this.getResults();
        this.getRandom()
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
    )), this.removeElements(),);
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
              </ul>
            </div>
            <br></br>
            <div className="card p-3" id="cardRandom" style={{display: 'none'}}>
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
              </ul>
            </div>
          </div>
        </div>
      </main>
    );
  }
}
export default App;