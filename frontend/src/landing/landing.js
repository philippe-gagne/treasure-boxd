import Header from '../header/header';
import './landing.scss';
import {Button} from "reactstrap";

function Landing() {
  return ( 
    <div className="App">
      <Header />
      <div className="landing-body">
        <h1 className="splash-text">
          discover something <br/> galactic
        </h1>
        
        <div className='body-text'>
          <p className='description'>using letterboxd data from users like you to find movies we think you'll love the most</p>
          <div className='call-to-action'>
            <p>enter your letterboxd username and discover something new:</p>
            <form>
              <div className='form-group'>
                <input type={Text} maxLength={15} className='form-control user-input' id='inputUsername' placeholder='your username'></input>
                {/* <button type='submit' className='go-btn'>→</button>        */}
                <button type='submit' className='go-btn'>
                  <a href=''><span className='button-text'>→</span></a>
                </button>
              </div>
            </form>
          </div>
        </div>

      </div>
    </div>
  );
}

export default Landing;
