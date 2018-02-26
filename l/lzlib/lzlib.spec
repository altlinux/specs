Name: lzlib
Version: 1.3
Release: alt1

Summary: The lzlib compression library provides in-memory LZMA compression and decompression functions
License: GPLv3+
Group: System/Libraries

URL: http://www.nongnu.org/lzip/lzlib.html
Source: http://download.savannah.gnu.org/releases-noredirect/lzip/lzlib-%version.tar.gz

%description
The lzlib compression library provides in-memory LZMA compression and
decompression functions, including integrity checking of the decompressed data.
The compressed data format used by the library is the lzip format.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package includes the files necessary for developing programs
which will use the %name library.

%prep
%setup

%build
subst 's/ ldconfig/ true/' Makefile.in
./configure --prefix=/usr --libdir=%_libdir --enable-shared CFLAGS="%optflags"
%make_build
make check

%install
%makeinstall_std

ln -s liblz.so.?.? %buildroot%_libdir/liblz.so

%files
%exclude %_libdir/*.a
%_libdir/lib*.so.*

%files devel
%_includedir/*
%_libdir/lib*.so
%_infodir/*.info*

%changelog
* Sun Apr 15 2012 Victor Forsiuk <force@altlinux.org> 1.3-alt1
- 1.3

* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 1.2-alt1
- 1.2

* Tue Jan 04 2011 Victor Forsiuk <force@altlinux.org> 1.1-alt1
- 1.1

* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1.1
- rebuild (with the help of girar-nmu utility)

* Thu Jun 17 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- 1.0

* Thu Feb 11 2010 Victor Forsiuk <force@altlinux.org> 0.9-alt1
- 0.9

* Wed Jan 27 2010 Victor Forsyuk <force@altlinux.org> 0.8-alt1
- Initial build.
