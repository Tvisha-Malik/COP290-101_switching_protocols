import { useState, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import SortForm from "./SortForm";
import PostPopUp from "./PostPopUp";
import PortalPopup from "./PortalPopup";
import styles from "./LeftMenu.module.css";

const LeftMenu = ({ onClose }) => {
  const navigate = useNavigate();
  const [isPostPopUpOpen, setPostPopUpOpen] = useState(false);

  const onHomeButtonClick = useCallback(() => {
    navigate("/home");
  }, [navigate]);

  const onHomeIconClick = useCallback(() => {
    navigate("/home");
  }, [navigate]);

  const onHomeTextClick = useCallback(() => {
    navigate("/home");
  }, [navigate]);

  const onTrendingBarClick = useCallback(() => {
    navigate("/home");
  }, [navigate]);

  const onTrendingTextClick = useCallback(() => {
    navigate("/home");
  }, [navigate]);

  const onTrendingIconClick = useCallback(() => {
    navigate("/home");
  }, [navigate]);

  const openPostPopUp = useCallback(() => {
    setPostPopUpOpen(true);
  }, []);

  const closePostPopUp = useCallback(() => {
    setPostPopUpOpen(false);
  }, []);

  return (
    <>
      <div className={styles.leftMenu} id="LeftMenu">
        <div className={styles.pageLinks}>
          <button className={styles.homebutton} onClick={onHomeButtonClick}>
            <div className={styles.home}>
              <img
                className={styles.homeIcon}
                alt=""
                src="/home.svg"
                onClick={onHomeIconClick}
              />
              <div className={styles.home1} onClick={onHomeTextClick}>
                Home
              </div>
            </div>
          </button>
          <button className={styles.homebutton} onClick={onTrendingBarClick}>
            <div className={styles.trending} onClick={onTrendingTextClick}>
              Trending
            </div>
            <img
              className={styles.trendingIcon}
              alt=""
              src="/trending@2x.png"
              onClick={onTrendingIconClick}
            />
          </button>
        </div>
        <SortForm />
        <button className={styles.newPost} onClick={openPostPopUp}>
          <img className={styles.image31Icon} alt="" src="/image-31@2x.png" />
          <div className={styles.newPost1}> New Post</div>
        </button>
      </div>
      {isPostPopUpOpen && (
        <PortalPopup
          overlayColor="rgba(113, 113, 113, 0.3)"
          placement="Centered"
          onOutsideClick={closePostPopUp}
        >
          <PostPopUp onClose={closePostPopUp} />
        </PortalPopup>
      )}
    </>
  );
};

export default LeftMenu;
