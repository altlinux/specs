Name: xfce4-volumed-pulse
Version: 0.2.0
Release: alt1

Summary: Daemon to add additional functionality to the volume keys of the keyboard (for pulseaudio)
License: %gpl3plus
Group: Graphical desktop/XFce

URL: http://xfce.org/
Source: %name-%version.tar
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfconf-devel >= 4.8
BuildRequires: glib2-devel libgtk+2-devel libpulseaudio-devel libkeybinder-devel libnotify4-devel

Conflicts: xfce4-volumed

%description
The %name adds additional functionality to the volume up/down
and mute keys of the keyboard. It makes the keys work without
configuration and uses the Xfce 4 mixer's defined card and track for
choosing which track to act on.
The volume level is shown in a notification.

Fork of Xfce4-Volumed to use PulseAudio.

%prep
%setup

%build
%xfce4reconf
%configure \
	--with-libnotify \
	--enable-debug=no
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%_bindir/%name

%changelog
* Mon Jan 20 2014 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Initial build.
