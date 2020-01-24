%define node_module mocha

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-mocha
Version: 7.0.0
Release: alt1

Summary: simple, flexible, fun javascript test framework for node.js & the browser

License: MIT License
Group: Development/Other
Url: https://github.com/mochajs/mocha

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mochajs/mocha/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-production-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

Requires: node >= 8
# rpm-build-nodejs

Provides: nodejs-%node_module = %version-%release
Obsoletes: nodejs-%node_module < %version
Provides: %node_module = %version-%release
Obsoletes: %node_module < %version

AutoReq: no
AutoProv: no
Requires: node

%description
Mocha is a feature-rich JavaScript test framework running on Node.js
and in the browser, making asynchronous testing simple and fun.
Mocha tests run serially, allowing for flexible and accurate reporting,
while mapping uncaught exceptions to the correct test cases.

%prep
%setup -a 1

%build
#pm prune --production

#%check
#npm test

%install
# replace node_modules with got after npm install --production
#rm -rf node_modules
#tar xf %SOURCE2

mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/mocha %buildroot%_bindir/mocha
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
rm -rf %buildroot/%nodejs_sitelib/%node_module/docs/

%files
%doc LICENSE README.md
%_bindir/mocha
%nodejs_sitelib/%node_module/

#files doc
#doc docs

%changelog
* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 7.0.0-alt1
- initial build for ALT Sisyphus
