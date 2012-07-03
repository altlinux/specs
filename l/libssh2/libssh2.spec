Name: libssh2
Version: 1.4.2
Release: alt1

Summary: A library implementing the SSH2 protocol
Group: Networking/Remote access
License: BSD
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Url: http://www.libssh2.org/
# http://downloads.sourceforge.net/%name/%name-%version.tar.gz
Source: %name-%version.tar
BuildRequires: openssl-devel zlib-devel

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS(22), SECSH-USERAUTH(25),
SECSH-CONNECTION(23), SECSH-ARCH(20), SECSH-FILEXFER(06)*,
SECSH-DHGEX(04), and SECSH-NUMBERS(10).

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files for
developing applications that use %name.

%package docs
Summary: Documentation for %name
Group: Development/C
BuildArch: noarch
Requires: %name = %version-%release

%description docs
This package contains manual pages and examples for
developing applications that use %name.

%prep
%setup

%build
#autoreconf
./buildconf
%configure --disable-static --enable-shared
mkdir docdir
cp -al AUTHORS COPYING HACKING README NEWS example docdir/
%make_build

%install
%makeinstall_std
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
cp -a docdir/* %buildroot%docdir/

%check
%make_build -k check

%files
%dir %docdir/
%docdir/[ACNR]*
%_libdir/*.so.*

%files docs
%dir %docdir/
%docdir/[He]*
%_mandir/man?/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Jun 11 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt1
- New version

* Fri Feb 03 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.0-alt1
- New version

* Thu Sep 29 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3.0-alt1
- New version

* Sat Sep 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.9-alt1
- New version
- Remove configure-fix-VERSION.patch (in upstream)

* Wed Apr 27 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.8-alt1
- New version
- Add configure-fix-VERSION.patch

* Wed Mar 09 2011 Dmitry V. Levin <ldv@altlinux.org> 1.2.7-alt3
- Rebuilt for soname set-versions and debuginfo.

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.7-alt2
- Fixed packaging of documentation.
- Enabled SMP build support.
- Moved test suite to %%check.
- Uncompressed tarball.
- Cleaned up specfile.
- Built with libcrypto.so.10.

* Sun Sep 26 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.7-alt1
- New version

* Tue Aug 03 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.6-alt1
- New version

* Thu Feb 11 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.3-alt1
- New version

* Sat Sep 12 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- New version

* Wed May 27 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.1-alt1
- Build for ALT
