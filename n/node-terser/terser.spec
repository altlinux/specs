
%define node_module terser
%def_without check

Name: node-terser
Version: 4.8.0
Release: alt1

Summary: Parser/mangler/compressor for ES6+ - Node.js library
License: BSD-2-clause
Group: Development/Tools
Url: https://www.npmjs.com/package/terser

Requires: node-source-map

Source: %node_module-%version.tar

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node

%if_with check
BuildRequires: npm(hashish)
BuildRequires: npm(chai)
BuildRequires: npm(mocha)
%endif

Provides: nodejs-%node_module = %EVR
BuildArch: noarch

%description
Terser is a parser, mangler, optimizer and beautifier toolkit
for ECMAScript 2015 and newer (ES6+).

terser is a fork of uglify-es
that retains API and CLI compatibility with uglify-es
(Debian packages node-uglify-js, libjs-uglify-js, and uglifyjs).

ECMAScript 2015 (ES2015) a.k.a. ECMAScript 6 (ES6)
is the 6th formal definition of JavaScript -
a high-level, interpreted programming language
most notably used in web browsers and in Node.js.

This package contains Terser usable with Node.js.

%prep
%setup -n %node_module-%version

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a package.json tools main.js dist lib %buildroot/%nodejs_sitelib/%node_module

%check
%nodejs_symlink_deps --check
mocha -R nyan

%files
%doc LICENSE README.md
%nodejs_sitelib/%node_module

%changelog
* Thu Aug 26 2021 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- initial build
