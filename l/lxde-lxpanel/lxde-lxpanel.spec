%define _unpackaged_files_terminate_build 1

%define upstreamname lxpanel
Name: lxde-%upstreamname
Version: 0.5.10
Release: alt3
Packager: LXDE Development Team <lxde at packages.altlinux.org>

Summary: LXPanel is a lightweight X11 desktop panel.
License: GPL
Group: Graphical desktop/Other
Url: http://lxde.sf.net

Source: %upstreamname-%version.tar
Patch: lxpanel-resize.patch
Patch1: lxpanel-taskbar-no-crash.patch
Patch2: lxpanel-xvt-default-terminal.patch
Patch3: lxpanel-0.5.8-alt-a-f2-fix.patch
Patch4: lxpanel-0.5.10-alt-fix-build.patch

Requires: lxde-freedesktop-menu
# Automatically added by buildreq on Tue May 04 2010
BuildRequires: imake intltool libalsa-devel libgtk+2-devel libmenu-cache-devel xorg-cf-files xsltproc
BuildRequires: libwnck-devel libwireless-devel docbook-dtds docbook-style-xsl

%description
lxpanel  is  a  program  that provides a panel for desktop, usually for
LXDE. It is lightweight GTK+ 2.x based desktop panel.

%package devel
Summary: development headers to build %name plugins
License: LGPL
Group: System/Libraries
Requires: %name = %version
%description devel
This package provides files required to build plugins
for %name

%prep
%setup -n %upstreamname-%version
%patch -p0
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2

%build
%autoreconf
%configure \
	--enable-man \
	--with-plugins=all \
	--enable-cast-checks

%make_build

%install
%makeinstall_std
%find_lang %upstreamname

%files -f %upstreamname.lang
%doc ChangeLog INSTALL README
%_bindir/*
%_datadir/%upstreamname
%_libdir/%upstreamname
%_man1dir/*

%files devel
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Wed Jun 20 2012 Radik Usupov <radik@altlinux.org> 0.5.10-alt3
- enabled alsa plugin

* Tue Jun 12 2012 Radik Usupov <radik@altlinux.org> 0.5.10-alt2
- All plugins build (Closes: 27435)
- Drop old patches

* Mon Jun 11 2012 Radik Usupov <radik@altlinux.org> 0.5.10-alt1
- New version (0.5.10)

* Tue May 08 2012 Radik Usupov <radik@altlinux.org> 0.5.9-alt1
- New version (0.5.9)

* Tue Mar 13 2012 Radik Usupov <radik@altlinux.org> 0.5.8-alt6
- Added lxpanel-fix-ru-po.patch

* Thu Feb 23 2012 Radik Usupov <radik@altlinux.org> 0.5.8-alt5
- Added batt_percentage_fix.patch (by Alexey Borisenkov) (Closes: 26948)

* Tue Jan 31 2012 Radik Usupov <radik@altlinux.org> 0.5.8-alt4
- New version from upstream git
- Fixed infinite loop (Closes: 24024)

* Mon Oct 03 2011 Radik Usupov <radik@altlinux.org> 0.5.8-alt3
- Updated russian translations
- Fixed menu not show due to incorect positioning

* Tue Sep 06 2011 Radik Usupov <radik@altlinux.org> 0.5.8-alt2
- fixed alt+f2 problem (thanks Alexey Borisenkov!)

* Mon Aug 29 2011 Radik Usupov <radik@altlinux.org> 0.5.8-alt1
- new version from upstream git

* Mon May 16 2011 Mykola Grechukh <gns@altlinux.ru> 0.5.6-alt7
- use xvt as default and fallback (fixes:#25608)

* Fri Mar 11 2011 Radik Usupov <radik@altlinux.org> 0.5.6-alt6
- rebuild for debuginfo

* Fri Mar 11 2011 Radik Usupov <radik@altlinux.org> 0.5.6-alt5
- changed requires for further transition to global freedesktop menu

* Fri Oct 29 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.6-alt4
- battery plugin fixed

* Wed Oct 20 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.6-alt3
- new version from upstream git
- Fixed segfault when exiting certain systray programs

* Wed Jul 21 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.6-alt1
- new upstream version

* Tue May 04 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.5-alt3.git3ad6e85
- devel subpackage

* Mon May 03 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.5-alt2.git3ad6e85
- new version from upstream git

* Fri Mar 12 2010 Nick S. Grechukh <gns@altlinux.ru> 0.5.5-alt1
- new version

* Wed Feb 03 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.4.1-alt5
- special font size for panel removed, now use gtk font

* Sat Jan 02 2010 Mykola Grechukh <gns@altlinux.ru> 0.5.4.1-alt3
- menu localization fixed (closes: #22649)

* Mon Dec 28 2009 Mykola Grechukh <gns@altlinux.ru> 0.5.4.1-alt2
- new upstream version

* Sat Dec 12 2009 Nick S. Grechukh <gns@altlinux.ru> 0.5.4-alt1
- new version

* Fri Aug 14 2009 Nick S. Grechukh <gns@altlinux.org> 0.5.3-alt2
- resize after xrandr event

* Fri Aug 14 2009 Nick S. Grechukh <gns@altlinux.org> 0.5.3-alt1
- new version

* Tue May 19 2009 Nick S. Grechukh <gns@altlinux.org> 0.4.1-alt2
- new version

* Wed Mar 04 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.3.999-alt1
- new version

* Fri Jan 09 2009 Eugene Ostapets <eostapets@altlinux.ru> 0.3.99-alt1
- new version

* Fri Jul 18 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.3.8.1-alt1
- new version

* Fri May 23 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.1-alt1
- First version of RPM package for Sisyphus.
