%define			src qmdnsengine

Name:			lib%src
Version:		0.2.0
Release:		alt1
Summary:		Library for multicast DNS as per RFC 676
Group:			System/Libraries
License:		MIT
Url:			https://github.com/nitroshare/%src
Source0:		%src-%version.tar.gz

# Automatically added by buildreq on Sun Sep 20 2020 (-bi)
# optimized out: cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libqt5-core libqt5-network libsasl2-3 libstdc++-devel python-base python-modules python3 python3-base rpm-build-python3 sh4
BuildRequires: cmake doxygen libssl-devel python3-dev qt5-base-devel

%description
This library provides an implementation of multicast DNS as per [RFC 6762]

%package -n %{name}1
Summary:		Library for multicast DNS as per RFC 676
Group:			System/Libraries

Provides:		%name
Obsoletes:		%name < 0.2.0

%description -n %{name}1
This library provides an implementation of multicast DNS as per [RFC 6762]

%package devel
Summary:		Development files for %name
Group:			Development/C++
Requires:		%{name}1 = %version-%release

%description devel
Library for multicast DNS as per RFC 676.
This package contains the development files.

%prep
%setup -n %src-%version

%build
mkdir build && cd build
cmake ../. \
		-DCMAKE_INSTALL_PREFIX=%prefix \
		-DLIB_INSTALL_DIR=%_libdir \
		-DCMAKE_CXX_FLAGS:STRING="%optflags" \
		-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build
cd ../doc && cmake ./. && doxygen Doxyfile

%install
cd build
%make_install DESTDIR=%buildroot install

%files -n %{name}1
%doc LICENSE.txt examples/ doc/html/
%_libdir/lib*.so.*

%files devel
%_includedir/*/
%_libdir/cmake/*/
%_libdir/lib*.so
# FIXME add pkgconfig
#%_libdir/pkgconfig/*.pc

%changelog
* Tue Sep 22 2020 Motsyo Gennadi <drool@altlinux.ru> 0.2.0-alt1
- 0.2.0
- build according to shared libs policy

* Sun Sep 20 2020 Motsyo Gennadi <drool@altlinux.ru> 0.1.0-alt1
- initial build
