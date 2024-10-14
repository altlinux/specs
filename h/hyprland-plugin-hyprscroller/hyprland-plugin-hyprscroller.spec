%define plugin hyprscroller

Name: hyprland-plugin-%plugin
Version: 0.42.0
Release: alt1
License: MIT

Summary: Hyprland layout plugin providing a scrolling layout like PaperWM

Group: Graphical desktop/Other

Url: https://github.com/dawsers/hyprscroller

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires: gcc-c++ cmake

BuildRequires: hyprland-devel
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(aquamarine)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libglvnd)

%description
%summary.

%prep
%setup

%build
%make_build all 

%install
install -d %buildroot%_libdir/hyprland

install %plugin.so %buildroot%_libdir/hyprland/

%files
%_libdir/hyprland/%plugin.so

%changelog
* Mon Oct 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.42.0-alt1
- Initial build
