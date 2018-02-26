
Name: multisync-gui
Version: 0.91.0
Release: alt3.svn353.qa3

Summary: A calendar (and other PIM data) synchronization program
License: GPL
Group: Communications
URL: http://www.opensync.org/

Source: %name-%version.tar.bz2
Source1: multisync.desktop
Source2: multisync48.png
Source3: multisync32.png
Source4: multisync16.png
Patch0: multisync-gui-alt-no-rpath.patch

Packager: Mobile Development Team <mobile@packages.altlinux.org>

Provides: multisync0.90
Obsoletes: multisync0.90

Requires: libopensync >= 0.30

BuildRequires: libglade-devel python-modules-compiler python-modules-encodings
BuildRequires: zlib-devel libxml2-devel
BuildRequires: libopensync-devel >= 0.30

%description
MultiSync is a program to synchronize calendars, addressbooks and other PIM data
between programs on your computer and other computers, mobile devices, PDAs or
cell phones. It relies on the OpenSync framework to do the actual
synchronisation.

%prep
%setup -q 
%patch0 -p2

%build

# %%configure
%add_optflags -I%_includedir/libxml2
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%_prefix
%make

%install
%make_install install DESTDIR=%buildroot
###rm -f buildroot%_bindir/convcard

%__install -pD -m 644 %SOURCE1 %buildroot%_datadir/applications/%name.desktop

%__install -pD -m 644  %SOURCE2 %buildroot%_liconsdir/%name.png
%__install -pD -m 644  %SOURCE3 %buildroot%_niconsdir/%name.png
%__install -pD -m 644  %SOURCE4 %buildroot%_miconsdir/%name.png

%files
%_bindir/*
##%doc AUTHORS README COPYING 
%_datadir/applications/%name.desktop
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png
%_datadir/pixmaps/*
%_datadir/%name/*

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.91.0-alt3.svn353.qa3
- Removed bad RPATH

* Tue May 10 2011 Andrey Cherepanov <cas@altlinux.org> 0.91.0-alt3.svn353.qa2
- Fix build (add correct path to libxml2-devel headers)

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.91.0-alt3.svn353.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for multisync-gui
  * update_menus for multisync-gui
  * postclean-05-filetriggers for spec file

* Thu Jan 24 2008 Alexey Shabalin <shaba@altlinux.ru> 0.91.0-alt3.svn353
- build svn version for opensync-0.3X

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.91.0-alt2
- rebuild with libopensync-0.22

* Wed Nov 08 2006 Alexey Shabalin <shaba@altlinux.ru> 0.91.0-alt1
- release 0.91.0

* Wed Oct 11 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt2
- release 0.19

* Thu Sep 21 2006 Alexey Shabalin <shaba@altlinux.ru> 0.19-alt1cvs20060921
- svn version 20060921
- remove patch multisync0.90-gcc4.patch

* Mon May 29 2006 Alexey Shabalin <shaba@altlinux.ru> 0.18-alt1cvs20060529
- two src rpm package: cli and gui
- add doc
- add icons
- add desktop file
- add patch for build with gcc4.1

* Tue Mar 07 2006 Alexey Shabalin <shaba@altlinux.ru> 0.90.18-alt2
- fix BuildRequires

* Tue Nov 22 2005 Alexey Shabalin <shaba@altlinux.ru> 0.90.18-alt1
- 0.18 release
- build for Sisyphus
- add Packager SynCE Development Team

* Fri Sep 30 2005 Alexey Shabalin <shaba@altlinux.ru> 0.90.18-alt0.1.cvs20050930
- Initial package
