Name: conspy
Version: 1.7
Release: alt1

Summary: Remote control for text mode virtual consoles

Group: Terminals
License: GPL
Url: http://ace-host.stuart.id.au/russell/files/conspy/

Source: http://www.stuart.id.au/russell/files/conspy//%name-%version.tar.bz2

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Automatically added by buildreq on Sat Jan 21 2006
BuildRequires: libncurses-devel libtinfo-devel

%description
Conspy takes over a text mode Linux virtual console in much
the same manner as VNC allows a remote user to take over a GUI.

%prep
%setup

%build
touch NEWS
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/conspy
%_man1dir/*

%changelog
* Fri Oct 09 2009 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- new version 1.7 (with rpmrb script)

* Mon Jan 12 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- new version 1.5 (with rpmrb script)

* Sat Jan 21 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt0.1
- initial build for ALT Linux Sisyphus

* Sun Jan 19 2006 Russell Stuart <russell-rpm@stuart.id.au>
- New upstream release.
* Sun Jan  9 2006 Russell Stuart <russell-rpm@stuart.id.au>
- New upstream release.
* Sun Jan  1 2006 Russell Stuart <russell-rpm@stuart.id.au>
- New upstream release.
* Wed May 21 2003 Russell Stuart <russell-rpm@stuart.id.au>
- Initial RPM
