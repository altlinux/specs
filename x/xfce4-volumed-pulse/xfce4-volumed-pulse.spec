Name: xfce4-volumed-pulse
Version: 0.2.3
Release: alt2

Summary: Daemon to add additional functionality to the volume keys of the keyboard (for pulseaudio)
License: GPLv3+
Group: Graphical desktop/XFce

URL: https://xfce.org/
Source: %name-%version.tar
Vcs: https://gitlab.xfce.org/apps/xfce4-volumed-pulse.git
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfconf-devel >= 4.8
BuildRequires: glib2-devel libgtk+3-devel libpulseaudio-devel libkeybinder3-devel libnotify4-devel

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
%xfce4reconf
%configure \
	--enable-libnotify \
	--enable-debug=minimum
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%_bindir/%name

%changelog
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
