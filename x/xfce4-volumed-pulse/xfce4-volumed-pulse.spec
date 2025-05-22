Name: xfce4-volumed-pulse
Version: 0.3.0
Release: alt1

Summary: Daemon to add additional functionality to the volume keys of the keyboard (for pulseaudio)
License: GPLv3+
Group: Graphical desktop/XFce

URL: https://xfce.org/
Source: %name-%version.tar
Vcs: https://gitlab.xfce.org/apps/xfce4-volumed-pulse.git
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): meson rpm-macros-meson >= 1.3.1-alt1
BuildRequires(pre): rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildRequires: libxfconf-devel >= 4.18
BuildRequires: glib2-devel libgtk+3-devel libpulseaudio-devel libkeybinder3-devel libnotify-devel

Conflicts: xfce4-volumed

%define _unpackaged_files_terminate_build 1

%description
The %name adds additional functionality to the volume up/down
and mute keys of the keyboard. It makes the keys work without
configuration and uses the Xfce 4 mixer's defined card and track for
choosing which track to act on.
The volume level is shown in a notification.

Fork of Xfce4-Volumed to use PulseAudio.

%prep
%setup
%patch -p1

%build
%meson \
	-Dlibnotify=enabled

%meson_build -v

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc AUTHORS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%_bindir/%name

%changelog
* Thu May 22 2025 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1
- Switched to meson build.
- Updated to 0.3.0.

* Thu Dec 26 2024 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Wed Jul 26 2023 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Wed Nov 02 2022 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt2
- Fixed build with xfce4-dev-tools >= 4.17.1.
- Added Vcs tag.
- Don't use rpm-build-licenses.

* Tue Aug 14 2018 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Updated BR.
- Updated url.
- Updated to 0.2.3.

* Wed Sep 14 2016 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Enable debug (minimum level).
- Fix configure option.
- Updated to 0.2.2.

* Mon Jun 08 2015 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt2
- Fork before gtk/dbus init.

* Mon Jan 20 2014 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Initial build.
