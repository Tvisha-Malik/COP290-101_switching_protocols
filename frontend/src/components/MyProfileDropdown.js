import { useState, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PortalPopup from "./PortalPopup";
import styles from "./MyProfileDropdown.module.css";

const MyProfileDropdown = ({ onClose }) => {
  const navigate = useNavigate();
  const [isMyProfileDropdown1Open, setMyProfileDropdown1Open] = useState(false);
  const [isMyProfileDropdown2Open, setMyProfileDropdown2Open] = useState(false);

  const onLogOutTextClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  const onPreferencesTextClick = useCallback(() => {
    // Please sync "Settings" to the project
  }, []);

  const onEditProfileTextClick = useCallback(() => {
    // Please sync "Edit Profile" to the project
  }, []);

  const openMyProfileDropdown1 = useCallback(() => {
    setMyProfileDropdown1Open(true);
  }, []);

  const closeMyProfileDropdown1 = useCallback(() => {
    setMyProfileDropdown1Open(false);
  }, []);

  const openMyProfileDropdown2 = useCallback(() => {
    setMyProfileDropdown2Open(true);
  }, []);

  const closeMyProfileDropdown2 = useCallback(() => {
    setMyProfileDropdown2Open(false);
  }, []);

  return (
    <>
      <div className={styles.myProfileDropdown}>
        <div className={styles.options}>
          <div className={styles.logOut} onClick={onLogOutTextClick}>
            Log out
          </div>
          <div className={styles.preferences}>
            <img className={styles.settingsIcon} alt="" src="/settings.svg" />
            <div
              className={styles.preferences1}
              onClick={onPreferencesTextClick}
            >
              Preferences
            </div>
          </div>
          <div className={styles.myStuff}>
            <img className={styles.image20Icon} alt="" src="/image-20@2x.png" />
            <div className={styles.myStuff1}>
              <span className={styles.m}>m</span>y Stuff
            </div>
          </div>
          <div className={styles.editProfile}>
            <div
              className={styles.preferences1}
              onClick={onEditProfileTextClick}
            >
              Edit Profile
            </div>
            <img className={styles.image20Icon} alt="" src="/image-21@2x.png" />
          </div>
        </div>
        <div className={styles.myProfile} onClick={openMyProfileDropdown1}>
          <div className={styles.myProfileChild} />
          <div className={styles.karma}>Karma</div>
          <div className={styles.username}>Username</div>
          <img className={styles.image15Icon} alt="" src="/image-15@2x.png" />
        </div>
        <img
          className={styles.image23Icon}
          alt=""
          src="/image-23@2x.png"
          onClick={openMyProfileDropdown2}
        />
      </div>
      {isMyProfileDropdown1Open && (
        <PortalPopup
          overlayColor="rgba(113, 113, 113, 0.3)"
          placement="Centered"
          onOutsideClick={closeMyProfileDropdown1}
        >
          <MyProfileDropdown onClose={closeMyProfileDropdown1} />
        </PortalPopup>
      )}
      {isMyProfileDropdown2Open && (
        <PortalPopup
          overlayColor="rgba(113, 113, 113, 0.3)"
          placement="Centered"
          onOutsideClick={closeMyProfileDropdown2}
        >
          <MyProfileDropdown onClose={closeMyProfileDropdown2} />
        </PortalPopup>
      )}
    </>
  );
};

export default MyProfileDropdown;
