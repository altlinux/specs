%define quake2_ver 8.70
%define ref_vk_ver 1.0.12

Name: yquake2
Version: %quake2_ver
Release: alt1
License: GPLv2 AND Info-ZIP AND MIT
Group: Games/Other
Summary: Yamagi Quake II is an alternative client for id Softwares Quake II
URL: https://www.yamagi.org/quake2/
# Vcs: https://github.com/yquake2/yquake2/archive/refs/tags/QUAKE2_%{quake2_ver}.tar.gz
Source0: %name-%version.tar
Source1: ref_vk-%ref_vk_ver.tar

# due same binary names
Conflicts: quake2

BuildRequires(pre): cmake ninja-build pkgconf
BuildRequires: libopenal-devel libcurl-devel libglvnd-devel libSDL3-devel libstb-devel libvulkan-devel

%description
Yamagi Quake II is an alternative client for id Softwares Quake II. Our goal is
to provide the best Quake II experience possible, we strive to preserve the
game play as it was back in 1997. Thus we aim mostly for bug fixes, stability
and gentle enhancements were appropriate.

%prep
%setup -a1
# unbundle stb
pushd src/client/refresh/files
ln -svf %_includedir/stb/stb_image.h \
	%_includedir/stb/stb_image_resize.h ./
popd
pushd ref_vk-%ref_vk_ver/src/files
ln -svf %_includedir/stb/stb_image.h \
	%_includedir/stb/stb_image_resize.h ./
popd

%build
%cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
pushd ref_vk-%ref_vk_ver
export CFLAGS='%optflags'
%make_build
popd

%install
mkdir -p %buildroot%_gamesbindir/
mkdir -p %buildroot%_libdir/%name
cp -ar %_cmake__builddir/release/* %buildroot%_libdir/%name/
cp -ar ref_vk-%ref_vk_ver/release/ref_vk.so %buildroot%_libdir/%name/
install -pm0644 ref_vk-%ref_vk_ver/README.md README.md-ref_vk
ln -sf %_libdir/%name/q2ded %buildroot%_gamesbindir/q2ded
ln -sf %_libdir/%name/quake2 %buildroot%_gamesbindir/quake2

%files
%doc README.md LICENSE CHANGELOG README.md-ref_vk doc stuff/yq2.cfg
%_libdir/%name
%_gamesbindir/quake2
%_gamesbindir/q2ded

%changelog
* Tue Jun 09 2026 L.A. Kostis <lakostis@altlinux.ru> 8.70-alt1
- quake2: updated to 8.70.
- ref_vk: updated to 1.0.12.
- SDL2->SDL3.
- ref_vk/BR: added pkgconf.

* Wed Sep 17 2025 L.A. Kostis <lakostis@altlinux.ru> 8.60-alt1
- quake2: updated to 8.60.
- ref_vk: updated to 1.0.11.

* Tue May 13 2025 L.A. Kostis <lakostis@altlinux.ru> 8.51-alt1
- quake2: update to 8.51.

* Tue May 13 2025 L.A. Kostis <lakostis@altlinux.ru> 8.41-alt3
- ref_vk: updated to 1.0.10.
- ref_vk: unbundle stb.

* Tue Mar 11 2025 L.A. Kostis <lakostis@altlinux.ru> 8.41-alt2
- ref_vk: update to 1.0.9.

* Mon Feb 10 2025 L.A. Kostis <lakostis@altlinux.ru> 8.41-alt1
- Initial build for ALTLinux.

