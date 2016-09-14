Name: xfce4-volumed-pulse
Version: 0.2.2
Release: alt1

Summary: Daemon to add additional functionality to the volume keys of the keyboard (for pulseaudio)
License: %gpl3plus
Group: Graphical desktop/XFce

URL: http://xfce.org/
# git://git.xfce.org/apps/xfce4-volumed-pulse
Source: %name-%version.tar
#Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfconf-devel >= 4.8
BuildRequires: glib2-devel libgtk+2-devel libpulseaudio-devel libkeybinder-devel libnotify4-devel

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
#patch -p1

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
* Wed Sep 14 2016 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Enable debug (minimum level).
- Fix configure option.
- Updated to 0.2.2.

* Mon Jun 08 2015 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt2
- Fork before gtk/dbus init.

* Mon Jan 20 2014 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Initial build.
