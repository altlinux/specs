
Summary: Library for producing small, fast columnar storage for Hadoop workloads
Name: apache-orc
Version: 1.9.1
Release: alt1
License: Apache-2.0
Url: http://orc.apache.org/
Group: System/Libraries
Source: %name-%version.tar
Patch1: %name-%version-%release.patch

# Apache ORC has numerous compile errors and apparently assumes a 64-bit
# build and runtime environment. The only consumer of this package is
# Ceph (by way of Apache Arrow) which is also 64-bit only
ExcludeArch: %ix86 %arm
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= 3.12.0
BuildRequires: gcc-c++
BuildRequires: libprotobuf-devel protobuf-compiler
BuildRequires: zlib-devel
BuildRequires: libzstd-devel
BuildRequires: liblz4-devel
BuildRequires: libsnappy-devel

%description
ORC is a self-describing type-aware columnar file format designed
for Hadoop workloads. It is optimized for large streaming reads,
but with integrated support for finding required rows quickly.
Storing data in a columnar format lets the reader read, decompress,
and process only the values that are required for the current query.
Because ORC files are type-aware, the writer chooses the most
appropriate encoding for the type and builds an internal index as
the file is written. Predicate pushdown uses those indexes to
determine which stripes in a file need to be read for a particular
query and the row indexes can narrow the search to a particular set
of 10,000 rows. ORC supports the complete set of types in Hive,
including the complex types: structs, lists, maps, and unions.

%package -n liborc1
Summary: Library for producing small, fast columnar storage for Hadoop workloads
Provides: %name = %EVR
Group: System/Libraries

%description -n liborc1
ORC is a self-describing type-aware columnar file format designed
for Hadoop workloads. It is optimized for large streaming reads,
but with integrated support for finding required rows quickly.
Storing data in a columnar format lets the reader read, decompress,
and process only the values that are required for the current query.
Because ORC files are type-aware, the writer chooses the most
appropriate encoding for the type and builds an internal index as
the file is written. Predicate pushdown uses those indexes to
determine which stripes in a file need to be read for a particular
query and the row indexes can narrow the search to a particular set
of 10,000 rows. ORC supports the complete set of types in Hive,
including the complex types: structs, lists, maps, and unions.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C++
Requires: liborc1 = %EVR

%description devel
ORC is a self-describing type-aware columnar file format designed
for Hadoop workloads. It is optimized for large streaming reads,
but with integrated support for finding required rows quickly.
Storing data in a columnar format lets the reader read, decompress,
and process only the values that are required for the current query.
Because ORC files are type-aware, the writer chooses the most
appropriate encoding for the type and builds an internal index as
the file is written. Predicate pushdown uses those indexes to
determine which stripes in a file need to be read for a particular
query and the row indexes can narrow the search to a particular set
of 10,000 rows. ORC supports the complete set of types in Hive,
including the complex types: structs, lists, maps, and unions.

Contains header files for developing applications that use the %name
library.

%prep
%setup
%patch1 -p1

%build
#export CXXFLAGS="$RPM_OPT_FLAGS -Wno-error=dangling-reference"

%cmake \
    -DOVERRIDE_INSTALL_PREFIX=/usr \
    -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
    -DCMAKE_INSTALL_LIBDIR:PATH=%_libdir \
    -DINSTALL_LIBDIR:PATH=%_libdir \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DBUILD_LIBHDFSPP:BOOL=OFF \
    -DSNAPPY_HOME="/usr" \
    -DLZ4_HOME="/usr" \
    -DZLIB_HOME="/usr" \
    -DZSTD_HOME="/usr" \
    -DGTEST_HOME="/usr" \
    -DPROTOBUF_HOME="/usr" \
    -Dorc_VERSION="%version" \
    -DBUILD_CPP_TESTS=off \
    -DBUILD_TOOLS=off \
    -DBUILD_JAVA=off \
    -DANALYZE_JAVA=off \
    "-GUnix Makefiles"
%cmake_build

%install
%cmake_install

%files -n liborc1
%doc README.md
%_libdir/liborc.so.*

%files devel
%_includedir/orc
%_libdir/liborc.so
%_libdir/cmake/orc

%changelog
* Thu Oct 19 2023 Alexey Shabalin <shaba@altlinux.org> 1.9.1-alt1
- New version 1.9.1.

* Fri Apr 07 2023 Alexey Shabalin <shaba@altlinux.org> 1.8.3-alt1
- Initial build.
