%define oname ginac

Name: libginac
Version: 1.6.2
Epoch: 1
Release: alt1.git20111208

Summary: C++ class library for symbolic calculations

License: GPLv2+
Group: Sciences/Mathematics
Url: http://www.ginac.de/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git://www.ginac.de/ginac.git
Source: ginac-%version.tar

# manually removed: xorg-sdk  rpm-build-java rpm-build-mono rpm-build-seamonkey
# Automatically added by buildreq on Wed Dec 03 2008
BuildRequires: doxygen flex gcc-c++ libcln-devel libncurses-devel
BuildRequires: libreadline-devel texlive-latex-base transfig
BuildPreReq: autogen

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
Requires: %name = %version-%release

%description devel
GiNaC is Not a Cocktail.

GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra
System)") is an open framework for symbolic computation within the
C++ programming language.

This is the libraries, include files and other resources you can use
for developing GiNaC applications.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make -C ginac function.h function.cpp
%make_build

%install
%makeinstall_std

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
%_bindir/ginac-excompiler
%_includedir/ginac/
#%_libdir/*.la
%_libdir/*.so
%_pkgconfigdir/*.pc
%_infodir/*.info*

%changelog
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

