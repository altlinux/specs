%def_with java
%define soversion 9

Name: protobuf-compat
Version: 2.6.1
Release: alt2
Summary: Protocol Buffers - Google's data interchange format
License: Apache License 2.0
Group: System/Libraries
Url: http://code.google.com/p/protobuf/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Obsoletes: libprotobuf <= 2.0.0-alt1

# Automatically added by buildreq on Wed Nov 19 2008
BuildRequires: gcc-c++ python-devel libnumpy-devel zlib-devel

%description
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

Provides: libprotobuf = %version-%release

%package -n lib%name%soversion
Summary: Protocol Buffer c++ library.
Group: System/Libraries

%description -n lib%name%soversion
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package -n lib%name%soversion-lite
Summary: Protocol Buffers LITE_RUNTIME libraries
Group: System/Libraries
Provides: libprotobuf-lite = %version-%release

%description -n lib%name%soversion-lite
Protocol Buffers built with optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%prep
%setup -q
%patch -p1

# without gtest
rm -rf gtest

%build
iconv -f iso8859-1 -t utf-8 CONTRIBUTORS.txt > CONTRIBUTORS.txt.utf8
mv CONTRIBUTORS.txt.utf8 CONTRIBUTORS.txt

rm -f m4/{lt*,libtool*}.m4
export PTHREAD_LIBS="-lpthread"
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%python_sitelibdir/google/

%files -n lib%name%soversion
%doc CONTRIBUTORS.txt README* examples/
%_libdir/*.so.*
%exclude %_libdir/libprotobuf-lite.so.*

%files -n lib%name%soversion-lite
%_libdir/libprotobuf-lite.so.*

%changelog
* Mon Nov 06 2017 Anton Midyukov <antohami@altlinux.org> 2.6.1-alt2
- build only library package for compat and java package

* Mon Jun 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.1-alt1.2
- Fixed build with gcc-6

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.1-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.6.0-alt1.2
- NMU: java is built according to new policy (using xmvn)

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.6.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1
- Version 2.6.0
- Added module for Python 3

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt2
- NMU: added BuildReq: maven-local

* Fri Sep 06 2013 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt2
- added protobuf-java subpackage (required for maven dependencies)

* Thu Nov 24 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt1
- 2.4.1

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
