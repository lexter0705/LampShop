import React from "react";
import { Link } from '../scripts';
import LampLogo from '../local/images/LampLogo.svg';

function StartPage() {
    return(
        <main>
          <div className="StartBox">
            <img src={LampLogo}></img>
            <Link path="/Login">
              ВХОД
            </Link><br/>
            <Link path="/Registration">
              РЕГИСТРАЦИЯ
            </Link>
          </div>
        </main>
      );
} 

export default StartPage;