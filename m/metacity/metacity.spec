%define ver_major 2.34
%def_disable static
%def_enable compositor
%def_enable render
%def_enable shape

Name: metacity
Version: %ver_major.3
Release: alt1

Summary: Metacity window manager
License: %gpl2plus
Group: Graphical desktop/GNOME
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>
Url: http://ftp.gnome.org/pub/gnome/sources/%name

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# http://bugzilla.gnome.org/show_bug.cgi?id=558723
Patch4: stop-spamming-xsession-errors.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=135056
Patch5: dnd-keynav.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=588119
# https://bugzilla.gnome.org/show_bug.cgi?id=598995
Patch16: Dont-focus-ancestor-window-on-a-different-workspac.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599097
Patch18: For-mouse-and-sloppy-focus-return-to-mouse-mode-on.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599248
Patch19: Add-nofocuswindows-preference-to-list-windows-that.patch
Patch119: Exclude-the-current-application-from-no_focus_window.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599261
Patch20: Add-a-newwindowsalwaysontop-preference.patch
Patch120: Apply-new_windows_always_on_top-to-newly-raised-acti.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=559816
Patch24: metacity-2.28-empty-keybindings.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=604319
Patch25: metacity-2.28-xioerror-unknown-display.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=599181
Patch28: Stop-confusing-GDK-s-grab-tracking.patch
# https://bugzilla.gnome.org/show_bug.cgi?id=622517
Patch29: Allow-breaking-out-from-maximization-during-mouse.patch


%define theme_prefix theme
%define old_theme_prefix themes

# From configure.in
%define gtk_ver 2.24.0
%define pango_ver 1.2.0
%define glib_ver 2.25.10
%define startup_notification_ver 0.7
%define xcomposite_ver 0.2
%define gsds_ver 3.3.0

Requires: %name-theme = %version-%release
Requires: lib%name = %version-%release
Requires: zenity

# From configure.in
BuildPreReq: rpm-build-gnome rpm-build-licenses
BuildPreReq: intltool >= 0.34.90
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: libpango-devel >= %pango_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libstartup-notification-devel >= %startup_notification_ver
BuildPreReq: gsettings-desktop-schemas-devel >= %gsds_ver
%if_enabled compositor
BuildPreReq: libXcomposite-devel >= %xcomposite_ver
BuildRequires: libXfixes-devel libXrender-devel libXdamage-devel libXtst-devel
%endif
%{?_enable_render:BuildRequires: libXrender-devel}
BuildRequires: libXcursor-devel libXt-devel libXinerama-devel
%{?_enable_shape:BuildRequires: libXext-devel}
BuildRequires: gnome-doc-utils zenity libcanberra-gtk2-devel
BuildRequires: libXrandr-devel libX11-devel libSM-devel libICE-devel perl-XML-Parser libgtop-devel

%description
Metacity is a simple window manager that integrates nicely with
GNOME 2. It can also be used as a standalone, EWMH-compliant window
manager.
Note: to use Metacity with GNOME, you should install %name-gnome package.

%package -n lib%name
Summary: Shared library for Metacity
Group: System/Libraries

%description -n lib%name
This package contains shared library needed to run Metacity.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C
Requires: lib%name = %version-%release
Requires: libgtk+2-devel >= %gtk_ver

%description -n lib%name-devel
This package contains headers and development libraries for lib%name

%package -n lib%name-devel-static
Summary: Static version of lib%name
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the lib%name static library.

%package gnome
Summary: GNOME-specific parts of Metacity
Group: Graphical desktop/GNOME
Provides: gnome-wm
BuildArch: noarch
Requires: %name = %version-%release
Requires: gnome-filesystem gnome-control-center

%description gnome
This package contains everything necessary to use Metacity in GNOME desktop
environment.

%package %{theme_prefix}s-default
Summary: Metacity default themes
Group: Graphical desktop/GNOME
BuildArch: noarch
Obsoletes: %name-themes < 2.14.0
Provides: %name-themes = %version-%release
Requires: %name-%theme_prefix-atlanta = %version-%release	%name-%theme_prefix-bright = %version-%release
Requires: %name-%theme_prefix-crux = %version-%release		%name-%theme_prefix-esco = %version-%release
Requires: %name-%theme_prefix-gorilla = %version-%release	%name-%theme_prefix-metabox = %version-%release
Requires: %name-%theme_prefix-simple = %version-%release

%description %{theme_prefix}s-default
This is virtual package that provides default themes for Metacity.

%package %theme_prefix-atlanta
Summary: Metacity theme - Atlanta
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: %name-theme = %version-%release
Obsoletes: %name-%old_theme_prefix-atlanta = %version-%release
Provides: %name-%old_theme_prefix-atlanta = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-atlanta
This package contains a simple low-overhead default theme for Metacity.

%package %theme_prefix-bright
Summary: Metacity theme - Bright
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: %name-theme = %version-%release
Obsoletes: %name-%old_theme_prefix-bright = %version-%release
Provides: %name-%old_theme_prefix-bright = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-bright
This package contains a simple theme based on Havoc Pennington's Atlanta.

