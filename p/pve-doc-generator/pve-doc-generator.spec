Name: pve-doc-generator
Summary: Proxmox VE Documentation helpers
Version: 4.2.10
Release: alt1
License: GPLv3
Group: Documentation
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar

Requires: asciidoc-a2x

BuildArch: noarch

%description
Tool to auto-generate various Proxmox VE Documentation files

%add_findreq_skiplist %_datadir/%name/*.pl

%prep
%setup -q -n %name-%version
rm -fr .gear debian doc-debian *.spec

%install
mkdir -p %buildroot%_datadir/%name
cp -a * %buildroot%_datadir/%name

%files
%_datadir/%name

%changelog
* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.10-alt1
- 4.2-10

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.8-alt1
- 4.2-8

* Mon Jun 06 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2.5-alt1
- 4.2-5

* Sat May 21 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.2-alt1
- initial release

