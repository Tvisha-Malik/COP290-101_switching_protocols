import { useState, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import PostPopUp from "./PostPopUp";
import PortalPopup from "./PortalPopup";
import styles from "./MosaicLeftMenu.module.css";

const MosaicLeftMenu = () => {
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
                src="/home1.svg"
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
        <div className={styles.sort} id="Sort">
          <div className={styles.sortWrapper}>
            <div className={styles.sort1}>
              <form className={styles.options} method="post">
                <div className={styles.bestbutton}>
                  <img
                    className={styles.radioButtonIcon}
                    alt=""
                    src="/radio-button.svg"
                  />
                  <label className={styles.best} htmlFor="Best">
                    Best
                  </label>
                </div>
                <div className={styles.newbutton}>
                  <img
                    className={styles.radioButtonIcon1}
                    alt=""
                    src="/radio-button1.svg"
                  />
                  <label className={styles.new} htmlFor="New">
                    New
                  </label>
                </div>
                <div className={styles.newbutton}>
                  <img
                    className={styles.radioButtonIcon1}
                    alt=""
                    src="/radio-button1.svg"
                  />
                  <label className={styles.new} htmlFor="Controversial">
                    Controversial
                  </label>
                </div>
                <div className={styles.newbutton}>
                  <img
                    className={styles.radioButtonIcon1}
                    alt=""
                    src="/radio-button1.svg"
                  />
                  <label className={styles.old} htmlFor="Old">
                    Old
                  </label>
                </div>
              </form>
              <div className={styles.sortbar}>
                <div className={styles.sort2}>Sort</div>
                <img
                  className={styles.image32Icon}
                  alt=""
                  src="/image-321@2x.png"
                />
              </div>
            </div>
          </div>
        </div>
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

export default MosaicLeftMenu;
