import React, { useState, useEffect } from 'react'
import './monsters.css'


const PostFormMonster = () => {
    
    return (
        <div class="monster_form">
            <form id="monster_poster">
	    <label>
	    	<span class="text">Monster name: </span>
	    	<input type="text" name="text"/>
	    </label>
	    <button>Submit</button>
	    </form>
	</div>
    )
};

export default PostFormMonster
