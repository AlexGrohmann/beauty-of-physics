import styles from './page.module.css'

export default function Home() {
  return (
    <main className={styles.main}>

      <div className={styles.center}>
        Beauty of physics
      </div>
      <div className={styles.formula}>
          <div>F = m * a</div>
          <div><span>F = </span><input className={styles.input} type='number' placeholder='m' /> * <input className={styles.input} type='number' placeholder='a' /></div>
      </div>
    </main>
  )
}
