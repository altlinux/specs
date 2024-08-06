Name: labwc
Version: 0.7.4
Release: alt1

Summary: A Wayland window-stacking compositor
License: GPL-2.0
Group: Graphical desktop/Other
Url: https://github.com/labwc/labwc

VCS: https://github.com/labwc/labwc.git
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
BuildRequires: pkgconfig(wlroots) >= 0.17.0
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(libdrm)

%description
%summary

%prep
%setup

%build
%meson \
    -Dxwayland=enabled
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%doc NEWS.md
%_bindir/%name
%_datadir/wayland-sessions/%name.desktop
%_docdir/%name/
%_mandir/man1/*.1*
%_mandir/man5/*.5*
%_iconsdir/hicolor/scalable/apps/%{name}*.svg

%changelog
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
