%define ver_major 6.0
%define _libexecdirname libexec
%define _libexecdir %_prefix/%_libexecdirname
%define _name cinnamon

Name: %{_name}-session
Version: %ver_major.1
Release: alt2

License: GPLv2+
Summary: The cinnamon session programs for the Cinnamon GUI desktop environment
Group: Graphical desktop/GNOME
URL: https://github.com/linuxmint/cinnamon-session

# Source-url: https://github.com/linuxmint/cinnamon-session/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Source1: %{_name}.session
Source2: %{_name}2d.session
Source3: %{_name}-wayland.session
Source4: start%{_name}-common
Source5: start%{_name}
Source6: start%{_name}2d
Source7: start%{_name}-wayland
Source8: %{_name}.desktop
Source9: %{_name}2d.desktop
Source10: %{_name}-wayland.desktop
Patch: %name-%version-%release.patch

# From configure.in
%define glib_ver 2.33.4
%define gtk_ver 3.0.0
%define polkit_ver 0.91
%define upower_ver 0.9

%{?_enable_wmsession:Requires(pre): xinitrc}
Requires: dconf libcanberra-gnome libcanberra-gtk3
Requires: altlinux-freedesktop-menu-cinnamon
Requires: gstreamer1.0 dbus-tools-gui
Requires: gnome-filesystem
Requires: cinnamon-settings-daemon
Requires: nemo
Requires: upower polkit-gnome gcr
Requires: %name-translations
Requires: cinnamon-screensaver

%add_python3_req_skip config

BuildRequires(pre): rpm-macros-python3
BuildPreReq: rpm-build-python3
# From configure.in
BuildPreReq: meson
BuildPreReq: intltool >= 0.35.0
BuildPreReq: libgio-devel glib2-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libupower-devel >= %upower_ver
BuildRequires: libpango-devel librsvg-devel libjson-glib-devel
BuildRequires: libX11-devel libXau-devel libXrandr-devel libXrender-devel libXt-devel
BuildRequires: libSM-devel libXext-devel libXtst-devel libXi-devel libXcomposite-devel libGL-devel
BuildRequires: xorg-xtrans-devel
BuildRequires: libcanberra-devel
BuildRequires: libcinnamon-desktop-devel
BuildRequires: xmlto
BuildRequires: libsystemd-devel libpolkit-devel
BuildRequires: libxapps-devel
BuildRequires: libGConf-devel

%description
Cinnamon is a Linux desktop which provides advanced innovative features
and a traditional user experience. The desktop layout is similar to Gnome 2.
The underlying technology is forked from Gnome Shell. The emphasis is put on
making users feel at home and providing them with an easy to use and comfortable
desktop experience.

This package provides the Cinnamon session manager.

%package wayland
Summary: Wayland session for Cinnamon
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires(pre): %{_name} >= %ver_major

%description wayland
Wayland session for Cinnamon.

%prep
%setup -q
%patch0 -p1

%build
%meson --libexecdir=%_libexecdirname
%meson_build

%install
%meson_install

install -pD -m655 %SOURCE1 %buildroot%_datadir/%name/sessions/%{_name}.session
install -pD -m655 %SOURCE2 %buildroot%_datadir/%name/sessions/%{_name}2d.session
install -pD -m655 %SOURCE3 %buildroot%_datadir/%name/sessions/%{_name}-wayland.session
install -pD -m755 %SOURCE4 %buildroot%_datadir/%name/start%{_name}-common
install -pD -m755 %SOURCE5 %buildroot%_bindir/start%{_name}
install -pD -m755 %SOURCE6 %buildroot%_bindir/start%{_name}2d
install -pD -m755 %SOURCE7 %buildroot%_bindir/start%{_name}-wayland

mkdir -p %buildroot%_datadir/xsessions
install -pD -m655 %SOURCE8 %buildroot%_datadir/xsessions
install -pD -m655 %SOURCE9 %buildroot%_datadir/xsessions

