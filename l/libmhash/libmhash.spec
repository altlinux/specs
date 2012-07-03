Name: libmhash
Version: 0.9.9.9
Release: alt1

Summary: Thread-safe hash library
License: LGPL
Group: System/Libraries
Url: http://mhash.sourceforge.net

Source: %url/dl/mhash-%version.tar.bz2

# Automatically added by buildreq on Tue Oct 22 2002
BuildRequires: glibc-devel-static

%package devel
Summary: Header files and libraries for developing apps which will use %name
Group: Development/C
Requires: %name = %version-%release

%package devel-static
Summary: Header files and libraries for developing apps which will use %name
Group: Development/C
Requires: %name = %version-%release

%description
Mhash is a thread-safe hash library, implemented in C, and provides a
uniform interface to a large number of hash algorithms (MD5, SHA-1,
HAVAL, RIPEMD128, RIPEMD160, TIGER, GOST). These algorithms can be
used to compute checksums, message digests, and other signatures.
The HMAC support implements the basics for message authentication,
following RFC 2104.

%description devel
The %name-devel package contains the header files and libraries needed
to develop programs that use the %name library.

%description devel-static
Static libraries for %name.

%prep
%setup -q -n mhash-%version
%__subst 's@-lltdl@@' aclocal.m4

%build
%configure --enable-static
%make_build

%install
%makeinstall transform=

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
#%_libdir/*.la
%_includedir/*
%_mandir/man?/*
%doc AUTHORS NEWS README TODO
%doc doc/skid2-authentication

%files devel-static
%_libdir/*.a

%changelog
* Tue Jun 12 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.9.9-alt1
- 0.9.9.9

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.8.18-alt1.1.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Thu Nov 12 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.18-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmhash
  * postun_ldconfig for libmhash
  * postclean-05-filetriggers for spec file

* Thu Dec 04 2003 Stanislav Ievlev <inger@altlinux.org> 0.8.18-alt1.1
- rebuild without .la files

* Fri Mar 28 2003 Stanislav Ievlev <inger@altlinux.ru> 0.8.18-alt1
- 0.8.18

* Tue Oct 22 2002 Stanislav Ievlev <inger@altlinux.ru> 0.8.17-alt1
- 0.8.17

* Tue Jun 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.8.16-alt1
- 0.8.16

* Mon Jan 21 2002 Stanislav Ievlev <inger@altlinux.ru> 0.8.13-alt1
- 0.8.13

* Fri Sep 07 2001 Stanislav Ievlev <inger@altlinux.ru> 0.8.10-alt1
- 0.8.10
- Added static package

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 0.8.9-ipl1
- Initial revision.
