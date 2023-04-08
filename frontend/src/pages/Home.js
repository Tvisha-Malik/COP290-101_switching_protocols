import { useCallback, useEffect } from "react";
import Header from "../components/Header";
import MosaicLeftMenu from "../components/MosaicLeftMenu";
import FeedCard from "../components/FeedCard";
import styles from "./Home.module.css";

const Home = () => {
  const onLoremIpsumDolorClick = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername2Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunityClick = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onCommentClick = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onImage8Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onABeautifulPictureClick = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onGotAPrettyClick = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername4Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity1Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment1Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onLoremIpsumDolor1Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername6Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity2Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment2Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onImage81Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onABeautifulPicture1Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onGotAPretty1Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername8Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity3Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment3Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onLoremIpsumDolor2Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername10Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity4Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment4Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onImage82Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onABeautifulPicture2Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onGotAPretty2Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername12Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity5Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment5Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onLoremIpsumDolor3Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername14Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity6Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment6Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onImage83Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onABeautifulPicture3Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onGotAPretty3Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername16Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity7Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment7Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onLoremIpsumDolor4Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername18Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity8Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment8Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onImage84Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onABeautifulPicture4Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onGotAPretty4Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername20Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity9Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment9Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onLoremIpsumDolor5Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername22Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity10Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment10Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onImage85Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onABeautifulPicture5Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onGotAPretty5Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

  const onUsername24Click = useCallback(() => {
    // Please sync "Profile2" to the project
  }, []);

  const onCommunity11Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onComment11Click = useCallback(() => {
    // Please sync "Post" to the project
  }, []);

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

  const onBlahBlahClick = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onBlahBlah1Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onBlahBlah2Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onBlahBlah3Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onBlahBlah4Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onBlahBlah5Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onBlahBlah6Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onBlahBlah7Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onBlahBlah8Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  const onBlahBlah9Click = useCallback(() => {
    // Please sync "Community" to the project
  }, []);

  return (
    <div className={styles.home}>
      <Header />
      <div className={styles.body}>
        <MosaicLeftMenu />
        <div className={styles.feedWrapper}>
          <FeedCard />
        </div>
        <div className={styles.rightMenu} data-animate-on-scroll>
          <div className={styles.popularct}>
            <h5 className={styles.popularCommunitiesToday}>
              Popular Communities Today:
            </h5>
            <div className={styles.popcommunitiestoday}>
              <a className={styles.blahBlah} onClick={onBlahBlahClick}>
                Blah Blah
              </a>
              <a className={styles.blahBlah} onClick={onBlahBlah1Click}>
                Blah Blah
              </a>
              <a className={styles.blahBlah} onClick={onBlahBlah2Click}>
                Blah Blah
              </a>
              <a className={styles.blahBlah} onClick={onBlahBlah3Click}>
                Blah Blah
              </a>
              <a className={styles.blahBlah} onClick={onBlahBlah4Click}>
                Blah Blah
              </a>
            </div>
          </div>
          <div className={styles.popularct}>
            <h5 className={styles.popularCommunitiesToday}>
              Communities you might like:
            </h5>
            <div className={styles.popcommunitiestoday}>
              <a className={styles.blahBlah} onClick={onBlahBlah5Click}>
                Blah Blah
              </a>
              <a className={styles.blahBlah} onClick={onBlahBlah6Click}>
                Blah Blah
              </a>
              <a className={styles.blahBlah} onClick={onBlahBlah7Click}>
                Blah Blah
              </a>
              <a className={styles.blahBlah} onClick={onBlahBlah8Click}>
                Blah Blah
              </a>
              <a className={styles.blahBlah} onClick={onBlahBlah9Click}>
                Blah Blah
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
