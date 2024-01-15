%def_disable qt5

%define soname 1

Name: kdsingleapplication
Version: 1.1.0
Release: alt1

Summary: KDAB's helper class for single-instance policy applications

License: MIT
Group: System/Libraries
Url: https://github.com/KDAB/KDSingleApplication

Source: %url/archive/v%version/KDSingleApplication-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++ cmake
%if_enabled qt5
BuildRequires: qt5-base-devel
%else
BuildRequires: qt6-base-devel
%endif

%description
%summary.

%if_enabled qt5

%package -n lib%name%soname
Group: System/Libraries
Summary: %summary

%description -n lib%name%soname
%summary.

This package provides lib%name for qt5.

%package -n lib%name-devel
Group: Development/C++
Summary: %summary
Requires: lib%name%soname

%description -n lib%name-devel
This package contains libraries and header files for developing applications
that use KDSingleApplication with Qt5.

%else

%package -n lib%name-qt6-%soname
Group: System/Libraries
Summary: %summary

%description -n lib%name-qt6-%soname
%summary.

This package provides lib%name for qt5.

%package -n lib%name-qt6-devel
Group: Development/C++
Summary: %summary
Requires: lib%name-qt6-%soname

%description -n lib%name-qt6-devel
This package contains libraries and header files for developing applications
that use KDSingleApplication with Qt6.

%endif

%prep
%setup -n KDSingleApplication-%version

%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if_enabled qt5
  -DKDSingleApplication_QT6=OFF \
%else
  -DKDSingleApplication_QT6=ON \
%endif
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%if_enabled qt5

%files -n lib%name%soname
%doc %_docdir/KDSingleApplication/LICENSE.txt
%doc %_docdir/KDSingleApplication/README.md
%dir %_docdir/KDSingleApplication/LICENSES/
%doc %_docdir/KDSingleApplication/LICENSES/MIT.txt
%doc %_docdir/KDSingleApplication/LICENSES/BSD-3-Clause.txt
%_libdir/lib%name.so.%{soname}*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/%name/
%_includedir/%name/%{name}*.h
%_includedir/%name/KDSingleApplication
%dir %_libdir/cmake/KDSingleApplication/
%_libdir/cmake/KDSingleApplication/KDSingleApplicationConfig*.cmake
%_libdir/cmake/KDSingleApplication/KDSingleApplicationTargets*.cmake
# %_libdir/qt5/mkspecs/modules/qt_KDSingleApplication.pri

%else

%files -n lib%name-qt6-%soname
%doc %_docdir/KDSingleApplication-qt6/LICENSE.txt
%doc %_docdir/KDSingleApplication-qt6/README.md
%dir %_docdir/KDSingleApplication-qt6/LICENSES/
%doc %_docdir/KDSingleApplication-qt6/LICENSES/MIT.txt
%doc %_docdir/KDSingleApplication-qt6/LICENSES/BSD-3-Clause.txt
%_libdir/lib%name-qt6.so.%{soname}*

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

%endif

%changelog
* Mon Jan 15 2024 Leontiy Volodin <lvol@altlinux.org> 1.1.0-alt1
- Initial build for ALT Sisyphus (for strawberry).
