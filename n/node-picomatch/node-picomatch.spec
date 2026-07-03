%define _unpackaged_files_terminate_build 1
%define node_module picomatch

%filter_from_requires /^nodejs.engine./d
%{?nodejs_find_provides_and_requires}

Name: node-picomatch
Version: 4.0.5
Release: alt1

Summary: Fast glob matcher with Bash-compatible glob features
License: MIT
Group: Development/Other
Url: https://github.com/micromatch/picomatch
Vcs: https://github.com/micromatch/picomatch.git

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
Picomatch is a fast and accurate JavaScript glob matcher with support for
standard and extended Bash glob features, including braces, extglobs, POSIX
brackets, and regular expressions.

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a package.json index.js posix.js lib %buildroot%nodejs_sitelib/%node_module/
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
node %nodejs_sitelib/mocha/bin/mocha.js \
  --ignore test/braces.js \
  --ignore test/options.expandRange.js

%files
%doc LICENSE README.md
%nodejs_sitelib/%node_module/

%changelog
* Fri Jul 03 2026 Grant Makyan <karonus@altlinux.org> 4.0.5-alt1
- Initial build for ALT.
