Name: pve-docs
Summary: Proxmox VE Documentation
Version: 4.3.2
Release: alt1
License: GPLv3
Group: Documentation
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: asciidoc-a2x source-highlight xmlto

%description
Proxmox VE Documentation files

%package -n pve-doc-generator
Summary: Proxmox VE Documentation helpers
Group: Documentation
Requires: asciidoc-a2x source-highlight xmlto

%description -n pve-doc-generator
Tool to auto-generate various Proxmox VE Documentation files

%add_findreq_skiplist %_datadir/pve-doc-generator/*.pl

%prep
%setup -q -n %name-%version
rm -fr .gear debian doc-debian *.spec
tar -cf ../%name.tar *

%build
%make

%install
mkdir -p %buildroot%_datadir/pve-doc-generator
tar -xf ../%name.tar -C %buildroot%_datadir/pve-doc-generator/

mkdir -p %buildroot%_datadir/%name/api-viewer
install -m644 *.{html,epub,pdf} %buildroot%_datadir/%name/
install -m644 api-viewer/apidoc.js %buildroot%_datadir/%name/api-viewer/
install -m644 api-viewer/index.html %buildroot%_datadir/%name/api-viewer/

%files
%_datadir/%name

%files -n pve-doc-generator
%_datadir/pve-doc-generator

%changelog
* Tue Oct 04 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.2-alt1
- 4.3-2

* Mon Sep 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.11-alt1
- 4.2-11

* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.10-alt1
- 4.2-10

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.8-alt1
- 4.2-8

* Mon Jun 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.5-alt1
- 4.2-5

* Sat May 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2-alt1
- initial release

