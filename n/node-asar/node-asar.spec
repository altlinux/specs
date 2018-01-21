%define node_module asar

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-asar
Version: 0.14.0
Release: alt1

Summary: Simple extensive tar-like archive format with indexing

License: MIT License
Group: Development/Other
Url: https://github.com/electron/asar

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/electron/asar/archive/v%version.tar.gz
Source: %name-%version.tar

#Source1: %name-preloaded-%version.tar
Source2: %name-production-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs
Requires: node
# rpm-build-nodejs

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

AutoReq: no
AutoProv: no
Requires: node

%description
Asar is a simple extensive archive format,
it works like tar that concatenates all files
together without compression,
while having random access support.

%prep
%setup -a 2

%build

# do not work without development requires
# and needs xvfb-maybe
#%check
#npm test

%install
# replace node_modules with got after npm install --production
#rm -rf node_modules
#tar xf %SOURCE2

mkdir -p %buildroot%nodejs_sitelib/%node_module/
chmod a+x bin/*
cp -rp bin lib node_modules package.json %buildroot/%nodejs_sitelib/%node_module

mkdir -p %buildroot%_bindir/
#ln -s %nodejs_sitelib/%node_module/bin/asar.js %buildroot%_bindir/asar
%_ln_sr %buildroot%nodejs_sitelib/%node_module/bin/asar.js %buildroot%_bindir/asar

#nodejs_symlink_deps

%files
%doc CHANGELOG.md LICENSE.md README.md
%_bindir/asar
%nodejs_sitelib/%node_module

%changelog
* Sun Jan 21 2018 Vitaly Lipatov <lav@altlinux.ru> 0.14.0-alt1
- new version (0.14.0) with rpmgs script

* Sat Sep 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- initial build for ALT Sisyphus
