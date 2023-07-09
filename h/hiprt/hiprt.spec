%define git a134c7

Name: hiprt
Version: 2.0.3
Release: alt1.g%{git}
Summary: HIP Ray Tracing
License: Proprietary
Group: Development/Other
Url: https://gpuopen.com/hiprt

# https://gpuopen.com/download/hiprt/hiprtSdk-%{version}%{git}.zip
Source: %name-%version.tar

ExclusiveArch: x86_64

%description
HIP RT is a ray tracing library for HIP, making it easy to write ray-tracing
applications in HIP. The APIs and library are designed to be minimal, lower
level, and simple to use and integrate into any existing HIP applications.

%package -n lib%{name}
Summary: HIP Ray Tracing Library and bitcode
Group: System/Libraries
Requires: hip-runtime-amd

%description -n lib%{name}
HIP Ray Tracing Library and bitcode

%package devel
Summary: %name development headers
Group: Development/C++
Requires: lib%{name} = %EVR hip-devel

%description devel
%name development headers

%prep
%setup

%install
mkdir -p %buildroot{%_libdir,%_datadir/%name,%_includedir/%name}
install -pm644 %name/linux64/*.so %buildroot%_libdir/
install -pm644 %name/*.h %buildroot%_includedir/%name/
install -pm644 %name/linux64/*.{bc,fatbin} %buildroot%_datadir/%name/
install -pm644 %name/linux64/*.hipfb %buildroot%_libdir/

%files -n lib%{name}
%_libdir/*.so
%_libdir/*.hipfb
%_datadir/%name

%files devel
%_includedir/%name

%changelog
* Fri Jul 07 2023 L.A. Kostis <lakostis@altlinux.ru> 2.0.3-alt1.ga134c7
- Initial build for ALTLinux.
