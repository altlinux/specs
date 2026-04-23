%def_enable tests
%def_enable qt5

%define ver_major 1.2

Name: kdsingleapplication
Version: 1.2.1
Release: alt1

Summary: KDAB's helper class for single-instance policy applications

License: MIT
Group: System/Libraries
Url: https://github.com/KDAB/KDSingleApplication
VCS: https://github.com/KDAB/KDSingleApplication

# Source-url: https://github.com/KDAB/KDSingleApplication/archive/v%version/KDSingleApplication-%version.tar.gz
Source: KDSingleApplication-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
%if_enabled tests
BuildRequires(pre): ctest
%endif
BuildRequires: gcc-c++ cmake qt6-base-devel libvulkan-devel
%if_enabled qt5
BuildRequires: qt5-base-devel
%endif

%description
%summary.

%package -n lib%name-common
Group: Development/Other
Summary: Common files for lib%name
BuildArch: noarch
Provides: lib%name-qt6-common = %EVR
Obsoletes: lib%name-qt6-common < %EVR

%description -n lib%name-common
This package provides common files for lib%name.

%if_enabled qt5

%package -n lib%name%ver_major
Group: System/Libraries
Summary: %summary

%description -n lib%name%ver_major
%summary.

This package provides lib%name for qt5.

%package -n lib%name-devel
Group: Development/C++
Summary: %summary
Requires: lib%name%ver_major

%description -n lib%name-devel
This package contains libraries and header files for developing applications
that use KDSingleApplication with Qt5.

%endif

%package -n lib%name-qt6_%ver_major
Group: System/Libraries
Summary: %summary

%description -n lib%name-qt6_%ver_major
%summary.

This package provides lib%name for qt5.

%package -n lib%name-qt6-devel
Group: Development/C++
Summary: %summary
Requires: lib%name-qt6_%ver_major

%description -n lib%name-qt6-devel
This package contains libraries and header files for developing applications
that use KDSingleApplication with Qt6.

%prep
%setup -n KDSingleApplication-%version
%autopatch -p1

%build
export LC_ALL=C.UTF-8

%if_enabled qt5
%cmake -B build5 \
 -GNinja \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DKDSingleApplication_QT6=OFF \
 -DECM_MKSPECS_INSTALL_DIR=%_libdir/qt5/mkspecs/modules \
%if_enabled tests
 -DKDSingleApplication_TESTS=ON \
%endif
#
cmake --build "build5" -j%__nprocs
%endif

%cmake -B build6 \
 -GNinja \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DKDSingleApplication_QT6=ON \
%if_enabled tests
 -DKDSingleApplication_TESTS=ON \
%endif
 -DINSTALL_DOC_DIR=%_docdir/%name-%version \
#
cmake --build "build6" -j%__nprocs

%install
export DESTDIR="%buildroot"
%if_enabled qt5
cmake --install "build5" --verbose
rm -rf %buildroot%_docdir/KDSingleApplication/
%endif
cmake --install "build6" --verbose

%if_enabled tests
%check
%if_enabled qt5
%ctest --test-dir "build5"
%endif
%ctest --test-dir "build6"
%endif

%files -n lib%name-common
%dir %_docdir/%name-%version/
%_docdir/%name-%version/LICENSE.txt
%_docdir/%name-%version/README.md
%_docdir/%name-%version/LICENSES/
%_docdir/%name-%version/LICENSES/MIT.txt
%_docdir/%name-%version/LICENSES/BSD-3-Clause.txt

%if_enabled qt5

%files -n lib%name%ver_major
%_libdir/lib%name.so.%{ver_major}*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/%name/
%_includedir/%name/%{name}*.h
%_includedir/%name/KDSingleApplication
%dir %_libdir/cmake/KDSingleApplication/
%_libdir/cmake/KDSingleApplication/KDSingleApplicationConfig*.cmake
%_libdir/cmake/KDSingleApplication/KDSingleApplicationTargets*.cmake
%_libdir/qt5/mkspecs/modules/qt_KDSingleApplication.pri

%endif

%files -n lib%name-qt6_%ver_major
%_libdir/lib%name-qt6.so.%{ver_major}*

%files -n lib%{name}-qt6-devel
%_libdir/lib%name-qt6.so
%dir %_includedir/%name-qt6/
%_includedir/%name-qt6/KDSingleApplication
%_includedir/%name-qt6/%{name}*.h
%dir %_libdir/cmake/KDSingleApplication-qt6/
%_libdir/cmake/KDSingleApplication-qt6/KDSingleApplication-qt6Config*.cmake
%_libdir/cmake/KDSingleApplication-qt6/KDSingleApplication-qt6Targets*.cmake
%_libdir/cmake/KDSingleApplication-qt6/KDSingleApplicationTargets*.cmake
%_libdir/qt6/mkspecs/modules/qt_KDSingleApplication.pri

%changelog
* Thu Apr 23 2026 Leontiy Volodin <lvol@altlinux.org> 1.2.1-alt1
- New version 1.2.1.
- Enabled tests.

* Fri Nov 14 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.0-alt3
- Fixed file conflicts when installing common subpackage.

* Fri Nov 14 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.0-alt2
- Fixed file conflicts between common and library subpackages.

* Tue May 27 2025 Leontiy Volodin <lvol@altlinux.org> 1.2.0-alt1
- New version 1.2.0.
- Built with vulkan support and qt5 library.
- Packaged common files separately.
- Added VCS tag.

* Mon Jan 15 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt1
- Initial build for ALT Sisyphus (for strawberry).
