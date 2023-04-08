import styles from "./SortForm.module.css";

const SortForm = () => {
  return (
    <div className={styles.sort} id="Sort">
      <div className={styles.sortWrapper}>
        <div className={styles.sort1}>
          <form className={styles.options} method="post">
            <div className={styles.bestbutton}>
              <input
                className={styles.radioButton}
                type="radio"
                defaultChecked={true}
                id="Best"
                name="options"
              />
              <label className={styles.best} htmlFor="Best">
                Best
              </label>
            </div>
            <div className={styles.newbutton}>
              <input
                className={styles.radioButton1}
                type="radio"
                id="Best"
                name="options"
              />
              <label className={styles.new} htmlFor="New">
                New
              </label>
            </div>
            <div className={styles.newbutton}>
              <input
                className={styles.radioButton1}
                type="radio"
                id="Controversial"
                name="options"
              />
              <label className={styles.new} htmlFor="Controversial">
                Controversial
              </label>
            </div>
            <div className={styles.newbutton}>
              <input
                className={styles.radioButton1}
                type="radio"
                id="Old"
                name="options"
              />
              <label className={styles.old} htmlFor="Old">
                Old
              </label>
            </div>
          </form>
          <div className={styles.sortbar}>
            <div className={styles.sort2}>Sort</div>
            <img className={styles.image32Icon} alt="" src="/image-32@2x.png" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default SortForm;
