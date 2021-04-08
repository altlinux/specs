%def_disable clang

Name: dtkcommon
Version: 5.5.2
Release: alt1
Summary: Deepin desktop schemas
License: LGPL-3.0+ and GPL-3.0+
Group: System/Configuration/Other
Url: https://github.com/linuxdeepin/dtkcommon
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires(pre): clang11.0-devel
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
%qmake_qt5 \
%if_enabled clang
    QMAKE_STRIP= -spec linux-clang \
%endif
    CONFIG+=nostrip \
    PREFIX=%prefix \
    DTK_VERSION=%version \
    VERSION=%version \
    LIB_INSTALL_DIR=%_libdir \
#
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files -n dtk5-common
%doc LICENSE README.md
%_sysconfdir/dbus-1/system.d/com.deepin.dtk.FileDrag.conf
%_libdir/cmake/Dtk/DtkConfig.cmake
%_qt5_archdatadir/mkspecs/features/*.prf
%_qt5_archdatadir/mkspecs/modules/qt_lib_dtkcommon.pri
%_datadir/glib-2.0/schemas/com.deepin.dtk.gschema.xml

%changelog
* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.2-alt1
- Initial build for ALT Sisyphus.
