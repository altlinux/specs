%def_disable gtk_doc

Name: cinnamon
Version: 5.6.4
Release: alt1

Summary: A Linux desktop which provides advanced innovative features and a traditional user experience.
License: GPLv2+
Group: Graphical desktop/GNOME

Url: http://cinnamon.linuxmint.com
Source0: %name-%version.tar
Source1: polkit-%name-authentication-agent-1.desktop

Patch: %name-%version-%release.patch

%add_python3_path %_datadir/%name
%set_typelibdir %_libdir/%name

%define gtk_ver 3.12.0
%define gi_ver 0.10.1
%define muffin_ver 4.0.3
%define json_glib_ver 0.13.2
%define cjs_ver 4.0.0
%define polkit_ver 0.100
%define folks_ver 0.5.2
%define bt_ver 3.0.0

Provides: desktop-notification-daemon

Requires: dconf
Requires: upower
Requires: polkit >= %polkit_ver
Requires: polkit-gnome
# needed for session files
Requires: cinnamon-session >= 2.6.2
# needed for on-screen keyboard
Requires: caribou
Requires: cinnamon-freedesktop-menu
Requires: %name-data = %version-%release
Requires: muffin >= %muffin_ver
Requires: muffin-cinnamon >= %muffin_ver
Requires: libmuffin-gir >= %muffin_ver
Requires: %name-translations
Requires: mintlocale
Requires: gst-plugins-base1.0

Requires: libsoup-gir

# needed to install applets
Requires: gettext-tools

BuildRequires(pre): rpm-build-gir >= 0.7.3 rpm-build-python3
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libcjs-devel >= %cjs_ver
BuildPreReq: libjson-glib-devel >= %json_glib_ver
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: libcinnamon-desktop-devel libgnome-keyring-devel libcinnamon-menus-devel
BuildRequires: libstartup-notification-devel libcinnamon-desktop-gir-devel
BuildRequires: libpolkit-devel libupower-devel libgudev-devel libsoup-devel libnm-devel libnm-gir-devel
BuildRequires: libcanberra-gtk3-devel libcroco-devel
BuildRequires: gobject-introspection >= %gi_ver libupower-gir-devel libgudev-gir-devel libsoup-gir-devel
BuildRequires: libcinnamon-menus-gir-devel
BuildRequires: gst-plugins1.0-devel

# for barriers
BuildRequires: libXfixes-devel >= 5.0
# used in unused BigThemeImage
BuildRequires: librsvg-devel
BuildRequires: libmuffin-devel >= %muffin_ver
BuildRequires: libmuffin-gir-devel >= %muffin_ver
BuildRequires: libdrm-devel libgbm-devel
BuildRequires: libpulseaudio-devel

BuildRequires: desktop-file-utils
BuildRequires: gtk-doc gnome-common intltool
BuildRequires: at-spi2-atk-devel
BuildRequires: rpm-build-xdg
BuildRequires: libxapps-devel libxapps-gir-devel

%description
Cinnamon is a Linux desktop which provides advanced innovative features
and a traditional user experience.

The desktop layout is similar to Gnome 2. The underlying technology is
forked from Gnome Shell. The emphasis is put on making users feel at
home and providing them with an easy to use and comfortable desktop
experience.

%package data
Summary: Arch independent files for Cinnamon
Group: Graphical desktop/GNOME
BuildArch: noarch
Provides: python3(cme)
Provides: python3(Spices)
# https://bugzilla.altlinux.org/36995
Requires: python3-module-PAM
Requires: python3-module-xapps-overrides
# Required for xapp-status applet
Requires: xapp-sn-watcher
# Required for cinnamon-settings info module
Requires: python3(distro)

%description data
This package provides noarch data needed for Cinnamon to work.

%package devel-doc
Summary: Development doc package for Cinnamon
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
Development docs package for Cinnamon.

%prep
%setup -n %name-%version
%patch -p1

rm -rf debian

%build
%meson --libexecdir=%{_libexecdir}/cinnamon
%meson_build

%install
%meson_install


