Name: hyprshutdown
Version: 0.1.0
Release: alt1
License: BSD-3-Clause

Summary: A graceful shutdown utility for Hyprland

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprshutdown
Vcs: https://github.com/hyprwm/hyprshutdown.git

ExcludeArch: %ix86
Source: %name-%version.tar

## Patch1: clang.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: clang libstdc++-devel

BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(aquamarine)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(hyprtoolkit)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)

BuildRequires: glaze-devel

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
%_bindir/%name

%changelog
* Wed Feb 11 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build
