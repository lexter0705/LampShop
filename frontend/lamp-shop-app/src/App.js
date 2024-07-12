import './App.css';
import { Pager, Pages, Page } from './scripts';
import StartPage from './pages/StartPage';
import LoginPage from './pages/LoginPage';
import RegistrationPage from './pages/RegistrationPage';
import HomePage from './pages/HomePage';
import CreatePage from './pages/CreatePage';
import RemovePage from './pages/RemovePage';
import UserPage from './pages/UserPage';
import CartPage from './pages/CartPage';

function App() {
  return (
    <div className="App">
      <Pager>
        <Pages>
          <Page element={<StartPage />} path="/Start" />
          <Page element={<LoginPage />} path="/Login" />
          <Page element={<RegistrationPage />} path="/Registration" />
          <Page element={<HomePage />} path="/Home" />
          <Page element={<CreatePage />} path="/Create" />
          <Page element={<RemovePage />} path="/Remove" />
          <Page element={<UserPage />} path="/User" />
          <Page element={<CartPage />} path="/Cart" />
        </Pages>
      </Pager>
    </div>
  );
}

export default App;

{/*import Header from './tags/Header';
import Main from './tags/Main';
import Footer from './tags/Footer'; 
<header><Header></Header></header>
<main><Main></Main></main>
<footer><Footer></Footer></footer> */}