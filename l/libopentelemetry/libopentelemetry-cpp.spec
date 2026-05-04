%define        _unpackaged_files_terminate_build 1
%define        oname opentelemetry

%ifarch %e2k
# ecf_opt64 segfault
%def_disable check
%else
%def_enable check
%endif

Name:          lib%oname
Version:       1.22.0
Release:       alt2
Group:         Development/C++
Summary:       The OpenTelemetry C++ Client
License:       Apache-2.0
Url:           https://opentelemetry-cpp.readthedocs.io/
Vcs:           https://github.com/open-telemetry/opentelemetry-cpp.git

Source:        %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: curl
BuildRequires: grpc-plugins
BuildRequires: protobuf-compiler
BuildRequires: opentelemetry-proto
BuildRequires: libcares-devel
BuildRequires: libidn2-devel
BuildRequires: libssl-devel
BuildRequires: zlib-devel
BuildRequires: libre2-devel
BuildRequires: libabseil-cpp-devel
BuildRequires: libgrpc-devel
BuildRequires: libprotobuf-devel
BuildRequires: libssh2-devel
BuildRequires: libnghttp2-devel
BuildRequires: libngtcp2-devel
BuildRequires: libnghttp3-devel
BuildRequires: libgsasl-devel
BuildRequires: libbrotli-devel
BuildRequires: libgsl-devel
BuildRequires: libp11-kit-devel
BuildRequires: libpsl-devel
BuildRequires: libzstd-devel
BuildRequires: libkrb5-devel
BuildRequires: libgtest-devel
BuildRequires: libgnutls-devel
BuildRequires: libnettle-devel
BuildRequires: libtasn1-devel
BuildRequires: libbenchmark-devel
BuildRequires: nlohmann-json-devel
BuildRequires: libprometheus-cpp-devel
BuildRequires: libmicrosoft-gsl-devel

%description
The OpenTelemetry C++ Client.


%package       devel
Group:         Development/C
Summary:       The OpenTelemetry C++ Client development files
Requires:      cmake
Requires:      ctest
Requires:      gcc-c++
Requires:      curl
Requires:      grpc-plugins
Requires:      protobuf-compiler
Requires:      opentelemetry-proto
Requires:      libcares-devel
Requires:      libidn2-devel
Requires:      libssl-devel
Requires:      zlib-devel
Requires:      libre2-devel
Requires:      libabseil-cpp-devel
Requires:      libgrpc-devel
Requires:      libprotobuf-devel
Requires:      libssh2-devel
Requires:      libnghttp2-devel
Requires:      libngtcp2-devel
Requires:      libnghttp3-devel
Requires:      libgsasl-devel
Requires:      libbrotli-devel
Requires:      libgsl-devel
Requires:      libp11-kit-devel
Requires:      libpsl-devel
Requires:      libzstd-devel
Requires:      libkrb5-devel
Requires:      libgtest-devel
Requires:      libgnutls-devel
Requires:      libnettle-devel
Requires:      libtasn1-devel
Requires:      libbenchmark-devel
Requires:      nlohmann-json-devel
Requires:      libprometheus-cpp-devel
Requires:      libmicrosoft-gsl-devel


%description   devel
Development headers and libraries for %oname.

The OpenTelemetry C++ Client.


%prep
%setup

%build
%cmake \
   -DARCH=%_arch \
   -DBUILD_TESTING=%{?_enable_check:ON}%{?!_enable_check:OFF} \
   -DBUILD_SHARED_LIBS=ON \
   -DOTELCPP_VERSIONED_LIBS=ON \
   -DOTELCPP_PROTO_PATH=%_datadir/opentelemetry-proto/ \
   -DWITH_PROMETHEUS=ON \
   -DWITH_OTLP_GRPC=ON \
   -DWITH_ELASTICSEARCH=ON \
   -DUSE_NLOHMANN_JSON=ON \
   -DWITH_GSL=ON \
   -DWITH_STL=ON \
   %nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest -E "SendPost|FinishIn|SendGet|ElegantQuit|OtlpGrpc"


%files
%doc README*
%_libdir/%{name}_*.so.*

%files         devel
%doc README*
%_libdir/%{name}_*.so
%_libdir/cmake/%{oname}-cpp
%_pkgconfigdir/%{oname}_*
%_includedir/%oname


%changelog
* Sat May 02 2026 Anton Farygin <rider@altlinux.org> 1.22.0-alt2
- libgrpc++-devel merged with libgrpc-devel according ALT bug #58350

* Wed Jul 16 2025 Pavel Skrylev <majioa@altlinux.org> 1.22.0-alt1
- ^ 1.21.0 -> 1.22.0
- * enable proto, prometeus, grpc, elasticsearch, nlohmann json, gsl, and tests

* Mon Jul 07 2025 Pavel Skrylev <majioa@altlinux.org> 1.21.0-alt1
- ^ 1.17.0p25 -> 1.21.0

* Mon Jul 07 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.17.0.25-alt0.2
- e2k build fix

* Mon Nov 11 2024 Pavel Skrylev <majioa@altlinux.org> 1.17.0.25-alt0.1
- ^ 1.13.0 > 1.17.0p25

* Wed Feb 28 2024 Ivan A. Melnikov <iv@altlinux.org> 1.13.0-alt1.1
- NMU: loongarch64 support.

* Wed Jan 10 2024 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- Initial build for Sisyphus
