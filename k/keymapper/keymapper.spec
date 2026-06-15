%define _unpackaged_files_terminate_build 1

Name: keymapper
Version: 5.6.0
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

Requires: notify-send

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
%exclude %_datadir/doc/keymapper/CHANGELOG.md
%exclude %_datadir/doc/keymapper/LICENSE
%exclude %_datadir/doc/keymapper/README.md
%exclude %_datadir/doc/keymapper/keymapper.conf

%changelog
* Mon Jun 15 2026 Nikolay Strelkov <snk@altlinux.org> 5.6.0-alt1
- New version 5.6.0.

* Sat May 02 2026 Nikolay Strelkov <snk@altlinux.org> 5.5.1-alt1
- New version 5.5.1.

* Wed Apr 22 2026 Nikolay Strelkov <snk@altlinux.org> 5.5.0-alt1
- New version 5.5.0.

* Sun Apr 05 2026 Nikolay Strelkov <snk@altlinux.org> 5.4.2-alt1
- New version 5.4.2.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 5.4.1-alt1
- New version 5.4.1.

* Wed Mar 04 2026 Nikolay Strelkov <snk@altlinux.org> 5.4.0-alt1
- New version 5.4.0.

* Sun Feb 08 2026 Nikolay Strelkov <snk@altlinux.org> 5.3.2-alt1
- New version 5.3.2.

* Fri Dec 05 2025 Nikolay Strelkov <snk@altlinux.org> 5.3.1-alt1
- New version 5.3.1.

* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 5.3.0-alt1
- New version 5.3.0.

* Sun Oct 26 2025 Nikolay Strelkov <snk@altlinux.org> 5.2.0-alt1
- New version 5.2.0.

* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 5.1.0-alt1
- New version 5.1.0.

* Fri Sep 12 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- New version 5.0.0.

* Wed Jul 23 2025 Nikolay Strelkov <snk@altlinux.org> 4.12.3-alt1
- New version 4.12.3.

* Sat Jul 12 2025 Nikolay Strelkov <snk@altlinux.org> 4.12.2-alt1
- New version 4.12.2.

* Wed May 28 2025 Nikolay Strelkov <snk@altlinux.org> 4.12.1-alt1
- New version 4.12.1.

* Sat Apr 12 2025 Nikolay Strelkov <snk@altlinux.org> 4.11.4-alt1
- New version 4.11.4.

* Mon Mar 31 2025 Nikolay Strelkov <snk@altlinux.org> 4.11.3-alt1
- New version 4.11.3.

* Sat Mar 29 2025 Nikolay Strelkov <snk@altlinux.org> 4.11.2-alt1
- New version 4.11.2.

* Thu Mar 13 2025 Nikolay Strelkov <snk@altlinux.org> 4.11.0-alt1
- Initial build for Sisyphus
