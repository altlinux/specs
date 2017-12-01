%def_disable tests

Name: libmongoc
Version: 1.8.2
Release: alt1%ubt
Summary: Client library written in C for MongoDB
Group: System/Libraries
License: ASL 2.0
Url: https://github.com/mongodb/mongo-c-driver
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-module-sphinx
BuildRequires: libbson-devel >= %version
BuildRequires: libssl-devel libsasl2-devel gcc-c++
BuildRequires: zlib-devel libsnappy-devel

%{?_enable_tests:BuildRequires: mongodb-server openssl}

%description
mongo-c-driver is a client library written in C for MongoDB.

%package devel
Group: Development/C
Summary: C Driver for MongoDB
Requires: %name = %EVR

%description devel
This package contains the header files and development libraries
for mongo-c-driver

%prep
%setup

%build
# Generate build scripts from sources
%autoreconf -I build/autotools
# delete bundled libbson sources
rm -rf src/libbson
%configure \
	--enable-shared \
	--disable-static \
	--disable-lto \
	--disable-maintainer-flags \
	--disable-optimizations \
	--disable-silent-rules \
	--enable-debug-symbols \
	--enable-shm-counters \
	--disable-automatic-init-and-cleanup \
	%{subst_enable tests} \
	--enable-sasl \
	--enable-ssl \
	--with-libbson=system \
	--with-snappy=system \
	--with-zlib=system \
	--disable-html-docs \
	--enable-man-pages


rm -rf src/zlib-*

%make_build all doc/man

%install
%makeinstall_std

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
#export MONGOC_TEST_SKIP_SLOW=on
make check || ret=1
# Cleanup
[ -s server.pid ] && kill $(cat server.pid)
exit $ret
%endif

%files
%doc COPYING NEWS *.md *.rst
%_bindir/*
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*

%changelog
* Fri Dec 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1%ubt
- 1.8.2

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20150310
- Version 1.1.2

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20140826
- Version 1.0.0

* Fri Mar 08 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.1-alt1
- Biuld fot ALT
