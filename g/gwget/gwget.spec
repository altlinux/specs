%define ver_major 1.0
%def_disable epiphany

Name: gwget
Version: %ver_major.4
Release: alt4.1

Summary: Gwget - Gnome2 wget Front-end
License: %gpl2plus
Group: Networking/File transfer
URL: http://gnome.org/projects/gwget
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar
Patch1: %name-%version-git.patch
Patch2: %name-%version-alt-fixes.patch
Patch3: %name-1.0.4-alt-glib2.patch

Provides: gwget2

BuildPreReq: rpm-build-gnome rpm-build-licenses common-licenses gnome-common
%{?_enable_epiphany:BuildRequires: epiphany-devel}
BuildRequires: gcc-c++ libgnomeui-devel libnotify-devel intltool
BuildRequires: libgtk+2-devel libdbus-glib-devel
BuildRequires: zlib-devel libGConf-devel
BuildRequires: libgio-devel >= 2.16.0

Requires: wget

%description
Gwget: Gnome2 wget Front-end.
Gwget it's a download manager for the Gnome Desktop. The main features are: 
* Resume: By default, gwget tries to continue any download.
* Notification: Gwget tries to use the Gnome notification area support, 
  if available. You can close the main window and gwget runs in the background.
* Recursivity: Gwget detects when you put a html, php, asp or a web page dir 
  in the url to download, and ask you 
  to only download certain files (multimedia, only the index, and so on).
* Drag & Drop: You can d&d a url to the main gwget window or 
  the notification area icon to add a new download. 

%if_enabled epiphany

%package -n epiphany-extension-gwget
Summary: Gwget extention for Epiphany browser
Group: Networking/File transfer
Requires:       %name = %version-%release
Requires:       epiphany epiphany-extensions
BuildRequires: epiphany-devel

%description -n epiphany-extension-gwget
Extention Gwget for Epiphany browser
%endif

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p0

rm -f COPYING
ln -s %_licensedir/GPL-2 COPYING

%build
./autogen.sh
%configure  \
%if_enabled epiphany
	--enable-epiphany-extension \
%endif
	--disable-static \
	--disable-schemas-install

%make_build

%install
%make_install install DESTDIR=%buildroot

# remove none-packaged files
%__rm -f %buildroot%_libdir/epiphany/*/extensions/*.{a,la}

%find_lang --with-gnome %name 

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
    %gconf2_uninstall %name
fi

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%doc --no-dereference COPYING
%_bindir/*
%_datadir/%name
%_datadir/pixmaps/*
%_datadir/applications/*
%config %_sysconfdir/gconf/schemas/*
%_datadir/dbus-1/services/*.service

%if_enabled epiphany
%files -n epiphany-extension-gwget
%_libdir/epiphany/*/extensions/*
%endif

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt4.1
- Fixed build

* Tue Jun 07 2011 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt4
- disable epiphany extension
- fix build with libnotify 0.7

* Sun Apr 11 2010 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt3
- git snapshot 160349a87de785ba2f3950fd197c18a19c7d32b5
- build with epiphany-2.30

* Mon Feb 22 2010 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt2
- support for Epiphany 2.29/2.30

* Mon Oct 19 2009 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue Aug 18 2009 Alexey Shabalin <shaba@altlinux.ru> 1.0.2-alt1.git20090815
- 1.0.2 + git 2009-08-15

* Tue Apr 07 2009 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sun Jan 18 2009 Alexey Shabalin <shaba@altlinux.ru> 0.99-alt2.svn20090107
- update svn r612

* Mon Oct 27 2008 Alexey Shabalin <shaba@altlinux.ru> 0.99-alt2.svn20080909
- update svn r160
- fix build with epiphany-2.24

* Tue Apr 01 2008 Alexey Shabalin <shaba@altlinux.ru> 0.99-alt2.svn20080309
- update to svn(20080309)
- fix build with epiphany-2.22

* Thu Nov 08 2007 Alexey Shabalin <shaba@altlinux.ru> 0.99-alt2.svn20071101
- update to svn(20071101) - update translations and fix two bugs
- fix build with epiphany-2.20

* Sat Jun 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.99-alt1
- 0.99
- remove patches
- remove SOURCE3 (dbus service in upstrem)

* Sat Mar 31 2007 Alexey Shabalin <shaba@altlinux.ru> 0.98.2-alt2
- fix build with epiphany 2.18

* Fri Nov 24 2006 Alexey Shabalin <shaba@altlinux.ru> 0.98.2-alt1
- 0.98.2
- add dbus service (source3)

* Thu Oct 26 2006 Alexey Shabalin <shaba@altlinux.ru> 0.98.1-alt2.cvs20061017
- cvs version 20061017
- Use dbus interface instead of bonobo
- Fix build with epiphany 2.16
- add %%set_verify_elf_method relaxed (undefined symbol in /usr/%_lib/epiphany/2.16/extensions/libgwgetextension.so)

* Wed May 17 2006 Alexey Shabalin <shaba@altlinux.ru> 0.98.1-alt1
- 0.98.1

* Tue Jan 10 2006 Alexey Shabalin <shaba@altlinux.ru> 0.97-alt1
- 0.97

* Wed Nov 09 2005 Alexey Shabalin <shaba@altlinux.ru> 0.96-alt2
- fix path epiphany-extension for epiphany v1.8
- fix BuildRequires

* Thu Aug 18 2005 Alexey Shabalin <shaba@altlinux.ru> 0.96-alt1
- 0.96 

* Tue May 24 2005 Alexey Shabalin <shaba@altlinux.ru> 0.95-alt1
- 0.95

* Fri May 13 2005 Alexey Shabalin <shaba@altlinux.ru> 0.94-alt1
- 0.94
- update spec 
- add epiphany-extension-gwget

* Sun Oct 26 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.7-alt1
- 0.7
- Added Recursive option if the url added it's not a file
- Cancel download in the popup menu now can be selected if the download it's in error state
- Added "Remove all downloads" and "Remove not running" options to the popup
- Added Japanese translation

* Mon Sep 29 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.6-alt1
- 0.6

* Wed Sep 17 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.5-alt2
- Cleanup spec

* Thu Jun 26 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.5-alt1
- 0.5
- Added Drag&Drop support.
- Added speed of the download information.

* Thu Jun 19 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.4-alt1
- 0.4

* Tue Jun 03 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.3-alt1
- 0.3

* Wed Apr 02 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.2-alt1
- First version of RPM package.

