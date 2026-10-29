%define plugins borders-plus-plus csgo-vulkan-fix hyprbars hyprfocus

Name: hyprland-plugins
Version: 0.56.1
Release: alt1
License: BSD-3-Clause

Summary: Official plugins for Hyprland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprland-plugins

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires: clang-devel libstdc++-devel

BuildRequires: hyprland-devel
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(aquamarine)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(pangocairo)

BuildRequires: glslang-devel

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

%package -n hyprland-plugin-hyprfocus
Summary: Flashfocus for hyprland
Group: Graphical desktop/Other

%description -n hyprland-plugin-hyprfocus
%summary.

%prep
%setup

%build
for i in %plugins; do
%make_build CXX=clang++ -C $i all 
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

%files -n hyprland-plugin-hyprfocus
%_libdir/hyprland/hyprfocus.so

%changelog
* Tue Jul 28 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.56.1-alt1
- new version 0.56.1
- drop old plugins

* Fri Mar 20 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.54.2-alt1
- new version 0.54.2
- drop plugin: hyprscrolling

* Sun Jan 25 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.53.3-alt1
- new version 0.53.3 (with rpmrb script)

* Fri Dec 05 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.52.2-alt1
- new version 0.52.2 (with rpmrb script)

* Sat Nov 15 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.52.1-alt1
- new version 0.52.1 (with rpmrb script)

* Wed Oct 22 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.51.1-alt1
- new version 0.51.1 (with rpmrb script)
- build with clang
- new plugin: hyprfocus
- new plugin: hyprscrolling

* Sat May 10 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.49.0-alt1
- new version 0.49.0 (with rpmrb script)

* Tue Mar 25 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.48.0-alt1
- new version 0.48.0 (with rpmrb script)

* Fri Feb 07 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.47.2-alt1
- new version 0.47.2 (with rpmrb script)
- new plugin: xtra-dispatchers

* Mon Dec 23 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.46.2-alt1
- new version 0.46.2 (with rpmrb script)

* Thu Nov 21 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.45.2-alt1
- new version 0.45.2 (with rpmrb script)

* Mon Nov 11 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.45.0-alt1
- new version 0.45.0 (with rpmrb script)

* Thu Oct 31 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.44.0-alt1
- new version 0.44.0 (with rpmrb script)

* Thu Oct 10 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.42.0-alt1
- Initial build
