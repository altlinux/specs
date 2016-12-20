Name: npm
Version: 3.10.9
Release: alt2

Summary: A package manager for node

Group: Development/Tools
License: MIT License
Url: http://nodejs.org/

# Source-url: https://github.com/npm/npm/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs

#BuildRequires: node >= 6.9
#Requires:	node >= 6.9

BuildArch:	noarch

# we do not need any module provides here
AutoProv: yes,nonodejs
AutoReq: yes,nonodejs

%description
npm is a package manager for node. You can use it to install and publish your
node programs. It manages dependencies and does other cool stuff.

npm is configured to use npm, Inc.'s public package registry
at https://registry.npmjs.org by default.


%prep
%setup

%build
#make man

%install
mkdir -p %buildroot%nodejs_sitelib/%name/ %buildroot%_bindir/
ln -s %nodejs_sitelib/%name/bin/npm-cli.js %buildroot%_bindir/%name

# need inet
#node cli.js install -g --prefix %buildroot%_prefix
# just copy, like in node package was
cp -a . %buildroot%nodejs_sitelib/%name/

rm -rf %buildroot%nodejs_sitelib/%name/node_modules/node-gyp/gyp/tools/emacs
# need python2.7(TestCommon)
rm -rf %buildroot%nodejs_sitelib/%name/node_modules/node-gyp/gyp/pylib/gyp/generator/ninja_test.py
# drop due empty fixtures/package.json
rm -rf %buildroot%nodejs_sitelib/test/
# drop due docker requires
rm -rf %buildroot%nodejs_sitelib/%name/node_modules/node-gyp/test/

%files -n npm
%_bindir/npm
%nodejs_sitelib/%name/

%changelog
* Sun Dec 18 2016 Vitaly Lipatov <lav@altlinux.ru> 3.10.9-alt2
- new version 3.10.9 (with rpmrb script)

* Sat Oct 08 2016 Vitaly Lipatov <lav@altlinux.ru> 3.10.3-alt1
- initial build for ALT Linux Sisyphus

