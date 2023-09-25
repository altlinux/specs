%define _unpackaged_files_terminate_build 1

%def_enable flight
%def_disable flight_sql
%def_disable gandiva
%def_disable mimalloc
%def_disable s3
%def_enable rapidjson
%def_enable re2
%def_enable utf8proc
%def_disable utils
%ifarch x86_64 aarch64 ppc64le
%def_enable orc
%endif

Name: arrow
Version: 12.0.0
Release: alt2
Summary: Apache Arrow is a data processing library for analysis
Group: Development/C++

License: Apache-2.0
Url: https://arrow.apache.org/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
ExcludeArch: %arm

BuildRequires(pre): rpm-macros-cmake rpm-macros-meson rpm-build-vala rpm-build-gir rpm-macros-python3
BuildRequires: bison
BuildRequires: boost-devel
BuildRequires: libbrotli-devel
BuildRequires: libcares-devel
BuildRequires: cmake meson ninja-build
%{?_enable_s3:BuildRequires: libcurl-devel}
BuildRequires: flex
BuildRequires: gcc-c++
BuildRequires: libgflags-devel
BuildRequires: git
BuildRequires: libglog-devel
BuildRequires: libgrpc++-devel grpc-plugins
BuildRequires: jsoncpp-devel
BuildRequires: bzlib-devel
BuildRequires: libzstd-devel
BuildRequires: liblz4-devel
BuildRequires: zlib-devel
BuildRequires: libsnappy-devel
BuildRequires: openssl-devel libssl-devel
BuildRequires: python3-devel python3-module-numpy libnumpy-py3-devel python3-module-cffi python3-module-Cython
BuildRequires: %pyproject_buildrequires
BuildRequires: python3-module-setuptools python3-module-setuptools_scm python3-module-wheel
BuildRequires: xsimd-devel
BuildRequires: libabseil-cpp-devel
%{?_enable_rapidjson:BuildRequires: rapidjson-devel}
%{?_enable_re2:BuildRequires: libre2-devel}
BuildRequires: thrift-devel
%{?_enable_orc:BuildRequires: apache-orc-devel}
%{?_enable_utf8proc:BuildRequires: libutf8proc-devel}

%if_enabled gandiva
BuildRequires: llvm-devel
BuildRequires: ncurses-devel
%endif

BuildRequires: gobject-introspection-devel rpm-build-gir
BuildRequires: gtk-doc
BuildRequires: vala vala-tools rpm-build-vala

%description
Apache Arrow is a data processing library for analysis.

%package -n lib%name
Summary: Runtime libraries for Apache Arrow C++
Group: System/Libraries

%description -n lib%name
This package contains the libraries for Apache Arrow C++.

%package devel
Summary: Libraries and header files for Apache Arrow C++
Group: Development/C++
Provides: lib%name-devel = %EVR
Requires: lib%name = %EVR
Requires: libbrotli-devel
Requires: bzlib-devel
Requires: libcares-devel
Requires: libcurl-devel
Requires: libgflags-devel
Requires: libglog-devel
Requires: jsoncpp-devel
Requires: libzstd-devel
Requires: liblz4-devel
Requires: openssl-devel
Requires: rapidjson-devel
Requires: libre2-devel
Requires: libsnappy-devel
Requires: thrift-devel
Requires: libutf8proc-devel
Requires: zlib-devel

%description devel
Libraries and header files for Apache Arrow C++.

%package -n lib%name-acero
Summary: C++ library to execute a query in streaming
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-acero
This package contains the libraries for Apache Arrow Acero.

%package -n lib%name-acero-devel
Summary: Libraries and header files for Apache Arrow Acero
Group: Development/C++
Requires: lib%name-acero = %EVR
Requires: %name-devel = %EVR

%description -n lib%name-acero-devel
Libraries and header files for Apache Arrow Acero.

%package -n lib%name-dataset
Summary: C++ library to read and write semantic datasets stored in different locations and formats
Group: System/Libraries
Requires: lib%name = %EVR
Requires: lib%name-acero = %EVR

%description -n lib%name-dataset
This package contains the libraries for Apache Arrow dataset.

%package -n lib%name-dataset-devel
Summary: Libraries and header files for Apache Arrow dataset
Group: Development/C++
Requires: lib%name-dataset = %EVR
Requires: lib%name-acero-devel = %EVR
Requires: %name-devel = %EVR

