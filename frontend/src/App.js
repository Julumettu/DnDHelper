import React, {Component} from 'react';
import Monsters from './components/monsters';
import PostFormMonster from './components/post_monster';

class App extends Component {
   render() {
        return (
	<div class="all_monsters">
            <Monsters monsters={this.state.monsters} />
	    <PostFormMonster />
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
