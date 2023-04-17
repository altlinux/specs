%define _unpackaged_files_terminate_build 1

Name: thrift
Version: 0.18.1
Release: alt1
Summary: Software framework for cross-language services development
Group: Development/Other
License: Apache-2.0
Url: https://thrift.apache.org/
Source: %name-%version.tar
Patch0001: 0001-fix-install-thrift_c_glibpc.patch

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel boost-locale-devel
BuildRequires: cmake ninja-build flex
BuildRequires: gcc-c++
BuildRequires: glib2-devel libgio-devel
BuildRequires: libevent-devel
BuildRequires: libssl-devel
BuildRequires: qt5-base-devel
BuildRequires: zlib-devel

Provides: lib%name = %EVR

%description
The Apache Thrift software framework for cross-language services
development combines a software stack with a code generation engine to
build services that work efficiently and seamlessly between C++, Java,
Python, %{?php_langname}and other languages.

%package devel
Group: Development/C++
Summary: Development files for %name
Provides: lib%name-devel = %EVR
Requires: %name = %EVR
#Requires: boost-complete

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package qt5
Group: Development/Other
Summary: Qt5 support for %name
Requires: %name = %EVR

%description qt5
The %name-qt package contains Qt bindings for %name.

%package glib
Group: Development/Other
Summary: GLib support for %name
Requires: %name = %EVR

%description glib
The %name-qt package contains GLib bindings for %name.

%package -n python3-module-%name
Group: Development/Python3
Summary: Python 3 support for %name
BuildRequires: python3-devel
BuildRequires: python3-module-pkg_resources python3-module-setuptools
Requires: %name = %EVR

%description -n python3-module-thrift
The python3-%name package contains Python bindings for %name.

%prep
%setup
%patch0001 -p1

%build
export PYTHON=%__python3
%cmake \
  -DBUILD_COMPILER=ON \
  -DBUILD_SHARED_LIBS=ON \
  -DWITH_NODEJS=OFF \
  -DWITH_JAVASCRIPT=OFF \
  -DBUILD_PYTHON=ON \
  -DCMAKE_INSTALL_DIR=%_libdir/cmake \
  -DPKGCONFIG_INSTALL_DIR=%_pkgconfigdir \
  -GNinja
%cmake_build

%install
%cmake_install
#fix cmake
sed -i 's|/usr//usr|%_prefix|g' %buildroot%_libdir/cmake/thrift/ThriftConfig.cmake
pushd lib/py
%python3_install
popd

%files
%doc LICENSE NOTICE
%_bindir/%name
%_libdir/libthrift.so.*
%_libdir/libthriftnb.so.*
%_libdir/libthriftz.so.*

%files glib
%_libdir/libthrift_c_glib*.so.*

%files qt5
%_libdir/libthriftqt5.so.*

%files devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*
%_libdir/cmake/%name
%doc NOTICE

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%version-py*.egg-info

%changelog
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
