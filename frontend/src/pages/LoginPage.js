import { useCallback, useEffect } from "react";
import SignInForm from "../components/SignInForm";
import styles from "./LoginPage.module.css";

const LoginPage = () => {
  useEffect(() => {
    const scrollAnimElements = document.querySelectorAll(
      "[data-animate-on-scroll]"
    );
    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting || entry.intersectionRatio > 0) {
            const targetElement = entry.target;
            targetElement.classList.add(styles.animate);
            observer.unobserve(targetElement);
          }
        }
      },
      {
        threshold: 0.15,
      }
    );

    for (let i = 0; i < scrollAnimElements.length; i++) {
      observer.observe(scrollAnimElements[i]);
    }

    return () => {
      for (let i = 0; i < scrollAnimElements.length; i++) {
        observer.unobserve(scrollAnimElements[i]);
      }
    };
  }, []);

  const onLogoImageClick = useCallback(() => {
    window.open("/home");
  }, []);

  return (
    <div className={styles.loginPage}>
      <img
        className={styles.logoIcon}
        alt=""
        src="/logo1@2x.png"
        onClick={onLogoImageClick}
        data-animate-on-scroll
      />
      <div className={styles.form}>
        <SignInForm />
      </div>
      <img
        className={styles.vectorsIcon}
        alt="design"
        src="/Bottom waves.svg"
      />
    </div>
  );
};

export default LoginPage;
