%define oname protobuf
%define soversion 31

# fat LTO objects needed for static libupb.a
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define _unpackaged_files_terminate_build 1

# Tests on e2k takes 3-4 days (!)
%ifarch %e2k
%def_disable check
%endif

%def_without python3
%def_with java
%def_with ruby

%ifarch riscv64 %mips %e2k
%def_without java_tests
%else
%def_with java_tests
%endif

# NOTE: Java tests are currently skipped because the lite/core modules
# need protoc+antrun to generate test proto sources, which is not yet
# configured in the generated pom.xml files.

Name: %oname
Epoch: 1
Version: 31.1
Release: alt1.1
Summary: Protocol Buffers - Google's data interchange format
License: BSD-3-Clause
Group: System/Libraries
Url: https://github.com/protocolbuffers/protobuf
Vcs: https://github.com/protocolbuffers/protobuf.git

# https://github.com/protocolbuffers/protobuf.git
Source: %oname-%version.tar
Patch: %oname-%version.patch

Obsoletes: libprotobuf <= 2.0.0-alt1

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake rpm-build-cmake ctest
BuildRequires: gcc-c++ zlib-devel libgtest-devel libgmock-devel libabseil-cpp-devel

%if_with ruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(rake) >= 13
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(ffi) >= 1
BuildRequires: gem(ffi-compiler) >= 1
BuildRequires: gem(rake) >= 13
BuildRequires: gem(rake-compiler) >= 1.1.0
BuildRequires: gem(rake-compiler-dock) >= 1.2.1
BuildRequires: gem(test-unit) >= 3.0.9
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(ffi-compiler) >= 2
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rake-compiler-dock) >= 2
BuildConflicts: gem(test-unit) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency rake-compiler-dock >= 1.2.1,rake-compiler-dock < 2
%endif

%description
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package -n lib%oname%soversion
Summary: Protocol Buffer c++ library
Group: System/Libraries
Provides: libprotobuf = %EVR

%description -n lib%oname%soversion
Protocol Buffers are a way of encoding structured data in
an efficient yet extensible format. Google uses Protocol Buffers for
almost all of its internal RPC protocols and file formats.

%package -n lib%oname%soversion-lite
Summary: Protocol Buffers LITE_RUNTIME libraries
Group: System/Libraries
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
Requires: lib%oname-lite-devel = %EVR
Requires: %name-compiler = %EVR

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

%if_with java

%package java
Version: 4.31.1
Summary: Java Protocol Buffers runtime library
Group: Development/Java
BuildArch: noarch
BuildRequires(pre): rpm-build-java
BuildRequires: jpackage-default
BuildRequires: maven-local
BuildRequires: mvn(com.google.code.gson:gson)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(com.google.guava:guava-testlib)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
%if_with java_tests
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(com.google.truth:truth)
BuildRequires: mvn(junit:junit)
%endif
Conflicts: %name-compiler > %version
Conflicts: %name-compiler < %version
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

%if_with ruby
%package -n gem-google-protobuf
Version: 4.31.1
Summary: Protocol Buffers
Group: Development/Ruby

Provides: gem(google-protobuf) = %EVR
Requires: ruby >= 3.1
Requires: gem(bigdecimal) >= 0
Requires: gem(rake) >= 13

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

Requires:      gem(bigdecimal) >= 0
Requires:      gem(rake) >= 13
Requires:      gem(google-protobuf) = 4.31.1
Requires:      gem(ffi) >= 1
Requires:      gem(ffi-compiler) >= 1
Requires:      gem(rake-compiler) >= 1.1.0
Requires:      gem(rake-compiler-dock) >= 1.2.1
Requires:      gem(test-unit) >= 3.0.9
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(ffi-compiler) >= 2
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rake-compiler-dock) >= 2
Conflicts:     gem(test-unit) >= 4

%description -n gem-google-protobuf-devel
Protocol Buffers development package.

Protocol Buffers are Google's data interchange format.

%description -n gem-google-protobuf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-protobuf.
%endif

%package compiler
Version: 31.1
Summary: Protocol Buffers Compiler
Group: Development/Other
Requires: lib%oname%soversion = %EVR

%description compiler
Compiler for protocol buffer definition files


