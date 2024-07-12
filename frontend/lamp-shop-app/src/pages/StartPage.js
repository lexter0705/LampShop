import React from "react";
import { Link } from '../scripts';
import LampLogo from '../local/images/LampLogo.svg';

function StartPage() {
    return(
        <main>
          <div className="StartBox">
            <img className="LogoImg" src={LampLogo}></img><br/>
            <Link path="/Login">
              <div  className="LoginButton">
                ВХОД
              </div>
            </Link><br/>
            <Link path="/Registration">
              <div className="RegistrationButton">
                РЕГИСТРАЦИЯ
              </div>
            </Link>
          </div>
        </main>
      );
} 

export default StartPage;