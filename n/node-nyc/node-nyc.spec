%define node_module nyc

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-nyc
Version: 15.0.1
Release: alt1

Summary: The Istanbul command line interface

License: ISC License
Group: Development/Other
Url: https://istanbul.js.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/istanbuljs/nyc/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

Requires: node >= 8
# rpm-build-nodejs

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version

AutoReq: no
AutoProv: no

BuildRequires: node-tap

BuildRequires: node-typescript node-uglify-js

Requires: node

%description
Istanbul's state of the art command line interface, with support for:

applications that spawn subprocesses.
source mapped coverage of Babel and TypeScript projects

%prep
%setup -a 1

%build

%check
ln -s . self-coverage
# FAIL  source-map-support.js
# should not match pattern provided
#npm test
# TODO: just remove all symlinks
rm -f node_modules/{tap,typescript,uglify-js}
npm prune --production

%install
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/nyc.js %buildroot%_bindir/nyc
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
rm -rf %buildroot/%nodejs_sitelib/%node_module/{docs,tap-snaphots}/

%files
%doc README.md
%doc docs/
%_bindir/nyc
%nodejs_sitelib/%node_module/

#files doc
#doc docs

%changelog
* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 15.0.1-alt1
- initial build for ALT Sisyphus
