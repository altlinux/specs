%global _unpackaged_files_terminate_build 1
%def_with check

Name: hyprlogin
Version: 0.4.0
Release: alt1
Summary: GPU-accelerated graphical greeter for greetd, built on Hyprland
License: BSD-3-Clause
Group: Graphical desktop/Other
URL: https://github.com/AuthenticSm1les/hyprlogin
VCS: https://github.com/AuthenticSm1les/hyprlogin

ExcludeArch: i586

Source: %name-%version.tar
Source1: %name-tmpfiles.conf

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-ninja-build
BuildRequires: rpm-build-ninja
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libGL-devel
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(hyprwayland-scanner)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(xkbcommon)

%if_with check
BuildRequires: ctest
BuildRequires: libgtest-devel
%endif

Requires: greetd
Requires: hyprland

Provides: greetd-greeter

%description
A GPU-accelerated graphical greeter for greetd, forked from hyprlock.
It runs inside a minimal Hyprland session started by greetd, authenticates
over the greetd IPC protocol and launches the session you pick.

%prep
%setup

%build
%cmake -GNinja -Wno-dev %{?_with_check:-DBUILD_TESTING=ON}
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
# replace upstream tmpfiles (owner "greeter") with ALT variant:
# ALT greetd runs the greeter as _greeter (see greetd sysusers config)
rm %buildroot%_prefix/lib/tmpfiles.d/%name.conf
install -Dm644 %SOURCE1 %buildroot%_tmpfilesdir/%name.conf

%check
cd %_cmake__builddir
%ninja_test

%files
%_bindir/%name
%_datadir/%name
%_tmpfilesdir/%name.conf

%changelog
* Sun Nov 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.0-alt1
- Initial build for ALT.
