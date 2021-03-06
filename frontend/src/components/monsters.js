import React, { useState, useEffect } from 'react'
import './monsters.css'


const Monsters = ({monsters}) => {
    
    const [divState, setdivState] = useState(false)
    const [specific_div, setspecific_div] = useState([])
    function changeView(monster){
	if(divState === true){
	    setdivState(false)
	    setspecific_div('')
	}
	else if(divState === false){
	    setdivState(true)
	    setspecific_div(monster)
	}
    }
    return (
        <div class="monsters_main_div">
            <center><h1>Monster List</h1></center>
            {monsters.map((monster) => (
		<table class="cinereousTable">
		<tr>
		<td>Name: { monster.name } <br></br> { monster.size } / { monster.allignment }</td>
		</tr>
		<button onClick={() => 
			changeView(monster.name)
		}>Show more/less</button>
		{ divState &&  monster.name === specific_div && <table class="more_info" style={{visibility: divState}}>
        <tr>
        <td>AC: { monster.armor_class }
        <br></br>HP: { monster.hit_points } / { monster.hit_points_dice }
        <br></br>Speed: { monster.speed } ft
        </td>
        </tr>
        <tr>
        <td>  <b>Ability scores</b> <br></br>
                <p id="str_mod"> STR { monster.strength } ( </p>
                <p id="dex_mod"> DEX { monster.dexterity } ( </p>
                <p id="const_mod"> CONST { monster.constitution } ( </p>
                <p id="int_mod"> INT { monster.intelligence } ( </p>
                <p id="wis_mod"> WIS { monster.wisdom } ( </p>
                <p id="cha_mod"> CHA { monster.charisma } ( </p>
        </td>
        </tr>
        <tr>
                <td>{ monster.abilities }<br></br>
            { monster.actions }</td>
        </tr>
        </table>
}
		</table>
		    ))}
		</div>
    )
};

export default Monsters
