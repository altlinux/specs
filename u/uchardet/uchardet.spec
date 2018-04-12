Name:		uchardet
Summary:	Universal charset detection
Version:	0.0.1
Release:	alt2
Group:		Development/Tools
License:	MPLv1.1
Url:		http://code.google.com/p/uchardet/
Source0:	http://uchardet.googlecode.com/files/%name-%version.tar.gz

Requires:	lib%name = %version-%release

# Automatically added by buildreq on Tue Oct 15 2013 (-bi)
# optimized out: cmake-modules elfutils libstdc++-devel pkg-config
BuildRequires: cmake gcc-c++

%description
uchardet is a C language binding of the original C++ implementation of the
universal charset detection library by Mozilla. uchardet is an encoding
detector library, which takes a sequence of bytes in an unknown character
encoding without any additional information, and attempts to determine the
encoding of the text.

%package -n lib%name
Summary: %name shared library
Group: System/Libraries

%description -n lib%name
This package contains shared library required by %name

%package -n lib%name-devel
Summary: Development files for uchardet
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files and Libraries for the package uchardet.

%package -n lib%name-devel-static
Summary: Static library for uchardet
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static library to build statically linked applications that lib%name

%prep
%setup

%build
cmake 	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_INSTALL_LIBDIR=%_libdir \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags"
%make_build

%install
make install DESTDIR=%buildroot

%files
%doc COPYING AUTHORS
%_bindir/%name
%_mandir/man1/%name.1.*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so
%_libdir/pkgconfig/%name.pc

%files -n lib%name-devel-static
%_libdir/lib%name.a

%changelog
* Thu Apr 12 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.1-alt2
- fixed packaging on 64bit arches other than x86_64

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.0.1-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Tue Oct 15 2013 Motsyo Gennadi <drool@altlinux.ru> 0.0.1-alt1
- initial build for ALT Linux from Fedora package
