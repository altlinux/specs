%define        _unpackaged_files_terminate_build 1
%define        oname opentelemetry

%ifarch %e2k
# ecf_opt64 segfault
%def_disable check
%else
%def_enable check
%endif

Name:          lib%oname
Version:       1.17.0.25
Release:       alt0.2
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
BuildRequires: libgtest-devel
BuildRequires: libbenchmark-devel

%description
The OpenTelemetry C++ Client.


%package       devel
Group:         Development/C
Summary:       The OpenTelemetry C++ Client development files
Requires:      /proc
Requires:      cmake
Requires:      ctest
Requires:      gcc-c++
Requires:      libgtest-devel
Requires:      libbenchmark-devel


%description   devel
Development headers and libraries for %oname.

The OpenTelemetry C++ Client.


%prep
%setup
%autopatch -p1

%build
%ifarch %e2k
export ARCH=e2k
%endif
%cmake_insource \
   -DBUILD_TESTING=%{?_enable_check:ON}%{?!_enable_check:OFF} \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DOTELCPP_VERSIONED_LIBS=ON \
   -DWITH_STL=ON

%install
%cmakeinstall_std

%check
%make test


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
* Mon Jul 07 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.17.0.25-alt0.2
- e2k build fix

* Mon Nov 11 2024 Pavel Skrylev <majioa@altlinux.org> 1.17.0.25-alt0.1
- ^ 1.13.0 > 1.17.0p25

* Wed Feb 28 2024 Ivan A. Melnikov <iv@altlinux.org> 1.13.0-alt1.1
- NMU: loongarch64 support.

* Wed Jan 10 2024 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- Initial build for Sisyphus
