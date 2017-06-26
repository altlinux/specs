# find-requires: message.h:112:18: fatal error: vector: No such file or directory
%add_findreq_skiplist /usr/include/google/protobuf/message.h
%add_findprov_skiplist /usr/include/google/protobuf/message.h

%define soversion 7
%define _name protobuf

Name: %{_name}-compat%{soversion}
Version: 2.4.1
Release: alt5
Summary: Protocol Buffers - Google's data interchange format
License: Apache License 2.0
Group: System/Libraries
Url: http://code.google.com/p/protobuf/
Packager: Mikhail A Pokidko <pma@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch2: protobuf-2.4.1-java-fixes.patch
Patch3: protobuf-alt-build.patch

# Automatically added by buildreq on Wed Nov 19 2008
BuildRequires: gcc-c++ python-devel libnumpy-devel zlib-devel

%description
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package -n lib%{_name}%{soversion}
Summary: Protocol Buffer c++ library.
Group: System/Libraries

Provides: libprotobuf = %version-%release
Provides: libprotobuf-compat77 = %version-%release
Obsoletes: libprotobuf-compat77 < %version-%release

%description -n lib%{_name}%{soversion}
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package -n lib%{_name}%{soversion}-lite
Summary: Protocol Buffers LITE_RUNTIME libraries
Group: System/Libraries
Provides: libprotobuf-lite = %version-%release
Provides: libprotobuf-compat77-lite = %version-%release
Obsoletes: libprotobuf-compat77-lite < %version-%release

%description -n lib%{_name}%{soversion}-lite
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

%if_with java
%patch2 -p1 -b .java-fixes
rm -rf java/src/test
%endif

%patch3 -p1

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

%files -n lib%{_name}%{soversion}
%doc CONTRIBUTORS.txt README.txt examples/
%_libdir/*.so.*
%exclude %_libdir/libprotobuf-lite.so.*

%files -n lib%{_name}%{soversion}-lite
%_libdir/libprotobuf-lite.so.*

%changelog
* Mon Jun 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.1-alt5
- Fixed build with gcc-6

* Thu Jul 31 2014 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt4
- fixed package name

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 2.4.1-alt3
- build only library package for compat

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
