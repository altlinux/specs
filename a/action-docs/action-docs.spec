%define _unpackaged_files_terminate_build 1
%define node_module action-docs

Name: %node_module
Version: 2.5.1
Release: alt1

Summary: Generate GitHub action docs based on action.yml
License: MIT
Group: Development/Tools

Url: https://github.com/npalm/action-docs
Vcs: https://github.com/npalm/action-docs
Source0: %name-%version.tar
Source1: %name-node_modules.tar

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-python3
BuildRequires: yarn
BuildRequires: /proc
BuildRequires: node-typescript

Requires: node

Provides: node-%node_module
Provides: nodejs-%node_module

BuildArch: noarch

ExcludeArch: i586

%description
%summary.

%prep
%setup -a 1

%build
yarn all

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module %buildroot%_bindir
cp -r lib src tsconfig.json node_modules README.md %buildroot%nodejs_sitelib/%node_module

rm -rf %buildroot%nodejs_sitelib/action-docs/node_modules/flatted

echo "
#!/bin/bash
node %nodejs_sitelib/%node_module/lib/cli.js
" > %buildroot%_bindir/%node_module
chmod +x %buildroot%_bindir/%node_module

%files
%nodejs_sitelib/%node_module
%_bindir/%node_module
%doc README.md

%changelog
* Fri Jun 13 2025 David Sultaniiazov <x1z53@altlinux.org> 2.5.1-alt1
- Initial build