%description -n lib%name-dataset-devel
Libraries and header files for Apache Arrow dataset.

%package -n lib%name-flight
Summary: C++ library for fast data transport
Group: System/Libraries
Requires: lib%name = %EVR
Requires: c-ares
Requires: openssl

%description -n lib%name-flight
This package contains the libraries for Apache Arrow Flight.

%package -n lib%name-flight-devel
Summary: Libraries and header files for Apache Arrow Flight
Group: Development/C++
Requires: lib%name-flight = %EVR
Requires: %name-devel = %EVR

%description -n lib%name-flight-devel
Libraries and header files for Apache Arrow Flight.

%package -n lib%name-flight-sql
Summary: C++ library for interacting with SQL databases
Group: System/Libraries
Requires: lib%name-flight = %EVR

%description -n lib%name-flight-sql
This package contains the libraries for Apache Arrow Flight SQL.

%package -n lib%name-flight-sql-devel
Summary: Libraries and header files for Apache Arrow Flight SQL
Group: Development/C++
Requires: lib%name-flight-sql = %EVR
Requires: %name-devel = %EVR

%description -n lib%name-flight-sql-devel
Libraries and header files for Apache Arrow Flight SQL.

%package -n libgandiva
Summary: C++ library for compiling and evaluating expressions on Apache Arrow data
Group: System/Libraries

%description -n libgandiva
This package contains the libraries for Gandiva.

%package -n libgandiva-devel
Summary: Libraries and header files for Gandiva
Group: Development/C++
Requires: %name-devel = %EVR
Requires: libgandiva = %EVR

%description -n libgandiva-devel
Libraries and header files for Gandiva.

%package -n libparquet
Summary: Runtime libraries for Apache Parquet C++
Group: System/Libraries
Requires: lib%name = %EVR
Requires: openssl

%description -n libparquet
This package contains the libraries for Apache Parquet C++.

%package -n libparquet-devel
Summary: Libraries and header files for Apache Parquet C++
Group: Development/C++
Requires: %name-devel = %EVR
Requires: libparquet = %EVR
Requires: zlib-devel

%description -n libparquet-devel
Libraries and header files for Apache Parquet C++.

%package -n parquet-tools
Summary: Tools for Apache Parquet C++
Group: Development/Other
Requires: libparquet = %EVR

%description -n parquet-tools
Tools for Apache Parquet C++.

%package -n lib%name-glib
Summary: Runtime libraries for Apache Arrow GLib
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-glib
This package contains the libraries for Apache Arrow GLib.

%package -n lib%name-glib-gir
Summary: GObject introspection data for the for Apache Arrow GLib
Group: System/Libraries
Requires: lib%name-glib = %EVR

%description -n lib%name-glib-gir
GObject introspection data for the for Apache Arrow GLib.

%package -n lib%name-glib-devel
Summary: Libraries and header files for Apache Arrow GLib
Group: Development/C
Requires: %name-devel = %EVR
Requires: lib%name-glib = %EVR lib%name-glib-gir = %EVR
Requires: gobject-introspection-devel

%description -n lib%name-glib-devel
Libraries and header files for Apache Arrow GLib.

%package glib-doc
Summary: Documentation for Apache Arrow GLib
Group: Development/Documentation

%description glib-doc
Documentation for Apache Arrow GLib.

%package -n lib%name-dataset-glib
Summary: Runtime libraries for Apache Arrow Dataset GLib
Group: System/Libraries
Requires: lib%name-dataset = %EVR
Requires: lib%name-glib = %EVR

%description -n lib%name-dataset-glib
This package contains the libraries for Apache Arrow Dataset GLib.

%package -n lib%name-dataset-glib-gir
Summary: GObject introspection data for the Apache Arrow Dataset GLib
Group: System/Libraries
Requires: lib%name-dataset-glib = %EVR

%description -n lib%name-dataset-glib-gir
GObject introspection data for the Apache Arrow Dataset GLib.

%package -n lib%name-dataset-glib-devel
Summary: Libraries and header files for Apache Arrow Dataset GLib
Group: Development/C
Requires: lib%name-dataset-glib = %EVR lib%name-dataset-glib-gir = %EVR
Requires: lib%name-dataset-devel = %EVR
Requires: lib%name-glib-devel = %EVR
Requires: gobject-introspection-devel

