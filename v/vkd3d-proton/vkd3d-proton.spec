%def_enable extras

Name: vkd3d-proton
Version: 3.1
Release: alt1

Summary: Fork of VKD3D, which aims at implementing the full Direct3D 12 API on top of Vulkan

Group: System/Libraries
License: LGPL-2.1-or-later and MIT
Url: https://github.com/HansKristian-Work/vkd3d-proton

Source: %name-%version.tar

# Fix parallel build race between installed header copies and compilation
Patch0: %name-meson-header-race.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ glslang wine-devel-tools
%if_enabled extras
BuildRequires: libxcb-devel libxcbutil-devel libxcbutil-keysyms-devel libxcbutil-icccm-devel
%endif

# widl (wine-devel-tools) exists only on these arches
ExclusiveArch: %ix86 x86_64 aarch64

%description
VKD3D-Proton is a fork of VKD3D, which aims to implement the full Direct3D 12
API on top of Vulkan. The project serves as the development effort for
Direct3D 12 support in Proton.

%package -n lib%name
Summary: %name libraries
Group: System/Libraries

%description -n lib%name
Native Linux build of libvkd3d-proton.

%package devel
Summary: %name development package
Group: Development/C
Requires: lib%name = %EVR

%description devel
Development headers for vkd3d-proton.

%package utils
Summary: %name utils
Group: Development/C
Requires: lib%name = %EVR

%description utils
vkd3d-proton utilities: vkd3d-proton-compiler, vkd3d-rs-parse.

%package demos
Summary: %name demos
Group: Development/C
Requires: lib%name = %EVR

%description demos
vkd3d-proton demos (gears, triangle).

%prep
%setup
%patch0 -p1

%build
%meson %{subst_enable_meson_bool extras enable_extras}
%meson_build

%install
%meson_install
%if_enabled extras
for f in gears triangle; do
  mv %buildroot%_bindir/$f %buildroot%_bindir/%name-$f
done
%endif

%files -n lib%name
%doc COPYING LICENSE README.md CHANGELOG.md
%_libdir/*.so

%files devel
%_includedir/%name
%_pkgconfigdir/*.pc

%if_enabled extras
%files utils
%_bindir/%name-compiler
%_bindir/vkd3d-rs-parse

%files demos
%_bindir/%name-gears
%_bindir/%name-triangle
%endif

%changelog
* Thu Nov 12 2026 Mikhail Tergoev <fidel@altlinux.org> 3.1-alt1
- initial build for ALT Sisyphus
