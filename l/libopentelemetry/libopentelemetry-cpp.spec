%define        _unpackaged_files_terminate_build 1
%define        oname opentelemetry

Name:          lib%oname
Version:       1.13.0
Release:       alt1
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
#%autopatch

%build
%cmake_insource \
   -DCMAKE_MODULE_PATH=%_libdir/cmake \
   -DBUILD_SHARED_LIBS=ON \
   -DWITH_STL=ON

%install
%cmakeinstall_std

%check
%make test


%files
%doc README*
%_libdir/%{name}_*.so

%files         devel
%doc README*
%_libdir/cmake/%{oname}-cpp
%_pkgconfigdir/%{oname}_*
%_includedir/%oname


%changelog
* Wed Jan 10 2024 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- Initial build for Sisyphus