%description -n lib%name-dataset-glib-devel
Libraries and header files for Apache Arrow Dataset GLib.

%package dataset-glib-doc
Summary: Documentation for Apache Arrow Dataset GLib
Group: Development/Documentation
BuildArch: noarch

%description dataset-glib-doc
Documentation for Apache Arrow dataset GLib.

%package -n lib%name-flight-glib
Summary: Runtime libraries for Apache Arrow Flight GLib
Group: System/Libraries
Requires: lib%name-flight = %EVR
Requires: lib%name-glib = %EVR

%description -n lib%name-flight-glib
This package contains the libraries for Apache Arrow Flight GLib.

%package -n lib%name-flight-glib-gir
Summary: GObject introspection data for Apache Arrow Flight GLib
Group: System/Libraries
Requires: lib%name-flight-glib = %EVR

%description -n lib%name-flight-glib-gir
GObject introspection data for Apache Arrow Flight GLib.

%package flight-glib-doc
Summary: Documentation for Apache Arrow Flight GLib
Group: Development/Documentation
BuildArch: noarch

%description flight-glib-doc
Documentation for Apache Arrow Flight GLib.

%package -n lib%name-flight-glib-devel
Summary: Libraries and header files for Apache Arrow Flight GLib
Group: Development/C
Requires: lib%name-flight-glib = %EVR lib%name-flight-glib-gir = %EVR
Requires: lib%name-flight-devel = %EVR
Requires: lib%name-glib-devel = %EVR
Requires: gobject-introspection-devel

%description -n lib%name-flight-glib-devel
Libraries and header files for Apache Arrow Flight GLib.

%package -n lib%name-flight-sql-glib
Summary: Runtime libraries for Apache Arrow Flight SQL GLib
Group: System/Libraries
Requires: lib%name-flight-sql = %EVR
Requires: lib%name-flight-glib = %EVR

%description -n lib%name-flight-sql-glib
This package contains the libraries for Apache Arrow Flight SQL GLib.

%package -n lib%name-flight-sql-glib-gir
Summary: GObject introspection data for Apache Arrow Flight SQL GLib
Group: System/Libraries
Requires: lib%name-flight-sql-glib = %EVR

%description -n lib%name-flight-sql-glib-gir
GObject introspection data for Apache Arrow Flight SQL GLib.

%package -n lib%name-flight-sql-glib-devel
Summary: Libraries and header files for Apache Arrow Flight SQL GLib
Group: Development/C
Requires: lib%name-flight-sql-glib = %EVR lib%name-flight-sql-glib-gir = %EVR
Requires: lib%name-flight-sql-devel = %EVR
Requires: lib%name-flight-glib-devel = %EVR
Requires: gobject-introspection-devel

%description -n lib%name-flight-sql-glib-devel
Libraries and header files for Apache Arrow Flight SQL GLib.

%package flight-sql-glib-doc
Summary: Documentation for Apache Arrow Flight SQL GLib
Group: Development/Documentation
BuildArch: noarch

%description flight-sql-glib-doc
Documentation for Apache Arrow Flight SQL GLib.

%package -n libgandiva-glib
Summary: Runtime libraries for Gandiva GLib
Group: System/Libraries
Requires: lib%name-glib = %EVR
Requires: libgandiva = %EVR

%description -n libgandiva-glib
This package contains the libraries for Gandiva GLib.

%package -n libgandiva-glib-gir
Summary: GObject introspection data for Gandiva GLib
Group: System/Libraries
Requires: libgandiva-glib = %EVR

%description -n libgandiva-glib-gir
GObject introspection data for Gandiva GLib.

%package -n libgandiva-glib-devel
Summary: Libraries and header files for Gandiva GLib
Group: Development/C
Requires: lib%name-glib-devel = %EVR
Requires: libgandiva-glib = %EVR libgandiva-glib-gir = %EVR
Requires: libgandiva-devel = %EVR
Requires: gobject-introspection-devel

%description -n libgandiva-glib-devel
Libraries and header files for Gandiva GLib.

%package -n gandiva-glib-doc
Summary: Documentation for Gandiva GLib
Group: Development/Documentation
BuildArch: noarch

%description -n gandiva-glib-doc
Documentation for Gandiva GLib.

