%define _unpackaged_files_terminate_build 1
%define node_module source-map

Name: node-source-map
Version: 0.5.6
Release: alt1

Summary: Node.js library that generates and consumes source maps
License: BSD
Group: Development/Tools
Url: https://www.npmjs.com/package/source-map
# Source-git: https://github.com/mozilla/source-map

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node

Provides: nodejs-%node_module = %EVR
BuildArch: noarch

%description
%summary.

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a package.json source-map.js lib %buildroot/%nodejs_sitelib/%node_module

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
node test/run-tests.js

%files
%doc LICENSE *.md
%nodejs_sitelib/%node_module

%changelog
* Wed Jul 18 2018 Stanislav Levin <slev@altlinux.org> 0.5.6-alt1
- Initial build for Sisyphus
