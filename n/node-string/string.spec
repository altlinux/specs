%define _unpackaged_files_terminate_build 1
%define node_module string

%def_without check

Name: node-string
Version: 3.1.1
Release: alt1

Summary: Lightweight JavaScript library provided extra String methods
License: MIT
Group: Development/Other
Url: https://www.npmjs.com/package/string
# Source-git: https://github.com/jprichardson/string.js.git

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node

%if_with check
BuildRequires: npm(uglify-js)
BuildRequires: npm(istanbul)
BuildRequires: npm(mocha)
%endif

Provides: nodejs-%node_module = %EVR
BuildArch: noarch

%description
string contains methods that aren't included in the vanilla JavaScript string
such as escaping html, decoding html entities, stripping tags, etc.

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a package.json lib %buildroot/%nodejs_sitelib/%node_module

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
mocha test

%files
%doc *.md
%nodejs_sitelib/%node_module

%changelog
* Wed Jul 18 2018 Stanislav Levin <slev@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
