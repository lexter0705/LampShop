import React from "react";
import LampLogo from '../local/images/LampLogo.svg';
import { Link } from '../scripts';

function LoginPage() {
    return(
      <main>
        <div className="StartBox">
          <img className="LogoImg" src={LampLogo}></img><br/>
          <form action="/enter" method="post">
            <input className="LoginInput" name="login" placeholder="Логин"></input><br/>
            <input className="PasswordInput" name="password" type="password" placeholder="Пароль"></input><br/>
            <button className="SubmitButon" type="submit">Войти</button>
          </form>
        </div>
      </main>
      );
} 

export default LoginPage;