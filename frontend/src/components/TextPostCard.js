import styles from "./TextPostCard.module.css";

const TextPostCard = ({
  productId,
  onLoremIpsumDolorClick,
  onUsername2Click,
  onCommunityClick,
  onCommentClick,
}) => {
  return (
    <div className={styles.textPost}>
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
      <div className={styles.description}>
        <a className={styles.loremIpsumDolor} onClick={onLoremIpsumDolorClick}>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam a quam
          eget dolor ullamcorper tristique. Sed a dolor in augue commodo
          imperdiet at a risus. Etiam ipsum ex, auctor sit amet neque sit amet.
        </a>
        <div className={styles.postedBy}>
          <a className={styles.username}>
            <img
              className={styles.vectorIcon}
              alt=""
              src="/usr_profile_pic.svg"
            />
            <a className={styles.username1} onClick={onUsername2Click}>
              username/
            </a>
          </a>
          <a className={styles.community} onClick={onCommunityClick}>
            community
          </a>
          <h6 className={styles.posted3DaysContainer}>
            <ul className={styles.posted3Days}>posted 3 days ago</ul>
          </h6>
        </div>
        <footer className={styles.postFooter}>
          <button className={styles.comment} onClick={onCommentClick}>
            <img className={styles.commentIcon} alt="" src="/comment.svg" />
            <label className={styles.comments} htmlFor="comment_button">
              27 Comments
            </label>
          </button>
          <a className={styles.share} href="https://web.whatsapp.com">
            <img className={styles.whatsappIcon} alt="" src="/whatsapp.svg" />
            <a className={styles.share1} href="https://web.whatsapp.com">
              Share
            </a>
          </a>
          <button className={styles.save}>
            <button className={styles.save1} autoFocus>
              <img className={styles.vectorIcon1} alt="" src="/vector1.svg" />
            </button>
            <label className={styles.save2} htmlFor="Save">
              Save
            </label>
          </button>
          <button className={styles.report} disabled>
            <img className={styles.whatsappIcon} alt="" src="/flag.svg" />
            <label className={styles.comments} htmlFor="Flag">
              Report
            </label>
          </button>
        </footer>
      </div>
    </div>
  );
};

export default TextPostCard;
