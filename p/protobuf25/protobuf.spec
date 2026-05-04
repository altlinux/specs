%define oname protobuf
%define soversion 25

# Legacy package: ships only libprotobuf.so.* and libprotobuf-lite.so.*
# for consumers still linked against ABI 25. No compiler, no headers,
# no python/java/ruby bindings, no tests.

Name: %oname%soversion
Version: 3.25.5
Release: alt9
Summary: Protocol Buffers - Google's data interchange format (legacy ABI 25)
License: BSD-3-Clause
Group: System/Legacy libraries
Url: https://github.com/protocolbuffers/protobuf
Vcs: https://github.com/protocolbuffers/protobuf.git

# https://github.com/protocolbuffers/protobuf.git
Source: %oname-%version.tar
Patch: %oname-%version.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake rpm-build-cmake
BuildRequires: gcc-c++ zlib-devel libabseil-cpp-devel

%description
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format.

This is the legacy package providing libprotobuf.so.%soversion and
libprotobuf-lite.so.%soversion for applications still linked against
protobuf ABI %soversion.

%package -n lib%oname%soversion
Summary: Protocol Buffer c++ library (legacy ABI %soversion)
Group: System/Legacy libraries
Provides: libprotobuf = %EVR

%description -n lib%oname%soversion
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format.

Legacy runtime library (ABI %soversion).

%package -n lib%oname%soversion-lite
Summary: Protocol Buffers LITE_RUNTIME libraries (legacy ABI %soversion)
Group: System/Legacy libraries
Provides: libprotobuf-lite = %EVR

%description -n lib%oname%soversion-lite
Protocol Buffers built with optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

Legacy runtime library (ABI %soversion).

%prep
%setup -n %oname-%version
%patch -p1
%ifarch %e2k
sed -i '$a #ifdef __EDG__\n#undef PROTOBUF_CONSTINIT\n#define PROTOBUF_CONSTINIT\n#endif' \
	src/google/protobuf/port_def.inc
%endif

rm -f src/solaris/libstdc++.la

%build
%ifarch %e2k
# lcc 1.23: be explicit with C++11
%add_optflags -fno-error-always-inline -std=gnu++11
%endif

# Add LTO flags for libutf8_validity.a (static) that is needed
# for utf8_range.pc, that is, in turn, needed for protobuf.pc:
%add_optflags -ffat-lto-objects

iconv -f iso8859-1 -t utf-8 CONTRIBUTORS.txt > CONTRIBUTORS.txt.utf8
mv CONTRIBUTORS.txt.utf8 CONTRIBUTORS.txt

rm -f m4/{lt*,libtool*}.m4

export PTHREAD_LIBS="-lpthread"

%ifarch %ix86
  %add_optflags -D_M_IX86
%endif

%cmake -DCMAKE_CXX_STANDARD=17 \
       -Dprotobuf_BUILD_TESTS=OFF \
       -Dprotobuf_BUILD_SHARED_LIBS=ON \
       -Dprotobuf_ABSL_PROVIDER=package \
       -Dutf8_range_ENABLE_INSTALL=OFF
%cmake_build

%install
%cmakeinstall_std

