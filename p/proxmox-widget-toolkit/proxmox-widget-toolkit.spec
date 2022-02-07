%define _unpackaged_files_terminate_build 1

Name: proxmox-widget-toolkit
Summary: ExtJS Helper Classes for Proxmox
Version: 3.4
Release: alt2
License: AGPL-3.0+
Group: Development/Other
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/proxmox-widget-toolkit.git
Source: %name-%version.tar
Patch: %name-%version.patch
BuildArch: noarch

Provides: pve-widget-toolkit = %EVR
Obsoletes: pve-widget-toolkit < %EVR
Requires: javascript-extjs

%description
ExtJS Helper Classes to easy access to Proxmox APIs.

%package dev
Summary: Development dependencies for Proxmox Projects
Group: Development/Other
Requires: %name = %EVR

%description dev
Contains some common javascript code that are dev-dependencies,
for various Proxmox projects.

%prep
%setup
%patch -p1

%build
%install
export PACKAGE=%name
%makeinstall_std -C src

#install dev files
install -pD -m644 src/Toolkit.js %buildroot%_datadir/javascript/%name-dev/Toolkit.js
install -pD -m644 src/api-viewer/APIViewer.js %buildroot%_datadir/javascript/%name-dev/APIViewer.js

%files
%_datadir/javascript/%name

%files dev
%_datadir/javascript/%name-dev

%changelog
* Mon Feb 07 2022 Alexey Shabalin <shaba@altlinux.org> 3.4-alt2
- Add Obsoltes: pve-widget-toolkit.

* Mon Jan 24 2022 Alexey Shabalin <shaba@altlinux.org> 3.4-alt1
- Initial build as separate package.
