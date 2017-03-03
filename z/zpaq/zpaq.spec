Name: zpaq
Version: 715
Release: alt2

Summary: A journaling archiver optimized for backup

Group: Archiving/Compression
License: Public domain
Url: http://mattmahoney.net/dc/zpaq.html

# Use $ rpmrb NEWVERSION for update the package
# Source-url: http://mattmahoney.net/dc/%name%version.zip
Source: %name-%version.tar

# Automatically added by buildreq on Thu Mar 21 2013
# optimized out: libstdc++-devel
BuildRequires: gcc-c++ perl-podlators

%description
zpaq is a journaling archiver optimized for user-level incremental
backup of directory trees. It supports 10 multi-threaded compression
levels and file fragment level deduplication. It adds only files whose
date has changed, and keeps both old and new versions. You can roll
back the archive date to restore from old versions of the archive.
The default compression level is faster than zip usually with better
compression.

%package -n lib%name
Group: System/Libraries
Summary: A journaling archiver optimized for backup library
%description -n lib%name
A journaling archiver optimized for backup library

%package -n lib%name-devel
Group: Development/C++
Summary: Development environment for lib%name
%description -n lib%name-devel
A journaling archiver optimized for backup library,
development environment.

%prep
%setup

%build
# XXX this is for funny libzpaq::error() callback:
# verify-elf: WARNING: ./usr/lib64/libzpaq.so.0: undefined symbol: _ZN7libzpaq5errorEPKc
%set_verify_elf_method unresolved=relaxed

%add_optflags -Wall
g++ %optflags -Dunix -shared -fPIC libzpaq.cpp -Wl,-soname,lib%name.so.0 -o lib%name.so.0 -lm
ln -s lib%name.so.0 lib%name.so
g++ %optflags -Dunix -DNDEBUG zpaq.cpp -L. -o zpaq -l%name -lm -lpthread
#g++ %optflags -Dunix zpaqd.cpp -L. -l%name -o zpaqd -L. -lzpaq -lm
pod2man zpaq.pod > zpaq.1

%install
install -D zpaq %buildroot%_bindir/zpaq
install -D zpaq %buildroot%_bindir/
install -D lib%name.so.0 %buildroot%_libdir/lib%name.so.0
install -D libzpaq.h %buildroot%_includedir/libzpaq.h
ln -s lib%name.so.0 %buildroot%_libdir/lib%name.so
install -m0644 -D zpaq.1 %buildroot%_man1dir/zpaq.1

%files
%doc readme.txt
%_bindir/zpaq
%_man1dir/*

%files -n lib%name
%_libdir/libzpaq.so.0

%files -n lib%name-devel
%_libdir/libzpaq.so
%_includedir/libzpaq.h

%changelog
* Fri Mar 03 2017 Vitaly Lipatov <lav@altlinux.ru> 715-alt2
- drop unused libgomp-devel require
- remove obsoleted copyright line
- fix linking

* Sun Sep 25 2016 Vitaly Lipatov <lav@altlinux.ru> 715-alt1
- new version 715 (with rpmrb script)

* Fri Jul 22 2016 Vitaly Lipatov <lav@altlinux.ru> 714-alt1
- new version 714 (with rpmrb script)

* Tue Apr 19 2016 Vitaly Lipatov <lav@altlinux.ru> 710-alt1
- new version 710 (with rpmrb script)

* Tue Jul 21 2015 Vitaly Lipatov <lav@altlinux.ru> 705-alt2
- convert and pack man page

* Fri Jul 17 2015 Vitaly Lipatov <lav@altlinux.ru> 705-alt1
- new version 705 (with rpmrb script)
- license changed to Public domain

* Mon Jan 19 2015 Vitaly Lipatov <lav@altlinux.ru> 660-alt1
- new version 660 (with rpmrb script)

* Thu Nov 20 2014 Vitaly Lipatov <lav@altlinux.ru> 655-alt1
- new version 655 (with rpmrb script) (ALT bug #30313)

* Thu Mar 21 2013 Fr. Br. George <george@altlinux.ru> 622-alt1
- Autobuild version bump to 622

* Thu Mar 21 2013 Fr. Br. George <george@altlinux.ru> 0-alt1
- Initial zero version build

