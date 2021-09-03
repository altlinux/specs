%define git aac8742

%def_enable aptx
%def_enable aac
%def_enable ldac
%def_enable mpg123
%def_enable mp3lame
%def_disable debug
%def_disable test

Name: bluez-alsa
Version: 3.1.0
Release: alt2.g%{git}
Epoch: 5
Summary: BlueZ ALSA backend for Linux
License: MIT
Group: Sound
URL: https://github.com/Arkq/bluez-alsa

Packager: L.A. Kostis <lakostis@altlinux.ru>

Source: %name-%version.tar

Provides: alsa-plugins-bluealsa = %EVR, bluealsa = %EVR

BuildRequires: systemd-devel libdbus-glib-devel, libbluez-devel, libalsa-devel, libsbc-devel libgio-devel python3-module-docutils
%{?_enable_aptx:BuildRequires: libfreeaptx-devel}
%{?_enable_aac:BuildRequires: libfdk-aac-devel}
%{?_enable_ldac:BuildRequires: libldac-devel}
%{?_enable_mpg123:BuildRequires: libmpg123-devel}
%{?_enable_mp3lame:BuildRequires: liblame-devel}
%{?_enable_test:BuildRequires: libcheck-devel}

%description
This project is a rebirth of a direct integration between Bluez and ALSA.

With this application (later named as BlueALSA), one can achieve the same goal
as with PulseAudio, but with less dependencies and more bare-metal-like.
BlueALSA registers all known Bluetooth audio profiles in Bluez, so in theory
every Bluetooth device (with audio capabilities) can be connected. In order to
access the audio stream, one has to connect to the ALSA PCM device called
bluealsa. The device is based on the ALSA software PCM plugin.

%prep
%setup -q

%build
%autoreconf
%configure \
        %{subst_enable aptx} \
	%{subst_enable aac} \
	%{subst_enable ldac} \
	%{subst_enable mpg123} \
	%{subst_enable mp3lame} \
	%{subst_enable debug} \
	%{subst_enable test} \
	%{?_enable_aptx:--with-libopenaptx } \
	--with-alsaconfdir=%_datadir/alsa/alsa.conf.d \
	--enable-systemd \
	--enable-upower \
	--enable-ofono \
	--enable-a2dpconf \
	--disable-static \
	--enable-manpages \
	--enable-msbc

%install
%make DESTDIR=%buildroot install

%if_enabled test
%check
%make check
%endif

%files
%doc README.md LICENSE AUTHORS
%_bindir/*
%_libdir/alsa-lib/*.so
%_datadir/alsa/alsa.conf.d/*.conf
%_sysconfdir/dbus-1/system.d/*.conf
%_unitdir/*.service
%_man1dir/*
%_man8dir/*

%changelog
* Fri Sep 03 2021 L.A. Kostis <lakostis@altlinux.ru> 5:3.1.0-alt2.gaac8742
- GIT aac8742.
- Switch to libfreeaptx.
- Disable debug flags.
- Disable static libraries.
- Enable manpages.

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 5:3.1.0-alt1.g06dc8dd
- GIT 06dc8dd.
- use libopenaptx.

* Thu Jan 07 2021 L.A. Kostis <lakostis@altlinux.ru> 5:3.0.0-alt2.g76929fd
- GIT 76929fd.
- Update buildrequires.

* Thu Dec 10 2020 L.A. Kostis <lakostis@altlinux.ru> 5:3.0.0-alt1.gbb39d41
- GIT bb39d41.

* Sat Mar 21 2020 L.A. Kostis <lakostis@altlinux.ru> 5:2.1.0-alt1
- 2.1.0.
- Enable upower (to expose battery change percentage).

* Wed Sep 18 2019 L.A. Kostis <lakostis@altlinux.ru> 5:1.4.0-alt0.5
- Added DBUS/systemd support.

* Tue Sep 17 2019 L.A. Kostis <lakostis@altlinux.ru> 5:1.4.0-alt0.4
- Added serial to fix collision with old bluez-4.x package.

* Tue Sep 17 2019 L.A. Kostis <lakostis@altlinux.ru> 1.4.0-alt0.3
- Added tests (can be only passed locally).

* Mon Sep 16 2019 L.A. Kostis <lakostis@altlinux.ru> 1.4.0-alt0.2
- Added debug switch.

* Mon Sep 16 2019 L.A. Kostis <lakostis@altlinux.ru> 1.4.0-alt0.1
- Initial build for ALTLinux.
