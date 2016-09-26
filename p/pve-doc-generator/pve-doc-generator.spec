Name: pve-doc-generator
Summary: Proxmox VE Documentation helpers
Version: 4.2.11
Release: alt1
License: GPLv3
Group: Documentation
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar

Requires: asciidoc-a2x

BuildArch: noarch
BuildRequires: asciidoc-a2x source-highlight

%description
Tool to auto-generate various Proxmox VE Documentation files

%package -n pve-docs
Summary: Proxmox VE Documentation
Group: Documentation

%description -n pve-docs
Proxmox VE Documentation files

%add_findreq_skiplist %_datadir/%name/*.pl

%prep
%setup -q -n %name-%version
rm -fr .gear debian doc-debian *.spec
tar -cf ../%name.tar *

%build
%make

%install
mkdir -p %buildroot%_datadir/%name
tar -xf ../%name.tar -C %buildroot%_datadir/%name/

mkdir -p %buildroot%_datadir/pve-docs/api-viewer
install -m644 *.{html,epub,pdf} %buildroot%_datadir/pve-docs/
install -m644 api-viewer/* %buildroot%_datadir/pve-docs/api-viewer/

%files
%_datadir/%name

%files -n pve-docs
%_datadir/pve-docs

%changelog
* Mon Sep 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.11-alt1
- 4.2.-11

* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.10-alt1
- 4.2-10

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.8-alt1
- 4.2-8

* Mon Jun 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.5-alt1
- 4.2-5

* Sat May 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2-alt1
- initial release

