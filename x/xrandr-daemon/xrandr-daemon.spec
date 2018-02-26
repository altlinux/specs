Name: xrandr-daemon
Version: 0.1.0
Release: alt2
Summary: X session daemon that controls screen orientation listening to ContextKit and DBus events
License: GPL v2.1
Group: System/X11
Url: http://wolneykien.github.com/xrandr-daemon/
Packager: Paul Wolneykien <manowar@altlinux.ru>

Source: %name-%version.tar

BuildRequires: libX11-devel libXrandr-devel xorg-util-macros contextkit-devel
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  gcc-c++

%description
X session daemon that controls screen orientation listening to
ContextKit and DBus events.

%prep
%setup

%build
%autoreconf
%configure

%make_build MOC=moc-qt4

%install
%makeinstall_std

%files
%_bindir/*
%_sysconfdir/xdg/autostart/*.desktop

%changelog
* Fri Apr 27 2012 Paul Wolneykien <manowar@altlinux.ru> 0.1.0-alt2
- Add the *.desktop file for autostart.

* Thu Apr 26 2012 Paul Wolneykien <manowar@altlinux.ru> 0.1.0-alt1
- Initial release for ALT Linux.
