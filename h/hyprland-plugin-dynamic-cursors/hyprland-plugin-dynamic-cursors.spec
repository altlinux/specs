%define plugin dynamic-cursors

Name: hyprland-plugin-%plugin
Version: 0.42.0
Release: alt1
License: MIT

Summary: a plugin to make your hyprland cursor more realistic

Group: Graphical desktop/Other

Url: https://github.com/VirtCode/hypr-dynamic-cursors

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires: gcc-c++

BuildRequires: hyprland-devel
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(aquamarine)

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

%build
%make_build all 

%install
install -d %buildroot%_libdir/hyprland

install out/%plugin.so %buildroot%_libdir/hyprland/

%files
%_libdir/hyprland/%plugin.so

%changelog
* Mon Oct 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.42.0-alt1
- Initial build
