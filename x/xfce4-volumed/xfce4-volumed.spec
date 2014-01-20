Name: xfce4-volumed
Version: 0.1.13
Release: alt3

Summary: Daemon to add additional functionality to the volume keys of the keyboard
License: %gpl3plus
Group: Graphical desktop/XFce

URL: http://xfce.org/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Xfce Team <xfce@packages.altlinux.org>

BuildRequires(pre): rpm-build-licenses

BuildPreReq: rpm-build-xfce4 >= 0.1.0 xfce4-dev-tools
BuildPreReq: libxfconf-devel >= 4.8
BuildRequires: glib2-devel libkeybinder-devel libnotify4-devel gstreamer-devel gst-plugins-devel

Requires: gst-plugins-good

Conflicts: xfce4-volumed-pulse

%description
The xfce4-volumed adds additional functionality to the volume up/down
and mute keys of the keyboard. It makes the keys work without
configuration and uses the Xfce 4 mixer's defined card and track for
choosing which track to act on.
The volume level is shown in a notification.

%prep
%setup
%patch -p1

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
* Mon Jan 20 2014 Mikhail Efremov <sem@altlinux.org> 0.1.13-alt3
- Add conflict with xfce4-volumed-pulse.

* Mon Jan 20 2014 Mikhail Efremov <sem@altlinux.org> 0.1.13-alt2
- Add missing cflags/libs/includes for gtk.
- Add gst-plugins-good requires.
- Drop xfce4-mixer from requires.
- Fix Xfce name (XFCE -> Xfce).
- Spec cleanup.
- Drop --disable-static.

* Sun Apr 17 2011 Mikhail Efremov <sem@altlinux.org> 0.1.13-alt1
- Initial build (based on Fedora spec).

