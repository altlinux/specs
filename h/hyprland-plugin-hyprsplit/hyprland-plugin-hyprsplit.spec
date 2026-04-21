%define _unpackaged_files_terminate_build 1
%define plugin hyprsplit

Name: hyprland-plugin-%plugin
Version: 0.54.3
Release: alt1

Summary: Hyprland plugin for separate sets of workspaces on each monitor
License: BSD-3-Clause
Group: Graphical desktop/Other
Url: https://github.com/shezdy/hyprsplit
VCS: https://github.com/shezdy/hyprsplit.git

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires: gcc-c++

BuildRequires: hyprland-devel
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprgraphics)
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
%autopatch -p1

%build
%make_build all

%install
install -d %buildroot%_libdir/hyprland
install %plugin.so %buildroot%_libdir/hyprland/

%files
%doc README.md LICENSE
%_libdir/hyprland/%plugin.so

%changelog
* Tue Apr 21 2026 Egor Ignatov <egori@altlinux.org> 0.54.3-alt1
- New version 0.54.3.

* Tue May 13 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.49.0-alt1
- new version 0.49.0 (with rpmrb script)

* Tue Apr 01 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.48.1-alt1
- new version 0.48.1 (with rpmrb script)

* Tue Mar 25 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.48.0-alt1
- new version 0.48.0 (with rpmrb script)

* Fri Feb 07 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.47.2-alt1
- new version 0.47.2 (with rpmrb script)

* Fri Jan 10 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.46.2-alt1
- new version 0.46.2 (with rpmrb script)
- switch build to commit-based

* Thu Nov 21 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.45.2-alt1
- new version 0.45.2 (with rpmrb script)

* Mon Nov 11 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.45.0-alt1
- new version 0.45.0 (with rpmrb script)

* Thu Oct 31 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.44.1-alt1
- new version 0.44.1 (with rpmrb script)

* Mon Oct 14 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.42.0-alt1
- Initial build
