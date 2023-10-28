%define _unpackaged_files_terminate_build 1
%define node_module cross-spawn

Name:    node-%node_module
Version: 7.0.3
Release: alt1

Summary: A cross platform solution to node's spawn and spawnSync
License: MIT
Group:   Other
URL:     https://www.npmjs.com/package/cross-spawn
VCS:     https://github.com/moxystudio/node-cross-spawn

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-nodejs

Provides: nodejs-%node_module = %EVR

BuildArch: noarch

%description
A cross platform solution to node's spawn and spawnSync.

%prep
%setup

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a lib %buildroot%nodejs_sitelib/%node_module/
cp -a index.js %buildroot%nodejs_sitelib/%node_module/
cp -a package.json %buildroot%nodejs_sitelib/%node_module/

%check

%files
%doc *.md
%nodejs_sitelib/%node_module

%changelog
* Sat Oct 28 2023 Andrey Limachko <liannnix@altlinux.org> 7.0.3-alt1
- Initial build for Sisyphus.
