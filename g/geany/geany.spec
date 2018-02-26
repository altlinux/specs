# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: geany
Version: 0.21
Release: alt2

Summary: A fast and lightweight IDE using GTK2
License: GPLv2
Group: Development/Tools
Url: http://geany.org

Source: %name-%version.tar.bz2

Requires: libvte
Requires: %name-data = %version
BuildPreReq: desktop-file-utils
BuildRequires: libgtk+2-devel gcc-c++ intltool

%add_findreq_skiplist %_datadir/%name/templates/files/*

%description
Geany is a small and lightweight integrated development environment.
It was developed to provide a small and fast IDE, which has only a few
dependencies from other packages. Another goal was to be as
independent as possible from a special Desktop Environment like KDE or
GNOME. So it is using only the GTK2 toolkit and therefore you need
only the GTK2 runtime libraries to run Geany.

%package data
Summary: Data files for Geany IDE
Group: Development/Tools
BuildArch: noarch
Requires: %name = %version

%description data
Architecture-independent data files for Geany IDE.

%package devel
Summary: Header files for building Geany plug-ins
Group: Development/C
Requires: %name = %version

%description devel
This package contains the header files and pkg-config file needed for
building Geany plug-ins. You do not need to install this package to
use Geany.

%prep
%setup

%build
%configure --docdir=%_defaultdocdir/%name-%version
%make_build --silent --no-print-directory

%install
%makeinstall_std --silent --no-print-directory
%find_lang %name
bzip2 %buildroot%_defaultdocdir/%name-%version/ChangeLog

%files
%_bindir/%name
%_libdir/%name/

%files -f %name.lang data
%_datadir/%name/
%_man1dir/%name.1.*
%_desktopdir/%name.desktop
%_miconsdir/classviewer-*.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg
%_defaultdocdir/%name-%version/

%files devel
%_includedir/%name/
%_pkgconfigdir/%name.pc

%changelog
* Mon May 21 2012 Fr. Br. George <george@altlinux.ru> 0.21-alt2
- DSO linking (@glebfm)

* Tue Oct 04 2011 Fr. Br. George <george@altlinux.ru> 0.21-alt1
- Autobuild version bump to 0.21

* Fri Jan 14 2011 Fr. Br. George <george@altlinux.ru> 0.20-alt1
- Autobuild version bump to 0.20

* Mon Dec 27 2010 Fr. Br. George <george@altlinux.ru> 0.19.2-alt0.M50P.1
- Rebuild for P5 (release fixed)

* Mon Dec 27 2010 Fr. Br. George <george@altlinux.ru> 0.19.2-alt0.M50p.1
- Rebuild for P5

* Fri Dec 24 2010 Fr. Br. George <george@altlinux.ru> 0.19.2-alt1
- Autobuild version bump to 0.19.2

* Mon Jul 19 2010 Fr. Br. George <george@altlinux.ru> 0.19-alt1
- Version up

* Mon Aug 17 2009 Slava Semushin <php-coder@altlinux.ru> 0.18-alt1
- Updated to 0.18
- Updated Summary and %%description of geany-devel subpackage

* Sun May 03 2009 Slava Semushin <php-coder@altlinux.ru> 0.17-alt1
- Updated to 0.17

* Sat Apr 11 2009 Slava Semushin <php-coder@altlinux.ru> 0.16-alt3
- Introduced -devel subpackage with files needed to build external
  plugins

* Thu Mar 26 2009 Slava Semushin <php-coder@altlinux.ru> 0.16-alt2
- Compress ChangeLog (noted by repocop)

* Fri Feb 20 2009 Slava Semushin <php-coder@altlinux.ru> 0.16-alt1
- Updated to 0.16

* Tue Dec 09 2008 Slava Semushin <php-coder@altlinux.ru> 0.15-alt2
- Moved data files to separated geany-data subpackage (noted by repocop)
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)
- Removed obsolete %%update_desktopdb/%%clean_desktopdb calls (noted by repocop)
- Changed Group to "Development/Tools"
- More proper License tag

* Mon Oct 20 2008 Slava Semushin <php-coder@altlinux.ru> 0.15-alt1
- Updated to 0.15
- New home page

* Sun Apr 27 2008 Slava Semushin <php-coder@altlinux.ru> 0.14-alt1
- Updated to 0.14 (deb #478126)
- Open local installed HTML documentation when user press F1
- Don't package headers and pkgconfig file
- Replace %%__autoreconf macros to %%autoreconf

* Thu Feb 07 2008 Slava Semushin <php-coder@altlinux.ru> 0.13-alt1
- Updated to 0.13

* Fri Oct 12 2007 Slava Semushin <php-coder@altlinux.ru> 0.12-alt1
- Updated to 0.12
- Don't force -Os gcc optimization for Scintilla (idea from OpenBSD)
- Don't specify full path and extension for Icon tag in desktop file
- Call %%{update,clean}_desktopdb in %%post/%%postun
- More strict Requires

* Sat May 26 2007 Slava Semushin <php-coder@altlinux.ru> 0.11-alt1
- Updated to 0.11
- Call %%update_menus/%%clean_menus in %%post/%%postun
- Removed find_svn_silently patch (applied by upstream)
- Imported into git and built with gear

* Mon Feb 26 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.10.2-alt1.1
- NMU based on spec from Slava Semushin <php-coder@>

* Mon Feb 26 2007 Slava Semushin <php-coder@altlinux.ru> 0.10.2-alt1
- Updated to 0.10.2 (bugfix release)
- Removed find_libvte_correctly patch (was backported from svn)

* Thu Feb 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.10-alt1.1
- Adapted spec from Slava Semushin <php-coder@>

* Thu Feb 08 2007 Slava Semushin <php-coder@altlinux.ru> 0.10-alt1
- Initial build for ALT Linux Sisyphus
- Applied two patches:
  + find_libvte_correctly (backported from SVN)
  + find_svn_silently (maded by me)

