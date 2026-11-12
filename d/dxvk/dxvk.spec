Name: dxvk
Version: 3.1.1
Release: alt1
Summary: Vulkan-based implementation of D3D8, D3D9, D3D10 and D3D11 (DXVK Native)

Group: System/Libraries
License: Zlib and MIT and Apache-2.0
Url: https://github.com/doitsujin/dxvk

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++ glslang
BuildRequires: libSDL2-devel libSDL3-devel libglfw3-devel

%description
DXVK is a Vulkan-based translation layer for Direct3D 8/9/10/11 which allows
running 3D applications on Linux using Wine.

This package provides DXVK Native: a native Linux build of DXVK with SDL2,
SDL3 and GLFW window system integration, for porting Direct3D applications
to Linux without Wine.

%package -n lib%name
Summary: %name libraries
Group: System/Libraries

%description -n lib%name
Native Linux build of DXVK libraries.

%package devel
Summary: %name development package
Group: Development/C
Requires: lib%name = %EVR

%description devel
Development headers and pkg-config files for DXVK Native.

%prep
%setup

%build
%ifarch %ix86
# dxbc-spirv subproject does not get dxvk's -msse2 flags; LTO then fails on i586
%add_optflags -msse -msse2 -mfpmath=sse
%endif

%meson \
  -Dnative_sdl2=enabled \
  -Dnative_sdl3=enabled \
  -Dnative_glfw=enabled \
  --force-fallback-for=libdisplay-info
%meson_build

%install
%meson_install
rm %buildroot%_includedir/%name/{README.md,COPYING.MinGW-w64.txt}

%files -n lib%name
%doc LICENSE README.md dxvk.conf
%_libdir/lib%{name}_*.so.*

%files devel
%doc include/native/directx/COPYING.MinGW-w64.txt
%_includedir/%name
%_libdir/lib%{name}_*.so
%_pkgconfigdir/%{name}-*.pc

%changelog
* Thu Nov 12 2026 Mikhail Tergoev <fidel@altlinux.org> 3.1.1-alt1
- initial build for ALT Sisyphus
