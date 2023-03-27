%define _unpackaged_files_terminate_build 1

Name: proxmox-widget-toolkit
Summary: ExtJS Helper Classes for Proxmox
Version: 3.6.4
Release: alt1
License: AGPL-3.0+
Group: Development/Other
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/proxmox-widget-toolkit.git
Source: %name-%version.tar
Patch: %name-%version.patch
BuildArch: noarch

BuildRequires: sassc

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
* Mon Mar 27 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.6.4-alt1
- 3.6.4

* Fri Mar 24 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.6.3-alt1
- 3.6.3

* Fri Mar 10 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.5.5-alt1
- 3.5.5

* Wed Sep 28 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.5.1-alt2
- change logo to BaseALT

* Thu Sep 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.5.1-alt1
- 3.5.1
- update marked.min.js (ALT #42101)

* Thu May 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.4.10-alt1
- 3.4-10

* Sun Mar 06 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.7-alt1
- 3.4-7

* Mon Feb 07 2022 Alexey Shabalin <shaba@altlinux.org> 3.4-alt2
- Add Obsoltes: pve-widget-toolkit.

* Mon Jan 24 2022 Alexey Shabalin <shaba@altlinux.org> 3.4-alt1
- Initial build as separate package.
