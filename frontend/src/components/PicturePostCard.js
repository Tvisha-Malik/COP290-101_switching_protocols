import styles from "./PicturePostCard.module.css";

const PicturePostCard = ({
  productId,
  onImage8Click,
  onABeautifulPictureClick,
  onGotAPrettyClick,
  onUsername4Click,
  onCommunity1Click,
  onComment1Click,
}) => {
  return (
    <div className={styles.picturePost} id="PicturePost">
      <div className={styles.voting}>
        <img className={styles.votingChild} alt="" src="/line-4@2x.png" />
        <img
          className={styles.arrowOutlineUpRight}
          alt=""
          src="/arrow-outline-up-right.svg"
        />
        <img className={styles.arrowOutlineUpRight1} alt="" src={productId} />
        <label className={styles.label} htmlFor="upvotes">
          999
        </label>
      </div>
      <img
        className={styles.image8Icon}
        alt=""
        src="/image@2x.png"
        onClick={onImage8Click}
      />
      <div className={styles.desciprtion}>
        <a
          className={styles.aBeautifulPicture}
          onClick={onABeautifulPictureClick}
        >
          A beautiful picture I took from my DSLR
        </a>
        <h4 className={styles.gotAPretty} onClick={onGotAPrettyClick}>
          Got a pretty good shot after quite a while. Any tips for me?
        </h4>
        <div className={styles.postedBy}>
          <a className={styles.username}>
            <img
              className={styles.vectorIcon}
              alt=""
              src="/usr_profile_pic1.svg"
            />
            <a className={styles.username1} onClick={onUsername4Click}>
              username/
            </a>
          </a>
          <a className={styles.community} onClick={onCommunity1Click}>
            community
          </a>
          <h6 className={styles.posted3DaysContainer}>
            <ul className={styles.posted3Days}>posted 3 days ago</ul>
          </h6>
        </div>
        <footer className={styles.postFooter}>
          <button className={styles.comment} onClick={onComment1Click}>
            <img className={styles.commentIcon} alt="" src="/comment1.svg" />
            <label className={styles.comments} htmlFor="comment_button">
              27 Comments
            </label>
          </button>
          <a className={styles.share} href="https://web.whatsapp.com">
            <img className={styles.whatsappIcon} alt="" src="/whatsapp1.svg" />
            <label className={styles.share1} htmlFor="WhatsApp">
              Share
            </label>
          </a>
          <button className={styles.save}>
            <button className={styles.save1} autoFocus>
              <img className={styles.vectorIcon1} alt="" src="/vector2.svg" />
            </button>
            <label className={styles.save2} htmlFor="Save">
              Save
            </label>
          </button>
          <button className={styles.report} disabled>
            <img className={styles.whatsappIcon} alt="" src="/flag1.svg" />
            <label className={styles.comments} htmlFor="Flag">
              Report
            </label>
          </button>
        </footer>
      </div>
    </div>
  );
};

export default PicturePostCard;
