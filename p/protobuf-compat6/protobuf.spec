%define soversion 6

Name: protobuf-compat%{soversion}
Version: 2.3.0
Release: alt2
Summary: Protocol Buffers - Google's data interchange format
License: Apache License 2.0
Group: System/Libraries
Url: http://code.google.com/p/protobuf/
Packager: Mikhail A Pokidko <pma@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Obsoletes: libprotobuf < 2.3.0-alt2

# Automatically added by buildreq on Wed Nov 19 2008
BuildRequires: gcc-c++ python-devel libnumpy-devel zlib-devel

%description
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package -n lib%{name}
Summary: Protocol Buffer c++ library.
Group: System/Libraries
Provides: libprotobuf = %version-%release
Obsoletes: lib%{name}%{soversion}

%description -n lib%{name}
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package -n lib%{name}-lite
Summary: Protocol Buffers LITE_RUNTIME libraries
Group: System/Libraries
Provides: libprotobuf-lite = %version-%release
Obsoletes: lib%{name}%{soversion}-lite

%description -n lib%{name}-lite
Protocol Buffers built with optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%prep
%setup -q
%patch -p1
rm -rf java/src/test

# without gtest
rm -rf gtest

%build
rm -f m4/{lt*,libtool*}.m4
export PTHREAD_LIBS="-lpthread"
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files -n lib%{name}
%doc CONTRIBUTORS.txt README.txt examples/
%_libdir/*.so.*
%exclude %_libdir/libprotobuf-lite.so.*

%files -n lib%{name}-lite
%_libdir/libprotobuf-lite.so.*

%changelog
* Thu Nov 24 2011 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt2
- build only library package for compat

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.0-alt1.1.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.1
- Rebuilt for debuginfo

* Mon Sep 20 2010 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0
- changed soname

* Fri Apr 30 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.0a-alt1
- 2.2.0a
- changed soname
- added export PTHREAD_LIBS="-lpthread"
- add libprotobuf-lite subpackage

* Fri Apr 30 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Fri Feb 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.2
- Rebuild with reformed NumPy

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1.1
- Rebuilt with python 2.6

* Thu Jun 18 2009 Mikhail Pokidko <pma@altlinux.org> 2.1.0-alt1
- Version up. libprotobuf->libprotobuf4. Preparings for  java separation.

* Thu Jun 18 2009 Mikhail Pokidko <pma@altlinux.org> 2.0.2-alt2
- Fixed gcc4.4 build errors.

* Mon Nov 17 2008 Mikhail Pokidko <pma@altlinux.org> 2.0.2-alt1
- Building protobuf with new subpackages structure and with python binding

* Wed Jul 23 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Linux Sisyphus (2.0.0 beta)
