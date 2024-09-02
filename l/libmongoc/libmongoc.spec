%def_disable tests

Name: libmongoc
Version: 1.27.5
Release: alt1
Summary: Client library written in C for MongoDB
Group: System/Libraries
License: Apache-2.0 and ISC and MIT and Zlib
Url: https://github.com/mongodb/mongo-c-driver
Vcs: https://github.com/mongodb/mongo-c-driver.git
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake >= 3.15
BuildRequires: python3-module-sphinx
BuildRequires: libssl-devel libsasl2-devel libicu-devel
BuildRequires: zlib-devel libsnappy-devel libzstd-devel
BuildRequires: libutf8proc-devel
BuildRequires(pre): rpm-macros-cmake

%{?_enable_tests:BuildRequires: mongo-server-mongod openssl}

%description
mongo-c-driver is a client library written in C for MongoDB.

%package devel
Group: Development/C
Summary: C Driver for MongoDB
Requires: %name = %EVR

%description devel
This package contains the header files and development libraries
for mongo-c-driver

%package -n libbson
Group: System/Libraries
License: Apache-2.0
Summary: A BSON utility library

%description -n libbson
libbson is a library providing useful routines related to building,
parsing, and iterating BSON documents. It is a useful base for those
wanting to write high-performance C extensions to higher level languages
such as python, ruby, or perl.

%package -n libbson-devel
Summary: Development files of libbson
Group: Development/C
Requires: libbson = %EVR

%description -n libbson-devel
libbson is a library providing useful routines related to building,
parsing, and iterating BSON documents. It is a useful base for those
wanting to write high-performance C extensions to higher level languages
such as python, ruby, or perl.

This package contains development files of libbson.

%prep
%setup
sed -i 's|sphinx-build|sphinx-build-3|' build/cmake/FindSphinx.cmake

%build
%cmake \
    %_cmake_skip_rpath \
    -DBUILD_VERSION=%version \
    -DENABLE_STATIC:STRING=OFF \
    -DENABLE_MONGOC:BOOL=ON \
    -DENABLE_SHM_COUNTERS:BOOL=ON \
    -DENABLE_SSL:STRING=OPENSSL \
    -DENABLE_SASL:STRING=CYRUS \
    -DENABLE_ICU:STRING=ON \
    -DENABLE_AUTOMATIC_INIT_AND_CLEANUP:BOOL=OFF \
    -DENABLE_MONGODB_AWS_AUTH:STRING=ON \
    -DENABLE_CRYPTO_SYSTEM_PROFILE:BOOL=ON \
    -DENABLE_MAN_PAGES:BOOL=ON \
    -DENABLE_ZLIB:STRING=SYSTEM \
    -DENABLE_ZSTD:STRING=ON \
    -DENABLE_SNAPPY:STRING=ON \
    %{?_disable_tests:-DENABLE_TESTS:BOOL=OFF} \
    -DENABLE_UNINSTALL:BOOL=OFF \
    -DENABLE_EXAMPLES:BOOL=OFF \
    -DUSE_BUNDLED_UTF8PROC:BOOL=OFF \
    -DENABLE_SRV:BOOL=ON

%cmake_build

%install
%cmake_install

%check
%if_enabled tests
# Run a server
mkdir dbtest
mongod \
  --journal \
  --unixSocketPrefix /tmp \
  --logpath     $PWD/server.log \
  --pidfilepath $PWD/server.pid \
  --dbpath      $PWD/dbtest \
  --fork
# Run the test suite
ret=0
export MONGOC_TEST_OFFLINE=on
export MONGOC_TEST_SKIP_MOCK=on
#export MONGOC_TEST_SKIP_SLOW=on
make check || ret=1
# Cleanup
[ -s server.pid ] && kill $(cat server.pid)
exit $ret
%endif

%files
%doc COPYING NEWS *.md *.rst
%_bindir/*
%_libdir/libmongoc*.so.*
%_datadir/mongo-c-driver

%files devel
%_includedir/libmongoc*
%_libdir/libmongoc*.so
%_pkgconfigdir/libmongoc*.pc
%_man3dir/mongoc*
%_libdir/cmake/libmongoc*
%_libdir/cmake/mongoc*

%files -n libbson
%doc NEWS README.rst
%_libdir/libbson*.so.*

%files -n libbson-devel
%_includedir/libbson*
%_libdir/libbson*.so
%_pkgconfigdir/libbson*.pc
%_man3dir/bson*
%_libdir/cmake/libbson*
%_libdir/cmake/bson*


%changelog
* Mon Sep 02 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.27.5-alt1
- 1.27.5

* Fri Jul 05 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.27.4-alt1
- 1.27.4

* Thu Jun 06 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.27.2-alt1
- 1.27.2

* Fri May 03 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.27.0-alt1
- 1.27.0

* Sun Apr 28 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.26.2-alt1
- 1.26.2

* Thu Mar 07 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.26.1-alt1
- 1.26.1

* Fri Jan 19 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.25.4-alt1
- 1.25.4

* Wed Dec 27 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.25.3-alt1
- 1.25.3

* Wed Sep 06 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.24.4-alt1
- 1.24.4

* Mon Aug 14 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.24.3-alt1
- 1.24.3

* Mon Jul 17 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.24.2-alt1
- 1.24.2

* Thu Jun 22 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.24.1-alt1
- 1.24.1

* Wed Jun 21 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.24.0-alt1
- 1.24.0

* Thu Jun 08 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.23.5-alt1
- 1.23.5

* Wed May 10 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.23.4-alt1
- 1.23.4

* Wed Apr 05 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.23.3-alt1
- 1.23.3

* Thu Jan 12 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.23.2-alt1
- 1.23.2

* Wed Nov 02 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.23.1-alt1
- 1.23.1

* Thu Sep 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.23.0-alt1
- 1.23.0

* Mon Aug 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.22.1-alt1
- 1.22.1

* Thu Jun 30 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.22.0-alt1
- 1.22.0

* Wed Jun 08 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.21.2-alt1
- 1.21.2

* Thu Mar 03 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.21.1-alt1
- 1.21.1

* Wed Feb 02 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.21.0-alt1
- 1.21.0

* Tue Jan 11 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.20.1-alt1
- 1.20.1

* Wed Nov 24 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.20.0-alt1
- 1.20.0

* Mon Nov 15 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.19.2-alt1
- 1.19.2

* Mon Oct 11 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.19.1-alt1
- 1.19.1

* Mon Sep 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.19.0-alt1
- 1.19.0

* Tue Aug 03 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.18.0-alt1
- 1.18.0

* Mon Aug 02 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.14.0-alt1.2
- NMU: fix FTBFS (sphinx).

* Tue Jun 01 2021 Arseny Maslennikov <arseny@altlinux.org> 1.14.0-alt1.1
- NMU: spec: adapt to new cmake macros.

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 1.14.0-alt1
- 1.14.0

* Tue Sep 04 2018 Alexey Shabalin <shaba@altlinux.org> 1.12.0-alt1
- 1.12.0

* Fri Mar 09 2018 Alexey Shabalin <shaba@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Tue Feb 13 2018 Alexey Shabalin <shaba@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Fri Dec 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20150310
- Version 1.1.2

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20140826
- Version 1.0.0

* Fri Mar 08 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.1-alt1
- Build fot ALT
