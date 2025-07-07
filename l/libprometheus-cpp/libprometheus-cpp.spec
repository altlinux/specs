%define        _unpackaged_files_terminate_build 1
%define        cognomen prometheus
%define        nomen prometheus-cpp

%def_enable    check

Name:          lib%nomen
Version:       1.3.0
Release:       alt1
Group:         Development/C++
Summary:       Prometheus Client Library for Modern C++
License:       MIT
Url:           https://github.com/jupp0r/prometheus-cpp
Vcs:           https://github.com/jupp0r/prometheus-cpp.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: civetweb
BuildRequires: libcurl-devel
BuildRequires: libgtest-devel
BuildRequires: civetweb-devel
BuildRequires: zlib-devel

%description
This library aims to enable Metrics-Driven Development for C++ services. It
implements the Prometheus Data Model, a powerful abstraction on which to
collect and expose metrics. We offer the possibility for metrics to be collected
by Prometheus, but other push/pull collections can be added as plugins..


%package       devel
Group:         Development/C
Summary:       Prometheus Client Library for Modern C++ development files
Requires:      /proc
Requires:      cmake
Requires:      ctest
Requires:      gcc-c++
Requires:      civetweb
Requires:      libcurl-devel
Requires:      libgtest-devel
Requires:      civetweb-devel
Requires:      zlib-devel

%description   devel
Development headers and libraries for %nomen.

This library aims to enable Metrics-Driven Development for C++ services. It
implements the Prometheus Data Model, a powerful abstraction on which to
collect and expose metrics. We offer the possibility for metrics to be collected
by Prometheus, but other push/pull collections can be added as plugins..


%prep
%setup

%build
%cmake \
   -DARCH=%_arch \
   -DBUILD_SHARED_LIBS=ON \
   -DENABLE_TESTING=%{?_enable_check:ON}%{?!_enable_check:OFF} \
   -DUSE_THIRDPARTY_LIBRARIES=OFF \
   -DRUN_IWYU=OFF \
   %nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest


%files
%doc README*
%_libdir/%{name}-*.so.*

%files         devel
%doc README*
%_libdir/%{name}-*.so
%_libdir/cmake/%{nomen}
%_pkgconfigdir/%{nomen}-*
%_includedir/%cognomen


%changelog
* Tue Jul 08 2025 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial build v1.3.0 for Sisyphus
