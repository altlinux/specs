Name: dirmngr
Version: 1.1.0
Release: alt2

Summary: Client for Managing/Downloading CRLs
Group: System/Libraries
License: GPLv2+
Url: http://www.gnupg.org/

# ftp://ftp.gnupg.org/gcrypt/dirmngr/%name-%version.tar.bz2
Source: %name-%version.tar
Patch1: dirmngr-1.1.0-alt-fix-linking.patch

BuildRequires: libassuan-devel libgcrypt-devel libksba-devel libldap-devel libpth-devel

%description
Dirmngr is a server for managing and downloading certificate
revocation lists (CRLs) for X.509 certificates and for downloading
the certificates themselves.  Dirmngr also handles OCSP requests as
an alternative to CRLs.  Dirmngr is either invoked internally by
gpgsm (from gnupg2) or when running as a system daemon through
the dirmngr-client tool.

%prep
%setup
%patch1 -p1
%autoreconf

%build
%define docdir %_docdir/%name-%version
%configure \
	--disable-rpath \
	--libexecdir=%_libexecdir/dirmngr \
	--docdir=%docdir
%make_build

%install
%makeinstall_std
install -pm644 AUTHORS NEWS README THANKS %buildroot%docdir/
%find_lang %name

%check
%make_build -k check

%files -f %name.lang
%_bindir/*
%_libexecdir/dirmngr/
%_infodir/*.info*
%_man1dir/*
%docdir

%changelog
* Fri Jun 15 2012 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt2
- fix to build with gcc-4.6

* Mon Jul 04 2011 Sergey V Turchin <zerg@altlinux.org> 1.1.0-alt1
- new version

* Sun Feb 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.3-alt4
- Rebuilt with libassuan0.so.0.
- Cleaned up specfile.
- Enabled test suite.

* Wed Feb 03 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt3
- rebuilt with static assuan

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt2
- rebuilt with libldap2.4

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 1.0.3-alt1
- new version

* Thu Jul 31 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.2-alt1
- new version

* Thu Nov 30 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt2
- fix build on x86_64

* Wed Nov 29 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- new version

* Fri Jan 20 2006 Sergey V Turchin <zerg at altlinux dot org> 0.9.3-alt1
- new version

* Tue Jun 21 2005 Sergey V Turchin <zerg at altlinux dot org> 0.9.2-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 0.5.6-alt1
- new version

* Tue Apr 06 2004 Sergey V Turchin <zerg at altlinux dot org> 0.5.2-alt1
- new version

* Wed Sep 03 2003 Sergey V Turchin <zerg at altlinux dot org> 0.4.5-alt1
- new version

* Wed May 07 2003 Sergey V Turchin <zerg at altlinux dot ru> 0.4.4-alt1
- new version

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 0.4.3-alt1
- build for ALT

* Wed Dec 11 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.4.3-1mdk
- Update from <fabrice-marie-sec@ifrance.com> spec file

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.4.2-1mdk
- first package

