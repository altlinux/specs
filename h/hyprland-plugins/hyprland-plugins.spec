%define plugins borders-plus-plus csgo-vulkan-fix hyprbars hyprexpo hyprtrails hyprwinwrap

Name: hyprland-plugins
Version: 0.42.0
Release: alt1
License: BSD-3-Clause

Summary: Official plugins for Hyprland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprland-plugins

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires: gcc-c++

BuildRequires: hyprland-devel
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(aquamarine)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libglvnd)
BuildRequires: pkgconfig(xcb-icccm)

%description
%summary.

%package -n hyprland-plugin-borders-plus-plus
Summary: Allows you to add one or two additional borders
Group: Graphical desktop/Other

%description -n hyprland-plugin-borders-plus-plus
Allows you to add one or two additional borders to your windows.
The borders added are static.

%package -n hyprland-plugin-csgo-vulkan-fix
Summary: A way to force apps to a fake resolution
Group: Graphical desktop/Other

%description -n hyprland-plugin-csgo-vulkan-fix
Originally meant for csgo / cs2, but can work with any app, really.
A way to force apps to a fake resolution without them realizing it.
If you want to play CS2, you're locked to your native res.
With this plugin, you aren't anymore.

%package -n hyprland-plugin-hyprbars
Summary: Adds simple title bars to windows
Group: Graphical desktop/Other

%description -n hyprland-plugin-hyprbars
%summary.

%package -n hyprland-plugin-hyprexpo
Summary: Overview plugin like gnome kde or wf
Group: Graphical desktop/Other

%description -n hyprland-plugin-hyprexpo
%summary.

%package -n hyprland-plugin-hyprtrails
Summary: A neat, but useless plugin to add trails behind windows
Group: Graphical desktop/Other

%description -n hyprland-plugin-hyprtrails
%summary.

%package -n hyprland-plugin-hyprwinwrap
Summary: Clone of xwinwrap for hyprland
Group: Graphical desktop/Other

%description -n hyprland-plugin-hyprwinwrap
%summary.

%prep
%setup

%build
for i in %plugins; do
%make_build -C $i all 
done

%install
install -d %buildroot%_libdir/hyprland

for i in %plugins; do
install $i/$i.so %buildroot%_libdir/hyprland/
done

%files -n hyprland-plugin-borders-plus-plus
%_libdir/hyprland/borders-plus-plus.so

%files -n hyprland-plugin-csgo-vulkan-fix
%_libdir/hyprland/csgo-vulkan-fix.so

%files -n hyprland-plugin-hyprbars
%_libdir/hyprland/hyprbars.so

%files -n hyprland-plugin-hyprexpo
%_libdir/hyprland/hyprexpo.so

%files -n hyprland-plugin-hyprtrails
%_libdir/hyprland/hyprtrails.so

%files -n hyprland-plugin-hyprwinwrap
%_libdir/hyprland/hyprwinwrap.so

%changelog
* Thu Oct 10 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.42.0-alt1
- Initial build
