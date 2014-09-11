Name: libmongoc
Version: 1.0.0
Release: alt1.git20140826
Summary: C Driver for MongoDB
Group: System/Libraries
License: ASL 2.0
Url: https://github.com/mongodb/mongo-c-driver
Source: %name-%version.tar

BuildRequires: python-module-sphinx-devel doxygen yelp-tools
BuildPreReq: libbson-devel libssl-devel libsasl2-devel gcc-c++

%description
This is then 10gen-supported MongoDB C driver. There are two goals for
this driver.
The first is to provide a strict, default compilation option for
ultimate portability, no dependencies, and generic embeddability.
The second is to support more advanced, platform-specific features, like
socket timeout, by providing an interface for platform-specific modules.
Until the 1.0 release, this driver should be considered alpha. Keep in
mind that the API will be in flux until then.

%package devel
Group: Development/C
Summary: C Driver for MongoDB
%description devel
This is then 10gen-supported MongoDB C driver. There are two goals for
this driver.
The first is to provide a strict, default compilation option for
ultimate portability, no dependencies, and generic embeddability.
The second is to support more advanced, platform-specific features, like
socket timeout, by providing an interface for platform-specific modules.
Until the 1.0 release, this driver should be considered alpha. Keep in
mind that the API will be in flux until then.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-debug \
	--enable-optimizations \
	--enable-debug-symbols=yes \
	--enable-html-docs=yes \
	--enable-yelp=yes \
	--enable-examples=no \
	--enable-tests=yes \
	--enable-sasl=yes \
	--enable-ssl=yes
%make_build V=1
%make -C doc html

%install
%makeinstall_std

#check
#make test

%files
%doc COPYING NEWS *.md *.rst
%_libdir/*.so.*

%files devel
%doc doc/doc/html examples
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20140826
- Version 1.0.0

* Fri Mar 08 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.1-alt1
- Biuld fot ALT
