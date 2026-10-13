%define node_module asar

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-asar
Version: 4.3.1
Release: alt1

Summary: Simple extensive tar-like archive format with indexing

License: MIT License
Group: Development/Other
Url: https://github.com/electron/asar

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/electron/asar/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar
Source2: %name-production-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node >= 22.12.0
BuildRequires: /usr/bin/tsc
BuildRequires(pre): rpm-macros-nodejs

Requires: node >= 22.12.0

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

AutoReq: no
AutoProv: no

%description
Asar is a simple extensive archive format,
it works like tar that concatenates all files
together without compression,
while having random access support.

%prep
%setup -a 1
# upstream sets the version only at npm publish (semantic-release)
sed -i 's|"version": "0.0.0-development"|"version": "%version"|' package.json
grep -F '"version": "%version"' package.json

%build
# compile TypeScript sources (src/*.ts -> lib/*.js) with the system tsc
# (the types from tsconfig.json come from the vendored development node_modules)
tsc
# replace the build tree node_modules with the production one
rm -r node_modules
tar xf %SOURCE2

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module/
chmod a+x bin/*
cp -rp bin lib node_modules package.json %buildroot/%nodejs_sitelib/%node_module

mkdir -p %buildroot%_bindir/
%_ln_sr %buildroot%nodejs_sitelib/%node_module/bin/asar.mjs %buildroot%_bindir/asar

%check
# upstream tests need vitest and electron: just check the CLI round trip
node bin/asar.mjs --version | grep -Fx 'v%version'
node bin/asar.mjs pack src check.asar
node bin/asar.mjs list check.asar | grep -Fx '/asar.ts'
node bin/asar.mjs extract check.asar check.out
cmp src/asar.ts check.out/asar.ts

#nodejs_symlink_deps

%files
%doc CHANGELOG.md LICENSE.md README.md
%_bindir/asar
%nodejs_sitelib/%node_module

%changelog
* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 4.3.1-alt1
- new version 4.3.1
- build lib from TypeScript sources with node-typescript
- asar command runs ESM bin/asar.mjs, requires node >= 22.12.0

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

* Thu Jun 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script)
 + drop support for Node < 8

* Sat Mar 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0 (with rpmrb script)

* Thu Jul 12 2018 Vitaly Lipatov <lav@altlinux.ru> 0.14.3-alt1
- new version 0.14.3 (with rpmrb script)
- use new node_modules predownloading implementation from rpmgs

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.14.2-alt1
- new version 0.14.2 (with rpmrb script)

* Sun Jan 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.14.0-alt1
- new version (0.14.0) with rpmgs script

* Sat Sep 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- initial build for ALT Sisyphus
