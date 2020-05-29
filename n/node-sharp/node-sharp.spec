%define node_module sharp

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-sharp
Version: 0.25.3
Release: alt2

Summary: High performance Node.js image processing, the fastest module to resize JPEG, PNG, WebP and TIFF images. Uses the libvips library

License: Apache License 2.0
Group: Development/Other
Url: https://sharp.pixelplumbing.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/lovell/sharp/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

#BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node node-gyp
BuildRequires(pre): rpm-macros-nodejs

BuildRequires: gcc-c++

# check the version in package.json
BuildRequires: libvips-devel >= 8.9.1

#Requires: node >= 8
# rpm-build-nodejs

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

#AutoReq: no
AutoProv: no
Requires: node

BuildRequires: node-nyc node-mocha

%description
The typical use case for this high speed Node.js module is to convert large images
in common formats to smaller, web-friendly JPEG, PNG and WebP images of varying dimensions.

Resizing an image is typically 4x-5x faster than using
the quickest ImageMagick and GraphicsMagick settings due to its use of libvips.

Colour spaces, embedded ICC profiles and alpha transparency channels are all handled correctly.
Lanczos resampling ensures quality is not sacrificed for speed.

As well as image resizing, operations such as rotation, extraction,
compositing and gamma correction are available.

%prep
%setup -a 1
%__subst "s|.*rpath.*||" binding.gyp

%build
node install/libvips && false
node-gyp configure
node-gyp build || :
echo "FIXME: who breaks pkg-config's result"
%__subst "s|/usr/lib/|%_libdir/|" build/sharp.target.mk
node-gyp build

# check
#npm run test
node_modules/.bin/semistandard
#cpplint
npm run test-unit || :
npm run test-licensing 

npm prune --production

#%check
#npm test

%install

mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a LICENSE README.md package.json lib/ node_modules/ %buildroot/%nodejs_sitelib/%node_module/
mkdir -p %buildroot%nodejs_sitelib/%node_module/build/Release/
cp -a build/Release/sharp.node %buildroot/%nodejs_sitelib/%node_module/build/Release/
#rm -rf %buildroot/%nodejs_sitelib/%node_module/docs/

%files
%doc LICENSE README.md
%nodejs_sitelib/%node_module/

#files doc
#doc docs

%changelog
* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 0.25.3-alt2
- use external modules for tests

* Wed May 27 2020 Vitaly Lipatov <lav@altlinux.ru> 0.25.3-alt1
- initial build for ALT Sisyphus
