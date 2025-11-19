Name: libva-driver-intel-hybrid
Version: 2.4.5
Release: alt1

Summary: VA-API (Video Acceleration API) user mode driver for Intel GEN Graphics family
License: MIT
Group: System/Libraries
Url: https://github.com/irql-notlessorequal/intel-vaapi-driver

Conflicts: libva < 1.1.0, libva-driver-intel

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: libdrm-devel libX11-devel libGL-devel libEGL-devel python3 rpm-build-python3
BuildRequires: libva-devel >= 2.22.0 libwayland-client-devel
ExclusiveArch: %ix86 x86_64

# due wayland compatiblity and crazy alt versioning
Requires: libva >= 2.22.0

%description
VA-API driver for Intel GEN Graphics family (plus fixes, works with Chromium).

%prep
%setup

%build
find -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS NEWS
%_libdir/dri/*.so

%changelog
* Tue Nov 18 2025 L.A. Kostis <lakostis@altlinux.ru> 2.4.5-alt1
- 2.4.5.
- spec based on libva-driver-intel.

