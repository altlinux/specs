%define _unpackaged_files_terminate_build 1
%define node_module is-glob

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-is-glob
Version: 4.0.3
Release: alt1

Summary: Returns true if the given string looks like a glob pattern
License: MIT
Group: Development/Other
Url: https://github.com/micromatch/is-glob
Vcs: https://github.com/micromatch/is-glob.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node
BuildRequires: node-mocha
BuildRequires: npm(is-extglob) >= 2.1.1

Requires: node
Requires: npm(is-extglob) >= 2.1.1

Provides: npm(%node_module) = %version
Provides: nodejs-%node_module = %EVR

%description
is-glob is a small Node.js module that returns true when a string looks like
a glob pattern or an extglob pattern.

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
node benchmark.js

%files
%doc LICENSE README.md
%nodejs_sitelib/%node_module/

%changelog
* Fri Jul 03 2026 Grant Makyan <karonus@altlinux.org> 4.0.3-alt1
- Initial build for ALT.
