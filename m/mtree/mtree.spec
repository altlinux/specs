Name: mtree
Version: 3.7.20050808
Release: alt2

Summary: Map a directory hierarchy
License: BSD
Group: File tools

Source: mtree-%version.tar
Patch1: mtree-3.7.20050808-freebsd-owl-vis.patch
Patch2: mtree-3.7.20050808-owl-fixes.patch
Patch3: mtree-3.7.20050808-owl-alt-linux.patch

BuildRequires: libssl-devel

%description
The mtree utility compares the file hierarchy rooted in the current
directory against a specification read from the standard input.
Messages are written to the standard output for any files whose
characteristics do not match the specification, or which are
missing from either the file hierarchy or the specification.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make_build CFLAGS='%optflags -Dlint -I. -I../../include' LDFLAGS=

%install
install -Dpm755 usr.sbin/mtree/mtree %buildroot%_sbindir/mtree
install -Dpm644 usr.sbin/mtree/mtree.8 %buildroot%_man8dir/mtree.8

%files
%_sbindir/*
%_mandir/man?/*

%changelog
* Wed Nov 17 2010 Dmitry V. Levin <ldv@altlinux.org> 3.7.20050808-alt2
- Rebuilt with libcrypto.so.10.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 3.7.20050808-alt1.1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 3.7.20050808-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Tue Mar 07 2006 Dmitry V. Levin <ldv@altlinux.org> 3.7.20050808-alt1
- Updated to 3.7.20050808-owl1.

* Tue Jan 18 2005 Stanislav Ievlev <inger@altlinux.org> 2.7-alt5
- fixed building with gcc3.4

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.7-alt4.1
- Rebuilt with openssl-0.9.7d.

* Wed Oct 23 2002 Stanislav Ievlev <inger@altlinux.ru> 2.7-alt4
- rebuild with gcc3
- rename patches according new policy

* Tue Aug 06 2002 Stanislav Ievlev <inger@altlinux.ru> 2.7-alt3
- Update Owl patch

* Fri Jun 28 2002 Stanislav Ievlev <inger@altlinux.ru> 2.7-alt2
- Updated from OpenBSD CVS. Now we have quotation for bad symbols.
- Owl patch re-adopted.

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.7-alt1
- ALT adaptions.

* Sun Jul 23 2000 Solar Designer <solar@owl.openwall.com>
- Updated to version from OpenBSD 2.7.

* Sat Jul 22 2000 Solar Designer <solar@owl.openwall.com>
- Ported mtree from OpenBSD, wrote initial version of this spec file.
