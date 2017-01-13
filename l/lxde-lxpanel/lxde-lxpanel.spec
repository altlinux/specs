%define _unpackaged_files_terminate_build 1
%define origname lxpanel
%define gtkver 2

Name: lxde-%origname
Version: 0.9.2
Release: alt1

Summary: LXPanel is a lightweight X11 desktop panel
License: GPL
Group: Graphical desktop/Other

Url: https://git.lxde.org/gitweb/?p=lxde/lxpanel.git
Source: %origname-%version.tar
Packager: LXDE Development Team <lxde at packages.altlinux.org>

#Requires: lxde-freedesktop-menu
Requires: altlinux-freedesktop-menu-lxde
Requires: menu-cache

# Automatically added by buildreq on Wed Jan 23 2013
# optimized out: fontconfig fontconfig-devel glib2-devel libX11-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libgtk+2-devel libmenu-cache libpango-devel libsystemd-daemon libwayland-client libwayland-server pkg-config xml-common xml-utils xorg-kbproto-devel xorg-xproto-devel xz
BuildRequires: docbook-dtds docbook-style-xsl imake intltool libalsa-devel libmenu-cache-devel libwireless-devel libwnck-devel xorg-cf-files xsltproc 

BuildRequires: libfm-devel libxml2-devel libkeybinder-devel
BuildPreReq: rpm-build-xdg libgtk+%gtkver-devel

%description
lxpanel is a program that provides a panel for desktop, usually LXDE.
It is lightweight GTK+ %gtkver.x based desktop panel.

%package devel
Summary: development headers to build %name plugins
License: LGPL
Group: System/Libraries
Requires: %name = %version

%description devel
This package provides files required to build plugins
for %name

%prep
%setup -n %origname-%version

%build
%autoreconf
%configure \
	--enable-man \
	--with-plugins=all \
	--enable-cast-checks \
%if %gtkver==3
    --enable-gtk3
%endif

%make_build

%install
%makeinstall_std
%find_lang %origname

%files -f %origname.lang
%doc AUTHORS ChangeLog README
%_bindir/*
%_xdgconfigdir/%origname
%_datadir/%origname
%_libdir/%origname
%_man1dir/*

%files devel
%_includedir/*
%_pkgconfigdir/*.pc

%changelog
* Wed Jan 11 2017 Anton Midyukov <antohami@altlinux.org> 0.9.2-alt1
- new version 0.9.2

* Wed Nov 23 2016 Anton Midyukov <antohami@altlinux.org> 0.9.1-alt1
- new version 0.9.1

* Sun Nov 20 2016 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- new version 0.9.0

* Tue May 24 2016 Anton Midyukov <antohami@altlinux.org> 0.8.2-alt2
- Replaced requires lxde-freedesktop-menu by altlinux-freedesktop-menu-lxde.

* Mon Apr 11 2016 Michael Shigorin <mike@altlinux.org> 0.8.2-alt1
- 0.8.2 (thx Alexey Borisenkov for suggestion)

* Wed Aug 27 2014 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- 0.7.0
- reorganized gear repo like lxqt-*
- minor spec cleanup

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 0.5.12-alt3.g3fd2186
- NMU: rebuilt against current libmenu-cache

* Sun Apr 27 2014 Michael Shigorin <mike@altlinux.org> 0.5.12-alt2.g3fd2186
- NMU: added R: menu-cache (closes: #30036)

* Wed Jan 23 2013 Mykola Grechukh <gns@altlinux.ru> 0.5.12-alt1.g3fd2186
- updated from upstream git

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
