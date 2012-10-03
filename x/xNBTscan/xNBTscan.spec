Name: xNBTscan
Version: 1.0
Release: alt3

Summary: xNBTscan is a graphical interface to NBTscan written in GTK+ 2.0
License: GPLv2+
Group: Networking/Other

Url: http://md2600.dyndns.org/~daten/

Source0: %name-%version.tar.bz2

Patch0: xNBTscan-1.0-alt-build.patch
Patch1: xnbtscan-alt-fix-warnings.patch

Requires: nbtscan

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Tue Oct 02 2012
BuildRequires: libgtk+2-devel

%description
xNBTscan is a graphical interface to NBTscan written in GTK+ 2.0.

NBTscan is a program for scanning IP networks for NetBIOS name
information. It sends NetBIOS status query to each address in
supplied range and lists received information in human
readable form. For each responded host it lists IP address,
NetBIOS computer name, logged-in user name and MAC address
(such as Ethernet).

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%make_build CFLAGS="%optflags"

%install
install -m755 -pD xnbtscan %buildroot%_bindir/xnbtscan

%files
%doc README
%_bindir/xnbtscan

%changelog
* Tue Oct 02 2012 Igor Zubkov <icesik@altlinux.org> 1.0-alt3
- rebuilt for debuginfo

* Mon Mar 27 2006 Igor Zubkov <icesik@altlinux.ru> 1.0-alt2
- fix build with new ld / -Wl,--as-needed

* Sat Jan 21 2006 Igor Zubkov <icesik@altlinux.ru> 1.0-alt1
- Initial build for Sisyphus
