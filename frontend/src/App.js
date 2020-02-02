import React, {Component, useState, useEffect} from 'react';
import Monsters from './components/monsters';
import PostFormMonster from './components/post_monster';


class App extends Component {
   render() {
        return (
	<div class="all_monsters">
            <label> Search For Specific monster </label>
	    <input type="text" id="monster_search" onChange={event => this.state.search_word = event.target.value} ></input>
            <Monsters monsters={this.state.monsters} />
	</div>
        )
    }
    state = {
        monsters: [],
        search_word : ""
    };

    componentDidUpdate() {
        fetch('http://localhost:8000/api/monsters/?search=' + this.state.search_word)
            .then(res => res.json())
            .then((data) => {
                this.setState({ monsters: data })
            })
            .catch(console.log)
    }
    componentDidMount() {
        this.setState({search_word : this.state.search_word})
    }
}

export default App;