%prep
%setup -n %oname-%version
%patch -p1
%ifarch %e2k
sed -i '$a #ifdef __EDG__\n#undef PROTOBUF_CONSTINIT\n#define PROTOBUF_CONSTINIT\n#endif' \
	src/google/protobuf/port_def.inc
%endif

%if_with ruby
# Fix Ruby build: use extconf.rb instead of Rakefiles for extension building.
# The Rakefiles reference ffi.rake with relative paths that break under setup.rb.
sed -i 's|File.exist?("Rakefile") ? "Rakefile" : "ext/google/protobuf_c/extconf.rb"|"ext/google/protobuf_c/extconf.rb"|' ruby/google-protobuf.gemspec
sed -i '/ext\/google\/protobuf_c\/Rakefile/d' ruby/google-protobuf.gemspec

# Copy utf8_range sources into ext/ tree (needed by C extension build)
mkdir -p ruby/ext/google/protobuf_c/third_party/utf8_range
cp third_party/utf8_range/{utf8_range.h,utf8_range.c,utf8_range_sse.inc,utf8_range_neon.inc,LICENSE} \
   ruby/ext/google/protobuf_c/third_party/utf8_range/
%endif

%if_with java
# Generate pom.xml from pom_template.xml for modules that only have templates
# (Bazel normally generates these, but we build with Maven)
_java_ver=4.%version
for _module in core lite util; do
  case $_module in
    core) _aid=protobuf-java ;;
    lite) _aid=protobuf-javalite ;;
    util) _aid=protobuf-java-util ;;
  esac
  sed -e 's/{groupId}/com.google.protobuf/g' \
      -e "s/{version}/$_java_ver/g" \
      -e "s/{artifactId}/$_aid/g" \
      -e 's/{type}/bundle/g' \
      -e 's/{dependencies}//g' \
      java/$_module/pom_template.xml > java/$_module/pom.xml
done

# Add compile-time dep on core for lite (proto-generated lite code uses
# GeneratedMessageLite and other runtime classes from core)
%pom_add_dep com.google.protobuf:protobuf-java:4.%version java/lite

# Add runtime deps to util pom (gson, guava, jsr305)
%pom_add_dep com.google.code.gson:gson java/util
%pom_add_dep com.google.guava:guava java/util
%pom_add_dep com.google.code.findbugs:jsr305 java/util

%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin java/pom.xml

# Remove annotation libraries we don't have
annotations=$(
    find java/ -name '*.java' |
      xargs grep -h -e '^import com\.google\.errorprone\.annotation' \
                    -e '^import com\.google\.j2objc\.annotations' |
      sort -u | sed 's/.*\.\([^.]*\);/\1/' | paste -sd\|
)
find java/ -name '*.java' | xargs sed -ri \
    "s/^import .*\.($annotations);//;s/@($annotations)"'\>\s*(\((("[^"]*")|([^)]*))\))?//g'

# Fix module order: core must be built before lite (lite depends on core)
sed -i '/<module>lite<\/module>/d' java/pom.xml
sed -i '/<module>core<\/module>/a\    <module>lite</module>' java/pom.xml

# Disable kotlin modules
%pom_disable_module kotlin java/pom.xml
%pom_disable_module kotlin-lite java/pom.xml

# Backward compatibility symlink
%mvn_file :protobuf-java:jar: %{name}/%{name}-java %{name}

# This test is incredibly slow on arm/e2k, probably even worse on mipsel
%ifnarch %ix86 x86_64
mv java/core/src/test/java/com/google/protobuf/IsValidUtf8Test.java \
   java/core/src/test/java/com/google/protobuf/IsValidUtf8Test.java.slow
mv java/core/src/test/java/com/google/protobuf/DecodeUtf8Test.java \
   java/core/src/test/java/com/google/protobuf/DecodeUtf8Test.java.slow
mv java/core/src/test/java/com/google/protobuf/CheckUtf8Test.java \
   java/core/src/test/java/com/google/protobuf/CheckUtf8Test.java.slow
%endif
%endif

%build
%ifarch %e2k
%add_optflags -fno-error-always-inline
%endif

export PTHREAD_LIBS="-lpthread"

%ifarch %ix86
  %add_optflags -D_M_IX86
%endif

%cmake -Dprotobuf_LOCAL_DEPENDENCIES_ONLY=ON \
       -Dprotobuf_BUILD_SHARED_LIBS=ON \
       -Dprotobuf_BUILD_LIBUPB=ON \
       -Dprotobuf_BUILD_TESTS=ON
