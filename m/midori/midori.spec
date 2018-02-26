%def_without devel

Name: midori
Version: 0.4.5a
Release: alt1

Summary: is a lightweight web browser
License: LGPL
Group: Networking/WWW
Url: http://www.twotoasts.de/index.php?/pages/midori_summary.html

# git://git.xfce.org/apps/midori
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildPreReq: rpm-build-gnome gnome-common

BuildRequires: libgio-devel libgtk+2-devel libgtksourceview2-devel libwebkitgtk2-devel libxml2-devel
BuildRequires: libunique-devel intltool librsvg-utils python-modules-logging libsqlite3-devel
BuildRequires: libsoup-devel libidn-devel python-module-docutils libnotify-devel
BuildRequires: libXScrnSaver-devel vala

%description
Midori is a lightweight web browser.
 * Full integration with GTK+2
 * Fast rendering with WebKit
 * Tabs, windows and session management
 * Flexibly configurable Web Search
 * User scripts and user styles support
 * Straightforward bookmark management
 * Customizable and extensible interface
 * Extensions such as Adblock, form history, mouse gestures or
   cookie management

%if_with devel
%package devel
Summary: Development files for 'External Applications' extension
Group: Development/C
Requires: %name = %version-%release

%description devel
%summary
%endif

%prep
%setup
%patch0 -p1

%build
./waf --nocache configure --prefix=%_prefix --libdir=%_libdir -j 1
./waf --nocache build

%install
./waf --nocache install --destdir=%buildroot

%find_lang --with-gnome %name

%files -f %name.lang
%_sysconfdir/xdg/%{name}*
%_bindir/%name
%_libdir/%name
%_desktopdir/%name.desktop
%_desktopdir/%name-private.desktop
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/*/categories/*
%_iconsdir/hicolor/*/status/*
%_docdir/%name

%if_with devel
%files devel
%_includedir/%name-*
%_datadir/vala/vapi/*.deps
%_datadir/vala/vapi/*.vapi
%endif

%changelog
* Sun Apr 22 2012 Michael Shigorin <mike@altlinux.org> 0.4.5a-alt1
- 0.4.5a

* Thu Mar 22 2012 Michael Shigorin <mike@altlinux.org> 0.4.4-alt1
- 0.4.4 (thx iZEN for a hint)

* Sun Dec 18 2011 Vladimir Lettiev <crux@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Tue Nov 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.4.2-alt1
- 0.4.2
- dropped patch for incorrectly written protocol

* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt2
- rebuild with libwebkitgtk2-1.6.1

* Mon Oct 10 2011 Mykola Grechukh <gns@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Mon Aug 15 2011 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt1
- 0.4.0
- added some new search providers as suggested by Mykola Grechukh
  (Closes: #26037)

* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 0.3.6-alt2
- devel subpackage disabled by default

* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 0.3.6-alt1
- New version 0.3.6

* Mon Mar 14 2011 Vladimir Lettiev <crux@altlinux.ru> 0.3.3-alt1
- New version 0.3.3

* Sun Feb 20 2011 Vladimir Lettiev <crux@altlinux.ru> 0.3.2-alt1
- New version 0.3.2

* Mon Jan 31 2011 Vladimir Lettiev <crux@altlinux.ru> 0.3.0-alt1
- New version 0.3.0

* Tue Jan 11 2011 Vladimir Lettiev <crux@altlinux.ru> 0.2.9-alt2
- Fixed case of incorrectly written protocol (same behaviour as
  firefox) (Closes: #24894)

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.9-alt1
- New version 0.2.9

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.8-alt2
- Rebuild with libwebkitgtk2

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.8-alt1
- New version 0.2.8

* Tue Aug 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.7-alt1
- New version 0.2.7

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.6-alt1
- New version 0.2.6

* Tue May 18 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.5-alt1
- New version 0.2.5 (Closes: #23492)
- Add devel subpackage ('External Applications' extension)

* Sun Mar 14 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.4-alt1
- New version 0.2.4

* Fri Mar 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.3-alt1
- New version 0.2.3

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.2-alt2
- add missing adblock config
- add libnotify-devel build req

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.2-alt1
- New version 0.2.2

* Mon Oct 26 2009 Vladimir Lettiev <crux@altlinux.ru> 0.2.0-alt1
- New version

* Mon Sep 07 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.9-alt1
- New version

* Tue Jul 21 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.8-alt1
- New version (3201370)

* Wed Jun 17 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.7-alt1
- New version
- build user docs

* Sat May 02 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.6-alt1
- New version
- removed patch0

* Tue Apr 07 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.5-alt1
- New version

* Wed Jan 28 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.2-alt2
- Fix build on x86_64

* Mon Jan 26 2009 Vladimir Lettiev <crux@altlinux.ru> 0.1.2-alt1
- New version
- Fix TEXTREL in extensions

* Mon Sep 22 2008 Vladimir Lettiev <crux@altlinux.ru> 0.0.21-alt1
- New version

* Mon Sep 22 2008 Vladimir Lettiev <crux@altlinux.ru> 0.0.20-alt1
- Initial build for Sisyphus



