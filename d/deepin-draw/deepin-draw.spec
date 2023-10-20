%def_disable clang

Name: deepin-draw
Version: 5.10.6
Release: alt1.1
Summary: A lightweight drawing tool for Linux Deepin
License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-draw
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires: clang12.0-tools
%else
BuildRequires: gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja desktop-file-utils
BuildRequires: cmake libfreeimage-devel dtk5-widget-devel libexif-devel libxcbutil-devel qt5-base-devel qt5-svg-devel qt5-linguist qt5-multimedia-devel qt5-x11extras-devel qt5-tools-devel
# Requires: deepin-session-shell deepin-qt5integration

%description
A lightweight drawing tool for Linux Deepin.

%prep
%setup

%build
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=Release \
  -DAPP_VERSION=%version \
  -DVERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
%if_enabled clang
  -DLLVM_PARALLEL_LINK_JOBS=1 \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  -DLLVM_TARGETS_TO_BUILD="all" \
  -DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD='AVR' \
  -DLLVM_ENABLE_LIBCXX:BOOL=OFF \
  -DLLVM_ENABLE_ZLIB:BOOL=ON \
%endif
  #
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang %name

%check
desktop-file-validate %buildroot%_desktopdir/%name.desktop ||:

%files -f %name.lang
%doc README.md
%doc LICENSE
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/deepin/apps/scalable/%name.svg
%_datadir/mime/packages/%name.xml
%_datadir/application/x-ddf.xml
%_datadir/dbus-1/services/com.deepin.Draw.service
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/draw/

%changelog
* Fri Oct 20 2023 Ivan A. Melnikov <iv@altlinux.org> 5.10.6-alt1.1
- NMU: remove (pre) from conditional BR's, they don't
  work like that and are not needed (fixes build on loongarch64).

* Wed Feb 09 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.6-alt1
- New version (5.10.6).

* Thu Aug 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.7-alt1
- New version (5.9.7).

* Mon Jun 07 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.4-alt1
- New version (5.9.4).
- Built with gcc-c++ and cmake instead clang and qmake.

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.20-alt1
- New version (5.8.0.20) with rpmgs script.

* Thu Jul 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.19-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
