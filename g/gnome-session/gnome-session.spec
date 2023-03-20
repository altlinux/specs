%def_disable snapshot
%define _userunitdir %(pkg-config systemd --variable systemduserunitdir)

%define ver_major 44
%define beta %nil
%define _libexecdir %_prefix/libexec
%def_enable systemd
%def_enable session_selector
%def_disable consolekit
%def_enable docs
%def_enable man

Name: gnome-session
Version: %ver_major.0
Release: alt1%beta

Summary: The gnome session programs for the GNOME GUI desktop environment
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://wiki.gnome.org/Projects/SessionManagement

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif
Source1: gnome.svg

# https://bugzilla.gnome.org/show_bug.cgi?id=775463
Patch: %name-2.91.6-alt-autosave_session.patch

# fedora patches:
# Blacklist NV30: https://bugzilla.redhat.com/show_bug.cgi?id=745202
Patch11: gnome-session-3.3.92-nv30.patch

# From configure.ac
%define glib_ver 2.46.0
%define gtk_ver 3.22.0
%define polkit_ver 0.91
%define upower_ver 0.9
%define systemd_ver 242

Requires(pre): xinitrc libcanberra-gnome libcanberra-gtk3
Requires: altlinux-freedesktop-menu-gnome3
Requires: dbus-tools-gui
Requires: gnome-filesystem
Requires: upower gcr gcr4
Requires: xdg-user-dirs

Requires: icon-theme-hicolor gnome-icon-theme-symbolic gnome-themes-standard

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-systemd
BuildRequires: meson libGConf2-devel
BuildRequires: libgio-devel glib2-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
# https://bugzilla.gnome.org/show_bug.cgi?id=710383
# BuildRequires: libupower-devel >= %upower_ver
BuildRequires: libgnome-desktop3-devel librsvg-devel libjson-glib-devel
BuildRequires: libX11-devel libXau-devel libXrandr-devel libXrender-devel libXt-devel
BuildRequires: libSM-devel libXext-devel libXtst-devel libXi-devel libXcomposite-devel
BuildRequires: libGL-devel libGLES-devel
BuildRequires: GConf browser-plugins-npapi-devel perl-XML-Parser xorg-xtrans-devel
BuildRequires: docbook-utils
%{?_enable_systemd:BuildRequires: pkgconfig(systemd) >= %systemd_ver libpolkit-devel}
%{?_enable_consolekit:BuildRequires: libdbus-glib-devel}
%{?_enable_docs:BuildRequires: docbook-utils xmlto}
%{?_enable_man:BuildRequires: docbook-utils docbook-style-xsl xsltproc}
# since 3.22.2
BuildRequires: libepoxy-devel

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.

This package provides the GNOME session manager, as well as a
configuration program to choose applications starting on login.

%package selector
Summary: The session selector for the GNOME
Group: Graphical desktop/GNOME
Requires: %name = %EVR

%description selector
This package permits to choose a saved GNOME session.

%package wayland
Summary: A Wayland session for the GNOME
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: %name = %EVR
Requires: xorg-xwayland

%description wayland
This package permits to log into GNOME using Wayland.

%prep
%setup -n %name-%version%beta
%patch11 -p1 -b .nv30

%build
export PATH=$PATH:/sbin
%meson \
    %{?_disable_systemd:-Dsystemd=false} \
    %{?_enable_consolekit:-Dconsolekit=true} \
    %{?_enable_session_selector:-Dsession_selector=true} \
    %{?_disable_docs:-Ddocbook=false} \
    %{?_disable_man:-Dman=false}
%nil
%meson_build

%install
%meson_install

%find_lang --with-gnome --output=%name.lang %name-%ver_major

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_bindir/%name-inhibit
%_bindir/%name-quit
%_libexecdir/%name-binary
%_libexecdir/%name-check-accelerated
%_libexecdir/%name-check-accelerated-gl-helper
%_libexecdir/%name-check-accelerated-gles-helper
%_libexecdir/%name-ctl
%_libexecdir/%name-failed
%dir %_datadir/%name
%_datadir/%name/hardware-compatibility

