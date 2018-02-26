Name: xNBTscan
Version: 1.0
Release: alt2

Summary: xNBTscan is a graphical interface to NBTscan written in GTK+ 2.0
License: GPL
Group: Networking/Other

Url: http://md2600.dyndns.org/~daten/

Source0: %name-%version.tar.bz2

Patch0: xNBTscan-1.0-alt-build.patch

Requires: nbtscan

Packager: Igor Zubkov <icesik@altlinux.ru>

# Automatically added by buildreq on Sat Jan 21 2006
BuildRequires: fontconfig freetype2 glib2-devel libatk-devel libcairo-devel libgtk+2-devel libpango-devel pkg-config

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

%build
%make_build CFLAGS="%optflags"

%install
%__install -m755 -pD xnbtscan %buildroot%_bindir/xnbtscan

%files
%doc README
%_bindir/xnbtscan

%changelog
* Mon Mar 27 2006 Igor Zubkov <icesik@altlinux.ru> 1.0-alt2
- fix build with new ld / -Wl,--as-needed

* Sat Jan 21 2006 Igor Zubkov <icesik@altlinux.ru> 1.0-alt1
- Initial build for Sisyphus