%package -n libparquet-glib
Summary: Runtime libraries for Apache Parquet GLib
Group: System/Libraries
Requires: lib%name-glib = %EVR
Requires: libparquet = %EVR

%description -n libparquet-glib
This package contains the libraries for Apache Parquet GLib.

%package -n libparquet-glib-gir
Summary: GObject introspection data for Apache Parquet GLib
Group: System/Libraries
Requires: libparquet-glib = %EVR

%description -n libparquet-glib-gir
GObject introspection data for Apache Parquet GLib.

%package -n libparquet-glib-devel
Summary: Libraries and header files for Apache Parquet GLib
Group: Development/C
Requires: lib%name-glib-devel = %EVR
Requires: libparquet-glib = %EVR libparquet-glib-gir = %EVR
Requires: libparquet-devel = %EVR
Requires: gobject-introspection-devel

%description -n libparquet-glib-devel
Libraries and header files for Apache Parquet GLib.

%package -n parquet-glib-doc
Summary: Documentation for Apache Parquet GLib
Group: Development/Documentation
BuildArch: noarch

%description -n parquet-glib-doc
Documentation for Apache Parquet GLib.

%package tools
Summary: Tools for Apache Arrow C++
Group: Development/Other
Requires: lib%name = %EVR

%description tools
Tools for Apache Arrow C++.

%package -n python3-module-pyarrow
Summary: Python library for Apache Arrow
Group: Development/Python3
%py3_provides pyarrow._cuda
%py3_provides pyarrow._orc
%py3_provides pyarrow._substrait

%description -n python3-module-pyarrow
Python library for Apache Arrow

%package -n python3-module-pyarrow-devel
Summary: Development files for python3-pyarrow
Group: Development/Python3
Requires: python3-module-pyarrow = %EVR

%description -n python3-module-pyarrow-devel
Development files for python3-pyarrow

%prep
%setup
%patch -p1
sed -r -i 's/(oldest-supported-)(numpy)/\2/' python/pyproject.toml

%build
pushd cpp
%cmake \
  -DCMAKE_CXX_STANDARD=17 \
  %{?_enable_flight:-DARROW_FLIGHT:BOOL=ON} \
  %{?_enable_flight_sql:-DARROW_FLIGHT_SQL:BOOL=ON} \
  %{?_enable_gandiva:-DARROW_GANDIVA:BOOL=ON} \
  %{?_enable_mimalloc:-DARROW_MIMALLOC:BOOL=ON} \
  %{?_enable_orc:-DARROW_ORC:BOOL=ON} \
  -DARROW_PARQUET:BOOL=ON \
  -DARROW_PYTHON:BOOL=ON \
  %{?_enable_utils:-DARROW_BUILD_UTILITIES:BOOL=ON} \
  -DARROW_JEMALLOC:BOOL=OFF \
  -DARROW_SIMD_LEVEL:STRING='NONE' \
  -Dxsimd_SOURCE="SYSTEM" \
  %{?_enable_s3:-DARROW_S3:BOOL=ON} \
  -DARROW_WITH_BROTLI:BOOL=ON \
  -DARROW_WITH_BZ2:BOOL=ON \
  -DARROW_WITH_LZ4:BOOL=ON \
  -DARROW_WITH_SNAPPY:BOOL=ON \
  -DARROW_WITH_ZLIB:BOOL=ON \
  -DARROW_WITH_ZSTD:BOOL=ON \
  -DARROW_USE_XSIMD:BOOL=ON \
  -DARROW_BUILD_STATIC:BOOL=OFF \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DARROW_GGDB_DEBUG=OFF \
  -DARROW_USE_CCACHE:BOOL=OFF \
  -DCMAKE_UNITY_BUILD:BOOL=ON \
  -DPARQUET_REQUIRE_ENCRYPTION:BOOL=ON \
  -DARROW_INSTALL_NAME_RPATH:BOOL=OFF \
  -GNinja

export VERBOSE=1
export GCC_COLORS=
%cmake_build
popd

pushd c_glib
%meson \
  -Darrow_cpp_build_dir=../cpp/%_cmake__builddir \
  -Darrow_cpp_build_type=relwithdebinfo \
  -Dgtk_doc=true \
  -Dvapi=true

%meson_build
popd

pushd cpp
DESTDIR="/tmp" %__cmake --install "%_cmake__builddir"
popd

