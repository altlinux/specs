%define oname protobuf
%define soversion 32

# set 'enable' to build legacy package
%def_disable legacy

%if_disabled legacy
%define _unpackaged_files_terminate_build 1

# Tests on e2k takes 3-4 days (!)
%ifarch %e2k
%def_disable check
%endif

# normal package may include python3 or java support
%def_with python3
%def_with java
%else
# for legacy package python3 and java should always be disabled since it's not packed anyway
%def_without python3
%def_without java
%endif

%if_disabled legacy
Name: %oname
%else
Name: %oname%soversion
%endif
Version: 3.21.12
Release: alt2
Summary: Protocol Buffers - Google's data interchange format
License: BSD-3-Clause
%if_disabled legacy
Group: System/Libraries
%else
Group: System/Legacy libraries
%endif
Url: https://github.com/protocolbuffers/protobuf
Vcs: https://github.com/protocolbuffers/protobuf.git

# https://github.com/protocolbuffers/protobuf.git
Source: %oname-%version.tar
Patch: %oname-%version.patch

Obsoletes: libprotobuf <= 2.0.0-alt1

# Automatically added by buildreq on Wed Nov 19 2008
BuildRequires: gcc-c++ libnumpy-devel zlib-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel
BuildRequires: python3-module-setuptools python-tools-2to3
BuildRequires: python3-module-dateutil
%endif
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake-compiler-dock) >= 1.1.0 gem(rake-compiler-dock) < 2
BuildRequires: gem(rake-compiler) >= 1.1.0 gem(rake-compiler) < 2
BuildRequires: gem(test-unit) >= 3.0 gem(test-unit) < 4

%ruby_use_gem_dependency rake-compiler >= 1.1.0,rake-compiler < 2
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package compiler
Summary: Protocol Buffers Compiler
Group: Development/Other
Requires: lib%oname%soversion = %EVR

%description compiler
Compiler for protocol buffer definition files

%package -n lib%oname%soversion
Summary: Protocol Buffer c++ library
%if_disabled legacy
Group: System/Libraries
%else
Group: System/Legacy libraries
%endif

Provides: libprotobuf = %EVR

%description -n lib%oname%soversion
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package -n lib%oname%soversion-lite
Summary: Protocol Buffers LITE_RUNTIME libraries
%if_disabled legacy
Group: System/Libraries
%else
Group: System/Legacy libraries
%endif
Provides: libprotobuf-lite = %EVR

%description -n lib%oname%soversion-lite
Protocol Buffers built with optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%package -n lib%oname-devel
Summary: Development files for %oname
Group: Development/C
Requires: lib%oname%soversion = %EVR

%description -n lib%oname-devel
This package contains development files required for packaging
%oname.

%package -n lib%oname-lite-devel
Summary: Protocol Buffers LITE_RUNTIME development libraries
Group: Development/C
Requires: lib%oname%soversion-lite = %EVR
Requires: lib%oname-devel = %EVR

%description -n lib%oname-lite-devel
This package contains development libraries built with
optimize_for = LITE_RUNTIME.

The "optimize_for = LITE_RUNTIME" option causes the compiler to generate code
which only depends libprotobuf-lite, which is much smaller than libprotobuf but
lacks descriptors, reflection, and some other features.

%package -n python3-module-%oname
Summary: Python module files for %oname
Group: Development/Python3
Requires: lib%oname%soversion = %EVR
Conflicts: %name-compiler > %version
Conflicts: %name-compiler < %version

%description -n python3-module-%oname
Python bindings for protocol buffers

%if_with java
%package java
Summary: Java Protocol Buffers runtime library
Group: Development/Java
BuildArch:      noarch
BuildRequires:  /proc
BuildRequires:  jpackage-default
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(com.google.guava:guava-testlib)
BuildRequires:  mvn(com.google.truth:truth)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires(pre):  rpm-build-java
BuildRequires:  libgmock-devel libgtest-devel
Conflicts: %name-compiler > %version
Conflicts: %name-compiler < %version
Obsoletes: %name-javanano < 3.6.0
# remove when xmvn will be patched to not insert this dep automatically
%filter_from_requires /^java-headless/d

