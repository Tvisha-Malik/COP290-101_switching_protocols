import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./Forgot.module.css";

const Forgot = () => {
  const navigate = useNavigate();

  const onLogoImageClick = useCallback(() => {
    window.open("/home");
  }, []);

  const onSendClick = useCallback(() => {
    navigate("/");
  }, [navigate]);

  return (
    <div className={styles.forgot}>
      <img
        className={styles.logoIcon}
        alt="MOSAIC"
        src="/logo1@2x.png"
        onClick={onLogoImageClick}
      />
      <form
        className={styles.form}
        action="/login/forgotPassword"
        method="post"
      >
        <input
          className={styles.username}
          type="email"
          placeholder="Email Address"
          required
        />
        <button className={styles.send} onClick={onSendClick}>
          <div className={styles.sendEmail}>Send Email</div>
        </button>
      </form>
      <img className={styles.vectorsIcon} alt="" src="/Bottom Waves.svg" />
    </div>
  );
};

export default Forgot;
