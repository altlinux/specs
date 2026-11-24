%define _unpackaged_files_terminate_build 1
%define abiversion %version

Name: thrift
Version: 0.25.0
Release: alt1

Summary: Software framework for cross-language services development
Group: Development/Other
License: Apache-2.0
URL: https://thrift.apache.org/
VCS: https://github.com/apache/thrift.git
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: thrift-installed-sdk-metadata.patch
Patch1: thrift-java-system-gradle.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-gradle
BuildRequires(pre): rpm-build-pyproject
BuildRequires: boost-locale-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: flex
BuildRequires: bison
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: libevent-devel
BuildRequires: libssl-devel
BuildRequires: python3-devel
%pyproject_builddeps_build
BuildRequires: qt5-base-devel
BuildRequires: zlib-devel
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(org.apiguardian:apiguardian-api)
BuildRequires: mvn(org.apache.httpcomponents.client5:httpclient5)
BuildRequires: mvn(org.apache.httpcomponents.core5:httpcore5)
BuildRequires: java-17-openjdk-devel
BuildRequires: mvn(jakarta.annotation:jakarta.annotation-api)
BuildRequires: mvn(jakarta.servlet:jakarta.servlet-api:5.0.0)
BuildRequires: mvn(org.junit.jupiter:junit-jupiter)
BuildRequires: mvn(org.junit.platform:junit-platform-launcher)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(org.slf4j:slf4j-simple)
BuildRequires: xgradle

%description
Apache Thrift combines a software stack with a code generation engine for
efficient cross-language services. This package contains the Thrift compiler.

%package -n libthrift%abiversion
Summary: Apache Thrift C++ runtime libraries
Group: System/Libraries

%description -n libthrift%abiversion
C++ protocol, transport and server libraries for Apache Thrift, including
nonblocking and zlib support.

%package -n libthrift_c_glib%abiversion
Summary: Apache Thrift GLib runtime libraries
Group: System/Libraries

%description -n libthrift_c_glib%abiversion
GLib protocol, transport and server libraries for Apache Thrift.

%package -n libthriftqt5_%abiversion
Summary: Apache Thrift Qt5 runtime library
Group: System/Libraries

%description -n libthriftqt5_%abiversion
Qt5 transport support for Apache Thrift.

%package -n libthrift-devel
Summary: Development files for Apache Thrift
Group: Development/C++
Requires: libthrift%abiversion = %EVR
Requires: %name = %EVR
Requires: qt5-base-devel
Provides: thrift-devel = %EVR
Obsoletes: thrift-devel < %EVR

%description -n libthrift-devel
Headers, linker files and build metadata for Apache Thrift C++, GLib and
Qt5 applications.

%package -n python3-module-%name
Group: Development/Python3
Summary: Python 3 support for %name

%description -n python3-module-thrift
The python3-%name package contains Python bindings for %name.

%package -n thrift-java
Summary: Apache Thrift Java runtime library
Group: Development/Java
BuildArch: noarch

%description -n thrift-java
Java protocols, transports and server APIs for Apache Thrift.

%prep
%setup
%autopatch -p1

pushd lib/py
%pyproject_deps_resync_build
popd

%build
%cmake \
  -DBUILD_COMPILER=ON \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_TESTING=OFF \
  -DWITH_JAVA=OFF \
  -DWITH_NODEJS=OFF \
  -DWITH_JAVASCRIPT=OFF \
  -DWITH_PYTHON=OFF \
  -DCMAKE_INSTALL_DIR=%_libdir/cmake \
  -DPKGCONFIG_INSTALL_DIR=%_pkgconfigdir \
  -GNinja
%cmake_build

pushd lib/py
%pyproject_build
popd

pushd lib/java
%gradle_publish -Prelease=true
popd

%install
%cmake_install
pushd lib/py
%pyproject_install
popd

pushd lib/java
%gradle_register --artifacts=libthrift
%gradle_install
popd

%check
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 -c \
    'import thrift.protocol.fastbinary as m; assert m.__file__.endswith(".so")'

thrift_compiler=$(realpath %_cmake__builddir/compiler/cpp/bin/thrift)
test -x "$thrift_compiler"
pushd lib/java
%gradle_check -Prelease=true -Pthrift.compiler="$thrift_compiler"
popd

%files
%doc LICENSE NOTICE
%_bindir/%name

%files -n libthrift%abiversion
%_libdir/libthrift.so.%abiversion
%_libdir/libthriftnb.so.%abiversion
%_libdir/libthriftz.so.%abiversion

%files -n libthrift_c_glib%abiversion
%_libdir/libthrift_c_glib.so.%abiversion
%_libdir/libthrift_c_glib_zlib.so.%abiversion

%files -n libthriftqt5_%abiversion
%_libdir/libthriftqt5.so.%abiversion

%files -n libthrift-devel
%_includedir/%name
%_libdir/libthrift*.so
%_pkgconfigdir/thrift*.pc
%_libdir/cmake/%name

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%{pyproject_distinfo thrift}

%files -n thrift-java -f lib/java/.mfiles

%changelog
* Mon Nov 23 2026 Ivan Khanas <xeno@altlinux.org> 0.25.0-alt1
- New version.
- Split the shared libraries by ABI.
- Package the Java runtime with upstream tests.

* Sun Jun 14 2026 Anton Midyukov <antohami@altlinux.org> 0.22.0-alt1
- 0.22.0.

* Wed Apr 12 2023 Alexey Shabalin <shaba@altlinux.org> 0.18.1-alt1
- 0.18.1
- switch to build with cmake
- not build perl module

* Wed Mar 15 2023 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt2
- fix build
- disable build libthriftnb.so
- cleanup spec
- ExcludeArch: armh

* Wed Jul 27 2022 Igor Vlasenko <viy@altlinux.org> 0.14.0-alt1_10
- new version

* Thu Apr 15 2021 Cronbuild Service <cronbuild@altlinux.org> 0.13.0-alt2_9
- rebuild to get rid of unmets

* Thu Oct 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.13.0-alt1_9
- new version

* Thu Oct 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt8_15jpp8
- fixed build with new java

* Sat Apr 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt7_15jpp8
- + lost binaries for ruby gem
- * rpm tags and syntax
- ! duplication file adding

* Mon Jul 08 2019 Alexey Shabalin <shaba@altlinux.org> 0.10.0-alt6_15jpp8
- build to Sisyphus

* Wed Mar 27 2019 Ivan A. Melnikov <iv@altlinux.org> 0.10.0-alt5_15jpp8.0.mips1
- build on mipsel
  + drop mono
  + fix linking with boost_atomic (debian patch)

* Tue Mar 19 2019 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt5_15jpp8
- Use Ruby Policy 2.0

* Sat Mar 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt4_15jpp8
- fixed build (closes: #36255)

* Sat Feb 02 2019 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt3_15jpp8
- fixed build

* Fri Dec 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_15jpp8
- build with new ssl

* Sat Jun 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_11jpp8
- java fc28+ update

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt2_9jpp8
- rebuild with tomcat9

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_9jpp8
- e2k support; java update

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.0-alt1_4jpp8
- new version

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_17.3jpp8
- cleaned up req on javapackages

* Tue Feb 23 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_16.4
- new version
- --without-haskell --without-csharp

* Mon Dec 13 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt3
- disable ruby module build

* Mon Nov 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt2
- name thrift jars properly

* Wed May 19 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0-alt1
- 0.3.0
- enable tests

* Mon Apr 05 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt1
- initial
