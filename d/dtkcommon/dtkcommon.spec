%def_disable clang

Name: dtkcommon
Version: 5.5.21
Release: alt1
Summary: Deepin desktop schemas
License: LGPL-3.0+ and GPL-3.0+
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dtkcommon
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang12.0-devel
%else
BuildRequires(pre): gcc-c++
%endif
BuildRequires: glibc-core
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools

%description
%summary.

%package -n dtk5-common
Summary: Deepin desktop schemas
Group: System/Configuration/Other

%description -n dtk5-common
%summary.

%prep
%setup
sed -i 's|$$PREFIX/lib/$$ARCH|%_libdir|; s|$$PREFIX/lib/$(ARCH)|%_libdir|' \
    dtkcommon.pro

%build
export QTDIR=%_qt5_prefix
export PATH=%_qt5_bindir:$PATH
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix \
    DTK_VERSION=%version \
    VERSION=%version \
    LIB_INSTALL_DIR=%_libdir \
    ARCH=%_arch \
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n dtk5-common
%doc LICENSE README.md
%_libdir/cmake/Dtk/DtkConfig.cmake
%_libdir/cmake/Dtk/DtkInstallDConfigConfig.cmake
%_qt5_archdatadir/mkspecs/features/*.prf
%_qt5_archdatadir/mkspecs/modules/qt_lib_dtkcommon.pri
%_datadir/glib-2.0/schemas/com.deepin.dtk.gschema.xml

%changelog
* Fri Apr 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.21-alt1
- New version (5.5.21).

* Tue Feb 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.20-alt1
- New version (5.5.20).

* Tue Jul 06 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.17-alt1
- New version (5.5.17).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.3-alt1
- New version (5.5.3) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.2-alt1
- Initial build for ALT Sisyphus.
