import { useCallback, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { Form } from "react-bootstrap";
import { useNavigate } from "react-router-dom";
import styles from "./PostPopUp.module.css";

const PostPopUp = ({ onClose }) => {
  const navigate = useNavigate();
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

  const onCommentButtonClick = useCallback(() => {
    navigate("/home");
  }, [navigate]);

  return (
    <div className={styles.postPopUp} data-animate-on-scroll>
      <input
        className={styles.searchCommunity}
        type="text"
        placeholder="Choose a community"
        minLength={3}
        required
      />
      <div className={styles.postBox}>
        <div className={styles.postAsUsernameContainer}>
          <span className={styles.postAsUsernameContainer1}>
            <span>
              <span className={styles.post}>{`Post `}</span>
            </span>
            <span>{`as  `}</span>
            <span className={styles.username}>username</span>
            <span className={styles.span}>{`  `}</span>
          </span>
        </div>
        <Form.Group className={styles.textboxFormgroup}>
          <Form.Control
            as="textarea"
            name="Post Content"
            rows={10}
            placeholder="What are your thoughts?"
          />
        </Form.Group>
        <div className={styles.footer}>
          <div className={styles.formating}>
            <img
              className={styles.iconsaxlineartextunderline}
              alt=""
              src="/iconsaxlineartextunderline.svg"
            />
            <div className={styles.b}>B</div>
            <div className={styles.i}>I</div>
            <img
              className={styles.iconsaxlinearlink2}
              alt=""
              src="/iconsaxlinearlink2.svg"
            />
            <img
              className={styles.iconsaxlinearimage}
              alt=""
              src="/iconsaxlinearimage.svg"
            />
            <img
              className={styles.iconsaxlinearvideocircle}
              alt=""
              src="/iconsaxlinearvideocircle.svg"
            />
            <img className={styles.vectorIcon} alt="" src="/vector.svg" />
          </div>
          <button
            className={styles.commentButton}
            autoFocus
            onClick={onCommentButtonClick}
          >
            <div className={styles.comment}>Post</div>
          </button>
        </div>
      </div>
    </div>
  );
};

export default PostPopUp;
