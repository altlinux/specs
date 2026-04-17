Name: hyprlauncher
Version: 0.1.5
Release: alt1
License: BSD-3-Clause

Summary: A multipurpose and versatile launcher/picker for Hyprland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprlauncher
Vcs: https://github.com/hyprwm/hyprlauncher.git

ExcludeArch: %ix86
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: clang libstdc++-devel

BuildRequires: pkgconfig(hyprtoolkit)
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(aquamarine)
BuildRequires: pkgconfig(hyprwire)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(libqalculate)
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
%_bindir/%name

%changelog
* Sun Jan 25 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.1.5-alt1
- new version 0.1.5 (with rpmrb script)

* Sat Nov 08 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.3-alt1
- new version 0.1.3 (with rpmrb script)

* Sat Nov 01 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- Initial build