pushd python
export \
  CMAKE_PREFIX_PATH=/tmp/usr \
  PYARROW_BUNDLE_ARROW_CPP_HEADERS=1 \
  PYARROW_BUNDLE_PLASMA_EXECUTABLE=0 \
  PYARROW_WITH_DATASET=1 \
  %{?_enable_flight:PYARROW_WITH_FLIGHT=1} \
  PYARROW_WITH_PARQUET=1 \
  %{?_enable_orc:PYARROW_WITH_ORC=1} \
  PYARROW_WITH_PARQUET_ENCRYPTION=1 \
  %{?_enable_gandiva:PYARROW_WITH_GANDIVA=1} \
  PYARROW_PARALLEL=%{_smp_build_ncpus} \
  ARROW_SIMD_LEVEL=NONE \
  PYARROW_INSTALL_TESTS=0
%pyproject_build
popd

%install

pushd python
export PYARROW_INSTALL_TESTS=0
%pyproject_install
popd

pushd c_glib
%meson_install
popd

pushd cpp
%cmake_install
popd

rm -rf %buildroot%_docdir/%name

%files -n lib%name
%_libdir/lib%name.so.*

%files devel
%doc README.md
%_includedir/arrow
%exclude %_includedir/arrow/dataset
%exclude %_includedir/arrow/acero
%if_enabled flight
%exclude %_includedir/arrow/flight
%exclude %_includedir/arrow-flight-glib
%endif
%dir %_libdir/cmake/Arrow
%_libdir/cmake/Arrow/Arrow*.cmake
%_libdir/cmake/Arrow/arrow*.cmake
%exclude %_libdir/cmake/Arrow/Find*
%_libdir/libarrow.so
%_pkgconfigdir/arrow-compute.pc
%_pkgconfigdir/arrow-csv.pc
%_pkgconfigdir/arrow-filesystem.pc
%_pkgconfigdir/arrow-json.pc
%if_enabled orc
%_pkgconfigdir/arrow-orc.pc
%endif
%_pkgconfigdir/arrow.pc
%_datadir/arrow
%_datadir/gdb/auto-load/%_libdir/libarrow.so.*-gdb.py

%if_enabled utils
%files tools
%_bindir/arrow-*
%endif

%files -n lib%name-acero
%_libdir/libarrow_acero.so.*

%files -n lib%name-acero-devel
%_includedir/arrow/acero
%_libdir/cmake/ArrowAcero
%_libdir/libarrow_acero.so
%_pkgconfigdir/arrow-acero.pc

%files -n lib%name-dataset
%_libdir/libarrow_dataset.so.*

%files -n lib%name-dataset-devel
%_includedir/arrow/dataset
%_libdir/cmake/ArrowDataset
%_libdir/libarrow_dataset.so
%_pkgconfigdir/arrow-dataset.pc

%if_enabled flight
%files -n lib%name-flight
%_libdir/libarrow_flight.so.*

%files -n lib%name-flight-devel
%_includedir/arrow/flight
%if_enabled flight_sql
%exclude %_includedir/arrow/flight/sql
%endif
%_libdir/cmake/ArrowFlight
%_libdir/libarrow_flight.so
%_pkgconfigdir/arrow-flight.pc

%if_enabled flight_sql
%files -n lib%name-flight-sql
%_libdir/libarrow_flight_sql.so.*

%files -n lib%name-flight-sql-devel
%_includedir/arrow/flight/sql
%_libdir/cmake/ArrowFlightSql
%_libdir/libarrow_flight_sql.so
%_pkgconfigdir/arrow-flight-sql.pc
%endif
%endif

%if_enabled gandiva
%files -n libgandiva
%_libdir/libgandiva.so.*

%files -n libgandiva-devel
%_includedir/gandiva
%_libdir/cmake/Gandiva
%_libdir/libgandiva.so
%_pkgconfigdir/gandiva.pc
%endif

%files -n libparquet
%_libdir/libparquet.so.*

%if_enabled utils
%files -n parquet-tools
%_bindir/parquet-*
%endif

%files -n libparquet-devel
%_includedir/parquet
%_libdir/cmake/Parquet
%_libdir/libparquet.so
%_pkgconfigdir/parquet.pc

%files -n lib%name-glib
%_libdir/libarrow-glib.so.*

