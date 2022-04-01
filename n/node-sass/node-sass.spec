%define pname node-sass

Name: node-sass
Version: 7.0.0
Release: alt2

Summary: Node.js bindings to libsass

License: MIT License
Group: Development/Other
Url: https://github.com/sass/node-sass

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/sass/node-sass/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

Source2: %name-production-%version.tar

#BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

BuildRequires: libsass-devel

BuildRequires: node-gyp node-mocha node-nan node-nyc

#Requires: node >= 8

AutoReq: yes,noperl,nonodejs
AutoProv: no
# TODO: improve macros (provide only base node_modules/name
Provides: npm(%pname) = %version

%description
Node-sass is a library that provides binding for Node.js to LibSass,
the C version of the popular stylesheet preprocessor, Sass.

It allows you to natively compile .scss files to css at incredible speed
and automatically via a connect middleware.

%prep
%setup -a 1
rm -rfv src/libsass/
# fix deps
rm -rfv node_modules/resolve/test/

%build
ln -s %nodejs_sitelib/node-gyp node_modules/
LIBSASS_EXT=auto npm run-script build
# can't build in the simple way
#npm_build
rm -f node_modules/node-gyp

#%check
#npm test

%install

%npm_install
# replace node_modules with got after npm install --production
rm -rf node_modules
tar xf %SOURCE2
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%pname/bin/node-sass %buildroot%_bindir/node-sass
cp -a node_modules %buildroot/%nodejs_sitelib/%pname/
cp -a vendor %buildroot/%nodejs_sitelib/%pname/
#npm_prune

%files
%doc LICENSE README.md TROUBLESHOOTING.md
%_bindir/node-sass
%nodejs_sitelib/%pname/

%changelog
* Thu Mar 31 2022 Vitaly Lipatov <lav@altlinux.ru> 7.0.0-alt2
- update node_modules, fix build

* Fri Mar 18 2022 Vitaly Lipatov <lav@altlinux.ru> 7.0.0-alt1
- new version 7.0.0 (with rpmrb script)

* Fri Sep 03 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0.1-alt1
- new version 6.0.1 (with rpmrb script)

* Thu Nov 12 2020 Vitaly Lipatov <lav@altlinux.ru> 4.14.1-alt3
- drop tests from packing, disable modules provides

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 4.14.1-alt2
- rebuild with optimized modules set

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 4.14.1-alt1
- new version 4.14.1 (with rpmrb script)

* Tue Mar 03 2020 Vitaly Lipatov <lav@altlinux.ru> 4.13.1-alt2
- rewrite spec

* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 4.13.1-alt1
- initial build for ALT Sisyphus
