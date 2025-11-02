%define plugin dynamic-cursors

Name: hyprland-plugin-%plugin
Version: 0.51.1
Release: alt1
License: MIT

Summary: a plugin to make your hyprland cursor more realistic

Group: Graphical desktop/Other

Url: https://github.com/VirtCode/hypr-dynamic-cursors

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires: clang-devel libstdc++-devel

BuildRequires: hyprland-devel
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(aquamarine)
BuildRequires: pkgconfig(hyprcursor)

BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libglvnd)
BuildRequires: pkgconfig(gbm)

%description
This plugin makes your cursor more realistic by simulating how
it would behave if it was an actual object being dragged across
your screen. This means that your cursor can change
based on how it is used, e.g. tilt in the direction
you are moving or straight out rotate towards it.

%prep
%setup
subst "s|--no-gnu-unique||" Makefile

%build
%make_build CXX=clang++ all 

%install
install -d %buildroot%_libdir/hyprland

install out/%plugin.so %buildroot%_libdir/hyprland/

%files
%_libdir/hyprland/%plugin.so

%changelog
* Wed Oct 22 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.51.1-alt1
- new version 0.51.1 (with rpmrb script)

* Mon May 12 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.49.0-alt1
- new version 0.49.0 (with rpmrb script)

* Sat Mar 29 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.48.1-alt1
- new version 0.48.1 (with rpmrb script)

* Wed Mar 26 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.48.0-alt1
- new version 0.48.0 (with rpmrb script)

* Thu Feb 13 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.47.2-alt1
- new version 0.47.2 (with rpmrb script)

* Sat Dec 28 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.46.2-alt1
- new version 0.46.2 (with rpmrb script)

* Thu Nov 21 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.45.2-alt1
- new version 0.45.2 (with rpmrb script)

* Thu Nov 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.45.0-alt1
- new version 0.45.0 (with rpmrb script)

* Thu Oct 31 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.44.1-alt1
- new version 0.44.1 (with rpmrb script)

* Mon Oct 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.42.0-alt1
- Initial build
