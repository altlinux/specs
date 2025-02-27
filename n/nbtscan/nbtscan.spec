Name: nbtscan
Version: 1.7.2
Release: alt1

Summary: NetBIOS Name Network Scanner
License: GPLv2
Group: Networking/Other
Url: https://github.com/resurrecting-open-source-projects/nbtscan

Source: %name-%version.tar

Packager: Igor Zubkov <icesik@altlinux.org>

%description
NBTscan is a program for scanning IP networks for NetBIOS name
information. It sends NetBIOS status query to each address in
supplied range and lists received information in human
readable form. For each responded host it lists IP address,
NetBIOS computer name, logged-in user name and MAC address
(such as Ethernet).

%prep
%setup

%build
./autogen.sh
%configure
%make_build

%install
make DESTDIR=%buildroot PREFIX=%prefix install

%files
%doc AUTHORS ChangeLog COPYING *.md
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Thu Feb 27 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.7.2-alt1
- NMU: New version 1.7.2.

* Mon Jun 24 2013 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt4
- Fix package summary

* Wed Oct 03 2012 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt3
- rebuilt for debuginfo

* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt2
- add Packager tag

* Sat Aug 27 2005 Igor Zubkov <icesik@altlinux.ru> 1.5.1-alt1
- Initial build for Sisyphus
