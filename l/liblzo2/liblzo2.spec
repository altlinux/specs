Name: liblzo2
Version: 2.06
Release: alt1

Summary: A real-time data compression library
License: GPL
Group: System/Libraries

URL: http://www.oberhumer.com/opensource/lzo/
Source: lzo-%version.tar.gz

%description
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory.

In addition there are slower compression levels achieving a quite
competitive compression ratio while still decompressing at
this very high speed.

%package devel
Summary: Libraries and header files for programs that use lzo
Group: Development/C
Requires: %name = %version-%release

%description devel
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory.

In addition there are slower compression levels achieving a quite
competitive compression ratio while still decompressing at
this very high speed.

%package devel-static
Summary: Static %name library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory.

In addition there are slower compression levels achieving a quite
competitive compression ratio while still decompressing at
this very high speed.

%prep
%setup -q -n lzo-%version

%build
%configure --enable-shared
%make_build

%check
make check

%install
%makeinstall_std

%files
%doc AUTHORS NEWS THANKS doc/LZO*
%_libdir/liblzo2.so.2*

%files devel
%dir %_includedir/lzo
%_includedir/lzo/lzo*.h
%_libdir/liblzo2.so

%files devel-static
%_libdir/liblzo2.a

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.06-alt1
- 2.06 -> 2.07
- rebuilt as plain src.rpm

* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 2.05-alt1
- 2.04 -> 2.05

* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 2.04-alt1.1
- rebuilt for debuginfo

* Fri Dec 17 2010 Alexey Tourbin <at@altlinux.ru> 2.04-alt1
- 2.03 -> 2.04

* Mon Oct 04 2010 Alexey Tourbin <at@altlinux.ru> 2.03-alt2.1
- rebuilt

* Sun Nov 23 2008 Alexey Tourbin <at@altlinux.ru> 2.03-alt2
- rebuilt with gcc-4.3
- removed ldconfig scriptlets

* Sat Aug 09 2008 Alexey Tourbin <at@altlinux.ru> 2.03-alt1
- 2.02 -> 2.03

* Sun Mar 26 2006 Andrey Brindeew <abr@altlinux.org> 2.02-alt1
- 2.02 released as separate package due ugly soname change
  procedure. Old version still available under liblzo name.
