%define rname vvdec

Name: lib%rname
Version: 3.1.0
Release: alt1
Summary: The Fraunhofer Versatile Video Decoder
Group: System/Libraries
License: BSD-3-Clause-Clear
URL: https://github.com/fraunhoferhhi/vvdec
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source0: %rname-%version.tar.xz
Source1: bitstreams.tar.xz

BuildRequires: cmake ctest gcc-c++

%description
VVdeC, the Fraunhofer Versatile Video Encoder, is a fast and efficient
software H.266/VVC encoder implementation

%package devel
Summary: Header files for vvdec development
Group: Development/C++

%description devel
The vvdec-devel package contains the header files needed
to develop programs that use the vvdec.

%prep
%setup -q -n %rname-%version
mkdir -p ext/bitstreams
tar -xf %SOURCE1 -C ext/bitstreams

%build
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DVVDEC_ENABLE_WERROR=OFF \
	-DVVDEC_INSTALL_VVDECAPP=OFF

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc README.md AUTHORS.md
%_libdir/*.so.*

%files devel
%_includedir/%rname
%_libdir/cmake/%rname
%_pkgconfigdir/*.pc
%_libdir/*.so

%changelog
* Thu May 21 2026 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt1
- initial release
