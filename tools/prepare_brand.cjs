// Render the unmodified official mark on its website's navy background.
const path = require('path');
const sharp = require(process.argv[2] || 'sharp');
const root = path.resolve(__dirname, '..');
sharp(path.join(root, 'assets/brand/polar-spark-mark.svg'), {density: 450})
  .resize(768,768)
  .flatten({background:'#101f3b'})
  .png()
  .toFile(path.join(root,'assets/brand/polar-spark-mark.png'))
  .catch(e=>{ console.error(e.message); process.exit(1); });
