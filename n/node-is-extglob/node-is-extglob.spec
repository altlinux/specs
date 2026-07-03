%define _unpackaged_files_terminate_build 1
%define node_module is-extglob

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-is-extglob
Version: 2.1.1
Release: alt1

Summary: Returns true if a string has an extglob
License: MIT
Group: Development/Other
Url: https://github.com/micromatch/is-extglob
Vcs: https://github.com/micromatch/is-extglob.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node
BuildRequires: node-mocha

Requires: node

Provides: npm(%node_module) = %version
Provides: nodejs-%node_module = %EVR

%description
is-extglob is a small Node.js module that returns true when a string contains
an extglob pattern such as ?(a), @(a), !(a), *(a), or +(a).

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a package.json index.js %buildroot%nodejs_sitelib/%node_module/
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
node %nodejs_sitelib/mocha/bin/mocha.js test.js

%files
%doc LICENSE README.md
%nodejs_sitelib/%node_module/

%changelog
* Fri Jul 03 2026 Grant Makyan <karonus@altlinux.org> 2.1.1-alt1
- Initial build for ALT.