%files -n lib%oname%soversion
%doc CONTRIBUTORS.txt README*
%_libdir/*.so.*
%exclude %_libdir/libprotobuf-lite.so.*

%files -n lib%oname%soversion-lite
%_libdir/libprotobuf-lite.so.*

%changelog
* Tue Apr 21 2026 Anton Farygin <rider@altlinux.org> 3.25.5-alt9
- legacy-only build: ship libprotobuf.so.%soversion and
  libprotobuf-lite.so.%soversion for ABI-%soversion consumers.
- dropped compiler, devel, python/java/ruby subpackages and tests.

* Fri Feb 27 2026 Evgeniy Serov <scala@altlinux.org> 3.25.5-alt8
- Fixed build with new guava.

* Wed Feb 11 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.25.5-alt7
- python bindings packaged elsewhere (closes: 55941)

* Wed Feb 26 2025 Paul Wolneykien <manowar@altlinux.org> 3.25.5-alt6
- Compile and provide utf8_range as a part of libprotobuf.so and
  libprotobuf-lite.so.

* Tue Feb 25 2025 Paul Wolneykien <manowar@altlinux.org> 3.25.5-alt5
- Fix: Make libprotobuf-devel libprotobuf-lite-devel.

* Thu Feb 13 2025 Paul Wolneykien <manowar@altlinux.org> 3.25.5-alt4
- Make libprotobuf-devel require lib%oname%soversion-lite and the
  protoc compiler (due to references in protobuf-targets-noconfig.cmake).

* Tue Feb 11 2025 Paul Wolneykien <manowar@altlinux.org> 3.25.5-alt3
- Make libprotobuf.so and libprotobuf-lite.so be an LD script
  (thx Gleb F.-M. for the idea).

* Thu Jan 30 2025 Paul Wolneykien <manowar@altlinux.org> 3.25.5-alt2
- Fixed building on i586.

* Wed Jan 22 2025 Paul Wolneykien <manowar@altlinux.org> 3.25.5-alt1
- New version 3.25.5 (Fixes: CVE-2024-7254).
- SO-version is now 25.5.0 (was 32.0.12).

* Fri Aug 02 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.21.12-alt5
- e2k: remove constinit to avoid compiler errors

* Mon Nov 27 2023 Ivan A. Melnikov <iv@altlinux.org> 3.21.12-alt4
- spec: added --without=ruby knob for bootstrap purposes (asheplyakov@);
- build w/o java tests on riscv64 and mipsel.

* Mon Aug 07 2023 Vitaly Lipatov <lav@altlinux.ru> 3.21.12-alt3
- drop unused BR: libnumpy-devel

* Thu Feb 16 2023 Alexey Shabalin <shaba@altlinux.org> 3.21.12-alt2
- fixed build with python 3.11

* Fri Dec 23 2022 Alexey Shabalin <shaba@altlinux.org> 3.21.12-alt1
- 3.21.12

* Wed Oct 19 2022 Alexey Shabalin <shaba@altlinux.org> 3.20.3-alt1
- 3.20.3

* Thu Aug 04 2022 Alexey Shabalin <shaba@altlinux.org> 3.20.1-alt1
- 3.20.1

* Thu Jun 02 2022 Pavel Skrylev <majioa@altlinux.org> 3.16.0-alt6.1
- !fix deps to rack-compiler gem

* Sat Nov 06 2021 Alexey Shabalin <shaba@altlinux.org> 3.16.0-alt6
- fixed FTBFS

* Mon Aug 16 2021 Pavel Skrylev <majioa@altlinux.org> 3.16.0-alt5.1
- + ruby gem packages support

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 3.16.0-alt5
- drop unused BR: python3-module-mox

* Tue Aug 03 2021 Andrew A. Vasilyev <andy@altlinux.org> 3.16.0-alt4
- drop unused BR: python3-module-pytz python3-module-gflags

* Sun Aug 01 2021 Vitaly Lipatov <lav@altlinux.ru> 3.16.0-alt3
- drop unused require google.apputils

* Sun Aug 01 2021 Vitaly Lipatov <lav@altlinux.ru> 3.16.0-alt2
- drop unused BR: python3-module-google-apputils

* Mon Jul 12 2021 Alexey Shabalin <shaba@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Jan 19 2021 Alexey Shabalin <shaba@altlinux.org> 3.14.0-alt1
- 3.14.0
- build without python2 module

* Fri Mar 13 2020 Alexey Shabalin <shaba@altlinux.org> 3.11.4-alt1
- 3.11.4

* Wed Apr 17 2019 Michael Shigorin <mike@altlinux.org> 3.6.1.3-alt2
- Fix ftbfs on e2k with lcc 1.23.

* Sun Mar 24 2019 Alexey Shabalin <shaba@altlinux.org> 3.6.1.3-alt1
- 3.6.1.3
- obsolete javanano subpackage; discontinued upstream

* Mon Dec 24 2018 Michael Shigorin <mike@altlinux.org> 3.5.2-alt2
- Skip *slow* IsValidUtf8Test on non-x86 platforms
  (very slow on arm/e2k, should be worse on mipsel,
  and maybe satisfactory/ok on ppc; known to pass)

* Mon May 28 2018 Mikhail Efremov <sem@altlinux.org> 3.5.2-alt1.E2K.1
- Disable test on e2k.
- Apply autogenerated patch.
- Use -fno-error-always-inline on e2k.
- Add missed function.
- Fix build on e2k.

* Thu May 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.2-alt1
- Updated to upstream version 3.5.2.
- Reworked spec.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Nov 06 2017 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt1
- New version 3.4.1 (Closes: 34120). Thanks Igor Vlasenko

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
