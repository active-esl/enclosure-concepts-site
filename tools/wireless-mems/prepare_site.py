"""Prepare the Wireless MEMS gallery entry from the reviewed ai-tools assets."""
from pathlib import Path
import json,re,hashlib,shutil
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'wireless-mems';P.mkdir(exist_ok=True)
report=json.loads((P/'parts-eval.json').read_text())
version=hashlib.sha256((P/'assembly.glb').read_bytes()).hexdigest()[:10]
labels={'board':'PCB substrate and solder mask','pressure_sensor':'Pressure sensor model (BMP390)','antenna':'Antenna model (U3)','connector':'Connector (J1)','package_envelopes':'U1 package envelope (part number unconfirmed)','passives':'Small components','markings':'Silkscreen','components':'Copper and other STEP features'}
parts=[{'id':k,'label':v,'visible':True,'face_colors':True,'opacity':1.0} for k,v in labels.items()]
manifest={'id':'wireless-mems','title':'Active Wireless MEMS','blurb':'Wireless MEMS pressure-sensor board · 20 × 16 × 3.23 mm from SENSOR.stp. BMP390 model present; radio variant and U1 part number await confirmation. Board-only concept; no enclosure or battery model.','glb':'assembly.glb','glb_version':version,'parts':parts,'dim_groups':[{'id':'overall','label':'Full model envelope','default':False,'dims':[{'label':'20.00 mm','mm':20,'a':[-.01,.004,.011],'b':[.01,.004,.011]},{'label':'16.00 mm','mm':16,'a':[.014,.004,-.008],'b':[.014,.004,.008]},{'label':'3.23 mm overall','mm':3.227337,'a':[-.014,-.000754,.008],'b':[-.014,.002473,.008]}]}],'views':{'front':[.75,.65,1.15],'rear':[-.75,.6,-1.15],'side':[1.4,.45,.15],'top':[0,1.4,.0001]},'features':{'outline': True, 'outline_default': False, 'explode': True, 'explode_axis': [0, 1, 0], 'explode_offsets_mm': {'board': 0, 'components': 0.3, 'markings': 0.5, 'passives': 2, 'pressure_sensor': 4, 'antenna': 4, 'package_envelopes': 5, 'connector': 6}, 'section': True, 'measure': True, 'deeplink': True},'pages_links':[]}
(P/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
canonical='https://concepts.active-esl.com/wireless-mems/'
def seo(url,title):
 desc='Explore the Active Wireless MEMS pressure-sensor board: a measured 20 × 16 mm STEP model, with a 360° view and component inspector.'
 return f'''<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/svg+xml" href="../assets/active-edge-favicon.svg">
<meta property="og:type" content="website"><meta property="og:site_name" content="Active-Edge">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{canonical}share-preview.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="627"><meta property="og:image:type" content="image/png">
<meta property="og:image:alt" content="Active Wireless MEMS board, rendered from its STEP geometry, with measured dimensions">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{canonical}share-preview.png">'''
ins=(ROOT/'flexi-sensor/assembly.html').read_text()
ins=ins.replace('Active Flexi Sensor','Active Wireless MEMS').replace('data-concept="flexi-sensor"','data-concept="wireless-mems"')
ins,n=re.subn(r'const MANIFEST = .*?;\s*\n\s*const PARTS', lambda m: 'const MANIFEST = '+json.dumps(manifest,indent=2,ensure_ascii=True)+';\n\n    const PARTS',ins,count=1,flags=re.S);assert n==1
ins=ins.replace('let col = PART_COLOR[partId] || 0x8e9298;','let col = meta.face_colors && !o.geometry.attributes.color && o.material?.color\n          ? o.material.color.clone() : (PART_COLOR[partId] || 0x8e9298);').replace('const useFaceColors = !!meta.face_colors;', 'const useFaceColors = !!meta.face_colors && !!o.geometry.attributes.color;').replace('>PLACEHOLDER<','>BOARD CONCEPT<')
ins=ins.replace('</head>',seo(canonical+'assembly.html','Active Wireless MEMS — Inspect | Active-Edge')+'\n</head>')
(P/'assembly.html').write_text(ins)
look=(ROOT/'handheld/index.html').read_text()
look=look.replace('Active Slim','Active Wireless MEMS').replace('data-concept="slim"','data-concept="wireless-mems"')
look=look.replace('Active Wireless MEMS · no onboard RJ45','20 × 16 × 3.23 mm · Wireless pressure-sensor board · Radio variant pending')
look=look.replace('Active Wireless MEMS enclosure with branded LCD','Active Wireless MEMS sensor board from SENSOR.stp; U1 is a package envelope')
look=re.sub(r'src="handheld.glb\?v=[^"]+"',f'src="assembly.glb?v={version}"',look)
look=look.replace('shadow-intensity="0.85"','shadow-intensity="0.85" camera-orbit="35deg 55deg auto" poster="beauty.png"')
look=look.replace('</head>',seo(canonical,'Active Wireless MEMS | Active-Edge')+'\n</head>')
look=look.replace('<div class="look-hint">', '<aside class="concept-notes" style="position:fixed;bottom:52px;left:16px;z-index:15;background:rgba(7,17,31,.9);padding:10px 14px;border-radius:10px;max-width:min(520px,90vw);font-size:13px;line-height:1.6">Pressure sensor model: BMP390 · U1: package envelope<br><a href="assembly.html" style="color:#20d6d2">Inspect components &amp; dimensions</a> · <a href="spec-check.html" style="color:#20d6d2">Specification check</a></aside>\n<div class="look-hint">')
(P/'index.html').write_text(look)
check='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Active Wireless MEMS — specification check</title><link rel="stylesheet" href="../site-nav.css"><style>body{margin:0;background:#07111f;color:#f7f9fc;font:17px/1.6 system-ui}main{max-width:850px;margin:120px auto 60px;padding:24px}a{color:#20d6d2}h1{line-height:1.1}table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:12px;border-bottom:1px solid #334155}</style></head><body><nav id="siteNav" class="site-nav" data-root="../" data-concept="wireless-mems" data-mode="inspect"></nav><script src="../site-nav.js" defer></script><main><p>Active-Edge · Under development</p><h1>Active Wireless MEMS</h1><p>A board concept based on SENSOR.stp, identified by Alex as the new wireless MEMS sensor board. This is the sensor node, separate from the RT1186 gateway.</p><table><tr><th>Item</th><th>What the source establishes</th></tr><tr><td>Envelope</td><td>20 × 16 × 3.23 mm overall, measured from STEP geometry.</td></tr><tr><td>Pressure sensor</td><td>BMP390 named model; fitted part and pressure connection require confirmation.</td></tr><tr><td>U1</td><td>6 × 6 × 1 mm package envelope, not an identified radio module.</td></tr><tr><td>U3 antenna / J1 connector</td><td>Named STEP models; RF specification, pinout and mating parts remain unconfirmed.</td></tr><tr><td>Radio variant</td><td>UWB or Bluetooth PAwR remains to be confirmed. The programme specification assigns no Wi-Fi to the sensor.</td></tr><tr><td>Power and enclosure</td><td>No separately identified battery in the source. Power source, vent/port, keep-outs and enclosure requirements remain open.</td></tr></table><p>The CAD does not establish radio range, battery life, pressure accuracy, sampling performance or compliance. No enclosure or release approval is implied.</p><p><a href="./">Orbit view</a> · <a href="assembly.html">Inspect</a> · <a href="../still.html?c=wireless-mems">Still image</a></p><p><small>Source fingerprint: SOURCE_HASH<br>Compared with the Wireless MEMS controlled specification on 15 October 2026. Google Doc comment reconciliation remains pending.<br>(Briar helped draft this.)</small></p></main></body></html>'''.replace('SOURCE_HASH',report['source_sha256'])
(P/'spec-check.html').write_text(check)
nav=ROOT/'site-nav.js';s=nav.read_text();needle='    {\n      id: "flexi-sensor",';entry='''    {
      id: "wireless-mems",
      label: "Wireless MEMS",
      maturity: "wip",
      look: `${root}wireless-mems/`,
      inspect: `${root}wireless-mems/assembly.html`,
      still: `${root}still.html?c=wireless-mems`,
    },
''';assert needle in s;s=s.replace(needle,entry+needle,1);nav.write_text(s)
navhash=hashlib.sha256(nav.read_bytes()).hexdigest()[:10]
gallery=ROOT/'index.html';s=gallery.read_text();needle='      <div class="card" data-maturity="wip" data-concept="flexi-sensor">';card='''      <div class="card" data-maturity="wip" data-concept="wireless-mems">
        <a class="card-look" href="wireless-mems/" aria-label="Open Active Wireless MEMS Look"><img src="wireless-mems/thumbnail.png" alt="Active Wireless MEMS pressure-sensor board rendered from SENSOR.stp" /></a>
        <div class="body" style="padding-top:16px">
          <h2>Active Wireless MEMS <span class="maturity-badge">WIP · under development</span></h2>
          <p>New wireless pressure-sensor board · 20 × 16 × 3.23 mm from SENSOR.stp. BMP390 model; radio variant pending confirmation.</p>
          <div class="ctas"><a href="wireless-mems/">Look</a><a class="secondary" href="still.html?c=wireless-mems">Still</a><a class="secondary" href="wireless-mems/assembly.html">Inspect</a></div>
        </div>
      </div>
''';assert needle in s;s=s.replace(needle,card+needle,1);gallery.write_text(s)
p=ROOT/'still.js';s=p.read_text();needle='  const STILLS = {';s=s.replace(needle,needle+'''\n    "wireless-mems": {
      src: "wireless-mems/beauty.png",
      look: "wireless-mems/",
      inspect: "wireless-mems/assembly.html",
      title: "Active Wireless MEMS — still",
      caption: "20 × 16 × 3.23 mm · FreeCAD STEP geometry / Blender Cycles · U1 is a package envelope",
    },''',1);p.write_text(s)
stillhash=hashlib.sha256(p.read_bytes()).hexdigest()[:10]
# Refresh shared nav/still script URLs across all current HTML, preserving page bodies.
for p in ROOT.rglob('*.html'):
 if '.git' in p.parts:continue
 old=p.read_text();new=re.sub(r'(site-nav\.js)\?v=[a-f0-9]+',r'\1?v='+navhash,old);new=re.sub(r'(still\.js)\?v=[a-f0-9]+',r'\1?v='+stillhash,new)
 if old!=new:p.write_text(new)
p=ROOT/'sitemap.xml';s=p.read_text();s=s.replace('</urlset>','  <url><loc>'+canonical+'</loc></url>\n</urlset>');p.write_text(s)
(P/'build.json').write_text(json.dumps({'id':'20261015-wireless-mems-'+version,'concept':'wireless-mems','source_sha256':report['source_sha256'],'assets':{'assembly.glb':version}},indent=2)+'\n')
print('Prepared Wireless MEMS Look, Inspect, Still, gallery, navigation and specification check.')
