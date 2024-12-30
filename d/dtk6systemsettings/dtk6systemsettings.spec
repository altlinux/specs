%def_disable clang
%def_without docs

%define sover 6

Name: dtk6systemsettings
Version: 6.0.2
Release: alt1

Summary: Deepin tool kit systemsettings modules

License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtk6systemsettings
Vcs: git://github.com/linuxdeepin/dtk6systemsettings.git

Source: %url/archive/%version/%name-%version.tar.gz
Patch: dtk6systemsettings-6.0.2-pkgconfig-dqt6-detection.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-dqt6
BuildRequires: cmake dqt6-base-devel dtk6-common-devel libdtk6core-devel
%if_with docs
BuildRequires: dqt6-tools-devel doxygen texlive-dist
%endif
%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif

%description
%summary.

%package -n lib%name%sover
Summary: Libraries for %name
Group: System/Libraries

%description -n lib%name%sover
Deepin tool kit log modules.
Libraries for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/KDE and QT
Provides: dtk6-log-devel = %EVR
Obsoletes: dtk6-log-devel < %EVR

%description -n lib%name-devel
Header files and libraries for %name.

%prep
%setup
%autopatch -p1

%build
%if_enabled clang
export CC=clang CXX=clang++ LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
%DQ6build \
  -DDTK_VERSION=6 \
  -DMKSPECS_INSTALL_DIR=%_dqt6_mkspecsdir/modules

%install
%DQ6install

%files -n lib%name%sover
%doc README.md LICENSE*
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/dtk6/
%dir %_includedir/dtk6/DSystemSettings/
%_includedir/dtk6/DSystemSettings/*
%dir %_libdir/cmake/Dtk6SystemSettings/
%_libdir/cmake/Dtk6SystemSettings/*.cmake
%_pkgconfigdir/%name.pc
%_dqt6_mkspecsdir/modules/qt_lib_dtk6systemsettings.pri

%changelog
* Mon Dec 30 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.2-alt1
- Initial build for ALT Sisyphus.
