%define node_module tap

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-tap
Version: 14.10.7
Release: alt1

Summary: Test Anything Protocol tools for node

License: ISC License
Group: Development/Other
Url: https://node-tap.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/tapjs/node-tap/archive/v%version.tar.gz
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

Requires: node

BuildRequires: node-typescript

%description
A TAP test framework for Node.js.

%prep
%setup -a 1

%build

%check
npm test || :
#rm -f node_modules/typescript
#npm prune --production

%install
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/run.js %buildroot%_bindir/tap
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
rm -rf %buildroot/%nodejs_sitelib/%node_module/{docs,tap-snaphots}/

%files
%doc LICENSE README.md
%doc docs/
%_bindir/tap
%nodejs_sitelib/%node_module/

#files doc
#doc docs

%changelog
* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 14.10.7-alt1
- initial build for ALT Sisyphus