%description java
This package contains Java Protocol Buffers runtime library.

%package javalite
Summary: Java Protocol Buffers lite runtime library
Group: Development/Java
BuildArch: noarch

%description javalite
This package contains Java Protocol Buffers lite runtime library.

%package javadoc
Summary: Javadocs for %oname-java
Group: Development/Documentation
BuildArch: noarch
Requires: %name-java = %EVR

%description javadoc
This package contains the API documentation for %oname-java.

%package java-util
Summary: Utilities for Protocol Buffers
Group: Development/Java
BuildArch: noarch

%description java-util
Utilities to work with protos. It contains JSON support
as well as utilities to work with proto3 well-known types.

%package parent
Summary: Protocol Buffer Parent POM
Group: Development/Java
BuildArch: noarch

%description parent
Protocol Buffer Parent POM.

%package bom
Summary: Protocol Buffer BOM POM
Group: Development/Java
BuildArch: noarch

%description bom
Protocol Buffer BOM POM.
%endif


%package -n gem-google-protobuf
Summary: Protocol Buffers
Group: Development/Ruby

Provides: gem(google-protobuf) = %EVR

%description -n gem-google-protobuf
Protocol Buffers are Google's data interchange format.

%package -n gem-google-protobuf-doc
Summary: Protocol Buffers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-protobuf
Group: Development/Documentation
BuildArch: noarch

Requires: gem(google-protobuf) = %EVR

%description -n gem-google-protobuf-doc
Protocol Buffers documentation files.

Protocol Buffers are Google's data interchange format.

%description -n gem-google-protobuf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-protobuf.

%package -n gem-google-protobuf-devel
Summary: Protocol Buffers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-protobuf
Group: Development/Ruby
BuildArch: noarch

Requires: gem(google-protobuf) = %EVR
Requires: gem(rake-compiler-dock) >= 1.1.0 gem(rake-compiler-dock) < 2
Requires: gem(rake-compiler) >= 1.1.0 gem(rake-compiler) < 2
Requires: gem(test-unit) >= 3.0 gem(test-unit) < 4

%description -n gem-google-protobuf-devel
Protocol Buffers development package.

Protocol Buffers are Google's data interchange format.

%description -n gem-google-protobuf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-protobuf.

%prep
%setup -n %oname-%version
%patch -p1

%if_with java
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin java/util/pom.xml java/pom.xml
%pom_remove_dep com.google.errorprone:error_prone_annotations java/util/pom.xml
%pom_remove_dep com.google.j2objc:j2objc-annotations java/util/pom.xml

# Remove annotation libraries we don't have
annotations=$(
    find -name '*.java' |
      xargs grep -h -e '^import com\.google\.errorprone\.annotation' \
                    -e '^import com\.google\.j2objc\.annotations' |
      sort -u | sed 's/.*\.\([^.]*\);/\1/' | paste -sd\|
)
find -name '*.java' | xargs sed -ri \
    "s/^import .*\.($annotations);//;s/@($annotations)"'\>\s*(\((("[^"]*")|([^)]*))\))?//g'

# These use easymockclassextension
rm java/core/src/test/java/com/google/protobuf/ServiceTest.java
# These use truth or error_prone_annotations or guava-testlib
rm java/core/src/test/java/com/google/protobuf/LiteralByteStringTest.java
rm java/core/src/test/java/com/google/protobuf/BoundedByteStringTest.java
rm java/core/src/test/java/com/google/protobuf/RopeByteStringTest.java
rm java/core/src/test/java/com/google/protobuf/RopeByteStringSubstringTest.java
rm java/core/src/test/java/com/google/protobuf/TextFormatTest.java
rm -r java/util/src/test/java/com/google/protobuf/util
rm -r java/util/src/main/java/com/google/protobuf/util
 
# Make OSGi dependency on sun.misc package optional
%pom_xpath_inject "pom:configuration/pom:instructions" "<Import-Package>sun.misc;resolution:=optional,*</Import-Package>" java/core
 
# Backward compatibility symlink
%mvn_file :protobuf-java:jar: %{name}/%{name}-java %{name}