%dir %_datadir/%name/sessions
%_datadir/%name/sessions/gnome.session
%_datadir/%name/sessions/gnome-dummy.session
%_datadir/xsessions/gnome.desktop
%_datadir/xsessions/gnome-xorg.desktop
%config %_datadir/glib-2.0/schemas/org.gnome.SessionManager.gschema.xml
%_datadir/GConf/gsettings/%name.convert
%{?_enable_man:
%_man1dir/%name-inhibit.*
%_man1dir/%name-quit.*
%_man1dir/%name.*}
%doc AUTHORS NEWS README

%dir %_userunitdir/gnome-launched-.scope.d
%_userunitdir/gnome-launched-.scope.d/override.conf
%_userunitdir/gnome-session-x11-services-ready.target
%dir %_userunitdir/gnome-session@gnome.target.d
%_userunitdir/gnome-session@gnome.target.d/gnome.session.conf
%_userunitdir/%name-failed.service
%_userunitdir/%name-failed.target
%_userunitdir/%name-initialized.target
%_userunitdir/%name-manager.target
%_userunitdir/%name-manager@.service
%_userunitdir/%name-monitor.service
%_userunitdir/%name-pre.target
%_userunitdir/%name-restart-dbus.service
%_userunitdir/%name-shutdown.target
%_userunitdir/%name-signal-init.service
%_userunitdir/%name-wayland.target
%_userunitdir/%name-wayland@.target
%_userunitdir/%name-x11-services.target
%_userunitdir/%name-x11.target
%_userunitdir/%name-x11@.target
%_userunitdir/%name.target
%_userunitdir/%name@.target

%if_enabled session_selector
%files selector
%_bindir/%name-custom-session
%_bindir/%name-selector
%_datadir/%name/session-selector.ui
%{?_enable_man:%_man1dir/%name-selector.*}
%_datadir/xsessions/gnome-custom-session.desktop
%endif

%files wayland
%_datadir/wayland-sessions/gnome.desktop
%_datadir/wayland-sessions/gnome-wayland.desktop


%changelog
* Mon Mar 20 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Wed Jan 12 2022 Yuri N. Sedunov <aris@altlinux.org> 41.3-alt1
- 41.3

* Wed Jan 12 2022 Yuri N. Sedunov <aris@altlinux.org> 40.8-alt1
- 40.8

* Sat May 15 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1.1-alt1
- 40.1.1

* Tue Apr 27 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Mon Apr 12 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Wed Feb 24 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.2.beta
- 40.beta

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Mon Jul 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1.1
- spec: improved build knobs

