%define git %nil

%def_enable systemd
%def_enable man
%def_disable consolekit
%def_disable elogind


Name: gnome-firmware
Version: 43.1
Release: alt1
Summary: Install firmware on devices
Group: System/Configuration/Hardware
License: GPLv2
Url: https://gitlab.gnome.org/World/gnome-firmware
Source0: %name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): meson
BuildRequires: libgtk4-devel libgio-devel fwupd-devel libxmlb-devel libadwaita-devel
%{?_enable_systemd:BuildRequires: libsystemd-devel}
%{?_enable_man:BuildRequires: help2man}
%{?_enable_consolekit:BuildRequires: libConsoleKit-devel}
%{?_enable_elogind:BuildRequires: libelogind-devel}

%description
GNOME Firmware application can:

- Upgrade, Downgrade, & Reinstall firmware on devices supported by fwupd.
- Unlock locked fwupd devices
- Verify firmware on supported devices
- Display all releases for a fwupd device

%prep
%setup
%patch -p1

%build
export LIB=%_lib
%meson \
	%{?_disable_systemd:-Dsystemd=false} \
	%{?_disable_man:-Dman=false} \
	%{?_disable_consolekit:-Dconsolekit=false} \
	%{?_disable_elogind:-Delogind=false}
%nil
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%doc README* COPYING
%_bindir/*
%_datadir/metainfo/org.gnome.Firmware.metainfo.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/symbolic/apps/*.svg
%_man1dir/*

%changelog
* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 43.1-alt1
- 43.1.

* Wed Sep 28 2022 L.A. Kostis <lakostis@altlinux.ru> 43.0-alt1
- 43.0.
- BR: switch to gtk4.

* Fri May 28 2021 L.A. Kostis <lakostis@altlinux.ru> 3.36.0-alt0.1.gf528107
- Initial build for ALTLinux.