mkdir -p %buildroot%_datadir/wayland-sessions
install -pD -m655 %SOURCE10 %buildroot%_datadir/wayland-sessions

rm -f %buildroot%_docdir/%name/dbus/cinnamon-session.html

%find_lang --with-gnome --output=%name.lang %name-3.0

%files -f %name.lang
%_bindir/*
%_libexecdir/cinnamon-session-check-accelerated
%_libexecdir/cinnamon-session-check-accelerated-helper
%dir %_datadir/%name
%_datadir/%name/*.glade
%_datadir/%name/hardware-compatibility
%_datadir/%name/start%{_name}-common
%dir %_datadir/%name/sessions
%_datadir/%name/sessions/%{_name}.session
%_datadir/%name/sessions/%{_name}2d.session
%_iconsdir/hicolor/*/apps/cinnamon-session-properties.*
%config %_datadir/glib-2.0/schemas/org.cinnamon.SessionManager.gschema.xml
%_mandir/man?/*
%_datadir/%name/cinnamon-session-quit.py
%_datadir/%name/config.py
%_datadir/xsessions/*.desktop
%doc AUTHORS NEWS README

%files wayland
%_datadir/cinnamon-session/sessions/%{_name}-wayland.session
%_datadir/wayland-sessions/%{_name}-wayland.desktop

%changelog
* Sun Dec 03 2023 Anton Midyukov <antohami@altlinux.org> 6.0.1-alt2
- pack cinnamon-session-quit.py

* Sat Dec 02 2023 Anton Midyukov <antohami@altlinux.org> 6.0.1-alt1
- 6.0.1
- add experimental wayland session
- cleanup spec

* Thu Jun 15 2023 Vladimir Didenko <cow@altlinux.org> 5.8.1-alt1
- 5.8.1

* Thu Jun 8 2023 Vladimir Didenko <cow@altlinux.org> 5.8.0-alt1
- 5.8.0

* Fri Nov 18 2022 Vladimir Didenko <cow@altlinux.org> 5.6.0-alt1
- 5.6.0

* Fri Jun 10 2022 Vladimir Didenko <cow@altlinux.org> 5.4.0-alt1
- 5.4.0

* Thu Dec 16 2021 Vladimir Didenko <cow@altlinux.org> 5.2.0-alt2
- Fix build with the new version of meson

* Mon Nov 29 2021 Vladimir Didenko <cow@altlinux.org> 5.2.0-alt1
- 5.2.0

* Mon Oct 18 2021 Vladimir Didenko <cow@altlinux.org> 5.0.1-alt2
- Add flatpak directories to XDG_DATA_DIRS (closes: #41135)

* Mon Aug 2 2021 Vladimir Didenko <cow@altlinux.org> 5.0.1-alt1
- 5.0.1

* Tue Jun 1 2021 Vladimir Didenko <cow@altlinux.org> 5.0.0-alt2
- use new cinnamon screensaver name for required components

* Fri May 28 2021 Vladimir Didenko <cow@altlinux.org> 5.0.0-alt1
- 5.0.0

* Fri Nov 27 2020 Vladimir Didenko <cow@altlinux.org> 4.8.0-alt1
- 4.8.0

* Thu Sep 3 2020 Vladimir Didenko <cow@altlinux.org> 4.6.2-alt1
- 4.6.2

* Wed May 27 2020 Vladimir Didenko <cow@altlinux.org> 4.6.1-alt1
- 4.6.1

* Thu May 14 2020 Vladimir Didenko <cow@altlinux.org> 4.6.0-alt1
- 4.6.0

* Tue Feb 18 2020 Vladimir Didenko <cow@altlinux.org> 4.4.1-alt1
- 4.4.1

* Wed Nov 20 2019 Vladimir Didenko <cow@altlinux.org> 4.4.0-alt1
- 4.4.0

* Fri Jul 19 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt2
- spec: made wmsession support optional (disabled by default),
  removed gconf stuff,
  updated (build)dependencies

* Mon Jul 8 2019 Vladimir Didenko <cow@altlinux.org> 4.2.1-alt1
- 4.2.1

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 4.2.0-alt1
- 4.2.0

* Wed Oct 31 2018 Vladimir Didenko <cow@altlinux.org> 4.0.0-alt1
- 4.0.0

* Fri May 4 2018 Vladimir Didenko <cow@altlinux.org> 3.8.1-alt1
- 3.8.1-2-g995980f

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 3.6.0-alt1
- 3.6.0

* Thu Aug 24 2017 Vladimir Didenko <cow@altlinux.org> 3.4.2-alt1
- 3.4.2

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 3.4.1-alt1
- 3.4.1

* Fri May 5 2017 Vladimir Didenko <cow@altlinux.org> 3.4.0-alt1
- 3.4.0-2-g33f6def

* Wed Apr 26 2017 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt4
- add g-s-d stuff to autostart blacklist

* Tue Apr 11 2017 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt3
- add cinnamon-screensaver to requires (closes: #33332)

* Tue Feb 7 2017 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt2
- remove ConsoleKit from dependencies

* Sat Nov 12 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- 3.2.0

* Thu Jul 7 2016 Vladimir Didenko <cow@altlinux.org> 3.0.1-alt1
- 3.0.1

* Thu Jun 2 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt2
- Set desktop name to X-Cinnamon

* Tue Apr 26 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Mar 16 2016 Vladimir Didenko <cow@altlinux.org> 2.8.3-alt1
- 2.8.3

* Mon Nov 16 2015 Vladimir Didenko <cow@altlinux.org> 2.8.2-alt1
- 2.8.2

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue Jun 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.3-alt1
- 2.6.3

* Tue Jun 2 2015 Vladimir Didenko <cow@altlinux.org> 2.6.2-alt1
- 2.6.2

* Thu May 28 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt3
- add desktop files to xsessions directory

* Sat May 23 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt2
- git20150523
- don't require gstreamer

* Tue May 19 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Fri May 8 2015 Vladimir Didenko <cow@altlinux.org> 2.5.1-alt2
- git20150506

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.1-alt1
- 2.5.1

* Mon Mar 30 2015 Vladimir Didenko <cow@altlinux.org> 2.4.3-alt1
- 2.4.3

* Wed Feb 18 2015 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt2
- explicitly set clutter backend

* Thu Nov 27 2014 Vladimir Didenko <cow@altlinux.org> 2.4.2-alt1
- 2.4.2

* Mon Nov 10 2014 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Tue Sep 2 2014 Vladimir Didenko <cow@altlinux.org> 2.3.0-alt1
- git20141006

* Tue Sep 2 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt2
- rebuild with new gnome

* Tue Jul 22 2014 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2

* Mon May 12 2014 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1

* Mon May 5 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt2
- add dependence on translations package

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0-1-g6a4aeb2

* Mon Apr 7 2014 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt4
- git20140402

* Tue Mar 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt3
- build with gnome-3.12

* Tue Nov 26 2013 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt2
- add cinnamon polkit agent to required components

* Mon Nov 25 2013 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt1
- 2.0.6

* Tue Nov 5 2013 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue Oct 29 2013 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Oct 21 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt2
- add nemo and fallback-mount-helper as required components

* Thu Oct 10 2013 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Sep 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt3
- rebuild for GNOME-3.10

* Thu Sep 5 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt2
- load cinnamon-settings-daemon2d.desktop in 2d session

* Thu Aug 29 2013 Vladimir Didenko <cow@altlinux.org> 1.9.0-alt1
- git20130824
- bump version

* Fri Aug 2 2013 Vladimir Didenko <cow@altlinux.org> 0.0.1-alt1
- Initial build - git20130723
