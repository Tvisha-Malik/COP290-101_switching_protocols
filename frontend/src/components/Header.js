import { useState, useCallback } from "react";
import LeftMenu from "./LeftMenu";
import PortalPopup from "./PortalPopup";
import MyProfileDropdown from "./MyProfileDropdown";
import styles from "./Header.module.css";

const Header = () => {
  const [isLeftMenuOpen, setLeftMenuOpen] = useState(false);
  const [isMyProfileDropdownOpen, setMyProfileDropdownOpen] = useState(false);

  const openLeftMenu = useCallback(() => {
    setLeftMenuOpen(true);
  }, []);

  const closeLeftMenu = useCallback(() => {
    setLeftMenuOpen(false);
  }, []);

  const openMyProfileDropdown = useCallback(() => {
    setMyProfileDropdownOpen(true);
  }, []);

  const closeMyProfileDropdown = useCallback(() => {
    setMyProfileDropdownOpen(false);
  }, []);

  return (
    <>
      <nav className={styles.naviBar}>
        <div className={styles.logo} onClick={openLeftMenu}>
          <img className={styles.image1Icon} alt="MOSAIC" src="/logo@2x.png" />
          <label className={styles.mosaic} htmlFor="logo">
            {" "}
            MOSAIC
          </label>
        </div>
        <form className={styles.searchBox} action="/c/" method="get">
          <img className={styles.searchIcon} alt="" src="/search.svg" />
          <input
            className={styles.search}
            type="text"
            placeholder="Search"
            minLength={-7}
          />
        </form>
        <div className={styles.sideitems}>
          <img className={styles.notifIcon} alt="" src="/notif@2x.png" />
          <img className={styles.notifIcon} alt="" src="/chat@2x.png" />
          <button className={styles.myProfile} disabled>
            <img
              className={styles.dropDownArrow}
              alt=""
              src="/drop-down-arrow@2x.png"
              onClick={openMyProfileDropdown}
            />
            <label className={styles.karma}>Karma</label>
            <label className={styles.username}>Username</label>
            <img className={styles.pfpIcon} alt="" src="/pfp@2x.png" />
          </button>
        </div>
      </nav>
      {isLeftMenuOpen && (
        <PortalPopup
          overlayColor="rgba(113, 113, 113, 0.3)"
          placement="Centered"
          onOutsideClick={closeLeftMenu}
        >
          <LeftMenu onClose={closeLeftMenu} />
        </PortalPopup>
      )}
      {isMyProfileDropdownOpen && (
        <PortalPopup
          overlayColor="rgba(113, 113, 113, 0.3)"
          placement="Centered"
          onOutsideClick={closeMyProfileDropdown}
        >
          <MyProfileDropdown onClose={closeMyProfileDropdown} />
        </PortalPopup>
      )}
    </>
  );
};

export default Header;
