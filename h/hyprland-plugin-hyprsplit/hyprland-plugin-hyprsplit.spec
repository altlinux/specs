%define plugin hyprsplit

Name: hyprland-plugin-%plugin
Version: 0.42.0
Release: alt1
License: BSD-3-Clause

Summary: Hyprland plugin for separate sets of workspaces on each monitor

Group: Graphical desktop/Other

Url: https://github.com/shezdy/hyprsplit

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires: gcc-c++

BuildRequires: hyprland-devel
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(aquamarine)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libinput)
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
