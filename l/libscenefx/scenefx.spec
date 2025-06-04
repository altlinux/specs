%define soversion 2

Name:     libscenefx
Version:  0.2.1
Release:  alt1

Summary:  A drop-in wlroots replacement that allows eye-candy effects
License:  MIT
Group:    System/Libraries

Url:      https://github.com/wlrfx/scenefx

# Source-url: https://github.com/wlrfx/scenefx/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(wayland-protocols) >= 1.27
BuildRequires: pkgconfig(wayland-server) >= 1.22.0
BuildRequires: pkgconfig(wlroots-0.18)

BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(gbm)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(xkbcommon)

%description
%summary.

%package -n %name%soversion
Summary: A drop-in wlroots replacement that allows eye-candy effects
Group: System/Libraries

%description -n %name%soversion
%summary.

%package -n %name-devel
Summary: Development files for %name
Group: Development/C
Requires: %name%soversion = %EVR

%description -n %name-devel
This package provides development files for %name library.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files -n %name%soversion
%doc README.md
%_libdir/%name-0.%soversion.so

%files -n %name-devel
%_includedir/scenefx-0.%soversion/
%_pkgconfigdir/scenefx-0.%soversion.pc

%changelog
* Wed Jun 04 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.1-alt1
- new version 0.2.1 (with rpmrb script)

* Thu Jun 13 2024 Roman Alifanov <ximper@altlinux.org> 0.1-alt2
- correction of files section (to avoid errors when the soversion changes)

* Fri May 24 2024 Roman Alifanov <ximper@altlinux.org> 0.1-alt1
- initial build for sisyphus