rm -f %buildroot/%_man1dir/cinnamon-session-cinnamon.1
rm -f %buildroot/%_man1dir/cinnamon-session-cinnamon2d.1

desktop-file-validate %buildroot%_desktopdir/cinnamon.desktop
desktop-file-validate %buildroot%_desktopdir/cinnamon2d.desktop

#install polkit files
install -D -p -m 0644 %SOURCE1 %buildroot/%_datadir/applications/

# Clean-up requires

# cinnamon/files/usr/share/cinnamon/cinnamon-settings/modules/cs_themes.py
# from gi.repository.Gtk import SizeGroup, SizeGroupMode
%filter_from_requires /python3[(]gi.repository.Gtk[)]/d

# There is already registered upstream issue https://github.com/linuxmint/muffin/issues/199
# But untill it will be fixed by Cinnamon devs we handle it manually.
# Note: to handle dependency we require libmuffin-gir explicitly
%filter_from_requires /typelib(Meta)/d

# Another conflict with gnome-shell
%filter_from_requires /typelib(St)/d

# Remove from explicit dependencies muffin private libraries. By default
# RPM doesn't generate this provides for muffin but generates requires
# for them in cinnamon debuginfo packages.
%filter_from_requires /libmuffin-clutter/d
%filter_from_requires /libmuffin-cogl/d

# Clean-up provides
# gnome-shell provides typelib(St) as well
%filter_from_provides /typelib(St)/d

