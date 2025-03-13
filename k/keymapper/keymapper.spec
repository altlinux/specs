%define _unpackaged_files_terminate_build 1

Name: keymapper
Version: 4.11.0
Release: alt1

Summary: A cross-platform context-aware key remapper
License: GPL-3.0
Group: System/Configuration/Hardware
Url: https://github.com/houmain/keymapper

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(libusb-1.0)
BuildRequires: pkgconfig(libudev)

%description
A cross-platform context-aware key remapper. It allows to:
- Redefine your keyboard layout and shortcuts systemwide or per
  application.
- Manage all your keyboard shortcuts in a single configuration file.
- Change shortcuts for similar actions in different applications at once.
- Share configuration files between multiple systems (GNU/Linux, 
  Windows, MacOS).
- Specify input and output as characters instead of the keys required to
  type them.
- Bind keyboard shortcuts to launch applications.
- Control the state from external applications using keymapperctl.
- Use mouse buttons and wheel in your mappings.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG.md LICENSE README.md keymapper.conf
%_bindir/*
%_sysconfdir/xdg/autostart/%{name}.desktop
%_libexecdir/systemd/system/*.service
%dir %_datadir/gnome-shell/extensions/keymapper@houmain.github.com
%_datadir/gnome-shell/extensions/keymapper@houmain.github.com/*
%_iconsdir/hicolor/*/apps/*
%dir %_datadir/kwin/scripts/keymapper
%_datadir/kwin/scripts/keymapper/*

%changelog
* Thu Mar 13 2025 Nikolay Strelkov <snk@altlinux.org> 4.11.0-alt1
- Initial build for Sisyphus
