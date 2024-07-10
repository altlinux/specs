%define _unpackaged_files_terminate_build 1

Name:    hyprlock
Version: 0.3.0
Release: alt1

Summary: Hyprland's GPU-accelerated screen locking utility
License: BSD-3-Clause
Group:   Other
Url:     https://github.com/hyprwm/hyprlock

Source: %name-%version.tar
patch0: hyprlock-0.3.0.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: libpam-devel

%description
%summary

%prep
%setup
%patch0

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
echo 'auth            include         system-auth' > %buildroot%_sysconfdir/pam.d/%name

%files
%doc *.md
%_bindir/*
%config(noreplace) %_sysconfdir/pam.d/%name

%changelog
* Fri Jul 05 2024 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Build to Sisyphus (ALT #50649) (thanks to Timofey Krymskiy).
- Adapt PAM module to ALT PAM stack.
