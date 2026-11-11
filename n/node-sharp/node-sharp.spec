%define node_module sharp

Name: node-sharp
Version: 0.35.5
Release: alt1

Summary: High performance Node.js image processing

License: Apache-2.0
Group: Development/Other
Url: https://sharp.pixelplumbing.com/

# Source-url: https://github.com/lovell/sharp/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
# sharp 0.35.5 wants libvips >= 8.18.7, Sisyphus and p11 have vips 8.18.6
# (bugfix release, no API change used by sharp); drop when vips >= 8.18.7
Patch1: sharp-libvips-8.18.6.patch
Patch2: sharp-local-addon.patch
Patch3: sharp-node-addon-api.patch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs node-devel node-gyp node-addon-api
BuildRequires: gcc-c++ libvips-devel >= 8.18.6

AutoReq: yes,nonodejs,nonodejs_native,noshebang,nolua
AutoProv: yes,nonodejs

Requires: /usr/bin/node

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

%description
Sharp converts large images in common formats to smaller, web-friendly
JPEG, PNG, WebP, GIF and AVIF images using libvips. It supports resizing,
rotation, extraction, compositing, colour spaces and transparency.

%prep
%setup -a1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# Generate both CJS and ESM entry points from upstream JavaScript sources.
node scripts/build.mjs
# Fail rather than silently selecting bundled libvips.
node -e 'if (!require("./dist/libvips.cjs").useGlobalLibvips()) process.exit(1)'
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
node-gyp rebuild --directory=src --nodedir=%_prefix --verbose

%check
node -e 'const s = require("."); if (s.versions.vips !== require("child_process").execSync("pkg-config --modversion vips-cpp").toString().trim()) process.exit(1); console.log(s.versions)'

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module/src/build/Release
cp -a package.json dist node_modules %buildroot%nodejs_sitelib/%node_module/
cp -a src/build/Release/*.node %buildroot%nodejs_sitelib/%node_module/src/build/Release/

%files
%doc LICENSE README.md
%nodejs_sitelib/%node_module/

%changelog
* Wed Nov 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.35.5-alt1
- new version 0.35.5 (return to ALT Sisyphus).
- build against system libvips 8.18.6 without prebuilt npm binaries.
- lower the libvips minimum from 8.18.7 to 8.18.6 (see the Patch1 comment).
- added BuildRequires: node-devel, node-addon-api.
- removed BuildRequires: rpm-build-intro, node, node-nyc, node-mocha.
- fixes:
  + CVE-2022-29256: remove vulnerable post-installation command handling.

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 0.25.3-alt2
- use external modules for tests

* Wed May 27 2020 Vitaly Lipatov <lav@altlinux.ru> 0.25.3-alt1
- initial build for ALT Sisyphus
