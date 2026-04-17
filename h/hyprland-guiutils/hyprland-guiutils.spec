Name: hyprland-guiutils
Version: 0.2.1
Release: alt1
License: BSD-3-Clause

Summary: Hyprland GUI utilities

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprland-guiutils
Vcs: https://github.com/hyprwm/hyprland-guiutils.git

ExcludeArch: i586
Source: %name-%version.tar

Obsoletes: hyprland-qtutils
Provides: hyprland-qtutils = %EVR

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: clang libstdc++-devel

BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(aquamarine)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(hyprtoolkit)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(xkbcommon)

%description
%summary.

%prep
%setup

%build
%cmake -DCMAKE_CXX_COMPILER=clang++
%cmake_build 

%install
%cmake_install

%files
%_bindir/hyprland-dialog
%_bindir/hyprland-update-screen
%_bindir/hyprland-donate-screen
%_bindir/hyprland-run
%_bindir/hyprland-welcome

%changelog
* Sun Jan 25 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.2.1-alt1
- new version 0.2.1 (with rpmrb script)

* Fri Dec 05 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- new version 0.2.0 (with rpmrb script)

* Sat Nov 08 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build