%package %theme_prefix-crux
Summary: Metacity theme - Crux
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: %name-theme = %version-%release
Obsoletes: %name-%old_theme_prefix-crux = %version-%release
Provides: %name-%old_theme_prefix-crux = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-crux
This package contains a port of the Crux theme by Arlo Rose and John
Harper.

%package %theme_prefix-esco
Summary: Metacity theme - Esco
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: %name-theme = %version-%release
Obsoletes: %name-%old_theme_prefix-esco = %version-%release
Provides: %name-%old_theme_prefix-esco = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-esco
This package contains a simple theme designed to look really good match
GTK+ well.

%package %theme_prefix-gorilla
Summary: Metacity theme - AgingGorilla
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: %name-theme = %version-%release
Obsoletes: %name-%old_theme_prefix-gorilla = %version-%release
Provides: %name-%old_theme_prefix-gorilla = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-gorilla
This package contains a port of the Gorilla theme by Jacub Steiner

%package %theme_prefix-metabox
Summary: Metacity theme - Metabox
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: %name-theme = %version-%release
Obsoletes: %name-%old_theme_prefix-metabox = %version-%release
Provides: %name-%old_theme_prefix-metabox = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-metabox
This package contains a theme that looks a little like BlackBox.

%package %theme_prefix-simple
Summary: Metacity theme - Simple
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: %name-theme = %version-%release
Obsoletes: %name-%old_theme_prefix-simple = %version-%release
Provides: %name-%old_theme_prefix-simple = %version-%release
Requires: %name = %version-%release

%description %theme_prefix-simple
This package contains default GNOME window theme. It based on Atlanta
theme.

%prep
%setup -q
%patch4 -p1 -b .stop-spamming-xsession-errors
%patch5 -p1 -b .dnd-keynav
%patch16 -p1 -b .focus-different-workspace
%patch18 -p1 -b .focus-on-motion
%patch19 -p1 -b .no-focus-windows
%patch119 -p1 -b .no-focus-windows-current-app
%patch20 -p1 -b .always-on-top
%patch120 -p1 -b .always-on-top-activate
%patch24 -p1 -b .empty-keybindings
%patch25 -p1 -b .xioerror-unknown-display
%patch28 -p1 -b .grab-tracking
%patch29 -p1 -b .mouse-unmaximize

%build
%autoreconf
%configure \
    %{subst_enable compositor} \
    %{subst_enable render} \
    %{subst_enable shape} \
    %{subst_enable static} \
    --enable-sm \
    --enable-startup-notification \
    --enable-xsync \
    --enable-xinerama \
    --disable-schemas-compile

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang  --with-gnome %name creating-%name-themes --output=%name.lang

