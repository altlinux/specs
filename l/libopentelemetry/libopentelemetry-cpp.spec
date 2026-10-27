%ifarch %e2k
# ecf_opt64 segfault
%def_disable   check
%else
%def_enable    check
%endif
%def_enable    devel
%def_disable   unstable

%if_enabled    devel
%define        _unpackaged_files_terminate_build 1
%endif
%define        nomen opentelemetry

Name:          lib%nomen
Version:       1.30.0
Release:       alt1
Group:         Development/C++
Summary:       The OpenTelemetry C++ Client
License:       Apache-2.0
Url:           https://opentelemetry-cpp.readthedocs.io/
Vcs:           https://github.com/open-telemetry/opentelemetry-cpp.git

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-cmake
%{?!_disable_check:BuildRequires: ctest}
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: curl
BuildRequires: grpc-plugins
BuildRequires: protobuf-compiler
BuildRequires: opentelemetry-proto
BuildRequires: pkgconfig(libcares)
BuildRequires: pkgconfig(libidn2)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(re2)
BuildRequires: pkgconfig(absl_base)
BuildRequires: pkgconfig(grpc++)
BuildRequires: pkgconfig(protobuf)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(libnghttp2)
BuildRequires: pkgconfig(libngtcp2)
BuildRequires: pkgconfig(libnghttp3)
BuildRequires: pkgconfig(libgsasl)
BuildRequires: pkgconfig(libbrotlicommon)
BuildRequires: pkgconfig(gsl)
BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: pkgconfig(libpsl)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(krb5)
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(libtasn1)
BuildRequires: pkgconfig(benchmark)
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(prometheus-cpp-core)
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
Requires:      pkgconfig(libcares)
Requires:      pkgconfig(libidn2)
Requires:      pkgconfig(openssl)
Requires:      pkgconfig(zlib)
Requires:      pkgconfig(re2)
Requires:      pkgconfig(absl_base)
Requires:      pkgconfig(grpc++)
Requires:      pkgconfig(protobuf)
Requires:      pkgconfig(libssh2)
Requires:      pkgconfig(libnghttp2)
Requires:      pkgconfig(libngtcp2)
Requires:      pkgconfig(libnghttp3)
Requires:      pkgconfig(libgsasl)
Requires:      pkgconfig(libbrotlicommon)
Requires:      pkgconfig(gsl)
Requires:      pkgconfig(p11-kit-1)
Requires:      pkgconfig(libpsl)
Requires:      pkgconfig(libzstd)
Requires:      pkgconfig(krb5)
Requires:      pkgconfig(gtest)
Requires:      pkgconfig(gnutls)
Requires:      pkgconfig(nettle)
Requires:      pkgconfig(libtasn1)
Requires:      pkgconfig(benchmark)
Requires:      pkgconfig(nlohmann_json)
Requires:      pkgconfig(prometheus-cpp-core)
Requires:      libmicrosoft-gsl-devel


%description   devel
Development headers and libraries for %nomen.

The OpenTelemetry C++ Client.


%prep
%setup

%build
%cmake \
   -DBUILD_TESTING=%{?_enable_check:ON}%{?!_enable_check:OFF} \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   -DBUILD_SHARED_LIBS=ON \
   -DOTELCPP_VERSIONED_LIBS=ON \
   -DOTELCPP_PROTO_PATH=%_datadir/opentelemetry-proto/ \
   -DOTELCPP_WITH_PROMETHEUS=ON \
   -DOTELCPP_WITH_OTLP_GRPC=ON \
   -DOTELCPP_WITH_ELASTICSEARCH=ON \
   -DUSE_NLOHMANN_JSON=ON \
   -DOTELCPP_WITH_GSL=ON \
%if_enabled    unstable
   -DOTELCPP_WITH_STL=ON \
%endif
   %nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest -E "SendPost|FinishIn|SendGet|ElegantQuit|OtlpGrpc|Curl"


%files
%doc README*
%_libdir/%{name}_*.so.*

%files         devel
%doc README*
%_libdir/%{name}_*.so
%_libdir/cmake/%{nomen}-cpp
%_pkgconfigdir/%{nomen}_*
%_includedir/%nomen


%changelog
* Mon Oct 26 2026 Pavel Skrylev <majioa@altlinux.org> 1.30.0-alt1
- ^ 1.28.0 -> 1.30.0
- - disabled unstable feature(s)

* Sat Aug 01 2026 Pavel Skrylev <majioa@altlinux.org> 1.28.0-alt1
- ^ 1.22.0 -> 1.28.0

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
