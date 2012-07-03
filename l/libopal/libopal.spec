Name: libopal
Version: 3.8.4
Release: alt2
Epoch: 1
Summary: Library for H323 spec
Url: http://www.opalvoip.org/
License: MPL
Group: System/Libraries
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Obsoletes: libopenh323

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libgsm-devel libspeex-devel libtheora-devel libavcodec-devel libx264-devel libpt-devel

%description
Open Phone Abstraction Library (aka OpenH323 v2)

%package devel
Summary: Development package for opal
Group: Development/Other
Requires: %name = %epoch:%version-%release
Obsoletes: libopenh323-devel

%description devel
Header files for development with opal.

%prep
%setup -q
%patch -p1

subst 's|^#\(LIBS.*\)|\1|' configure*

%build
%configure \
	--disable-vpb \
	--disable-static
%make

%install
%make DESTDIR=%buildroot install

%files
%doc mpl-1.0.htm
%_libdir/*.so.*
%_libdir/opal-%version

%files devel
%_includedir/opal
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:3.8.4-alt2
- resurrect

* Tue Mar 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:3.8.4-alt1
- 3.8.4

* Wed Oct 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.8-alt3
- disabled celt

* Thu Sep 02 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.8-alt2
- fixed API breakage with x264

* Mon May 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.8-alt1
- 3.6.8

* Sun Jan 31 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.6-alt3
- rebuild with celt-0.7.1

* Thu Dec 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.6-alt2
- rebuild with celt-0.7.0

* Tue Sep 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.6-alt1
- 3.6.6

* Tue Sep 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.4-alt3
- rebuild with libldap2.4

* Thu Jul 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.4-alt2
- build celt plugin

* Tue Jul 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.4-alt1
- 3.6.4

* Tue Jun 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.3-alt2
- 3.6.3 release

* Wed May 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.3-alt1
- 3.6.3

* Mon Apr 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.1-alt2
- disabled voicetronix vpb

* Sun Apr 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:3.6.1-alt1
- 3.6.1

* Fri Jan 16 2009 Vitaly Lipatov <lav@altlinux.ru> 1:3.4.4-alt2
- disable vpb plugin due incorrect linking with unexisted libpvb

* Tue Jan 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1:3.4.4-alt1
- new version 3.4.4 (with rpmrb script)

* Tue Nov 18 2008 Vitaly Lipatov <lav@altlinux.ru> 1:3.4.2-alt1
- new version 3.4.2 (with rpmrb script)
- cleanup spec

* Thu Oct 16 2008 Vitaly Lipatov <lav@altlinux.ru> 1:3.4.1-alt1
- new version 3.4.1 (with rpmrb script)

* Wed Oct 10 2007 Vitaly Lipatov <lav@altlinux.ru> 1:2.2.11-alt1
- new version 2.2.11 (with rpmrb script)

* Tue Sep 18 2007 Vitaly Lipatov <lav@altlinux.ru> 1:2.2.10-alt1
- new version 2.2.10 (with rpmrb script)

* Sun Jun 10 2007 Vitaly Lipatov <lav@altlinux.ru> 1:2.2.8-alt2
- fix internal requires

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 1:2.2.8-alt1
- new version 2.2.8 (with rpmrb script)

* Tue Mar 20 2007 Vitaly Lipatov <lav@altlinux.ru> 1:2.2.6-alt2
- fix requires

* Sun Mar 11 2007 Vitaly Lipatov <lav@altlinux.ru> 1:2.2.6-alt1
- new version 2.2.6 (with rpmrb script)

* Sat Feb 17 2007 Vitaly Lipatov <lav@altlinux.ru> 1:2.2.5-alt1
- new version (2.2.5)

* Thu Oct 12 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt0.1cvs20061011
- new snapshot

* Sun Jul 23 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1cvs20060723
- new snapshot
- drop gcc patch

* Wed Jun 07 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1cvs20060605
- new snapshot
- fix GCC4 errors

* Thu May 25 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1cvs20060524
- really build from CVS 20060524

* Wed May 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1cvs20060521
- new snapshot

* Tue May 16 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1cvs20060515
- new snapshot

* Thu Apr 13 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1cvs20060413
- new snapshot
- use make_build
- add patch for as-needed

* Tue Feb 28 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3.0-alt0.1cvs20060228
- new snapshot (thanks to Yuri)

* Sat Feb 25 2006 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt0.1
- current cvs snapshot

* Tue Feb 14 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- new version
- add Obsoletes for libopenh323

* Sat Jan 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- new version (release)

* Sat Jan 07 2006 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt0.1.cvs20060107
- new version (actually is snapshot)
- initial build for ALT Linux Sisyphus

* Wed Mar 09 2005 Johnny Strom <johnny.strom@linuxvaasa.com> 1.15.3
- Adjusted for the 1.2.1 relase of gnomemeeting.

* Mon Feb 21 2005 Peter Robinson <pbrobinson@gmail.com> 2.1.0-1.FC3
- Initial OPAL rpm
