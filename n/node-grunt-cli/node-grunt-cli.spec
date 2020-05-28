%define pname grunt-cli

Name: node-grunt-cli
Version: 1.3.2
Release: alt1

Summary: Grunt's command line interface

License: MIT
Group: Development/Other
Url: https://github.com/gruntjs/grunt-cli

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/gruntjs/grunt-cli/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

#Provides: npm(%pname) = %version
#AutoReq: no
AutoProv: no

%description
The Grunt command line interface.

%prep
%setup -a 1

%build
%npm_build
npm test
npm prune --production

%install
%npm_install
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%pname/bin/grunt %buildroot%_bindir/grunt
cp -a node_modules %buildroot/%nodejs_sitelib/%pname/
# TODO: remove all test subdir
rm -rf %buildroot/%nodejs_sitelib/%pname/test/
rm -rf %buildroot/%nodejs_sitelib/%pname/node_modules/resolve/test/

%files
%doc LICENSE-MIT README.md
%_bindir/grunt
%nodejs_sitelib/%pname/

%changelog
* Thu May 28 2020 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- initial build for ALT Sisyphus
