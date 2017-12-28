Name: gpodder
Version: 3.9.5
Release: alt1

Summary: podcast receiver/catcher in PyGTK
License: GPLv3
Group: Sound
Url: http://gpodder.org
BuildArch: noarch

# VCS: https://github.com/gpodder/gpodder.git
Source: %url/src/%name-%version.tar.gz

BuildRequires: python-devel rpm-build-python python-module-mygpoclient
BuildRequires: python-module-feedparser help2man intltool desktop-file-utils

%description
gPodder enables you to subscribe to RSS feeds and download
podcast episodes from these feeds. gPodder can operate in
GUI mode and in CLI mode. Downloaded podcasts can either
be synchronized to portable MP3 players (including iPods)
or played back on the user's desktop.

%prep
%setup

%build
%make

%install
%makeinstall_std

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Tuner \
	%buildroot%_desktopdir/gpodder.desktop

%files -f %name.lang
%_bindir/*
%python_sitelibdir/*
%_desktopdir/%name.desktop
%_desktopdir/%name-url-handler.desktop
%_datadir/dbus-1/services/org.gpodder.service
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.svg
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/*/apps/%name.ico
%_man1dir/*

# non-linux os-specific stuff
%exclude %python_sitelibdir/gpodder/gtkui/macosx.*
%exclude %_datadir/%name/extensions/ubuntu_*
%exclude %_datadir/%name/extensions/notification-win32.py*
%exclude %_datadir/%name/extensions/taskbar_progress.py*
# https://github.com/SoCo/SoCo
%exclude %_datadir/%name/extensions/sonos.py*

%changelog
* Thu Dec 28 2017 Yuri N. Sedunov <aris@altlinux.org> 3.9.5-alt1
- 3.9.5

* Sat Jan 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.9.3-alt1
- 3.9.3

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.9.1-alt1
- 3.9.1

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.9.0-alt1
- 3.9.0

* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.8.5-alt1
- 3.8.5

* Fri May 29 2015 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Mon Nov 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Wed Oct 08 2014 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Jul 07 2014 Yuri N. Sedunov <aris@altlinux.org> 3.7.0-alt1
- 3.7.0

* Tue Jul 10 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.2-alt1
- 3.1.2

* Thu Jan 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.3-alt1
- 3.0.3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3-alt1.qa1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.3-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gpodder

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 2.3-alt1
- 2.3

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- new version

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.1-alt1.qa1.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.12.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gpodder
  * postclean-05-filetriggers for spec file

* Fri Jul 25 2008 Alexander Myltsev <avm@altlinux.ru> 0.12.1-alt1
- new version: bug fixes, usability enhancements.

* Tue Mar 11 2008 Alex V. Myltsev <avm@altlinux.ru> 0.11-alt1
- new version: systray icon, Bluetooth support, usability changes, bug fixes

* Fri Jan 18 2008 Alex V. Myltsev <avm@altlinux.ru> 0.10.3-alt1
- New version.

* Sun Nov 11 2007 Alex V. Myltsev <avm@altlinux.ru> 0.10.1-alt1
- Initial build for Sisyphus.
