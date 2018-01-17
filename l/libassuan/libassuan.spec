Name: libassuan
Version: 2.5.1
Release: alt1%ubt

Summary: IPC library used by some GnuPG related software
License: LGPLv2.1+
Group: System/Libraries
Url: http://gnupg.org/related_software/libraries.html

# ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-%version.tar.bz2
Source: libassuan-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: libgpg-error-devel

%def_disable static
# explicitly added texinfo for info files
BuildRequires: texinfo

%package devel
Summary: Development files for the libassuan library
Group: Development/C
Requires: %name = %version-%release
Conflicts: libassuan0-devel

%package devel-static
Summary: Static libassuan library
Group: Development/C
Requires: %name-devel = %version-%release

%description
This is the IPC library used by GnuPG 2, GPGME and a few other packages.

%description devel
This package contains development files for the libassuan library.

%description devel-static
This package contains static libassuan library.

%prep
%setup

# Rename library: libassuan -> libassuan2.
sed -i 's/libassuan\(.la\)/libassuan2\1/g' */Makefile.am

%build
%autoreconf
%configure --enable-shared %{subst_enable static}
%make_build

%install
%makeinstall_std
mv %buildroot%_libdir/libassuan{2,}.so

%check
%make_build check

%files
%doc AUTHORS NEWS README THANKS
%_libdir/lib*.so.0*

%files devel
%_bindir/libassuan-config
%_libdir/*.so
%_includedir/*.h
%_datadir/aclocal/*.m4
%_infodir/*.info*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Jan 17 2018 Sergey V Turchin <zerg@altlinux.org> 2.5.1-alt1%ubt
- new version

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 2.4.3-alt1%ubt
- new version

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1.1
- NMU: added BR: texinfo

* Fri Aug 28 2015 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt1
- new version

* Tue Jun 23 2015 Sergey V Turchin <zerg@altlinux.org> 2.2.1-alt1
- new version

* Tue Nov 25 2014 Sergey V Turchin <zerg@altlinux.org> 2.1.3-alt0.M70P.1
- built for M70P

* Tue Nov 25 2014 Sergey V Turchin <zerg@altlinux.org> 2.1.3-alt1
- new version

* Mon Feb 25 2013 Sergey V Turchin <zerg@altlinux.org> 2.1.0-alt1
- new version

* Wed Jul 25 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.3-alt1
- new version

* Mon Jul 04 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.2-alt1
- new version

* Tue Mar 08 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt2
- Rebuilt for debuginfo.

* Sat Nov 06 2010 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt1
- Updated to 2.0.1.

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.1
- Rebuilt for soname set-versions

* Sun Feb 07 2010 Dmitry V. Levin <ldv@altlinux.org> 2.0.0-alt2
- Renamed library: libassuan -> libassuan2.
- Fixed compilation warnings.
- Cleaned up specfile.
- Enabled test suite.

* Wed Feb 03 2010 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt1
- new version

* Mon Dec 21 2009 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt2
- remove ldconfig from %%post

* Tue Jun 10 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0.5-alt1
- new version

* Thu Dec 20 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.4-alt1
- new version
- add versioning

* Tue Jul 10 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.2-alt1
- new version

* Tue Jan 30 2007 Sergey V Turchin <zerg at altlinux dot org> 1.0.1-alt1
- new version

* Wed Nov 01 2006 Sergey V Turchin <zerg at altlinux dot org> 1.0.0-alt1
- new version

* Wed Oct 11 2006 Sergey V Turchin <zerg at altlinux dot org> 0.9.3-alt1
- new version

* Fri Jan 21 2005 Sergey V Turchin <zerg at altlinux dot org> 0.6.10-alt1
- new version

* Mon Oct 11 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6.7-alt1
- new version

* Mon Apr 05 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6.4-alt1
- new version sync patches with PLD

* Thu Nov 27 2003 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt2
- remove *.la

* Mon Nov 24 2003 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt1
- new version
- fix compile with text relocations

* Mon Sep 29 2003 Sergey V Turchin <zerg at altlinux dot org> 0.6.0-alt1
- build for ALT

* Thu Aug 21 2003 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org

$Log: libassuan.spec,v $
Revision 1.3  2003/08/21 08:41:47  qboosh
- epoch 1, release 2 (due to older libassuan-devel in pinentry.spec)

Revision 1.2  2003/08/11 11:03:36  qboosh
- typo in URL (probably there is no more libassuan-specific page, so use this)

Revision 1.1  2003/08/10 11:49:35  qboosh
- new - built as shared library
