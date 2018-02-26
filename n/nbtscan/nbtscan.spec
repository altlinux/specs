Name: nbtscan
Version: 1.5.1
Release: alt2

Summary: NBTScan - NetBIOS Name Network Scanner
License: GPL v2
Group: Networking/Other
Url: http://www.inetcat.org/software/nbtscan.html

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

%description
NBTscan is a program for scanning IP networks for NetBIOS name
information. It sends NetBIOS status query to each address in
supplied range and lists received information in human
readable form. For each responded host it lists IP address,
NetBIOS computer name, logged-in user name and MAC address
(such as Ethernet).

%prep
%setup -q -n %name-%{version}a

%build
%configure
%make_build

%install
mkdir -p %buildroot%_bindir/
install -m755 nbtscan %buildroot%_bindir/

%files
%doc ChangeLog README
%_bindir/nbtscan

%changelog
* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 1.5.1-alt2
- add Packager tag

* Sat Aug 27 2005 Igor Zubkov <icesik@altlinux.ru> 1.5.1-alt1
- Initial build for Sisyphus
