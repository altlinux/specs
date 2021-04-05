Summary: srecord programs
Name: srecord
Version: 1.64
Release: alt4
License: GPLv3
Group: Development/Tools
Source: http://srecord.sourceforge.net/%name-%version.tar.gz
Patch0: srecord_rm_pdf_docs.patch
URL: http://srecord.sourceforge.net/

# Automatically added by buildreq on Mon Sep 09 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libgpg-error-devel libstdc++-devel python-base python-modules sh4
BuildRequires: boost-devel-headers gcc-c++ groff-base libgcrypt-devel

%description
The srecord package is a collection of powerful tools for manipulating EPROM
load files. It reads and writes numerous EPROM file formats, and can perform
many different manipulations.

%package -n lib%name
Summary: srecord libraries
Group: Development/Tools

%description -n lib%name
This package contains the shared libraries for programs that manipulate EPROM
load files.

%package devel
Summary: srecord development files
Group: Development/Tools

%description devel
This package contains static libraries and header files for compiling programs
that manipulate EPROM load files.

%prep
%setup

%patch0 -p1

%build
%configure
%make_build

%install
%makeinstall DESTDIR=%buildroot
rm -f %buildroot%_libdir/*.la
rm -f %buildroot%_libdir/libsrecord.a

%check
%make sure

%files
%doc LICENSE BUILDING README
%_bindir/srec_cat
%_bindir/srec_cmp
%_bindir/srec_info
%_man1dir/*
%_man5dir/*

%files -n lib%name
%_libdir/libsrecord.so.*

%files devel
%dir %_includedir/srecord
%_includedir/srecord/*
%_libdir/pkgconfig/srecord.pc
%_libdir/libsrecord.so
%_man3dir/*

%changelog
* Mon Apr 05 2021 Grigory Ustinov <grenka@altlinux.org> 1.64-alt4
- Fixed FTBFS.
- Fixed license tag.

* Mon Sep 09 2019 Grigory Ustinov <grenka@altlinux.org> 1.64-alt3
- Update BR list.

* Thu Sep 05 2019 Grigory Milev <week@altlinux.ru> 1.64-alt2
- remove pdf docs

* Tue Oct 02 2018 Grigory Ustinov <grenka@altlinux.org> 1.64-alt1
- Build new version.

* Wed Sep 26 2018 Grigory Ustinov <grenka@altlinux.org> 1.61-alt2
- Fixed FTBFS.

* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.61-alt1.qa1
- NMU: rebuilt with libgcrypt.so.11 -> libgcrypt.so.20.

* Mon Jan 28 2013 Grigory Milev <week@altlinux.ru> 1.61-alt1
- Initial build for ALTLinux

