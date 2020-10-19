%define			soversion 1
%define			src qhttpengine

Name:			lib%src
Version:		1.0.1
Release:		alt2
Summary:		HTTP server for Qt applications
Group:			System/Libraries
License:		MIT
Url:			https://github.com/nitroshare/%src
Source0:		%src-%version.tar.gz

# Automatically added by buildreq on Sun Sep 20 2020 (-bi)
# optimized out: cmake-modules elfutils gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libqt5-core libqt5-network libsasl2-3 libstdc++-devel pkg-config python-base python-modules python3 python3-base rpm-build-python3 sh4
BuildRequires: cmake doxygen libssl-devel python3-dev qt5-base-devel

%description
Simple set of classes for developing HTTP server applications in Qt.

%package -n %{name}%soversion
Summary:		Library for multicast DNS as per RFC 676
Group:			System/Libraries

Provides:		%name
Obsoletes:		%name < 1.0.1

%description -n %{name}%soversion
Simple set of classes for developing HTTP server applications in Qt.

%package devel
Summary:		Development files for %name
Group:			Development/C++
Requires:		%{name}%soversion = %EVR

%description devel
HTTP server for Qt applications.
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

%files -n %{name}%soversion
%doc LICENSE.txt examples/ doc/html/
%_libdir/lib*.so.%soversion
%_libdir/lib*.so.%soversion.*

%files devel
%_includedir/*/
%_libdir/cmake/*/
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc

%changelog
* Mon Oct 19 2020 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2
- NMU: proper shared libs policy (closes: #38976)

* Tue Sep 22 2020 Motsyo Gennadi <drool@altlinux.ru> 1.0.1-alt1
- 1.0.1 & build according to shared libs policy (altbug #38976)

* Sun Sep 20 2020 Motsyo Gennadi <drool@altlinux.ru> 1.0.0-alt1
- initial build
