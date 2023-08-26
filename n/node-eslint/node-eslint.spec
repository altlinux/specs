%define node_module eslint

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-eslint
Version: 8.47.0
Release: alt1

Summary: Find and fix problems in your JavaScript code

License: MIT
Group: Development/Tools
Url: https://eslint.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/eslint/eslint/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-production-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

Requires: node >= 8
# rpm-build-nodejs

Provides: nodejs-%node_module = %EVR
Obsoletes: nodejs-%node_module < %version

Provides: %node_module = %EVR

Provides: eslint = %EVR

AutoReq: no
AutoProv: no

%description
ESLint is a tool for identifying and reporting on patterns found
in ECMAScript/JavaScript code.
In many ways, it is similar to JSLint and JSHint with a few exceptions:
* ESLint uses Espree for JavaScript parsing.
* ESLint uses an AST to evaluate patterns in code.
* ESLint is completely pluggable, every single rule is a plugin and you can add more at runtime.

%prep
%setup -a 1

%build

%install
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/eslint.js %buildroot%_bindir/%node_module
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
rm -rf %buildroot/%nodejs_sitelib/%node_module/{docs,tests}/

%files
%doc README.md
%_bindir/%node_module
%nodejs_sitelib/%node_module/

%changelog
* Sat Aug 26 2023 Vitaly Lipatov <lav@altlinux.ru> 8.47.0-alt1
- new version 8.47.0 (with rpmrb script) (ALT bug 47277)
- don't pack docs
- add Provides: eslint

* Wed Nov 11 2020 Vitaly Lipatov <lav@altlinux.ru> 7.11.0-alt1
- new version 7.11.0 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 7.1.0-alt1
- initial build for ALT Sisyphus
