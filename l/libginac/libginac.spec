%define oname ginac

Name: libginac
Version: 1.8.6
Release: alt1
Epoch: 1

Summary: C++ class library for symbolic calculations

License: GPLv2+
Group: Sciences/Mathematics
Url: http://www.ginac.de/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://ginac.de/ginac-%version.tar

BuildRequires: python3
BuildRequires: flex gcc-c++ libcln-devel libncurses-devel libreadline-devel
BuildRequires: makeinfo

%description
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This is the libraries, include files and other resources you can use
for developing GiNaC applications.

%package -n %oname
Summary: Libraries, includes and more for developing GiNaC applications
Group: Development/C++

%description -n %oname
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

%package devel
Summary: Libraries, includes and more for developing GiNaC applications
Group: Development/C++
Requires: %name = %EVR

%description devel
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This is the libraries, include files and other resources you can use
for developing GiNaC applications.

%prep
%setup -n %oname-%version
# https://bugzilla.altlinux.org/show_bug.cgi?id=39854
subst "s|2\.7|3.0|" configure.ac

%build
%autoreconf

%configure \
	--disable-static \
	--disable-rpath
%make_build

%install
%makeinstall_std
#mv %buildroot/usr/lib/ginac-excompiler %buildroot%_bindir/
rm -fv %buildroot/usr/lib/ginac-excompiler

%files -n %oname
%doc AUTHORS NEWS README
%_bindir/ginsh
%_bindir/viewgar
%_man1dir/ginsh.1*
%_man1dir/viewgar.1*

%files
%_libdir/*.so.*

%files devel
%doc ChangeLog
#_bindir/ginac-excompiler
%_includedir/ginac/
#%_libdir/*.la
%_libdir/*.so
%_pkgconfigdir/*.pc
%_infodir/*.info*

%changelog
* Sat Feb 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1:1.8.6-alt1
- new version 1.8.6 (with rpmrb script)

* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 1:1.8.5-alt1
- new version 1.8.5 (with rpmrb script)

* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 1:1.8.3-alt1
- new version 1.8.3 (with rpmrb script)

* Mon Jan 24 2022 Vitaly Lipatov <lav@altlinux.ru> 1:1.8.2-alt1
- new version 1.8.2 (with rpmrb script)

* Mon Mar 29 2021 Vitaly Lipatov <lav@altlinux.ru> 1:1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Sat Feb 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1:1.7.8-alt1
- new version 1.7.8 (with rpmrb script)

* Tue Jun 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1:1.7.6-alt1
- new version 1.7.6 (with rpmrb script)

* Wed Feb 06 2019 Vitaly Lipatov <lav@altlinux.ru> 1:1.7.4-alt1
- new version 1.7.4 (with rpmrb script)
- disable doc build

* Wed Feb 06 2019 Grigory Ustinov <grenka@altlinux.org> 1:1.6.2-alt1.git20140518.2
- Rebuild with libreadline7.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.6.2-alt1.git20140518.1.1
- NMU: added BR: texinfo

* Thu Jun 18 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:1.6.2-alt1.git20140518.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.6.2-alt1.git20140518
- New snapshot

* Thu Nov 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.6.2-alt1.git20131103
- New snapshot

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.6.2-alt1.git20120921
- New snapshot

* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 1:1.6.2-alt1.git20111208.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for libginac

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.6.2-alt1.git20111208
- Version 1.6.2

* Tue Aug 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.6.1-alt1.git20110726
- Version 1.6.1 (previous version does not valid)

* Wed May 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1.git20110510
- Version 2.0.2

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.8-alt2.git20101209.2
- Rebuilt for debuginfo

* Thu Dec 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.8-alt2.git20101209.1
- Rebuilt with libcln6

* Sun Dec 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.8-alt2.git20101209
- Built from upstream git repository

* Fri Jul 30 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.8-alt1
- new version 1.5.8 (with rpmrb script) (ALT bug #23818)

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Sat Apr 25 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version 1.5.1 (with rpmrb script), fix bug #19769
- disable static

* Wed Dec 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva)

* Sun Apr 20 2008 David Walluck <walluck@mandriva.org> 1.4.3-1mdv2009.0
+ Revision: 195976
- 1.4.3

* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.1-2mdv2008.1
+ Revision: 182203
- rebuild for new cln
- add missing buildrequires on bison and flex
- make use of %%major in file list
- do not package COPYING file
- new license policy

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 24 2007 David Walluck <walluck@mandriva.org> 1.4.1-1mdv2008.1
+ Revision: 111739
- 1.4.1

* Fri Oct 19 2007 David Walluck <walluck@mandriva.org> 1.4.0-2mdv2008.1
+ Revision: 100279
- rebuild

* Tue Sep 18 2007 David Walluck <walluck@mandriva.org> 1.4.0-1mdv2008.1
+ Revision: 89368
- 1.4.0

* Thu Aug 23 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.3.7-2mdv2008.0
+ Revision: 70249
- kill file require on info-install

* Fri Mar 23 2007 David Walluck <walluck@mandriva.org> 1.3.7-1mdv2007.1
+ Revision: 148697
- 1.3.7

* Sat Dec 16 2006 David Walluck <walluck@mandriva.org> 1.3.6-1mdv2007.1
+ Revision: 98069
- 1.3.6
- Import ginac

* Mon Sep 11 2006 David Walluck <walluck@mandriva.org> 1.3.5-1mdv2007.0
- 1.3.5
- major should be 2
- fix macro in changelog

* Wed Apr 19 2006 David Walluck <walluck@mandriva.org> 1.3.4-1mdk
- 1.3.4

* Sun Oct 30 2005 David Walluck <walluck@mandriva.org> 1.3.3-1mdk
- 1.3.3
- drop gcc4 patch (merged upstream)

* Sat Sep 03 2005 David Walluck <walluck@mandriva.org> 1.3.2-1mdk
- 1.3.2
- name is now ginac
- apply gcc4 patch from suse
- BuildRequires: doxygen, tetex, tetex-dvips, tetex-latex, transfig
- don't use PreReq

* Mon Apr 04 2005 Abel Cheung <deaddog@mandrake.org> 1.3.0-3mdk
- Rebuild & multiarch

* Tue Dec 28 2004 Abel Cheung <deaddog@mandrake.org> 1.3.0-2mdk
- Cleanup this beautified crap, at least make sure devel package
  is usable

* Tue Oct 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3.0-1mdk
- 1.3.0

* Thu Oct 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.4-1mdk
- 1.2.4

* Sun Aug 29 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2.3-2mdk
- %%major in include path
- provide icons in the 2 sizes
- fix distlint DIRM
- fix menu capitalisation

* Sat Aug 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.3-1mdk
- 1.2.3

* Thu Aug 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-1mdk
- 1.2.2

* Wed Jun 16 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2.1-2mdk
- rebuild
- %%mklibname

* Tue Jun 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.1-1mdk
- 1.2.1

