%define _unpackaged_files_terminate_build 1

Name: overwitch
Version: 2.2
Release: alt1

Summary: JACK client for Overbridge devices
License: GPL-3.0-only
Group: Sound
Url: https://dagargo.github.io/overwitch/
Vcs: https://github.com/dagargo/overwitch.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libusb-devel
BuildRequires: pipewire-jack-libs-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libsystemd-devel
BuildRequires: libjson-glib-devel
BuildRequires: libgtk4-devel

Requires: libtool gettext pipewire-jack

%description
Overwitch is a set of JACK (JACK Audio Connection Kit) clients for Overbridge 2
devices.
Since PipeWire is ABI compatible with JACK, Overwitch works with PipeWire too.

%package devel
Summary: Overwitch headers
Group: Development/C
Requires: %name = %EVR

%description devel
%summary.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
install -pDm 0644 udev/91-usb-elektron.rules %buildroot%_udevrulesdir/91-usb-elektron.rules
install -pDm 0644 udev/91-usb-elektron.hwdb %buildroot%_udevhwdbdir/91-usb-elektron.hwdb
install -pDm 0644 systemd/overwitch.service %buildroot%_user_unitdir/overwitch.service

%files
%doc AUTHORS ChangeLog README THANKS
%_bindir/overwitch
%_bindir/overwitch-cli
%_bindir/overwitch-play
%_bindir/overwitch-record
%_bindir/overwitch-service
%_libdir/liboverwitch.so.0
%_libdir/liboverwitch.so.0.0.0
%_user_unitdir/overwitch.service
%_udevrulesdir/91-usb-elektron.rules
%_udevhwdbdir/91-usb-elektron.hwdb
%_datadir/applications/io.github.dagargo.Overwitch.desktop
%_datadir/dbus-1/services/io.github.dagargo.OverwitchService.service
%_datadir/icons/hicolor/scalable/apps/io.github.dagargo.Overwitch-symbolic.svg
%_datadir/icons/hicolor/scalable/apps/io.github.dagargo.Overwitch.svg
%_datadir/locale/ca/LC_MESSAGES/overwitch.mo
%_datadir/locale/en/LC_MESSAGES/overwitch.mo
%_datadir/locale/es/LC_MESSAGES/overwitch.mo
%dir %_datadir/overwitch
%_datadir/overwitch/THANKS
%_datadir/overwitch/devices.json
%_datadir/overwitch/overwitch.ui

%files devel
%_includedir/overwitch.h
%_libdir/liboverwitch.so

%post
udevadm control --reload || :
udevadm trigger || :
systemd-hwdb update || :

%postun
udevadm control --reload || :
udevadm trigger || :
systemd-hwdb update || :

%changelog
* Mon May 04 2026 Nikita Stavtsev <nst@altlinux.org> 2.2-alt1
- Initial build