%files
%exclude %_bindir/%{name}-launcher
%_bindir/*
%_libdir/cinnamon/
%_libexecdir/cinnamon/cinnamon-hotplug-sniffer
%_libexecdir/cinnamon/cinnamon-perf-helper
%_libexecdir/cinnamon/cinnamon-calendar-server.py

%files data
%exclude %_xdgmenusdir/cinnamon-applications-merged
%exclude %_xdgmenusdir/cinnamon-applications.menu
%exclude %_datadir/xsessions/*.desktop
%exclude %_datadir/cinnamon-session/sessions/*.session
%_datadir/cinnamon/
%_datadir/dbus-1/services/org.Cinnamon.HotplugSniffer.service
%_datadir/dbus-1/services/org.Cinnamon.Melange.service
%_datadir/dbus-1/services/org.Cinnamon.Slideshow.service
%_datadir/dbus-1/services/org.cinnamon.CalendarServer.service
%_datadir/desktop-directories/*.directory
%_datadir/glib-2.0/schemas/*.xml
%_datadir/polkit-1/actions/org.cinnamon.settings-users.policy
%python3_sitelibdir_noarch/cinnamon/
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*.svg
%_iconsdir/hicolor/*/*/*.png
%_man1dir/*.1.*

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Fri Dec 2 2022 Vladimir Didenko <cow@altlinux.org> 5.6.4-alt1
- 5.6.4

* Fri Nov 18 2022 Vladimir Didenko <cow@altlinux.org> 5.6.1-alt1
- 5.6.1

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.org> 5.4.12-alt1
- 5.4.12

* Fri Aug 26 2022 Vladimir Didenko <cow@altlinux.org> 5.4.11-alt1
- 5.4.11

* Tue Aug 2 2022 Vladimir Didenko <cow@altlinux.org> 5.4.9-alt1
- 5.4.9

* Thu Jul 21 2022 Vladimir Didenko <cow@altlinux.org> 5.4.5-alt1
- 5.4.5

* Tue Jul 12 2022 Vladimir Didenko <cow@altlinux.org> 5.4.2-alt1
- 5.4.2-31-g1fe1f5256

* Tue Jun 21 2022 Vladimir Didenko <cow@altlinux.org> 5.4.1-alt1
- 5.4.1

* Sat Jun 11 2022 Vladimir Didenko <cow@altlinux.org> 5.4.0-alt1
- 5.4.0-2-gdb2866ec3

* Mon Mar 28 2022 Vladimir Didenko <cow@altlinux.org> 5.2.7-alt3
- Fix build with meson 0.61

* Fri Mar 18 2022 Vladimir Didenko <cow@altlinux.org> 5.2.7-alt2
- Replace blueberry by blueman

* Wed Jan 12 2022 Vladimir Didenko <cow@altlinux.org> 5.2.7-alt1
- 5.2.7

* Wed Dec 15 2021 Vladimir Didenko <cow@altlinux.org> 5.2.5-alt1
- 5.2.5-11-g72f56d106

* Wed Dec 1 2021 Vladimir Didenko <cow@altlinux.org> 5.2.1-alt2
- Fix path to the cinnamon-calendar-server script

* Mon Nov 29 2021 Vladimir Didenko <cow@altlinux.org> 5.2.1-alt1
- 5.2.1-1-g8fc2df08b

* Tue Nov 9 2021 Vladimir Didenko <cow@altlinux.org> 5.0.7-alt1
- 5.0.7

* Wed Oct 27 2021 Vladimir Didenko <cow@altlinux.org> 5.0.6-alt1
- 5.0.6

* Wed Aug 4 2021 Vladimir Didenko <cow@altlinux.org> 5.0.5-alt1
- 5.0.5-5-g86bab3b54

* Tue Jun 29 2021 Vladimir Didenko <cow@altlinux.org> 5.0.3-alt1
- 5.0.3

* Thu Jun 17 2021 Vladimir Didenko <cow@altlinux.org> 5.0.2-alt1
- 5.0.2-9-g50814dec4

* Tue Jun 1 2021 Vladimir Didenko <cow@altlinux.org> 5.0.0-alt1
- 5.0.0

* Wed Apr 07 2021 Anton Midyukov <antohami@altlinux.org> 4.8.6-alt5
- Add Requires: libsoup-gir (Closes: 39890)

* Wed Mar 24 2021 Vladimir Didenko <cow@altlinux.org> 4.8.6-alt4
- Resolve deps conflict with gnome-shell

* Mon Feb 15 2021 Vladimir Didenko <cow@altlinux.org> 4.8.6-alt3
- Fix meson build deps for js test executable

* Wed Jan 20 2021 Vladimir Didenko <cow@altlinux.org> 4.8.6-alt2
- Another fix for parallel build

* Mon Jan 18 2021 Vladimir Didenko <cow@altlinux.org> 4.8.6-alt1
- 4.8.6

* Tue Jan 12 2021 Vladimir Didenko <cow@altlinux.org> 4.8.5-alt1
- 4.8.5

* Fri Dec 22 2020 Vladimir Didenko <cow@altlinux.org> 4.8.3-alt3
- Another try to fix parallel build

* Fri Dec 22 2020 Vladimir Didenko <cow@altlinux.org> 4.8.3-alt2
- Disable parallel build because it is still broken

* Mon Dec 21 2020 Vladimir Didenko <cow@altlinux.org> 4.8.3-alt1
- 4.8.3-2-gea573265

* Fri Dec 11 2020 Vladimir Didenko <cow@altlinux.org> 4.8.2-alt2
- Don't use parallel build since it is broken

* Fri Dec 11 2020 Vladimir Didenko <cow@altlinux.org> 4.8.2-alt1
- 4.8.2-7-gc2e7db6a

* Fri Nov 27 2020 Vladimir Didenko <cow@altlinux.org> 4.8.0-alt1
- 4.8.0-3-g8171c084

* Mon Nov 23 2020 Vladimir Didenko <cow@altlinux.org> 4.6.7-alt2
- Clean-up provides

* Thu Sep 3 2020 Vladimir Didenko <cow@altlinux.org> 4.6.7-alt1
- 4.6.7

* Mon Aug 3 2020 Vladimir Didenko <cow@altlinux.org> 4.6.6-alt2
- Add python3(distro) to dependencies (closes: #38775)
- Don't show input method module (closes: #38776)

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.org> 4.6.6-alt1
- 4.6.6-1-g60f631c7

* Tue Jun 23 2020 Vladimir Didenko <cow@altlinux.org> 4.6.5-alt1
- 4.6.5-1-g4531ff5e

* Tue Jun 9 2020 Vladimir Didenko <cow@altlinux.org> 4.6.3-alt1
- 4.6.3

* Wed May 27 2020 Vladimir Didenko <cow@altlinux.org> 4.6.2-alt1
- 4.6.2

* Thu May 21 2020 Vladimir Didenko <cow@altlinux.org> 4.6.1-alt1
- 4.6.1

* Mon May 18 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt4
- fix applets configuration

* Sat May 16 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt3
- return systray to default applets (xapp-status doesn't cover
  all use cases)

* Fri May 15 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt2
- add xapp-sn-watcher to requires
- remove systray from default applets (xapp-status is used instead)
- remove printers from default applets (see
  https://github.com/linuxmint/cinnamon/issues/9265)

* Thu May 14 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt1
- 4.6.0

* Wed Mar 11 2020 Vladimir Didenko <cow@altlinux.org> 4.4.8-alt2
- fix compatibility with Python 3.8

* Wed Jan 8 2020 Vladimir Didenko <cow@altlinux.org> 4.4.8-alt1
- 4.4.8

* Tue Dec 17 2019 Vladimir Didenko <cow@altlinux.org> 4.4.5-alt1
- 4.4.5

* Wed Dec 11 2019 Vladimir Didenko <cow@altlinux.org> 4.4.4-alt1
- 4.4.4-3-ge3712c51

* Mon Dec 2 2019 Vladimir Didenko <cow@altlinux.org> 4.4.2-alt1
- 4.4.2

* Thu Nov 28 2019 Vladimir Didenko <cow@altlinux.org> 4.4.1-alt1
- 4.4.1-3-g24eca8dd

* Mon Nov 25 2019 Vladimir Didenko <cow@altlinux.org> 4.4.0-alt1
- 4.4.0

* Wed Nov 20 2019 Vladimir Didenko <cow@altlinux.org> 4.2.4-alt3
- 4.2.3-109-g72f60941

* Fri Sep 27 2019 Vladimir Didenko <cow@altlinux.org> 4.2.4-alt2
- fix default apps module of cinnamon-settings

* Thu Sep 12 2019 Vladimir Didenko <cow@altlinux.org> 4.2.4-alt1
- 4.2.4

* Wed Aug 21 2019 Anton Midyukov <antohami@altlinux.org> 4.2.3-alt2
- Add missing Requires: typelib(Soup)

* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 4.2.3-alt1
- 4.2.3-1-g8f1480e7

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 4.2.1-alt1
- 4.2.1
- fix lightdm-settings call

* Tue Jul 09 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt4
- added dconf to requires
- data: added python3-module-{PAM,xapps-overrides} dependencies (ALT #36995),

* Thu Jul 04 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt3
- spec: dropped a batch of manual python3/typelib dependencies,
  used rpm-build-{python3,gir} to generate automatic ones.
  removed obsolete gconf and telepathy stuff.
  updated other (build)dependencies.

* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt2
- add python3-module-tinycss to requires

* Mon Jul 1 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0-3-g4d1da807

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 4.0.9-alt6
- 4.0.9-129-g8cff53c1

* Mon Jun 17 2019 Michael Shigorin <mike@altlinux.org> 4.0.9-alt5
- dropped BR: eds, libfolks (unneeded)
- explicitly disabled gtk_doc knob
- spec cleanup

* Tue Apr 30 2019 Vladimir Didenko <cow@altlinux.org> 4.0.9-alt4
- add python3-module-xapps-overrides to requires (closes: #36699)

* Tue Feb 12 2019 Vladimir Didenko <cow@altlinux.org> 4.0.9-alt3
- add pillow and pexpect python modules to requires (closes: #36078)

* Mon Feb 4 2019 Vladimir Didenko <cow@altlinux.org> 4.0.9-alt2
- add gettext-tools to requires

* Wed Jan 16 2019 Vladimir Didenko <cow@altlinux.org> 4.0.9-alt1
- 4.0.9-1-gc42a03a0

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 4.0.8-alt1
- 4.0.8-1-g24637679

* Tue Dec 4 2018 Vladimir Didenko <cow@altlinux.org> 4.0.3-alt1
- 4.0.3-3-gf3786e06

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.org> 4.0.2-alt1.1
- fix requires

* Wed Nov 21 2018 Vladimir Didenko <cow@altlinux.org> 4.0.2-alt1
- 4.0.2

* Thu Nov 8 2018 Vladimir Didenko <cow@altlinux.org> 3.8.9-alt2
- use libnm instead of libnm-glib

* Fri Sep 14 2018 Vladimir Didenko <cow@altlinux.org> 3.8.9-alt1
- 3.8.9

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 3.8.8-alt1
- 3.8.8-2-gb4338cb

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 3.8.6-alt1
- 3.8.6-2-g66e54f4

* Wed Jun 20 2018 Vladimir Didenko <cow@altlinux.org> 3.8.4-alt2
- fix build requires for libnm

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 3.8.4-alt1
- 3.8.4

* Mon May 7 2018 Vladimir Didenko <cow@altlinux.org> 3.8.2-alt1
- 3.8.2

* Fri May 4 2018 Vladimir Didenko <cow@altlinux.org> 3.8.1-alt1
- 3.8.1-8-g19ec2b0

* Tue Dec 26 2017 Vladimir Didenko <cow@altlinux.org> 3.6.7-alt1
- 3.6.7

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 3.6.6-alt1
- 3.6.6

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Sep 4 2017 Vladimir Didenko <cow@altlinux.org> 3.4.6-alt2
- Show lightdm-settings module in cinnamon-settings

* Thu Aug 24 2017 Vladimir Didenko <cow@altlinux.org> 3.4.6-alt1
- 3.4.6

* Fri Jul 7 2017 Vladimir Didenko <cow@altlinux.org> 3.4.4-alt1
- 3.4.4

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 3.4.3-alt1
- 3.4.3-6-g2fdfc6f

* Mon Jun 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- 3.4.1-9-ge9fcf47

* Mon May 15 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt2
- fix cinnamon-settings-users

* Fri May 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Jan 9 2017 Vladimir Didenko <cow@altlinux.org> 3.2.8-alt1
- 3.2.8

* Fri Dec 23 2016 Vladimir Didenko <cow@altlinux.org> 3.2.7-alt1
- 3.2.7

* Thu Dec 15 2016 Vladimir Didenko <cow@altlinux.org> 3.2.6-alt1
- 3.2.6

* Thu Nov 24 2016 Vladimir Didenko <cow@altlinux.org> 3.2.2-alt1
- 3.2.2

* Wed Nov 23 2016 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt2
- 3.2.1-29-gb781072

* Sun Nov 13 2016 Vladimir Didenko <cow@altlinux.org> 3.2.1-alt1
- 3.2.1-5-g43c61aa

* Mon Oct 24 2016 Vladimir Didenko <cow@altlinux.org> 3.0.7-alt3
- restore cinnamon-menu-editor (closes: #32646)

* Mon Oct 3 2016 Vladimir Didenko <cow@altlinux.org> 3.0.7-alt2
- fix build requires

* Mon Jul 18 2016 Vladimir Didenko <cow@altlinux.org> 3.0.7-alt1
- 3.0.7-1-g287dc1b

* Fri Jun 24 2016 Vladimir Didenko <cow@altlinux.org> 3.0.6-alt1
- 3.0.6

* Wed Jun 1 2016 Vladimir Didenko <cow@altlinux.org> 3.0.5-alt1
- 3.0.5
- network applet: set new wireless connections as user-owned.

* Tue May 24 2016 Vladimir Didenko <cow@altlinux.org> 3.0.4-alt1
- 3.0.4

* Fri May 20 2016 Vladimir Didenko <cow@altlinux.org> 3.0.3-alt1
- 3.0.3

* Thu May 12 2016 Vladimir Didenko <cow@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- 3.0.1

* Wed Mar 30 2016 Vladimir Didenko <cow@altlinux.org> 2.8.8-alt1
- 2.8.8

* Wed Mar 16 2016 Vladimir Didenko <cow@altlinux.org> 2.8.7-alt1
- 2.8.7

* Mon Dec 14 2015 Vladimir Didenko <cow@altlinux.org> 2.8.6-alt1
- 2.8.6-4-g7d93ce9

* Tue Nov 24 2015 Vladimir Didenko <cow@altlinux.org> 2.8.5-alt1
- 2.8.5

* Mon Nov 16 2015 Vladimir Didenko <cow@altlinux.org> 2.8.4-alt1
- 2.8.4-2-g7384c43

* Mon Nov 2 2015 Vladimir Didenko <cow@altlinux.org> 2.8.2-alt1
- 2.8.2-2-g2bce9b5

* Tue Oct 27 2015 Vladimir Didenko <cow@altlinux.org> 2.8.1-alt1
- 2.8.1

* Wed Oct 21 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.7.0-alt1
- 2.6.13-272-g6027667

* Tue Sep 8 2015 Vladimir Didenko <cow@altlinux.org> 2.6.13-alt3
- Add python-module-PAM to requirements (closes: #31262)

* Mon Jul 27 2015 Vladimir Didenko <cow@altlinux.org> 2.6.13-alt2
- Don't require Meta typelib (libmuffin-gir doesn't provide it anymore)

* Thu Jul 16 2015 Vladimir Didenko <cow@altlinux.org> 2.6.13-alt1
- 2.6.13-6-g53359f

* Wed Jul 1 2015 Vladimir Didenko <cow@altlinux.org> 2.6.12-alt1
- 2.6.12

* Tue Jun 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.9-alt1
- 2.6.9

* Mon Jun 15 2015 Vladimir Didenko <cow@altlinux.org> 2.6.8-alt1
- 2.6.8

* Thu Jun 11 2015 Vladimir Didenko <cow@altlinux.org> 2.6.7-alt3
- remove upstream hack for pidgin and thunderbird systray icons

* Fri Jun 5 2015 Vladimir Didenko <cow@altlinux.org> 2.6.7-alt2
- specify keybinder version

* Wed Jun 3 2015 Vladimir Didenko <cow@altlinux.org> 2.6.7-alt1
- 2.6.7

* Thu May 28 2015 Vladimir Didenko <cow@altlinux.org> 2.6.3-alt1
- 2.6.3

* Sun May 24 2015 Vladimir Didenko <cow@altlinux.org> 2.6.2-alt2
- Fix startup module in cinnamon-settings

* Sat May 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.2-alt1
- 2.6.2-6-g4dd9362
- switch to gstramer1.0

* Wed May 20 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri May 8 2015 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt2
- git20150508(g05ad66d)

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt1
- 2.5.0

* Wed Apr 1 2015 Vladimir Didenko <cow@altlinux.org> 2.4.7-alt1
- 2.4.7

* Mon Jan 20 2015 Vladimir Didenko <cow@altlinux.org> 2.4.6-alt1
- 2.4.6

* Fri Jan 16 2015 Vladimir Didenko <cow@altlinux.org> 2.4.5-alt2
- 2.4.5-40-ga41fa83

* Thu Nov 27 2014 Vladimir Didenko <cow@altlinux.org> 2.4.5-alt1
- 2.4.5

* Tue Nov 25 2014 Vladimir Didenko <cow@altlinux.org> 2.4.4-alt1
- 2.4.4

* Thu Nov 20 2014 Vladimir Didenko <cow@altlinux.org> 2.4.3-alt1
- 2.4.3-14-gcca2d02

* Mon Nov 10 2014 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt1
- 2.4.2

* Wed Nov 5 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0-23-gbad763d

* Tue Oct 14 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- git20141013

* Tue Oct 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.16-alt3
- theme fixes for gtk 3.14

* Tue Sep 2 2014 Vladimir Didenko <cow@altlinux.org> 2.2.16-alt2
- rebuild with new gnome

* Thu Aug 21 2014 Vladimir Didenko <cow@altlinux.org> 2.2.16-alt1
- 2.2.16

* Tue Jul 22 2014 Vladimir Didenko <cow@altlinux.org> 2.2.14-alt1
- 2.2.14

* Thu May 29 2014 Vladimir Didenko <cow@altlinux.org> 2.2.13-alt2
- use mintlocale for language selection

* Tue May 27 2014 Vladimir Didenko <cow@altlinux.org> 2.2.13-alt1
- 2.2.13-2-gcb815e4

* Wed May 21 2014 Vladimir Didenko <cow@altlinux.org> 2.2.10-alt1
- 2.2.10-1-g903c455

* Mon May 12 2014 Vladimir Didenko <cow@altlinux.org> 2.2.8-alt1
- 2.2.8-4-g172f5f8

* Mon May 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.6-alt1
- 2.2.6-1-g4e8190d

* Wed Apr 30 2014 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt2
- 2.2.3-37-g03fa8a4

* Fri Apr 18 2014 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- 2.2.3-19-g17cb76f

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1-2-gb7e9d8f

* Wed Apr 9 2014 Vladimir Didenko <cow@altlinux.org> 2.0.14-alt5
- use c-c-c region panel instead mintlocale

* Tue Apr 8 2014 Vladimir Didenko <cow@altlinux.org> 2.0.14-alt4
- fix label trancation

* Tue Apr 8 2014 Vladimir Didenko <cow@altlinux.org> 2.0.14-alt3
- git20140406

* Tue Mar 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.14-alt2
- build with gnome-3.12

* Thu Dec 5 2013 Vladimir Didenko <cow@altlinux.org> 2.0.14-alt1
- 2.0.14-2-gf297108
- fix path to cinnamon-settings-users

* Tue Nov 25 2013 Vladimir Didenko <cow@altlinux.org> 2.0.13-alt2.1
- fix build requires

* Tue Nov 25 2013 Vladimir Didenko <cow@altlinux.org> 2.0.13-alt2
- add polkit agent

* Mon Nov 25 2013 Vladimir Didenko <cow@altlinux.org> 2.0.13-alt1
- 2.0.13-4-g5d393c2

* Tue Nov 12 2013 Vladimir Didenko <cow@altlinux.org> 2.0.12-alt1
- 2.0.12

* Tue Nov 5 2013 Vladimir Didenko <cow@altlinux.org> 2.0.10-alt1
- 2.0.10

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.7-alt1
- 2.0.7

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3-1-g4e5c584

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- 2.0.2-2-g160b5fe

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.1-alt5
- rebuild for GNOME-3.10

* Mon Sep 16 2013 Vladimir Didenko <cow@altlinux.org> 1.9.1-alt4
- 1.9.1-193-g98ccb1e

* Thu Aug 29 2013 Vladimir Didenko <cow@altlinux.org> 1.9.1-alt3
- 1.9.1-181-gd7955c3

* Mon Aug 12 2013 Vladimir Didenko <cow@altlinux.org> 1.9.1-alt2
- Drop background manager patch

* Mon Aug 8 2013 Vladimir Didenko <cow@altlinux.org> 1.9.1-alt1
- 1.9.1-110-g124cc05

* Thu Aug 8 2013 Vladimir Didenko <cow@altlinux.org> 1.8.7-alt2
- provide desktop-notification-daemon

* Tue Jun 4 2013 Vladimir Didenko <cow@altlinux.org> 1.8.7-alt1
- 1.8.7
- remove gnome-shell.desktop before start

* Sat May 25 2013 Vladimir Didenko <cow@altlinux.org> 1.8.6-alt1
- 1.8.6-2-g0a892f4

* Tue May 21 2013 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- 1.8.3-12-g81cc166

* Fri May 17 2013 Vladimir Didenko <cow@altlinux.org> 1.8.2-alt1
- 1.8.2-10-ge56078e

* Mon May 6 2013 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0

* Fri Apr 26 2013 Vladimir Didenko <cow@altlinux.org> 1.7.4-alt3
- Merged patches for gnome-3.8 compat

* Tue Apr 23 2013 Vladimir Didenko <cow@altlinux.org> 1.7.4-alt2
- 1.7.4-146-ga4c48c2

* Tue Apr 23 2013 Vladimir Didenko <cow@altlinux.org> 1.7.4-alt1
- 1.7.4

* Fri Mar 22 2013 Vladimir Didenko <cow@altlinux.org> 1.7.3-alt1
- 1.7.3
- ported to gdbus

* Fri Feb 22 2013 Vladimir Didenko <cow@altlinux.org> 1.7.1-alt1
- 1.7.1-6-g315d07b
- Restored text shadow for panel applets
- Switched to cinnamon-screensaver

* Sat Dec 29 2012 Vladimir Didenko <cow@altlinux.org> 1.6.7-alt6
- Fix notification applet

* Wed Dec 19 2012 Vladimir Didenko <cow@altlinux.org> 1.6.7-alt5
- Disabled text shadow for panel applets
- Explicitly set width for panel status button

* Thu Dec 13 2012 Yuri N. Sedunov <aris@altlinux.org> 1.6.7-alt4
- rebuilt to update arepo dependencies after polkit-0.108

* Wed Nov 21 2012 Vladimir Didenko <cow@altlinux.org> 1.6.7-alt3
- switched to cinnamon-freedesktop-menu (closes: #28004)
- moved arch independent data to cinnamon-data subpackage
- added dependency to muffin

* Thu Nov 15 2012 Vladimir Didenko <cow@altlinux.org> 1.6.7-alt2
- fixed session files - changed fallback to cinnamon2d

* Thu Nov 15 2012 Vladimir Didenko <cow@altlinux.org> 1.6.7-alt1
- 1.6.7
- added desktop files to start gnome-screensaver

* Tue Nov 13 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.6.6-alt1
- 1.6.6

* Tue Nov 6 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.6.5-alt1
- 1.6.5

* Wed Oct 31 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.6.4-alt1
- 1.6.4

* Wed Oct 03 2012 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Jun 12 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt7
- used %%set_typelibdir macros

* Wed May 30 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt6
- rebuilt for Sisyphus (closes: #27381)

* Tue May 29 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.4.0-alt5
- update to 1.4-UP3
- window-attention.patch that disables annoying window popups

* Wed May 23 2012 Vladimir Didenko <vladimir.didenko@gmail.com> 1.4.0-alt4
- update to 1.4-UP1

* Thu May 10 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt3.1
- changed wmsession priority from 05 to 02 so that
  02Cinnamon comes just before 02Gnome (the rationale
  being that if this GNOME3 extension is installed it's
  likely to have been desired in the first place)

* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt3
- removed harmful gir_bluetooth.patch
- removed menu.patch, used system gnome3-applications.menu instead
- DM integration
- updated buildreqs, reqs
- and other small cleanups

* Thu Apr 12 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt2
- courtesy of Vladimir Didenko:
  + added missing dependencies for cinnamon-settings to work
  + moved session desktop file to %_x11sysconfdir/sessions/

* Wed Apr 11 2012 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- rebuilt for Sisyphus
- minor spec cleanup

* Mon Apr 09 2012 Vyacheslav Dikonov <slava@altlinux.ru> 1.4.0-slava1
- ALTLinux build

* Sat Mar 31 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.4.0-3
- rebuild for gnome 3.4.0 changes
- patch so gir can find bluetooth-applet libs

* Tue Mar 13 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.4.0-1
- update to 1.4.0

* Mon Feb 20 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.3.1-1
- update to 1.3.1
- remove static lib
- remove mozilla plugin

* Fri Feb 17 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.3.0-1
- update to 1.3.0 release

* Mon Jan 22 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.2.0-1
- update to 1.2.0 release
- add build requires muffin-devel
- add Br libgudev1-devel
- add only-show-in=GNOME to settings desktop file
- make changes for source changes, applets, settings and session added
- delete session files and use my own
- move settings from lib to usr (it had no libs)
- replace menu icon
- change description

* Wed Jan 04 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.1.3-2
- add requires gnome-session
- clean up spec file ready for review

* Mon Jan 02 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.1.3-1
- update to version 1.1.3

* Sun Jan 01 2012 Leigh Scott <leigh123linux@fedoraproject.org> - 1.1.2-2
- fix firefox launchers

* Fri Dec 30 2011 Leigh Scott <leigh123linux@fedoraproject.org> - 1.1.2-1
- first build based on gnome-shell srpm
- add session files