# This test is incredibly slow on arm/e2k, probably even worse on mipsel
# https://github.com/google/protobuf/issues/2389
%ifnarch %ix86 x86_64
mv java/core/src/test/java/com/google/protobuf/IsValidUtf8Test.java \
   java/core/src/test/java/com/google/protobuf/IsValidUtf8Test.java.slow
mv java/core/src/test/java/com/google/protobuf/DecodeUtf8Test.java \
   java/core/src/test/java/com/google/protobuf/DecodeUtf8Test.java.slow

mv java/core/src/test/java/com/google/protobuf/CheckUtf8Test.java \
   java/core/src/test/java/com/google/protobuf/CheckUtf8Test.java.slow
mv java/core/src/test/java/com/google/protobuf/Proto3SchemaTest.java \
   java/core/src/test/java/com/google/protobuf/Proto3SchemaTest.java.slow
mv java/core/src/test/java/com/google/protobuf/Proto3LiteSchemaTest.java \
   java/core/src/test/java/com/google/protobuf/Proto3LiteSchemaTest.java.slow
%endif
%endif

rm -f src/solaris/libstdc++.la

%build
%ifarch %e2k
# lcc 1.23: be explicit with C++11
%add_optflags -fno-error-always-inline -std=gnu++11
%endif

iconv -f iso8859-1 -t utf-8 CONTRIBUTORS.txt > CONTRIBUTORS.txt.utf8
mv CONTRIBUTORS.txt.utf8 CONTRIBUTORS.txt

rm -f m4/{lt*,libtool*}.m4
export PTHREAD_LIBS="-lpthread"
%autoreconf
%configure \
	--disable-static \
	--localstatedir=%_var \

%make_build
%make_build CXXFLAGS="-Wno-error=type-limits"

%if_with python3
pushd python
%python3_build --cpp_implementation
popd
%endif

%if_with java
%ifarch %ix86 s390x %arm
export MAVEN_OPTS=-Xmx1024m
%endif
%pom_disable_module kotlin java/pom.xml
%pom_disable_module kotlin-lite java/pom.xml
%mvn_build -s -- -f java/pom.xml
%endif

%ruby_build

%install
%makeinstall_std
%ruby_install

%if_with python3
pushd python
%python3_install --cpp_implementation
popd
%endif

%if_with java
%mvn_install
%endif

%if_disabled legacy
%files compiler
%_bindir/protoc
%endif

%files -n lib%oname%soversion
%doc CONTRIBUTORS.txt README* examples/
%_libdir/*.so.*
%exclude %_libdir/libprotobuf-lite.so.*

%if_disabled legacy
%files -n lib%oname-devel
%dir %_includedir/google/
%_includedir/google/protobuf/
%_pkgconfigdir/protobuf.pc
%_libdir/*.so
%exclude %_libdir/libprotobuf-lite.so
%endif

%files -n lib%oname%soversion-lite
%_libdir/libprotobuf-lite.so.*

%if_disabled legacy
%files -n lib%oname-lite-devel
%_libdir/libprotobuf-lite.so
%_pkgconfigdir/protobuf-lite.pc

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%if_with java
%files java -f .mfiles-protobuf-java
%doc examples/AddPerson.java examples/ListPeople.java
%doc java/README.md
%doc LICENSE

%files java-util -f .mfiles-protobuf-java-util

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%files parent -f .mfiles-protobuf-parent
%doc LICENSE

%files bom -f .mfiles-protobuf-bom
%doc LICENSE

%files javalite -f .mfiles-protobuf-javalite
%doc LICENSE
%endif
%endif

%files -n gem-google-protobuf
%ruby_gemspecdir/google-protobuf-*.gemspec
%ruby_gemslibdir/google-protobuf-*
%ruby_gemsextdir/google-protobuf-*

%files -n gem-google-protobuf-doc
%ruby_gemsdocdir/google-protobuf-*

%files -n gem-google-protobuf-devel
%_includedir/google/protobuf_c/


%changelog
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

* Wed Jul 23 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Linux Sisyphus (2.0.0 beta)
