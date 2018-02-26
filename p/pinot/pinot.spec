%def_disable deskbar

Name: pinot
Version: 0.98
Release: alt2

Summary: Personal search and metasearch tool
License: GPLv2+
Group: File tools

Url: http://pinot.berlios.de/
Source: http://pinot-search.googlecode.com/files/pinot-%version.tar.gz

# Automatically added by buildreq on Sat Nov 26 2011
BuildRequires: boost-devel-headers desktop-file-utils gcc-c++ libarchive-devel libattr-devel libchm-devel libcurl-devel libdbus-glib-devel libexiv2-devel libgmime-devel libgtkmm2-devel libsqlite3-devel libssl-devel libtag-devel libtextcat-devel libxapian-devel libxml++2-devel

%description
Pinot is a D-Bus service that crawls, indexes your documents and monitors them
for changes, as well as a GTK-based user interface that enables to query the
index built by the service and your favourite Web engines, and display and
analyze the results.

%package deskbar
Summary: Pinot plugin for DeskbarApplet
Group: File tools
Requires: %name = %version-%release
Requires: deskbar-applet

%description deskbar
The included plugin enables Deskbar to search documents indexed by Pinot.

%prep
%setup

subst 's~glib/gunicode.h~glib.h~' IndexSearch/cjkv/CJKVTokenizer.h

%build
# Add missing Additional Category
subst 's/Settings;X/Settings;DesktopSettings;X/' pinot-prefs.desktop
%configure --enable-libarchive --enable-chmlib
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS FAQ NEWS README
%config(noreplace) %_sysconfdir/pinot/
%_bindir/pinot
%_bindir/pinot-dbus-daemon
%_bindir/pinot-index
%_bindir/pinot-label
%_bindir/pinot-prefs
%_bindir/pinot-search
%_libdir/pinot/
%_datadir/dbus-1/services/de.berlios.Pinot.service
%_datadir/pinot/
%_iconsdir/hicolor/48x48/apps/pinot.png
%_iconsdir/hicolor/32x32/apps/pinot.png
%_iconsdir/hicolor/24x24/apps/pinot.png
%_iconsdir/hicolor/22x22/apps/pinot.png
%_iconsdir/hicolor/16x16/apps/pinot.png
%_sysconfdir/xdg/autostart/*.desktop
%_desktopdir/*.desktop
%_man1dir/pinot*

%if_enabled deskbar
%files deskbar
%_libdir/deskbar-applet/handlers/pinot-*
%_libexecdir/deskbar-applet/modules-2.20-compatible/pinot-*
%endif

%changelog
* Fri Apr 06 2012 Victor Forsiuk <force@altlinux.org> 0.98-alt2
- Fix glib include compile problem.

* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 0.98-alt1
- 0.98

* Tue Jun 07 2011 Alexey Shabalin <shaba@altlinux.ru> 0.97-alt2
- build without deskbar applet

* Tue Mar 29 2011 Victor Forsiuk <force@altlinux.org> 0.97-alt1
- 0.97

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 0.96-alt1.1
- NMU: rebuilt against libxapian-1.2.3

* Tue Jul 13 2010 Victor Forsiuk <force@altlinux.org> 0.96-alt1
- 0.96

* Fri Dec 25 2009 Victor Forsyuk <force@altlinux.org> 0.95-alt1
- 0.95

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.94-alt1.1
- Rebuilt with python 2.6

* Wed Jul 08 2009 Victor Forsyuk <force@altlinux.org> 0.94-alt1
- 0.94
- Build with libarchive.

* Mon Dec 01 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.89-alt1
- new version

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.85-alt1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Sat May 10 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.85-alt1
- First build for ALTLinux

