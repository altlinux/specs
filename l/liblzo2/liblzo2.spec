Name: liblzo2
Version: 2.08
Release: alt1

Summary: Data compression library with very fast (de)compression
License: GPLv2+
Group: System/Libraries
URL: http://www.oberhumer.com/opensource/lzo/
# http://www.oberhumer.com/opensource/lzo/download/lzo-%version.tar.gz
# SHA1: 64c3e44843a44ffc4533aa89e41516f42bfefa76
Source: lzo-%version.tar.gz

%description
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory.

In addition there are slower compression levels achieving a quite
competitive compression ratio while still decompressing at
this very high speed.

%package devel
Summary: Development files for the LZO library
Group: Development/C
Requires: %name = %version-%release

%description devel
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory.

In addition there are slower compression levels achieving a quite
competitive compression ratio while still decompressing at
this very high speed.

This package contains files needed to develop programs that use
the LZO library.

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

This package contains the static LZO library needed to develop
statically linked programs that use the LZO library.

%prep
%setup -n lzo-%version
find asm -name '*.o' -delete
sed -i 's/\$host_cpu-\$ac_cv_sizeof_void_p/$target_cpu-$ac_cv_sizeof_void_p/' configure*

%build
%define docdir %_docdir/%name
%configure --enable-shared --docdir=%docdir --disable-silent-rules
%make_build

%check
%make_build -k check

%install
%makeinstall_std

%files
%_libdir/liblzo2.so.2*
%docdir/

%files devel
%_includedir/lzo/
%_libdir/liblzo2.so

%files devel-static
%_libdir/liblzo2.a

%changelog
* Tue Jul 15 2014 Dmitry V. Levin <ldv@altlinux.org> 2.08-alt1
- Updated to 2.08 (fixes CVE-2014-4607).
- Cleaned up specfile.

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.06-alt1
- 2.05 -> 2.06
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