%files -n lib%name-glib-gir
%_typelibdir/Arrow-*.typelib

%files -n lib%name-glib-devel
%_datadir/arrow-glib/example
%_girdir/Arrow-*.gir
%_vapidir/arrow-glib.*
%_includedir/arrow-glib
%_libdir/libarrow-glib.so
%_pkgconfigdir/arrow-glib.pc
%if_enabled orc
%_pkgconfigdir/arrow-orc-glib.pc
%endif

%files glib-doc
%_docdir/arrow-glib
%_datadir/gtk-doc/html/arrow-glib

%files -n lib%name-dataset-glib
%_libdir/libarrow-dataset-glib.so.*

%files -n lib%name-dataset-glib-gir
%_typelibdir/ArrowDataset-*.typelib

%files -n lib%name-dataset-glib-devel
%_girdir/ArrowDataset-*.gir
%_vapidir/arrow-dataset-glib.*
%_includedir/arrow-dataset-glib
%_libdir/libarrow-dataset-glib.so
%_pkgconfigdir/arrow-dataset-glib.pc

%files dataset-glib-doc
%_datadir/gtk-doc/html/arrow-dataset-glib

%if_enabled flight
%files -n lib%name-flight-glib
%_libdir/libarrow-flight-glib.so.*

%files -n lib%name-flight-glib-gir
%_typelibdir/ArrowFlight-*.typelib

%files -n lib%name-flight-glib-devel
%_girdir/ArrowFlight-*.gir
%_vapidir/arrow-flight-glib.*
%_includedir/arrow-flight-glib
%_libdir/libarrow-flight-glib.so
%_pkgconfigdir/arrow-flight-glib.pc

%files flight-glib-doc
%_datadir/gtk-doc/html/arrow-flight-glib

%if_enabled flight_sql
%files -n lib%name-flight-sql-glib
%_libdir/libarrow-flight-sql-glib.so.*

%files -n lib%name-flight-sql-glib-gir
%_typelibdir/ArrowFlightSQL-*.typelib

%files -n lib%name-flight-sql-glib-devel
%_girdir/ArrowFlightSQL-*.gir
%_vapidir/arrow-flight-sql-glib.*
%_includedir/arrow-flight-sql-glib
%_libdir/libarrow-flight-sql-glib.so
%_pkgconfigdir/arrow-flight-sql-glib.pc

%files flight-sql-glib-doc
%_datadir/gtk-doc/html/arrow-flight-sql-glib
%endif
%endif

%if_enabled gandiva
%files -n libgandiva-glib
%_libdir/libgandiva-glib.so.*

%files -n libgandiva-glib-gir
%_typelibdir/Gandiva-*.typelib

%files -n libgandiva-glib-devel
%_girdir/Gandiva-*.gir
%_vapidir/gandiva-glib.*
%_includedir/gandiva-glib
%_libdir/libgandiva-glib.so
%_pkgconfigdir/gandiva-glib.pc

%files -n gandiva-glib-doc
%_datadir/gtk-doc/html/gandiva-glib
%endif

%files -n libparquet-glib
%_libdir/libparquet-glib.so.*

%files -n libparquet-glib-gir
%_typelibdir/Parquet-*.typelib

%files -n libparquet-glib-devel
%_girdir/Parquet-*.gir
%_vapidir/parquet-glib.*
%_includedir/parquet-glib
%_libdir/libparquet-glib.so
%_pkgconfigdir/parquet-glib.pc

%files -n parquet-glib-doc
%_datadir/gtk-doc/html/parquet-glib

%files -n python3-module-pyarrow
%python3_sitelibdir/pyarrow
%python3_sitelibdir/pyarrow-*.dist-info
%exclude %python3_sitelibdir/pyarrow/lib_api.h
%exclude %python3_sitelibdir/pyarrow/include

%files -n python3-module-pyarrow-devel
%python3_sitelibdir/pyarrow/lib_api.h
%python3_sitelibdir/pyarrow/include

%changelog
* Sun Sep 24 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 12.0.0-alt2
- NMU: fixed FTBFS on LoongArch.

* Mon May 22 2023 Alexey Shabalin <shaba@altlinux.org> 12.0.0-alt1
- 12.0.0.

* Fri Apr 07 2023 Alexey Shabalin <shaba@altlinux.org> 11.0.0-alt1
- Initial build.

