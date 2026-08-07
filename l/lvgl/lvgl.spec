%define _unpackaged_files_terminate_build 1
%define abiversion 9

%def_without check

Name: lvgl
Version: 9.5.0
Release: alt1
Summary: Light and Versatile Graphics Library for embedded GUIs
License: MIT
Group: System/Libraries
Url: https://lvgl.io/
Vcs: https://github.com/lvgl/lvgl

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: python3

%description
LVGL is a free and open-source UI library that enables you to create graphical
user interfaces for any MCUs and MPUs from any vendor on any platform.

%package -n lib%name%abiversion
Summary: Shared libraries for %name
Group: System/Libraries

%description -n lib%name%abiversion
Shared libraries for LVGL.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name%abiversion = %version-%release

%description -n lib%name-devel
Headers and development files for LVGL.

%prep
%setup
# Generate lv_conf.h from upstream install defaults (same as .github/workflows/install.yml).
python3 ./scripts/generate_lv_conf.py \
	--template lv_conf_template.h \
	--config lv_conf.h \
	--defaults configs/ci/install/lv_conf.defaults
# Shared build cannot link cyclic lvgl <-> thorvg; disable ThorVG for packaging.
sed -i \
	-e "s|^#define LV_USE_THORVG_INTERNAL .*|#define LV_USE_THORVG_INTERNAL 0|" \
	-e "s|^#define LV_USE_LOTTIE .*|#define LV_USE_LOTTIE 0|" \
	-e "s|^#define LV_USE_VECTOR_GRAPHIC .*|#define LV_USE_VECTOR_GRAPHIC 0|" \
	lv_conf.h
# Fix pkg-config libdir for multiarch (lib64).
sed -i "s|libdir=\${prefix}/lib|libdir=\${prefix}/%_lib|" lvgl.pc.in

%build
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DLIB_INSTALL_DIR=%_libdir \
	-DLV_BUILD_LVGL_H_SYSTEM_INCLUDE=ON \
	-DCONFIG_LV_BUILD_DEMOS=OFF \
	-DCONFIG_LV_BUILD_EXAMPLES=OFF \
	-DCONFIG_LV_USE_THORVG_INTERNAL=OFF
%cmake_build

%install
%cmake_install

%files -n lib%name%abiversion
%doc README.md COPYRIGHTS.md LICENCE.txt
%_libdir/liblvgl.so.%abiversion
%_libdir/liblvgl.so.%abiversion.*

%files -n lib%name-devel
%_libdir/liblvgl.so
%_includedir/lvgl/
%_datadir/pkgconfig/lvgl.pc

%changelog
* Fri Aug 07 2026 Pavel Shilov <zerospirit@altlinux.org> 9.5.0-alt1
- Initial build for Sisyphus.
