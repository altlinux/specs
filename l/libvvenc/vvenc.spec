%define rname vvenc

Name: lib%rname
Version: 1.14.0
Release: alt1
Summary: The Fraunhofer Versatile Video Encoder
Group: System/Libraries
License: BSD-3-Clause-Clear
URL: https://github.com/fraunhoferhhi/vvenc
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %rname-%version.tar.xz

BuildRequires: cmake ctest gcc-c++ nlohmann-json-devel

%description
VVenC, the Fraunhofer Versatile Video Encoder, is a fast and efficient
software H.266/VVC encoder implementation

%package devel
Summary: Header files for vvenc development
Group: Development/C++

%description devel
The vvenc-devel package contains the header files needed
to develop programs that use the vvenc.

%prep
%setup -q -n %rname-%version

%build
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DVVENC_ENABLE_THIRDPARTY_JSON=SYSTEM \
	-DVVENC_INSTALL_FULLFEATURE_APP=OFF

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc LICENSE.txt README.md changelog.txt AUTHORS.md
%_libdir/*.so.*

%files devel
%_bindir/vvencapp
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/vvenc/
%_includedir/vvenc/

%changelog
* Thu May 21 2026 Valery Inozemtsev <shrek@altlinux.ru> 1.14.0-alt1
- initial release

