%define _unpackaged_files_terminate_build 1
%define node_module window-size

%def_without check

Name: node-window-size
Version: 0.1.4
Release: alt1

Summary: Get the height and width of the terminal in a node.js environment
License: MIT
Group: Development/Other
Url: https://www.npmjs.com/package/window-size
# Source-git: https://www.npmjs.com/package/window-size

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node

%if_with check
BuildRequires: npm(semistandard)
BuildRequires: npm(tap)
%endif

Provides: nodejs-%node_module = %EVR
BuildArch: noarch

%description
Reliable way to get the height and width of terminal/console, since it's not
calculated or updated the same way on all platforms, environments and node.js
versions.

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -a package.json index.js %buildroot/%nodejs_sitelib/%node_module

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
node test.js

%files
%doc LICENSE README.md
%nodejs_sitelib/%node_module

%changelog
* Wed Jul 18 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus
