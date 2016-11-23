Name: pve-docs
Summary: Proxmox VE Documentation
Version: 4.3.16
Release: alt1
License: GPLv3
Group: Documentation
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar

ExclusiveArch: x86_64
BuildArch: noarch
BuildRequires: asciidoc-a2x source-highlight xmlto inkscape mailcap pve-common pve-ha-manager
BuildRequires: perl(MediaWiki/API.pm) perl(JSON.pm)

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

%build
%make

%install
mkdir -p %buildroot%_datadir/pve-doc-generator/asciidoc
cp *.adoc *.pl *.mk *.xml %buildroot%_datadir/pve-doc-generator/
cp asciidoc/*pve*.conf %buildroot%_datadir/pve-doc-generator/asciidoc/

mkdir -p %buildroot%_datadir/%name/api-viewer
install -m644 *.{html,epub,pdf} %buildroot%_datadir/%name/
install -m644 api-viewer/apidoc.js %buildroot%_datadir/%name/api-viewer/
install -m644 api-viewer/index.html %buildroot%_datadir/%name/api-viewer/
install -pD -m755 asciidoc-pve %buildroot%_bindir/asciidoc-pve

%files
%_datadir/%name

%files -n pve-doc-generator
%_bindir/asciidoc-pve
%_datadir/pve-doc-generator

%changelog
* Wed Nov 23 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.16-alt1
- 4.3-16

* Fri Oct 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.12-alt1
- 4.3-12

* Sun Oct 09 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.5-alt2
- pve-doc-generator: fixed build man pages

* Fri Oct 07 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.3.5-alt1
- 4.3-5

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

