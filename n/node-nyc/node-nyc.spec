%define node_module nyc

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-nyc
Version: 15.1.0
Release: alt2

Summary: The Istanbul command line interface

License: ISC License
Group: Development/Other
Url: https://istanbul.js.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/istanbuljs/nyc/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar
Source2: %name-production-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs >= 0.20.5

Requires: node >= 8
# rpm-build-nodejs

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version

AutoReq: no
AutoProv: no

# FIXME: there is no such devDepends
BuildRequires: node-typescript node-tap node-uglify-js

Requires: node

%description
Istanbul's state of the art command line interface, with support for:

applications that spawn subprocesses.
source mapped coverage of Babel and TypeScript projects

%prep
%setup -a 1

%build

%check
#ln -s . self-coverage
# FAIL  source-map-support.js
# should not match pattern provided
#npm test

%install
# replace node_modules with got after npm install --production
rm -rf node_modules
tar xf %SOURCE2

mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/nyc.js %buildroot%_bindir/nyc
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
rm -rf %buildroot/%nodejs_sitelib/%node_module/tap-snaphots/
rm -rf %buildroot/%nodejs_sitelib/%node_module/test/


#cd %buildroot/%nodejs_sitelib/%node_module/
#npm remove node-typescript node-tap node-uglify-js --save
#npm_prune

%files
%doc README.md
%doc docs/
%_bindir/nyc
%nodejs_sitelib/%node_module/

#files doc
#doc docs

%changelog
* Fri Aug 26 2022 Vitaly Lipatov <lav@altlinux.ru> 15.1.0-alt2
- use production node_modules instead of prune development one

* Thu Dec 23 2021 Vitaly Lipatov <lav@altlinux.ru> 15.1.0-alt1
- new version 15.1.0 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 15.0.1-alt1
- initial build for ALT Sisyphus
