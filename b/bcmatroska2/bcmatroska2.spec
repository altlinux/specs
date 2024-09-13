%define sover 0

Name: bcmatroska2
Version: 5.3.83
Release: alt1

Summary: C Library to Deal with Matroska Files

License: BSD-3-Clause AND Zlib AND GPL-2.0-or-later
Group: System/Libraries
Url: https://gitlab.linphone.org/BC/public/bcmatroska2

Source: https://gitlab.linphone.org/BC/public/bcmatroska2/-/archive/%version/%name-%version.tar.bz2

BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake libbctoolbox-devel

%description
Bcmatroska2 is a C library to parse Matroska files (.mkv and .mka).

%package -n lib%name-%sover
Summary: C Library to Deal with Matroska Files
Group: System/Libraries

%description -n lib%name-%sover
Bcmatroska2 is a C library to parse Matroska files (.mkv and .mka).

%package -n lib%name-devel
Summary: Development files for bcmatroska2
Group: Development/C

%description -n lib%name-devel
This package includes the files necessary for compiling and linking
applications which will use libbcmatroska2.

%prep
%setup
sed -i 's|VERSION 0.23|VERSION %version|' CMakeLists.txt
sed -i '/DESTINATION/s|${CMAKE_INSTALL_INCLUDEDIR}|${CMAKE_INSTALL_INCLUDEDIR}/%name|' \
  $(find ./ -name '*CMakeLists.txt')
sed -i '/CMAKE_MODULES_INSTALL_DIR/s|${CMAKE_INSTALL_DATADIR}/${PROJECT_NAME}/cmake|${CMAKE_INSTALL_LIBDIR}/cmake/${PROJECT_NAME}|g' \
  CMakeLists.txt

%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_SHARED_LIBS=ON \
  -DCMAKE_MODULES_INSTALL_DIR=%_libdir/cmake/BCMatroska2
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files -n lib%name-%sover
%_libdir/lib%name.so.%{sover}*

%files -n lib%name-devel
%_libdir/libbcmatroska2.so
%dir %_includedir/%name
%dir %_includedir/%name/corec
%_includedir/%name/corec/*
%dir %_includedir/%name/ebml
%_includedir/%name/ebml/*
%dir %_includedir/%name/matroska
%_includedir/%name/matroska/*
%dir %_libdir/cmake/BCMatroska2/
%_libdir/cmake/BCMatroska2/*.cmake

%changelog
* Fri Sep 13 2024 Leontiy Volodin <lvol@altlinux.org> 5.3.83-alt1
- Initial build for ALT Sisyphus (ALT #51472).
