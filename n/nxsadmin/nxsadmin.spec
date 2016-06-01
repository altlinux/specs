Name: nxsadmin
Version: 0.2.1
Release: alt7

Summary: Administering graphic tool for FreeNX server

License: GPL
Url: https://github.com/vitlav/nxsadmin
Group: System/Configuration/Other

Requires: freenx-server

#Source: http://download.berlios.de/nxsadmin/%name-%version.tar
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar
Source1: %name.desktop

# Automatically added by buildreq on Fri Apr 11 2008
BuildRequires: gcc-c++ libgtkmm2-devel perl-XML-Parser intltool

%description
FreeNX Sessions Administrator provides a graphical tool for management of active NX sessions on FreeNX server.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_desktopdir %buildroot%_niconsdir
install -m 644 %SOURCE1 %buildroot%_desktopdir
install -m 644 %name-icon.png %buildroot%_niconsdir
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README TODO
%_sbindir/nxsadmin
%_desktopdir/%name.desktop
%_niconsdir/*.png

%changelog
* Mon May 30 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt7
- rewrite configure.am
- enable -std=c++0x if compiler supports it (for gtkmm built with C++11)

* Tue May 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt6
- cleanup spec

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.2.1-alt5.qa1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.1-alt5.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * altlinux-policy-obsolete-buildreq for nxsadmin

* Fri May 22 2009 Boris Savelev <boris@altlinux.org> 0.2.1-alt5
- fix build with new toolchain
- fix requires
- remove pre/post

* Fri Aug 01 2008 Boris Savelev <boris@altlinux.org> 0.2.1-alt4
- repocop tests fix

* Wed Jun 18 2008 Boris Savelev <boris@altlinux.org> 0.2.1-alt3
- add icon

* Mon Jun 16 2008 Boris Savelev <boris@altlinux.org> 0.2.1-alt2
- fix path in desktop file

* Fri Apr 11 2008 Boris Savelev <boris@altlinux.org> 0.2.1-alt1
- new version (0.2.1)

* Fri Mar 07 2008 Boris Savelev <boris@altlinux.org> 0.2-alt1
- initial build
