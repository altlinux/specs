%define _unpackaged_files_terminate_build 1
%define soname 5

Name: mmg
Version: 5.5.2
Release: alt1
Summary: Surface and volume remeshers

License: LGPLv3+
Group: Graphics
URL: https://www.mmgtools.org/
Source: %name-%version.tar

Patch0: %name-%version-%release.patch

BuildRequires:  doxygen
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libscotch-devel

Requires:       libmmg-%soname = %EVR
Requires:       mmgs = %EVR
Requires:       mmg2d = %EVR
Requires:       mmg3d = %EVR

%description
mmg is an open source software for bidimensional and tridimensional surface and
volume remeshing. It provides:
- The mmg2d application and library: adaptation and optimization of a
  bidimensional triangulation
- The mmgs application and library: adaptation and optimization of a surface
  triangulation and isovalue discretization
- The mmg3d application and library: adaptation and optimization of a
  tetrahedral mesh and implicit domain meshing
- The mmg library, combining the mmg2d, mmgs and mmg3d libraries.

%package -n libmmg-%soname
Summary:        Surface and volume remesher library
Group:          System/Libraries

%description -n libmmg-%soname
The mmg library, combining the mmg2d, mmgs and mmg3d libraries.

%package devel
Summary:        Development files for %name
Group:          Development/C
Requires:       libmmg-%soname = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package -n mmg2d
Summary:        Surface remesher
Group:          Graphics
Requires:       libmmg2d-%soname = %EVR

%description -n mmg2d
The mmg2d application and library: adaptation and optimization of a
bidimensional triangulation.

%package -n libmmg2d-%soname
Summary:        Surface remesher libraries
Group:          System/Libraries

%description -n libmmg2d-%soname
The mmg2d library: adaptation and optimization of a
bidimensional triangulation.

%package -n mmg2d-devel
Summary:        Development files for mmg2d
Group:          Development/C
Requires:       mmg2d = %EVR

%description -n mmg2d-devel
The mmg2d-devel package contains libraries and header files for
developing applications that use mmg2d.

%package -n mmg2d-devel-doc
Summary:        Development documentation for mmg2d
Group:          Development/C
BuildArch:      noarch

%description -n mmg2d-devel-doc
The mmg2d-devel-doc package contains the documentation for developing
applications that use mmg2d.

%package -n mmgs
Summary:        Surface remesher
Group:          Graphics
Requires:	libmmgs-%soname = %EVR

%description -n mmgs
The mmgs application and library: adaptation and optimization of a surface
triangulation and isovalue discretization.

%package -n libmmgs-%soname
Summary:        Surface remesher
Group:          System/Libraries

%description -n libmmgs-%soname
The mmgs library: adaptation and optimization of a surface
triangulation and isovalue discretization.

%package -n mmgs-devel
Summary:        Development files for mmgs
Group:          Development/C
Requires:       mmgs = %EVR

%description -n mmgs-devel
The mmgs-devel package contains libraries and header files for
developing applications that use mmgs.

%package -n mmgs-devel-doc
Summary:        Development documentation for mmgs
Group:          Development/C
BuildArch:      noarch

%description -n mmgs-devel-doc
The mmgs-devel-doc package contains the documentation for developing
applications that use mmgs.

%package -n mmg3d
Summary:        Volume remesher
Group:          Graphics
Requires:       libmmg3d-%soname = %EVR

%description -n mmg3d
The mmg3d application and library: adaptation and optimization of a
tetrahedral mesh and implicit domain meshing.

%package -n libmmg3d-%soname
Summary:        Volume remesher
Group:          System/Libraries
Provides:       mmg3d-libs = %EVR

%description -n libmmg3d-%soname
The mmg3d library: adaptation and optimization of a
tetrahedral mesh and implicit domain meshing.

%package -n mmg3d-devel
Summary:        Development files for mmg3d
Group:          Development/C
Requires:       mmg3d = %EVR

%description -n mmg3d-devel
The mmg3d-devel package contains libraries and header files for
developing applications that use mmg3d

%package -n mmg3d-devel-doc
Summary:        Development documentation for mmg3d
Group:          Development/C
Requires:       mmg3d = %EVR

%description -n mmg3d-devel-doc
The mmg3d-devel-doc package contains the documentation for developing
applications that use mmg3d

%prep
%setup
%patch0 -p1

%build
%cmake -DBUILD_SHARED_LIBS=ON

%cmake_build
%cmake_build doc

%install
%cmakeinstall_std

# Install suffix-less symlinks
ln -s mmg2d_O3 %buildroot/%_bindir/mmg2d
ln -s mmgs_O3 %buildroot/%_bindir/mmgs
ln -s mmg3d_O3 %buildroot/%_bindir/mmg3d

# Install man pages
install -Dpm 0644 doc/man/mmg2d.1.gz %buildroot%_man1dir/mmg2d.1.gz
install -Dpm 0644 doc/man/mmgs.1.gz %buildroot%_man1dir/mmgs.1.gz
install -Dpm 0644 doc/man/mmg3d.1.gz %buildroot%_man1dir/mmg3d.1.gz

%files

%files -n libmmg-%soname
%doc AUTHORS README.md LICENSE COPYING COPYING.LESSER
%_libdir/libmmg.so.%{soname}
%_libdir/libmmg.so.%{soname}.*

%files devel
%dir %_includedir/mmg
%_includedir/mmg/libmmg.h
%_includedir/mmg/libmmgf.h
%_libdir/libmmg.so
%_libdir/cmake/mmg/

%files -n mmg2d
%doc AUTHORS README.md LICENSE COPYING COPYING.LESSER
%_bindir/mmg2d_O3
%_bindir/mmg2d
%_man1dir/mmg2d.1*

%files -n libmmg2d-%soname
%_libdir/libmmg2d.so.%{soname}
%_libdir/libmmg2d.so.%{soname}.*

%files -n mmg2d-devel
%dir %_includedir/mmg
%_includedir/mmg/mmg2d/
%_libdir/libmmg2d.so

%files -n mmg2d-devel-doc
%doc BUILD/doc/mmg2d/html

%files -n mmgs
%doc AUTHORS README.md LICENSE COPYING COPYING.LESSER
%_bindir/mmgs_O3
%_bindir/mmgs
%_man1dir/mmgs.1*

%files -n libmmgs-%soname
%_libdir/libmmgs.so.%{soname}
%_libdir/libmmgs.so.%{soname}.*

%files -n mmgs-devel
%dir %_includedir/mmg
%_includedir/mmg/mmgs/
%_libdir/libmmgs.so

%files -n mmgs-devel-doc
%doc BUILD/doc/mmgs/html

%files -n mmg3d
%doc AUTHORS README.md LICENSE COPYING COPYING.LESSER
%_bindir/mmg3d_O3
%_bindir/mmg3d
%_man1dir/mmg3d.1*

%files -n libmmg3d-%soname
%_libdir/libmmg3d.so.%{soname}
%_libdir/libmmg3d.so.%{soname}.*

%files -n mmg3d-devel
%dir %_includedir/mmg
%_includedir/mmg/mmg3d/
%_libdir/libmmg3d.so

%files -n mmg3d-devel-doc
%doc BUILD/doc/mmg3d/html

%changelog
* Tue Jan 12 2021 Danil Shein <dshein@altlinux.org> 5.5.2-alt1
- Initial build for Sisyphus


