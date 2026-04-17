Name: hyprpwcenter
Version: 0.1.2
Release: alt1
License: BSD-3-Clause

Summary: A GUI Pipewire control center

Group: Sound

Url: https://github.com/hyprwm/hyprpwcenter
Vcs: https://github.com/hyprwm/hyprpwcenter.git

ExcludeArch: %ix86
Source: %name-%version.tar

Patch1: clang.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: clang libstdc++-devel

BuildRequires: pkgconfig(hyprtoolkit)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(aquamarine)

BuildRequires: pkgconfig(libpipewire-0.3)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%cmake -DCMAKE_CXX_COMPILER=clang++
%cmake_build 

%install
%cmake_install

%files
%_bindir/hyprpwcenter
%_desktopdir/hyprpwcenter.desktop

%changelog
* Wed Feb 11 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- new version 0.1.2

* Tue Oct 28 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.1-alt1
- Initial build
