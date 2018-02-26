%define oname PlayOnLinux

Summary: Play your Windows games on Linux
Name: playonlinux
Version: 3.7.3
Release: alt1.1
License: GPLv3
Group: Games/Other
Url: http://www.playonlinux.com
Packager: Boris Savelev <boris@altlinux.org>

Source: http://www.playonlinux.com/script_files/%oname/%version/%{oname}_%version.tar.gz
Source1: playonlinux.sh
Source2: %oname.desktop

Requires: ImageMagick
Requires: wget
Requires: gettext
Requires: unzip
Requires: cabextract
Requires: xterm
Requires: /usr/bin/wine
Requires: binutils

%add_findreq_skiplist %_datadir/%name/bash/*

ExclusiveArch: %ix86

%description
PlayOnLinux is a piece of sofware which allow you to install
and use easily numerous games and software designed to run
with Microsoft(R)'s Windows(R). Indeed, currently, still few
games are compatible with GNU/Linux, and it could be a factor
preventing from migrating to this system. PlayOnLinux brings an
accessible and efficient solution to this problem, cost-free
and respectful of the free software.

%prep
%setup -n %name

%install
mkdir %buildroot
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/desktop-directories
mkdir -p %buildroot%_desktopdir
mkdir -p %buildroot%_pixmapsdir

cp -a * %buildroot%_datadir/%name

install -p %SOURCE1 %buildroot%_bindir/%name
rm %buildroot%_datadir/%name/LICENCE
cp %SOURCE2 %buildroot%_desktopdir/%oname.desktop
cp etc/%name.png %buildroot%_pixmapsdir/%name.png
cp etc/PlayOnLinux.directory %buildroot%_datadir/desktop-directories/%oname.directory
rm -f %buildroot%_datadir/%name/bin/smile

%files
%doc LICENCE CHANGELOG
%_bindir/%name
%_datadir/%name
%_desktopdir/%oname.desktop
%_pixmapsdir/%name.png
%_datadir/desktop-directories/%oname.directory

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.3-alt1.1
- Rebuild with Python-2.7

* Sun Mar 14 2010 Boris Savelev <boris@altlinux.org> 3.7.3-alt1
- new version
- add findreq skiplist (closes: #23149)

* Tue Jul 21 2009 Boris Savelev <boris@altlinux.org> 3.6-alt1
- new version

* Thu Mar 12 2009 Boris Savelev <boris@altlinux.org> 3.4-alt1
- initial build for Sisyphus

* Sat Mar 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3.4-1mdv2009.1
+ Revision: 351817
- update to new version 3.4

* Fri Feb 13 2009 Guillaume Bedot <littletux@mandriva.org> 3.3.1-2mdv2009.1
+ Revision: 340055
- Make pol installable again
- Fix description

* Mon Feb 02 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3.3.1-1mdv2009.1
+ Revision: 336455
- update to new version 3.3.1

* Mon Jan 26 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3.3-1mdv2009.1
+ Revision: 333868
- update to new version 3.3

* Mon Dec 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2.2-2mdv2009.1
+ Revision: 320803
- rebuild for new python

* Mon Dec 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2.2-1mdv2009.1
+ Revision: 314396
- update to new version 3.2.2

* Sun Nov 30 2008 Emmanuel Andry <eandry@mandriva.org> 3.2.1-1mdv2009.1
+ Revision: 308522
- New version (bugfix)

* Sat Nov 29 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2-1mdv2009.1
+ Revision: 308015
- update to new version 3.2

* Tue Nov 11 2008 Emmanuel Andry <eandry@mandriva.org> 3.1.3-1mdv2009.1
+ Revision: 302278
- update to new version 3.1.3

* Mon Oct 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1.2-1mdv2009.1
+ Revision: 295743
- update to new version 3.1.2
- fix executable script

* Thu Jul 10 2008 Olivier Blin <oblin@mandriva.com> 3.0.8-3mdv2009.0
+ Revision: 233490
- do not untar the main source two times
- improve helper (use sh, do not fork, keep return code)
- python-devel is not required to build
- require wxPythonGTK
- gnome-python-extras/pygtk2.0/python-dbus are not used anymore

* Thu Jul 10 2008 Olivier Blin <oblin@mandriva.com> 3.0.8-2mdv2009.0
+ Revision: 233481
- require mesa-demos (for glxinfo)
- require cabextract and lzma
- require binutils for ar

* Thu Jul 03 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.8-1mdv2009.0
+ Revision: 231165
- update to new version 3.0.8

* Wed Jun 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.7-1mdv2009.0
+ Revision: 228894
- update to new version 3.0.7

* Mon Jun 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.4-1mdv2009.0
+ Revision: 219635
- add source and spec file
- Created package structure for playonlinux.

