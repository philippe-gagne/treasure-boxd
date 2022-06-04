import './header.scss';
import logo from '../logoish.svg';

function Header() {
  return ( 
    <div className="header">
        <div className='brand-box'>
          <img className='logo' src={logo} alt='treasureboxd logo'/>
          <h3 className='title'> treasureboxd </h3>
        </div>
        <div className='quicklinks'>
          <p className='header-link'>about</p>
          <p className='header-link'>contact</p>
          
            <button className='header-button' tabIndex={-1}>
              <a href=''><span className='button-text'>share</span></a>
            </button>
          
        </div>
    </div>
  );
}

export default Header;
