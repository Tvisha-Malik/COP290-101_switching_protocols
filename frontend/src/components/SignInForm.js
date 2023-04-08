import { useCallback, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import styles from "./SignInForm.module.css";



const SignInForm = () => {
  const [username, setUserName] = useState('reaper_113');
  const [password, setPassword] = useState('zxcvbnm');
  const navigate = useNavigate();

  const onContinueWithGoogleLeftAlClick = useCallback(() => {
    navigate("/home");
  }, [navigate]);

  const onForgotUsernameOrClick = useCallback(() => {
    navigate("/login/forgotPassword");
  }, [navigate]);

  const onSignUpClick = useCallback(() => {
    navigate("/signUp");
  }, [navigate]);

  return (
    <form className={styles.extraDetails} method="POST" action="http://localhost:8080/api/v3/u/login" 
    onClick={
        async () => {
          const user = {'username': username, 'password': password};
          console.log('thik hai bhai');
          const response = await fetch('http://localhost:8080/api/v3/u/login',{
            method : 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
          })

          if(response.ok){
            navigate("http://localhost:3000/home");
            console.log("yahuuuu")
          }
          else{
            console.log("password or username is wrong consult a psychiatrist you are experiencing memory losses")
          }
        }
      }
    >
      <div className={styles.details}>
        <button
          className={styles.continueWithGoogleLeftAl}
          disabled
          onClick={onContinueWithGoogleLeftAlClick}
        >
          <img
            className={styles.googleLogoIcon}
            alt=""
            src="/google-logo.svg"
          />
          <div className={styles.continueWithGoogle}>Sign In with Google</div>
        </button>
        <input
          className={styles.username}
          type="text"
          value={username}
          onChange={e => setUserName(e.target.value)}
          placeholder="Username"
          required
        />
        <input
          className={styles.password}
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          placeholder="Password"
          minLength={6}
          required
        />
      </div>
      <div className={styles.sectionForgot}>
        <div className={styles.rememberMe}>
          <input className={styles.rememberMeChild} type="checkbox" />
          <u className={styles.rememberMe1}>Remember me</u>
        </div>
        <Link
          className={styles.forgotUsernameOr}
          to="/login/forgotPassword"
          onClick={onForgotUsernameOrClick}
        >
          Forgot username or password?
        </Link>
      </div>
      <div className={styles.login}>
        <button className={styles.loginBtn} 
          onClick={
            async () => {
              const user = {'username': username, 'password': password};
              console.log('thik hai bhai');
              const response = await fetch('http://localhost:8080/api/v3/u/login',{
                method : 'POST',
                headers: {
                  'Content-Type': 'application/json'
                },
                body: JSON.stringify(user)
              })

              if(response.ok){
                navigate("http://localhost:3000/home");
                console.log("yahuuuu")
              }
              else{
                console.log("password or username is wrong consult a psychiatrist you are experiencing memory losses")
              }
            }
          }
        >
          <label className={styles.login1} htmlFor="Login Button">
            login
          </label>
        </button>
        <div className={styles.newUser}>
          <label className={styles.newToMosaic}>New to MOSAIC?</label>
          <Link className={styles.signUp} to="/signUp" onClick={onSignUpClick}>
            Sign Up
          </Link>
        </div>
      </div>
    </form>
  );
};

export default SignInForm;
