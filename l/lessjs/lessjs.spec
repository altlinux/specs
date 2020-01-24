%define node_module lessjs

Name: lessjs
Version: 3.10.3
Release: alt1

Summary: Less.js The dynamic stylesheet language

# cssmin.js is licensed under BSD license
# everything else is ASL 2.0
License: ASL 2.0 and BSD

Group: Development/Tools
Url: http://lesscss.org

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/less/less.js/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-production-%version.tar

# Use /usr/share paths instead of /usr/lib
# Remove pre-built files from the dist/ directory

BuildRequires: rpm-macros-nodejs

#BuildRequires: node
Requires: node

%description
LESS extends CSS with dynamic behavior such as variables, mixins,
operations and functions. LESS runs on both the client-side (Chrome,
Safari, Firefox) and server-side, with Node.js and Rhino.

%prep
%setup -a 1

%build
# Nothing to be built, we're just carrying around flat files

# TODO
#check
#make_build test
chmod a+rx bin/lessc

%install
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/lessc %buildroot%_bindir/lessc
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
#rm -rf %buildroot/%nodejs_sitelib/%node_module/docs/

%files
%doc LICENSE README.md
%_bindir/lessc
%nodejs_sitelib/%node_module/

%changelog
* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 3.10.3-alt1
- new version 3.10.3 (with rpmrb script)
- use usual node modules dir
- drop node buildreq (build nothing here)
- add optional node_modules (see package.json)

* Wed May 16 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- New veersion (ALT #34914).

* Sat Aug 27 2016 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version 2.5.1 (with rpmrb script)

* Mon Aug 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- cleanup spec

* Mon Jul 15 2013 Pavel Shilovsky <piastry@altlinux.org> 1.3.1-alt1
- Initial release for Sisyphus (based on Fedora)
