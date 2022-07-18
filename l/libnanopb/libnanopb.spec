%define oname nanopb
Name: libnanopb
Version: 0.4.1
Release: alt1

Summary: Nanopb - Protocol Buffers for Embedded Systems

License: BSD-like
Group: System/Libraries
Url: https://jpa.kapsi.fi/nanopb/

# Source-url: https://github.com/nanopb/nanopb/archive/%version/%oname-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake python3

%description
Nanopb is a small code-size Protocol Buffers implementation in ANSI C.
It is especially suitable for use in microcontrollers, but fits any
memory restricted system.

%package devel
Summary: Header files for Nanopb library
Group: Development/C
Requires: %name = %EVR

%description devel
Header files for Nanopb library.


%prep
%setup
subst "s|PythonInterp 2.7|PythonInterp 3|" CMakeLists.txt

%build
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DBUILD_STATIC_LIBS=OFF \
	-Dnanopb_BUILD_GENERATOR=OFF \
	-DCMAKE_C_FLAGS=-DPB_ENABLE_MALLOC=1 -DPB_NO_PACKED_STRUCTS=1 \
	-DCMAKE_POSITION_INDEPENDENT_CODE=ON

%cmake_build

%install
%cmakeinstall_std
#rm -rv %buildroot/usr/lib/python3/site-packages/

%files
%doc AUTHORS.txt CHANGELOG.txt LICENSE.txt README.md docs/{*.rst,*.css,logo}
%_libdir/libprotobuf-nanopb.so.0

%files devel
%_libdir/libprotobuf-nanopb.so
%_includedir/pb*.h
%_libdir/cmake/nanopb/

%changelog
* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- initial build for ALT Sisyphus

* Wed Apr 29 2020 PLD Linux Team <feedback@pld-linux.org>
- For complete changelog see: http://git.pld-linux.org/?p=packages/nanopb.git;a=log;h=master

* Wed Apr 29 2020 Jakub Bogusz <qboosh@pld-linux.org> a942230
- new