%files -f %name.lang
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_man1dir/*
%doc README AUTHORS NEWS

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%doc doc/*.txt doc/*.dtd HACKING

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files gnome
%_datadir/gnome/wm-properties/*.desktop
%_datadir/gnome-control-center/keybindings/50-metacity*.xml
%_datadir/glib-2.0/schemas/org.gnome.metacity.gschema.xml
%_datadir/GConf/gsettings/metacity-schemas.convert

%files %{theme_prefix}s-default

%files %theme_prefix-gorilla
%_datadir/themes/AgingGorilla/*

%files %theme_prefix-atlanta
%_datadir/themes/Atlanta/*

%files %theme_prefix-bright
%_datadir/themes/Bright/*

%files %theme_prefix-crux
%_datadir/themes/Crux/*

%files %theme_prefix-esco
%_datadir/themes/Esco/*

%files %theme_prefix-metabox
%_datadir/themes/Metabox/*

%files %theme_prefix-simple
%_datadir/themes/Simple/*

%changelog
* Tue Mar 20 2012 Yuri N. Sedunov <aris@altlinux.org> 2.34.3-alt1
- 2.34.3

* Wed Feb 08 2012 Yuri N. Sedunov <aris@altlinux.org> 2.34.2-alt1
- 2.34.2

* Wed Jun 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.1-alt1
- 2.34.1

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0
- upstreamed patches removed
- updated buildreqs

* Mon Dec 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt3
- useless libcm removed from buildreqs

* Mon Oct 18 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.3-alt2
- add patches from fedora
- build themes as noarch

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.3-alt1
- 2.30.3

* Wed Sep 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sat Apr 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- fixed crash on right click on window title

* Thu Apr 01 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Jan 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Sep 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.1-alt1
- 2.27.1
- updated buildreqs

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Mon Feb 02 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.144-alt1
- 2.25.144
- removed upstreamed patches

* Fri Jan 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.89-alt1
- 2.25.89
- removed obsolete %%post{,un} scripts
- drop upstreamed patches
- updated buildreqs

* Wed Oct 01 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt2
- add fedora patches
- package included /usr/share/applications/metacity.desktop

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.0-alt1
- New version (2.24.0).

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- New version (2.22.0).

* Mon Mar 10 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.21-alt1
- New version (2.21.21).

* Mon Feb 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.20.2-alt1
- New version (2.20.2).
- update home url
- add Packager

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- New version (2.20.1).

* Sun Nov 04 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.0-alt1
- New version (2.20.0).
- Use rpm-build-licenses, use more macros from rpm-build-gnome.
- Revpatch from the previous build has been applied upstream.
- Moved %_datadir/gnome/wm-properties dir entry to gnome-filesystem
  package.
- Updated dependencies and the files list.
- Fixed installation method (%%make_install instead of %%makeinstall)

* Fri Jul 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.5-alt2
- added revpatch to fix metacity crash on logout, if there are windows that
  don't support session management. As a consequence of this crash, the next
  GNOME session would have started without metacity.

* Thu Jun 28 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.5-alt1
- new version (2.18.5)
- replaced the patch from GNOME Bug 155216 with the one from GNOME Bug 112560,
  as it is more elegant, more general and already marked as commit-now.
- minor spec tweaks

* Fri Jun 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.2-alt1
- new version (2.18.2)

* Sat Mar 31 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.5-alt2
- fixed Bug #11079.

* Wed Jan 31 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.5-alt1
- new version 2.16.5 (with rpmrb script)

* Mon Oct 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.3-alt2
- themes subpackages renamed to metacity-theme-*, to comply with the draft
  of GNOME themes policy.

* Tue Oct 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.3-alt1
- new version 2.16.3 (with rpmrb script)

* Sun Sep 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.2-alt2
- moved GNOME-specific parts to a separate -gnome subpackage.

* Fri Sep 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.2-alt1
- new version (2.16.2)
- updated dependencies
- removed explicit Atlanta theme requires, introduced metacity-theme
  provides and requires instead.

* Tue Aug 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.34-alt1
- new version 2.15.34 (with rpmrb script)

* Tue Aug 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.21-alt1
- new version 2.15.21 (with rpmrb script)

* Thu Aug 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.13-alt2
- added a patch that makes top pixels sensitive (GNOME bug 97703)

* Tue Jul 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.13-alt1
- new version 2.15.13 (with rpmrb script)

* Tue May 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.5-alt0.1
- new version 2.14.5 (with rpmrb script)

* Sat Apr 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.3-alt1
- new version 2.14.3 (with rpmrb script)

* Tue Apr 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Fri Mar 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt2
- fix metacity-dialog location.

* Fri Mar 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Fri Mar 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.89-alt0.1
- new version . (with rpmrb script)

* Sun Feb 19 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.89-alt2
- Added a patch from GNOME Bug 155216 to let window keybindings end windows switching.

* Mon Feb 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.89-alt1
- new version

* Thu Feb 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.55-alt1
- new version

* Sun Jan 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.34-alt1
- new version
- updated dependencies, introduced compositor, shape, render, gconf switches.

* Mon Jan 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.21-alt1
- new version

* Wed Jan 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.13-alt1
- new version

* Tue Nov 22 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.3-alt1
- new version

* Sat Nov 19 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version

* Tue Oct 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.0-alt1
- new version

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed more excess buildreqs.

* Tue Aug 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.3-alt1
- 2.11.3
- Removed excess buildreqs.

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Tue Apr 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Tue Feb 22 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.21-alt1
- 2.9.21

* Tue Feb 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.13-alt1
- 2.9.13

* Thu Dec 09 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.8-alt1
- 2.8.8

* Tue Nov 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.6-alt1
- 2.8.6

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.5-alt1
- 2.8.5

* Mon Aug 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.4-alt1
- 2.8.4 (temporarily closes problem #5056).

* Sat Aug 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.3-alt1
- 2.8.3

* Tue Aug 03 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Wed May 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Sun Mar 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Mon Feb 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Mon Feb 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt2
- do not package .la files.
- do not build devel-static subpackage by default.
- metacity-themes-simple subpackage.

* Tue Oct 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Thu Oct 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Fri Sep 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Wed Sep 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Thu Sep 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Wed Jul 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Sun Jun 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt2
- provides gnome-wm

* Wed May 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Sat May 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Sun Mar 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Wed Feb 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.34-alt1
- 2.4.34

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.21-alt1
- 2.4.21

* Fri Jan 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.13-alt1
- 2.4.13

* Tue Dec 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.8-alt2
- Remove obsoleted config dialog.

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Sat Nov 30 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.5-alt2
- fixed ru.po

* Tue Nov 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.5-alt1
- 2.4.5
- lib%name{,-devel{,-static}} subpackages.

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.3-alt2
- Rebuild with startup-notification.

* Tue Oct 29 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.3-alt1
- new version.

* Thu Oct 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt2.1
- Removed dependence on Metacity for default theme.

* Fri Oct 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt2
- %name-themes renamed to %name-themes-default.

* Sat Oct 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2
- themes splitted in separate packages.

* Sat Sep 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- First build for Sisyphus.
