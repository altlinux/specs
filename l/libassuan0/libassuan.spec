Name: libassuan0
Version: 1.0.5
Release: alt5.1

Summary: IPC library used by some GnuPG related software
License: LGPLv2.1+
Group: System/Libraries
Url: http://gnupg.org/related_software/libraries.html
Packager: Sergey V Turchin <zerg@altlinux.org>

# ftp://ftp.gnupg.org/gcrypt/libassuan/libassuan-%version.tar.bz2
Source0: libassuan-%version.tar
Source1: version-script-assuan-%version.map
Source2: version-script-assuan-pth-%version.map

Patch1: libassuan-1.0.5-alt-texinfo.patch
Patch2: libassuan-1.0.5-alt-warnings.patch
Patch3: libassuan-1.0.1-alt-shared.patch
Patch4: libassuan-1.0.4-alt-linking.patch

BuildRequires: libgpg-error-devel libpth-devel

%def_enable shared
%def_disable static

%package devel
Summary: Development files for the libassuan library
Group: Development/C
%if_enabled shared
Requires: %name = %version-%release
%endif
Conflicts: libassuan-devel

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
%setup -n libassuan-%version
install -m 0644 %SOURCE1 src/version-script-assuan.map
install -m 0644 %SOURCE2 src/version-script-assuan-pth.map
%patch1 -p1
%patch2 -p1
%if_enabled shared
%patch3 -p1
%patch4 -p1
%endif

# Rename library: libassuan -> libassuan0.
sed -i 's/libassuan\(.la\)/libassuan0\1/g' */Makefile.am

%build
%autoreconf
%if_disabled shared
%add_optflags %optflags_shared
%endif
%configure \
    %{subst_enable shared} \
    %{subst_enable static}
%make_build

%install
%makeinstall_std
mv %buildroot%_libdir/libassuan{0,}.so

%check
%make_build check

%if_enabled shared
%files
%doc AUTHORS NEWS README THANKS
%_libdir/lib*.so.*
%endif

%files devel
%_bindir/libassuan-config
%if_enabled shared
%_libdir/lib*.so
%else
%doc AUTHORS NEWS README THANKS
%endif
%_includedir/*.h
%_datadir/aclocal/*.m4
%_infodir/*.info*

%if_enabled static
%files devel-static
%_libdir/lib*.a
%endif

%changelog
* Wed Nov 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt5.1
- Rebuilt for soname set-versions

* Sun Feb 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.5-alt5
- Disabled build of static library.
- Fixed compilation warnings.
- Cleaned up specfile.
- Enabled test suite.

* Fri Feb 05 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt4
- build shared libarary with different soname

* Wed Feb 03 2010 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt3
- built only static library

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
