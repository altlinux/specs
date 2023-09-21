# a hack: should be fixed
%def_without doc
%define _cmake_skip_rpath -DCMAKE_SKIP_RPATH:BOOL=OFF

Name: qpid-proton
Version: 0.36.0
Release: alt2
Summary: A high performance, lightweight messaging library
Group: System/Libraries

License: Apache-2.0
Url: http://qpid.apache.org/proton/

%define proton_datadir %_datadir/proton

Source: %name-%version.tar

BuildRequires: cmake >= 2.8.12
BuildRequires: gcc-c++
BuildRequires: swig
BuildRequires: doxygen
BuildRequires: libuuid-devel
BuildRequires: libuv-devel
BuildRequires: jsoncpp-devel
BuildRequires: libssl-devel
BuildRequires: libsasl2-devel
BuildRequires: python3-module-setuptools
BuildRequires(pre): rpm-build-python3

%description
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

%package -n lib%name
Summary: C libraries for Qpid Proton
Group: System/Libraries

%description -n lib%name
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

C libraries for Qpid Proton

%package -n lib%name-devel
Requires: lib%name = %version-%release
Summary: Development libraries for writing messaging apps with Qpid Proton
Group: Development/C

%description -n lib%name-devel
Development libraries for writing messaging apps with Qpid Proton

%package -n lib%name-cpp
Summary: C++ libraries for Qpid Proton
Group: Development/C++

%description -n lib%name-cpp
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

C++ libraries for Qpid Proton

%package -n lib%name-cpp-devel
Summary: Development libraries for writing messaging apps with Qpid Proton
Group: Development/C++
Requires: lib%name-cpp = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-cpp-devel
Development libraries for writing messaging apps with Qpid Proton

%package -n python3-module-qpid-proton
Summary: Python3 language bindings for the Qpid Proton messaging framework
Group: Development/Python3
Requires: lib%name = %version-%release

%description -n python3-module-qpid-proton
Python3 language bindings for the Qpid Proton messaging framework

%package  -n lib%name-devel-doc
Summary: Documentation for the C development libraries for Qpid Proton
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
Documentation for the C development libraries for Qpid Proton

%package -n python3-module-qpid-proton-doc
Summary: Documentation for the Python language bindings for Qpid Proton
Group: Development/Documentation
BuildArch: noarch

%description -n python3-module-qpid-proton-doc
Documentation for the Python language bindings for Qpid Proton

%prep
%setup

%build
#%%add_optflags -Wno-error=return-type -Wno-error=format-security

%cmake \
    -DPYTHON_SITEARCH_PACKAGES=%python3_sitelibdir \
    -DSYSINSTALL_BINDINGS=ON \
    -DENABLE_FUZZ_TESTING=NO \
    -DPYTHON_EXECUTABLE=%__python3 \
    -DPYTHON_INCLUDE_DIR=%python3_includedir \
    "-DCMAKE_C_FLAGS=$CFLAGS -Wno-deprecated-declarations" \
    -DPYTHON_LIBRARY=%__libpython3

%cmake_build --target generated_c_files
%cmake_build

(cd %_cmake__builddir/python/dist; %python3_build)

%install
%cmake_install
(cd %_cmake__builddir/python/dist; %python3_install)

find %buildroot%proton_datadir/examples/python -name "*.py" -exec sed -i 's/!\/usr\/bin\/env python/!\/usr\/bin\/python3/' {} \;
#sed -i 's/!\/usr\/bin\/python/!\/usr\/bin\/python3/' %buildroot%proton_datadir/examples/c/testme
#sed -i 's/!\/usr\/bin\/python/!\/usr\/bin\/python3/' %buildroot%proton_datadir/examples/cpp/testme
echo '#!/usr/bin/python3' > %buildroot%proton_datadir/examples/python/proton_server.py.original
cat %buildroot%proton_datadir/examples/python/proton_server.py >> %buildroot%proton_datadir/examples/python/proton_server.py.original
mv %buildroot%proton_datadir/examples/python/proton_server.py.original %buildroot%proton_datadir/examples/python/proton_server.py

mkdir -p %buildroot%_defaultdocdir/%name-%version
mv %buildroot%proton_datadir/examples %buildroot%_defaultdocdir/%name-%version/

# cleanup
rm -rf %buildroot%proton_datadir/tests
rm -rf %buildroot%proton_datadir/CMakeLists.txt

%files -n lib%name
%dir %proton_datadir
%doc %proton_datadir/LICENSE.txt
%doc %proton_datadir/README*
%_libdir/libqpid-proton.so.*
%_libdir/libqpid-proton-core.so.*
%_libdir/libqpid-proton-proactor.so.*

%files -n lib%name-devel
%_includedir/proton
%_libdir/libqpid-proton.so
%_libdir/libqpid-proton-core.so
%_libdir/libqpid-proton-proactor.so
%_pkgconfigdir/libqpid-proton.pc
%_pkgconfigdir/libqpid-proton-core.pc
%_pkgconfigdir/libqpid-proton-proactor.pc
%_libdir/cmake/Proton
%doc %_defaultdocdir/%name-%version/

%files -n lib%name-cpp
%_libdir/libqpid-proton-cpp.so.*

%files -n lib%name-cpp-devel
%_libdir/libqpid-proton-cpp.so
%_pkgconfigdir/libqpid-proton-cpp.pc
%_libdir/cmake/ProtonCpp

%if_with doc
%files -n lib%name-devel-doc
%doc %proton_datadir/docs/api-c
%endif

%files -n python3-module-qpid-proton
%python3_sitelibdir/*

%if_with doc
%files -n python3-module-qpid-proton-doc
%doc %proton_datadir/docs/api-py
%endif

%changelog
* Thu Sep 21 2023 Artyom Bystrov <arbars@altlinux.org> 0.36.0-alt2
- Fix FTBFS (added -Wno-deprecated-declarations).

* Wed Dec 22 2021 Alexey Shabalin <shaba@altlinux.org> 0.36.0-alt1
- new version 0.36.0.
- drop python2 package.

* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 0.28.0-alt2
- NMU: fixed BuildRequires.

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 0.28.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sat Jul 20 2019 Alexey Shabalin <shaba@altlinux.org> 0.28.0-alt1
- new version 0.28.0

* Thu Jan 31 2019 Alexey Shabalin <shaba@altlinux.org> 0.26.0-alt1
- new version 0.26.0
- drop perl binding package
- add python3 package
- add cpp library package

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.18.1-alt1.3
- rebuild with new perl 5.28.1

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.18.1-alt1.2
- NMU: Rebuild with new openssl 1.1.0.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.18.1-alt1.1
- rebuild with new perl 5.26.1

* Fri Nov 24 2017 Igor Vlasenko <viy@altlinux.ru> 0.18.1-alt1
- NMU: fixed build && updated version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1.1
- rebuild with new perl 5.24.1

* Tue Aug 30 2016 Alexey Shabalin <shaba@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Tue Dec 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2.1
- rebuild with new perl 5.22.0

* Fri Nov 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2
- fixed build for perl 5.22 update
- (conditional doc; quick hack to fix the build)


* Tue Feb 17 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8-alt1
- initial build