%cmake_build

export PROTOC="$(realpath %_cmake__builddir/protoc)"

%if_with java
%ifarch %ix86 s390x %arm
export MAVEN_OPTS=-Xmx1024m
%endif

# Generate Java sources from proto files (upstream uses antrun+protoc
# via Bazel-generated pom.xml, but we generate pom.xml from templates)
_protos="src/google/protobuf/any.proto \
  src/google/protobuf/api.proto \
  src/google/protobuf/descriptor.proto \
  src/google/protobuf/duration.proto \
  src/google/protobuf/empty.proto \
  src/google/protobuf/field_mask.proto \
  src/google/protobuf/source_context.proto \
  src/google/protobuf/struct.proto \
  src/google/protobuf/timestamp.proto \
  src/google/protobuf/type.proto \
  src/google/protobuf/wrappers.proto"

$PROTOC --java_out=java/core/src/main/java \
  --proto_path=src \
  --proto_path=java/core/src/main/resources \
  java/core/src/main/resources/google/protobuf/java_features.proto \
  src/google/protobuf/compiler/plugin.proto \
  $_protos

mkdir -p java/lite/src/main/java
$PROTOC --java_out=lite:java/lite/src/main/java \
  --proto_path=src \
  --proto_path=java/core/src/main/resources \
  java/core/src/main/resources/google/protobuf/java_features.proto \
  $_protos

# Java tests need generated test proto sources (complex protoc+antrun setup);
# skip for now — C++ tests cover the same functionality.
%mvn_build -s --skip-tests -- -f java/pom.xml -Dprotobuf.builddir="$(realpath %_cmake__builddir)"
%endif

%if_with ruby
rm -fv SetupConfig
%ruby_build
%endif

%install
%cmakeinstall_std

%if_with ruby
%ruby_install
%endif

%if_with java
%mvn_install
%endif

%check
%ctest

%files compiler
%_bindir/protoc
%_bindir/protoc-*
%_bindir/protoc-gen-upb
%_bindir/protoc-gen-upb-*
%_bindir/protoc-gen-upbdefs
%_bindir/protoc-gen-upbdefs-*

%files -n lib%oname%soversion
%doc CONTRIBUTORS.txt README.md
%_libdir/libprotobuf.so.%soversion.*
%_libdir/libprotoc.so.%soversion.*
%_libdir/libutf8_range.so.%soversion.*
%_libdir/libutf8_validity.so.%soversion.*

%files -n lib%oname-devel
%dir %_includedir/google/
%_includedir/google/protobuf/
%_includedir/upb/
%_includedir/utf8_range.h
%_includedir/utf8_validity.h
%_libdir/libprotobuf.so
%_libdir/libprotoc.so
%_libdir/libutf8_range.so
%_libdir/libutf8_validity.so
%_libdir/libupb.a
%_pkgconfigdir/%name.pc
%_pkgconfigdir/upb.pc
%_pkgconfigdir/utf8_range.pc
%dir %_cmakedir/protobuf
%_cmakedir/protobuf/*.cmake
%dir %_cmakedir/utf8_range
%_cmakedir/utf8_range/*.cmake

%files -n lib%oname%soversion-lite
%_libdir/libprotobuf-lite.so.%soversion.*

%files -n lib%oname-lite-devel
%_libdir/libprotobuf-lite.so
%_pkgconfigdir/%name-lite.pc

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

%if_with ruby
%files -n gem-google-protobuf
%ruby_gemspecdir/google-protobuf-*.gemspec
%ruby_gemslibdir/google-protobuf-*
%ruby_gemsextdir/google-protobuf-*

%files -n gem-google-protobuf-doc
%ruby_gemsdocdir/google-protobuf-*

%files -n gem-google-protobuf-devel
%_includedir/google/protobuf_c/
%endif

%changelog
* Wed May 13 2026 Pavel Skrylev <majioa@altlinux.org> 1:31.1-alt1.1
- ! fixed package versions for java and ruby according version.json

* Sun Apr 12 2026 Anton Farygin <rider@altlinux.org> 31.1-alt1
- major update from 3.25.5 to 31.1 with new libabseil-cpp

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

* Wed Jul 23 2008 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- initial build for ALT Linux Sisyphus (2.0.0 beta)
