#%%global _qt5_qmldir %%{_qt5_archdatadir}/qml
%global __provides_exclude ^libGSettingsQmlPlugin\\.so.*$

%def_disable clang

Name: gsettings-qt
Version: 0.2
Release: alt2.gitd5e002d
Summary: Qt/QML bindings for GSettings
License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/core/gsettings-qt
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %name-%version.tar.gz

%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: libgio-devel qt5-declarative-devel

%description
Qt/QML bindings for GSettings.

%package -n lib%name
Summary: Qt/QML bindings for GSettings
Group: System/Libraries

%description -n lib%name
Libraries for %name.

%package devel
Summary: Development package for %name
Group: Graphical desktop/Other

%description devel
Header files and libraries for %name.

%prep
%setup
#__subst 's|<QObject>|<QtCore/QObject>|; s|<QStringList>|<QtCore/QStringList>|' src/qgsettings.h

%build
export PATH=%_qt5_bindir:$PATH
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif

%qmake_qt5 \
  CONFIG+=nostrip \
%if_enabled clang
  QMAKE_STRIP= -spec linux-clang \
%endif
%nil
# Parallel build not supported. It causes error when linking
%make

%install
%makeinstall INSTALL_ROOT=%buildroot

# remove test
rm -rf %buildroot%_qt5_prefix/tests -rf
find %buildroot -iname test* -exec rm -f {} \;
find %buildroot -iname cpptest* -exec rm -f {} \;

%files -n lib%name
%_libdir/lib%name.so.*
%doc COPYING
%dir %_qt5_qmldir/GSettings.1.0/
%_qt5_qmldir/GSettings.1.0/libGSettingsQmlPlugin.so
%_qt5_qmldir/GSettings.1.0/plugins.qmltypes
%_qt5_qmldir/GSettings.1.0/qmldir

%files devel
%doc COPYING
%dir %_qt5_headerdir/QGSettings/
%_qt5_headerdir/QGSettings/*
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so

%changelog
* Thu Dec 01 2022 Leontiy Volodin <lvol@altlinux.org> 0.2-alt2.gitd5e002d
- Built from commit d5e002d7e0bce46c315bcc99a44a8bd51f49f488.
- Updated url tag.

* Fri Aug 09 2019 Leontiy Volodin <lvol@altlinux.org> 0.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for spec).
