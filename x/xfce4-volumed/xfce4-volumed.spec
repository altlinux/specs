Name: xfce4-volumed
Version: 0.1.13
Release: alt1

Summary: Daemon to add additional functionality to the volume keys of the keyboard
License: %gpl3plus
Group: Graphical desktop/XFce

URL: http://xfce.org/
Source: %name-%version.tar
Packager: XFCE Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfconf-devel >= 4.8
BuildRequires: glib2-devel libkeybinder-devel libnotify4-devel gstreamer-devel gst-plugins-devel

Requires: xfce4-mixer

%description
The xfce4-volumed adds additional functionality to the volume up/down
and mute keys of the keyboard. It makes the keys work without
configuration and uses the XFCE 4 mixer's defined card and track for
choosing which track to act on.
The volume level is shown in a notification.

%prep
%setup

%build
%xfce4reconf
%configure \
	--disable-static \
	--with-libnotify \
	--enable-debug=no
%make_build

%install
%makeinstall_std
%find_lang %_name

%files -f %_name.lang
%doc AUTHORS README
%config %_sysconfdir/xdg/autostart/%name.desktop
%_bindir/%name

%changelog
* Sun Apr 17 2011 Mikhail Efremov <sem@altlinux.org> 0.1.13-alt1
- Initial build (based on Fedora spec).

