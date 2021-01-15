# -*- rpm-spec -*-
# $Id: tcl-readline,v 1.13 2006/07/22 12:12:05 me Exp $

%define teaname readline
%define srcname tclreadline
%define srcver 2.3.8

Name: tcl-%teaname
Version: %srcver
Release: alt1

Summary: GNU readline for the Tcl scripting language
License: BSD
Group: Shells
Url: https://github.com/flightaware/tclreadline

# repacked https://github.com/flightaware/tclreadline/archive/v%version.tar.gz
Source0: %srcname-%srcver.tar
Source1: tcl-readline.watch

Patch1: DEBIAN-functions.patch
Patch2: 0001-ALT-init.patch
Patch3: 0002-ALT-lib64.patch
Patch4: 0003-ALT-DEBIAN-man-page.patch

BuildRequires: libreadline-devel libtinfo-devel rpm-build >= 4.0.4-alt41 tcl-devel >= 8.4.0-alt1 tk-devel
Requires: tcl >= 8.4.0-alt1

%description
%name makes the gnu readline available to the scripting language tcl.
The primary purpose of the package is to facilitate the interactive
script development by the means of word and file name completion
as well as history expansion (well known from shells like bash).

%prep
%setup -q -n %srcname-%srcver
%patch1 -p1
%patch2 -p2
%patch3 -p2
%patch4 -p2

%build
autoreconf -fisv -Iaux
%add_optflags -DUSE_NON_CONST
%configure \
	--disable-static \
	--enable-tclstub \
	--libdir=%_tcllibdir \
	--with-tk=%_libdir \
	--with-tlib-library="-ltinfo" \
	#
%make_build

%install
%make_install DESTDIR=%buildroot install \
	libdir=%_tcllibdir tclrldir=%_tcllibdir/%teaname

%files
%doc AUTHORS COPYING ChangeLog README.md TODO sample.tclshrc
%_tcllibdir/lib%{srcname}*.so
%_tcllibdir/%teaname
%_mandir/mann/%srcname.n.*

%changelog
* Thu Jan 14 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.8-alt1
- Updated to 2.3.8.

* Fri Nov 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.7-alt1
- Updated to 2.3.7.
- Built according ALT TCL extension policy (archdep extentsions should hold
  pkgIndex.tcl in %%_tcllibdir/%%teaname), reworked patches and spec.
- Built with tclstub.
- Removed non-in-the-source sample.tclshrc.
- spec: Put --disable-static to %%configure.
- Packed watch file to the sourcerpm.

* Sun Aug 18 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3.6-alt1
- 2.3.6.
- Refreshed Url for new upstream.
- Dropped devel subpackage.

* Tue Jul 25 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.1.1-alt8
- Fixed working with threaded Tcl (Debian #175192).
- Fixed implicit declaration (Debian #226565).
- Fixed typos in man page (Debian #242369).
- Built devel subpackage.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.1.1-alt7.qa1
- NMU: rebuilt for debuginfo.

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt7
- fixed build on x86_64

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.1-alt6.1
- Rebuilt with libreadline.so.5.

* Sat Apr 16 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt6
- rebuilt in new env

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt5
- rebuilt against new shiny tcl reqprov finder

* Tue Sep 30 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt4
- rebuilt without ncurses

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt3
- rebuilt in new env

* Tue Oct  1 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1.1-alt2
- rebuilt with tcl 8.4
- name changed

* Tue Jun  4 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1.1-alt1
- 2.1.1
- delibification
- rl shells removed, `package require' use instead recommended
- libpath changed to %_tcllibdir

* Fri Dec  7 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.1.0-alt2
- rebuild in new env

* Thu Apr 26 2001 Sergey Bolshakoff <s.bolshakov@belcaf.com>
- First spec for ALTLinux distribution





