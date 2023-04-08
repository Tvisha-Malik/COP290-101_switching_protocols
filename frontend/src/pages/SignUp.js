import { useCallback } from "react";
import { useNavigate } from "react-router-dom";
import styles from "./SignUp.module.css";

const SignUp = () => {
  const navigate = useNavigate();

  const onLogoImageClick = useCallback(() => {
    navigate("/home");
  }, [navigate]);

  return (
    <div className={styles.signUp}>
      <img
        className={styles.logoIcon}
        alt="MOSAIC"
        src="/logo1@2x.png"
        onClick={onLogoImageClick}
      />
      <form className={styles.form} action="/api/v3/u/create" method="post">
        <input
          className={styles.emailAddress}
          type="email"
          placeholder="Email"
          required
          text-indent="10px"
        />
        <input
          className={styles.username}
          type="text"
          placeholder="Username"
          required
        />
        <input
          className={styles.password}
          type="text"
          placeholder="Password"
          minLength={8}
          required
        />
        <button className={styles.loginBtn} autoFocus>
          <div className={styles.signUp1}>Sign Up</div>
        </button>
      </form>
      <img className={styles.vectorsIcon} alt="" src="/Bottom Waves1.svg" />
    </div>
  );
};

export default SignUp;
