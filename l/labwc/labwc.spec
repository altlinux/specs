# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: labwc
Version: 0.20.1
Release: alt1

Summary: A Wayland window-stacking compositor
License: GPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/labwc/labwc

# Source-url: https://github.com/labwc/labwc/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libinput) >= 1.14
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(scdoc)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-server) >= 0.19.0
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wlroots-0.20)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libsfdo-basedir)
BuildRequires: pkgconfig(xwayland)

Requires: labwc-base = %EVR

%description
%summary.

%package base
Summary: A Wayland window-stacking compositor (without session)
Group: Engineering
Conflicts: labwc < 0.8.1

%description base
%summary.

%prep
%setup

%build
%meson \
    -Dxwayland=enabled
%meson_build

%install
%meson_install
%find_lang %name

# remove unsupported locale
rm -rv %buildroot%_datadir/locale/sr_Latn

%files base -f %name.lang
%doc NEWS.md
%_bindir/%name
%_bindir/lab-sensible-terminal
%_bindir/labnag
%_datadir/xdg-desktop-portal/labwc-portals.conf
%_docdir/%name/
%_mandir/man1/*.1*
%_mandir/man5/*.5*
%_iconsdir/hicolor/scalable/apps/%{name}*.svg

%files
%_datadir/wayland-sessions/%name.desktop

%changelog
* Thu Jul 02 2026 Anton Midyukov <antohami@altlinux.org> 0.20.1-alt1
- New version 0.20.1.

* Sat Jun 20 2026 Anton Midyukov <antohami@altlinux.org> 0.9.8-alt1
- New version 0.9.8.

* Sat Apr 18 2026 Anton Midyukov <antohami@altlinux.org> 0.9.7-alt1
- New version 0.9.7.

* Sun Mar 15 2026 Anton Midyukov <antohami@altlinux.org> 0.9.6-alt1
- New version 0.9.6.

* Thu Mar 05 2026 Anton Midyukov <antohami@altlinux.org> 0.9.5-alt1
- New version 0.9.5.

* Fri Feb 27 2026 Anton Midyukov <antohami@altlinux.org> 0.9.4-alt1
- New version 0.9.4.

* Sat Dec 20 2025 Anton Midyukov <antohami@altlinux.org> 0.9.3-alt1
- New version 0.9.3.

* Fri Oct 10 2025 Anton Midyukov <antohami@altlinux.org> 0.9.2-alt1
- new version (0.9.2) with rpmgs script

* Sat Aug 02 2025 Anton Midyukov <antohami@altlinux.org> 0.9.1-alt1
- new version (0.9.1) with rpmgs script

* Fri Jul 18 2025 Anton Midyukov <antohami@altlinux.org> 0.9.0-alt1
- new version (0.9.0) with rpmgs script

* Sat May 03 2025 Anton Midyukov <antohami@altlinux.org> 0.8.4-alt1
- new version (0.8.4) with rpmgs script

* Sun Apr 20 2025 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt1
- new version (0.8.3) with rpmgs script

* Wed Jan 22 2025 Anton Midyukov <antohami@altlinux.org> 0.8.2-alt1
- new version (0.8.2) with rpmgs script

* Thu Nov 14 2024 Anton Midyukov <antohami@altlinux.org> 0.8.1-alt1
- new version (0.8.1) with rpmgs script
- separate base subpackage without %%_datadir/wayland-sessions/%%name.desktop
- unpackaged files terminate build

* Sat Aug 17 2024 Roman Alifanov <ximper@altlinux.org> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)
- move to tarball

* Tue Aug 06 2024 Roman Alifanov <ximper@altlinux.org> 0.7.4-alt1
- new version 0.7.4 (with rpmrb script)

* Sat May 25 2024 Roman Alifanov <ximper@altlinux.org> 0.7.2-alt1
- new version 0.7.2 (with rpmrb script)

* Mon Dec 25 2023 Roman Alifanov <ximper@altlinux.org> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Sat Dec 16 2023 Roman Alifanov <ximper@altlinux.org> 0.6.6-alt1
- new version 0.6.6 (with rpmrb script)

* Mon Oct 02 2023 Roman Alifanov <ximper@altlinux.org> 0.6.5-alt1
- new version 0.6.5 (with rpmrb script)

* Sat May 20 2023 Roman Alifanov <ximper@altlinux.org> 0.6.3-alt1
- new version 0.6.3 (ALT bug 46139)

* Wed Apr 26 2023 Roman Alifanov <ximper@altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus
