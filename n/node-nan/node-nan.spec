%define pname nan

Name: node-nan
Version: 2.15.0
Release: alt1

Summary: Native Abstractions for Node.js

License: MIT License
Group: Development/Other
Url: https://github.com/nodejs/nan

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/nodejs/nan/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18
BuildRequires(pre): rpm-macros-nodejs >= 0.20.5

BuildRequires: rpm-build-nodejs

#AutoReq: no
#AutoProv: no

%description
Thanks to the crazy changes in V8 (and some in Node core),
keeping native addons compiling happily across versions,
particularly 0.10 to 0.12 to 4.0, is a minor nightmare.
The goal of this project is to store all logic necessary
to develop native Node.js addons without having
to inspect NODE_MODULE_VERSION and get yourself into a macro-tangle.

This project also contains some helper utilities
that make addon development a bit more pleasant.

%prep
%setup -a 1

%build
%npm_build
node-gyp rebuild -C test

%check
%npm_test

%install
%npm_install
%npm_prune
rm -rf %buildroot/%nodejs_sitelib/%pname/tools/

%files
%doc LICENSE.md README.md
%nodejs_sitelib/%pname/

%changelog
* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.15.0-alt1
- new version 2.15.0 (with rpmrb script)

* Wed Oct 28 2020 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt3
- use npm_test and npm_prune macros (with rpm-macros-nodejs 0.25.5)

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt2
- do test in check section

* Wed Oct 14 2020 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Fri Feb 28 2020 Vitaly Lipatov <lav@altlinux.ru> 2.14.0-alt1
- initial build for ALT Sisyphus
