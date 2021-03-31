%define ver_major 1.0
%def_disable epiphany

Name: gwget
Version: %ver_major.4
Release: alt5

Summary: Gwget - Gnome wget Front-end
License: GPL-2.0+
Group: Networking/File transfer
URL: http://gnome.org/projects/gwget
Source: %name-%version.tar
Patch1: %name-%version-git.patch
Patch2: %name-%version-alt-fixes.patch

Provides: gwget2

%{?_enable_epiphany:BuildRequires: epiphany-devel}
BuildRequires: gcc-c++ libnotify-devel intltool
BuildRequires: libgtk+3-devel libdbus-glib-devel
BuildRequires: zlib-devel
BuildRequires: libgio-devel >= 2.16.0
BuildRequires: ImageMagick-tools
Requires: wget

%description
Gwget: Gnome wget Front-end.
Gwget it's a download manager for the Gnome Desktop. The main features are:
* Resume: By default, gwget tries to continue any download.
* Notification: Gwget tries to use the Gnome notification area support,
  if available. You can close the main window and gwget runs in the background.
* Recursivity: Gwget detects when you put a html, php, asp or a web page dir
  in the url to download, and ask you
  to only download certain files (multimedia, only the index, and so on).
* Drag & Drop: You can d&d a url to the main gwget window or
  the notification area icon to add a new download.

%package -n epiphany-extension-gwget
Summary: Gwget extention for Epiphany browser
Group: Networking/File transfer
Requires:       %name = %version-%release
Requires:       epiphany epiphany-extensions

%description -n epiphany-extension-gwget
Extention Gwget for Epiphany browser

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%add_optflags -fcommon
%autoreconf
%configure  \
%if_enabled epiphany
	--enable-epiphany-extension \
%endif
	--disable-static \
	--disable-schemas-install

%make_build

%install
%make_install install DESTDIR=%buildroot

mkdir -p %buildroot%_iconsdir/hicolor/{48x48,64x64,128x128}/apps/
convert pixmaps/gwget-large.png +set date:create +set date:modify -resize 48x48 -alpha on "%buildroot%_iconsdir/hicolor/48x48/apps/gwget.png"
convert pixmaps/gwget-large.png +set date:create +set date:modify -resize 64x64 -alpha on "%buildroot%_iconsdir/hicolor/64x64/apps/gwget.png"
convert pixmaps/gwget-large.png +set date:create +set date:modify -resize 128x128 -alpha on "%buildroot%_iconsdir/hicolor/128x128/apps/gwget.png"

# remove none-packaged files
rm -f %buildroot%_libdir/epiphany/*/extensions/*.{a,la}

%find_lang --with-gnome %name


%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_datadir/%name
%_datadir/pixmaps/*
%_iconsdir/hicolor/*/apps/gwget.png
%_datadir/applications/*
%_datadir/dbus-1/services/*.service
%_datadir/glib-2.0/schemas/*.xml

%if_enabled epiphany
%files -n epiphany-extension-gwget
%_libdir/epiphany/*/extensions/*
%endif

%changelog
* Wed Mar 31 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.4-alt5
- Add patches from Arch:
  + drop libgnomeui
  + gtk3 port
  + gsettings port
  + various fixes

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

