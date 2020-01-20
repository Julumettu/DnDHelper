import React, {Component} from 'react';
import Monsters from './components/monsters';

class App extends Component {
  
   constructor() {
	super()
	this.state={
		showMe:true,
		monsters: []
	}
	
   }
   operation()
   {
	   alert("This works!")
   }
   render() {
        return (
	<div class="all_monsters">
            <Monsters monsters={this.state.monsters} />
	</div>
        )
    }

    state = {
        monsters: [],
    };

    componentDidMount() {
        fetch('http://localhost:8000/api/monsters/')
            .then(res => res.json())
            .then((data) => {
                this.setState({ monsters: data })
            })
            .catch(console.log)
    }
}

export default App;