* Mon Mar 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Thu Nov 28 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Sep 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed Apr 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Tue Feb 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt2
- removed autosave_session.patch (see BGO#775463, ALT#33126)

* Mon Nov 07 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Wed Oct 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Jul 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Oct 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1.1-alt1
- 3.18.1.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Dec 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt2
- disabled alt-specific mechanism for run gnome sessions, packaged
  standard *sessions/*.desktops instead

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Sun Jan 19 2014 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt3
- fixed problem with "classic" session when auto-save-session is set to true

* Wed Nov 20 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt2
- 3.10.1 snapshot (3f3066f3), fixed BGO ##710582, 710480

* Fri Oct 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Jul 30 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2.1-alt1
- 3.8.2.1
- new -selector subpackage

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1
- removed metacity-gnome from rqs (ALT #28840)

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.92-alt1
- 3.7.92
- by gnome-fallback session

* Fri Dec 21 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt2.1
- fixed install for gnome-authentication-agent.desktop

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt2
- updated to 15c3af7
- run polkit-gnome-authentication-agent-1 if session is gnome-fallback

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Thu Oct 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt2.1
- shaba:
  add fedora patches:
  gnome-session-3.3.1-llvmpipe.patch: Don't consider llvmpipe unsupported
  gnome-session-3.3.92-nv30.patch: blacklist NV30 family

* Tue Oct 02 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt2
- updated to 765827a

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Oct 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt2
- fixed string format in show_fallback_dialog()

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue Sep 20 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.92-alt1
- 3.1.92

* Tue Sep 13 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt2
- added /etc/X11/wmsession.d/02Gnome-fallback for fallback mode

* Mon Sep 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.91-alt1
- 3.1.91

* Thu Sep 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.90-alt1
- 3.1.90

* Thu Sep 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt2
- fixed a set of base directories exported by XDG_DATA_DIRS variable
  in startgnome script

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Sat May 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt6
- use gnome3- as XDG_MENU_PREFIX
- updated reqs/buildreqs

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt5
- added %%_datadir/gnome to $XDG_DATA_DIRS for use with gnome-specific
  defaults.list as in 2.32.1-alt2

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt4
- /usr/bin/startgnome removes
  ~/.config/gnome-session/saved-session/gnome-shell.desktop
  to avoid gnome-shell crash when
  /apps/gnome-session/options/auto_save_session is set to true
- Gconf-sanity-check reqs
- gnome-icon-theme-symbolic, gnome-icon-theme-standard temporarily added
  to reqs
- obsolete reqs and conflicts removed

* Tue May 03 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- added %%_datadir/gnome to $XDG_DATA_DIRS for use with gnome-specific
  defaults.list

* Wed Nov 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Wed Nov 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt3
- added libcanbera-gnome to rqs

* Thu Oct 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- debugging code removed

* Tue Oct 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.6-alt1
- 2.31.6

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Sun Apr 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- updared buildreqs

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Wed Jan 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6

* Sat Sep 26 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- splash screen enabled by default
- rebuild with new %%browser_plugins_path

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Thu Aug 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91
- PolicyKit-gnome -> polkit-gnome

* Tue Aug 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.5-alt2
- fixed http://bugzilla.gnome.org/show_bug.cgi?id=585614
- requires PolicyKit-gnome

* Wed Aug 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.5-alt1
- 2.27.5
- updated {build,}reqs
- set metacity as default wm

* Thu Jul 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt2
- set XDG_MENU_PREFIX variable to "gnome-" in startgnome2 (closes #20852)

* Wed Jul 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Fri May 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt2
- not packaged /usr/share/xsessions/gnome.desktop

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Wed Apr 08 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0.90-alt1
- new version

* Tue Mar 31 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- told where at-spi-registryd is

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Wed Mar 04 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Tue Feb 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.91-alt1
- 2.25.91

* Fri Jan 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Thu Dec 11 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt2
- requires GConf-sanity-check

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%{update,clean}_wms from %%post* scripts
- drop upstreamed patches
- don't package useless gnome-wm
- conflicts with old gdm (altbug #16911)

* Fri Oct 31 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- fix gnome bug #536915 (patch0)
- fix altbug #12333
- updated buildreqs

* Wed Oct 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sun Sep 28 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- drop obsoleted 2.13.4-no-crashes.patch
- Fedora's patches (5,6)

* Mon Jun 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.3-alt1
- new version (2.22.3)

* Mon Jun 02 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- new version (2.22.2)

* Sat May 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1.1-alt1
- new version (2.22.1.1)

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- new version (2.22.1)

* Sat Mar 29 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)

* Mon Dec 10 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20.2-alt2
- Moved autostart directory from gnome-session to gnome-filesystem.
- Updated buildreqs.

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.2-alt1
- new version (2.20.2)

* Fri Nov 23 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- new version (2.20.1)
- add Packager

* Mon Aug 13 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt4
- fixed Bug #12333 (thanks to raorn@ for gnome-wm script).
- use more macros

* Fri Jul 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt3
- fixed building on x86_64

* Fri Jul 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt2
- removed dbus-launch from startgnome2 script - the session bus is already
  launched at the start of X session (see dbus-tools-gui package).

* Wed Jul 04 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt1
- new version (2.18.3)
- BROWSER is now always set to gnome-open in /usr/bin/startgnome2, so that the
  preferred browser is always used no matter how invoked
- WINDOW_MANAGER is no more initialized in /usr/bin/startgnome2,
  /usr/bin/gnome-wm can choose a proper window manager without hints
- temporarily removed splash-screen customization, since there is no GNOME
  artworks in the version 4.0 of design-graphics-desktop package
- updated dependencies and files list

* Wed Oct 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt3
- added dependency on dbus-tools-gui (for dbus-launch).

* Wed Sep 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt2
- fixed various problems with applying settings (incl. themes) in GNOME,
  due to DBus session unlaunched or launched improperly.

* Sun Sep 24 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)
- added /usr/share/gnome/autostart directory.

* Fri Sep 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt3
- add dependency on gnome-control-center >= 2.15.90 due to transtion from Bonobo to DBus.

* Wed Aug 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt2
- rebuilt with new gstreamer.

* Sun Aug 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt1
- new version (2.15.92)

* Fri Aug 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version (2.15.91)
- updated dependencies
- spec cleanup

* Thu Jun 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Tue Apr 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Sat Feb 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.90-alt1
- new version
- Fixed Bug #8442.
- don't flip the cursor in startgnome2 script.

* Tue Feb 07 2006 Mikhail Zabaluev <mhz@altlinux.ru> 2.12.0-alt1.1
- Rebuild with libgnomeui which has been fixed up for modular Xorg
- Correct xsetroot path since it was moved to /usr/bin
- Removed Debian-style menu
- Buildreq

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed excess buildreqs.

* Tue Aug 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.91-alt1
- 2.11.91

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.4-alt1
- 2.9.4

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.91-alt1
- 2.7.91

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Mon Sep 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt3
- Another fix gnome-splash location.

* Fri Sep 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- fix gnome-splash location.

* Tue Sep 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6.2-alt1
- 2.3.6.2

* Wed Jul 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Sat Jul 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3.1-alt1
- 2.3.3.1

* Sun Jun 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3
- Epiphany is a default BROWSER.
- Requires gnome-wm.

* Wed May 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Mon Apr 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt2
- Changed reboot-command to %_bindir/reboot and halt-command
  to %_bindir/poweroff (slava). Requires SysVinit-usermode to use.
  Close ## 2106, 1506

* Sun Mar 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Feb 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.2-alt2
- export BROWSER=galeon

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.2-alt1
- 2.2.0.2

* Wed Jan 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.90-alt1
- 2.1.90

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Thu Nov 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Mon Nov 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt2
- Built with new libwrap.

* Mon Nov 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Fri Oct 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Fri Oct 04 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-alt1.3
- remove pixmaps into design package (this package must provides
  "gnome-session-splash")

* Wed Oct 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.7-alt1.2
- Fonts antialiasing turned on by default.
- Metacity is a default window manager.

* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.7-alt1.1
- update buildreq to remove rsh

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.7-alt1
- 2.0.7
- Metacity added to requires list.

* Sat Jun 22 2002 Igor Androsov <blake@altlinux.ru> 2.0.1-alt1
- New release
- gnome-session-2.0.1-splash.patch
- Fix from Yuri Sedunov <aris@altlinux.ru>
	+ Added Gnome2.xpm
	+ Replace command by macros
	+ cleanup spec
	+ clean_wms run in postun
	
* Thu May 16 2002 Igor Androsov <blace@mail.ru> 1.5.19-blk1
- New version from CVS

* Mon May 13 2002 Igor Androsov <blace@mail.ru> 1.5.18-blk1
- Changes for AltLinux
- cleanup spec
- Added wmsession and script

* Tue Mar 05 2002 Chris Chabot <chabotc@reviewboard.com>
- Final cleanups
- make .spec.in

* Fri Feb 15 2002 Chris Chabot <chabotc@reviewboard.com>
- initial spec file for gnome-session
