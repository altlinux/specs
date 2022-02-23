Name:           libuvc
Version:        0.0.6
Release:        alt1
Summary:        libuvc is a cross-platform library for USB video devices.
#Summary(ru_RU.UTF8): 
License:        BSD
URL:            https://github.com/libuvc/libuvc
Packager: 	Alexei Mezin <alexvm@altlinux.org>
Vendor: 	ALT Linux Team
Group:		System/Libraries


Source0:        %{name}-%{version}.tar.gz
Patch0:		%{name}-soversion.patch
Patch1:		%{name}-libdir.patch


BuildPreReq: cmake rpm-macros-cmake
# Automatically added by buildreq on Thu Feb 24 2022
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libsasl2-3 libstdc++-devel pkg-config python-modules python2-base python3 python3-base python3-dev python3-module-paste sh4 tzdata
# BuildRequires: cmake doxygen gcc-c++ libdb4-devel libjpeg-devel libnss-resolve libssl-devel libusb-devel python3-module-mpl_toolkits python3-module-setuptools python3-module-yieldfrom python3-module-zope selinux-policy
BuildRequires: gcc-c++ doxygen libjpeg-devel libusb-devel


%description 
libuvc is a cross-platform library for USB video devices, built atop libusb. It enables fine-grained control over USB video devices exporting the standard USB Video Class (UVC) interface, enabling developers to write drivers for previously unsupported devices, or just access UVC devices in a generic fashion.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C++
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup
%patch0 -p1
%patch1 -p1
%cmake -DCMAKE_BUILD_TARGET="Shared"

%build
%cmake_build
doxygen doxygen.conf


%install
%cmake_install

%files
%_libdir/lib*.so.*

%files devel
%_pkgconfigdir/lib*.pc
%_libdir/lib*.so
%_libdir/cmake/%{name}/*.cmake
%_includedir/%{name}
%doc doc/*

%changelog
* Wed Feb 23 2022 Alexei Mezin <alexvm@altlinux.org> 0.0.6-alt1
- Initial build

