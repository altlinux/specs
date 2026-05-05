Name: croaring
Version: 4.6.1
Release: alt1

Summary: Roaring bitmaps in C (and C++)

License: Apache-2.0
Group: System/Libraries
Url: https://github.com/RoaringBitmap/CRoaring

# Source-url: https://github.com/RoaringBitmap/CRoaring/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.16
BuildRequires: gcc-c++

%description
Roaring bitmaps are compressed bitmaps which tend to outperform conventional
compressed bitmaps such as WAH, EWAH or Concise. They are used by several
major systems such as Apache Lucene, Apache Druid, Apache Spark, and LinkedIn.

%package -n libroaring21
Summary: CRoaring shared library
Group: System/Libraries

%description -n libroaring21
Shared library for CRoaring bitmaps.

%package -n libroaring-devel
Summary: Development files for CRoaring
Group: Development/C
Requires: libroaring21 = %EVR

%description -n libroaring-devel
Header files and CMake configuration for developing with CRoaring.

%prep
%setup

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DENABLE_ROARING_TESTS=OFF \
    -DROARING_USE_CPM=OFF
%cmake_build

%install
%cmake_install

%files -n libroaring21
%doc LICENSE
%_libdir/libroaring.so.21
%_libdir/libroaring.so.4.*

%files -n libroaring-devel
%doc README.md
%_includedir/roaring/
%_libdir/libroaring.so
%_libdir/cmake/roaring/
%_libdir/pkgconfig/roaring.pc

%changelog
* Tue May 05 2026 Vitaly Lipatov <lav@altlinux.ru> 4.6.1-alt1
- new version 4.6.1
- rename libroaring18 to libroaring21 (soname bump)

* Mon Mar 30 2026 Vitaly Lipatov <lav@altlinux.ru> 4.3.2-alt1
- initial build for ALT Sisyphus

