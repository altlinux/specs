%define major 8.5

%add_tcl_req_skip ttk::theme::default

Name: tk
Version: 8.5.9
Release: alt3

Summary: A Tk toolkit fot Tcl scripting language
License: BSD
Group: Development/Tcl
Url: http://www.tcl.tk/

# git://git.altlinux.org/gears/t/tk.git
Source: %name-%version-%release.tar

BuildRequires(pre): rpm-build-tcl >= 0.4-alt1
BuildRequires: tcl-devel = %version libXt-devel libXft-devel libXScrnSaver-devel
Requires: tcl = %version lib%name = %version-%release

Provides: tcl(Ttk) = %version

%package -n lib%name
Summary: A Tk toolkit fot Tcl scripting language - shared library
Group: System/Libraries

%package devel
Summary: Header files and C programming manual for Tk
Group: Development/C
Requires: %name = %version-%release  tcl-devel = %version

%package demos
Summary: A collection of programs to demonstrate the features of the Tk toolkit
Group: Development/Tcl
BuildArch: noarch
Requires: %name = %version-%release

%description
Tk is a X Windows widget set designed to work closely with the tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

%description -n lib%name
Tk is a X Windows widget set designed to work closely with the tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

This package includes shared tk library only.

%description devel
Tk is a X Windows widget set designed to work closely with the tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

This package includes header files and C programming manual for Tk.

%description demos
Tk is a X Windows widget set designed to work closely with the tcl
scripting language. It allows you to write simple programs with full
featured GUI's in only a little more time then it takes to write a
text based interface. Tcl/Tk applications can also be run on Windows
and Macintosh platforms.

This package contains a collection of programs to demonstrate
the features of the Tk toolkit.

%prep
%setup
sed -i "s@^\([[:blank:]]\+relative=\)\`[^\`]\+\`\(.\+\)\$@\1'.. .. .. %_lib '\2@" unix/Makefile.in

%build
cd unix
autoconf
%configure --disable-rpath --enable-xft
%make_build

%install
%define docdir %_defaultdocdir/%name-%version
%make_install INSTALL_ROOT=%buildroot install -C unix
ln -sf wish%major %buildroot%_bindir/wish
ln -sf lib%name%major.so %buildroot%_libdir/lib%name.so
ln -s ../unix/tkUnixPort.h %buildroot%_includedir/tk/generic/tkUnixPort.h

mkdir -p %buildroot%docdir
bzip -9f changes ChangeLog
install -pm0644 README license.terms changes.bz2 ChangeLog.bz2 %buildroot%docdir

%files
%dir %docdir
%docdir/README
%docdir/license.terms
%docdir/changes.*

%_bindir/wish*
%dir %_tcldatadir/%name%major
%_tcldatadir/%name%major/*
%exclude %_tcldatadir/%name%major/demos
%exclude %_tcldatadir/%name%major/%{name}AppInit.c
%_man1dir/*
%_mandir/mann/*

%files -n lib%name
%_libdir/lib%name%major.so

%files devel
%docdir/ChangeLog.*
%_includedir/*
%_libdir/lib%name.so
%_libdir/lib%{name}stub%{major}.a
%_libdir/%{name}Config.sh
%_tcldatadir/%name%major/%{name}AppInit.c
%_man3dir/*

%files demos
%_tcldatadir/%name%major/demos

%changelog
* Tue Jun 14 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.9-alt3
- drop handmade reqs found in devel subpackage, we have cpp.req for that

* Fri Feb 25 2011 Dmitry V. Levin <ldv@altlinux.org> 8.5.9-alt2
- Fixed xft detection during build.
- Packaged tk-demos subpackage as noarch.
- Rebuilt for debuginfo (closes: #25123).

* Mon Sep 13 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.9-alt1
- 8.5.9 released

* Wed Jan 06 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.8-alt1
- 8.5.8 released

* Sat Apr 18 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.7-alt1
- 8.5.7 released

* Mon Dec 29 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.6-alt2
- report absence of any font and abort instead of segfault

* Tue Dec 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.6-alt1
- 8.5.6 released

* Sun Dec  7 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.5-alt3
- obsolete by filetriggers macros removed

* Thu Oct 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.5-alt2
- removed XFT_LIBS from TK_LIBS defs, it makes more harm than profit

* Tue Oct 14 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.5-alt1
- 8.5.5 released

* Sun Aug 24 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.4-alt1
- 8.5.4 released

* Mon Jun 30 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.3-alt1
- 8.5.3 released

* Sat Mar 29 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.2-alt1
- 8.5.2 released

* Wed Feb  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.1-alt2
- CVE-2008-0553 fixed

* Tue Feb  5 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.1-alt1
- 8.5.1 released

* Thu Dec 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt2
- added libXScrnSaver-devel & libXext-devel to tk-devel reqs

* Thu Dec 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt1
- 8.5.0 released

* Sun Nov 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.4
- garbage in tkConfig.sh fixed

* Fri Nov 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.3
- 8.5b3 released

* Tue Nov 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.2
- 8.5b2 released

* Mon Nov 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.1
- 8.5b1 released

* Tue Sep 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.16-alt1
- 8.4.16

* Sat Sep 15 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.15-alt1
- 8.4.15

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 8.4.13-alt2.0
- Automated rebuild.

* Sun Jul 23 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.13-alt2
- fixed index on x86_64
- weaken req to tcl

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.13-alt1
- 8.4.13

* Tue Jan 10 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.12-alt1
- 8.4.12

* Wed Jul 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.11-alt1
- 8.4.11

* Mon Jun 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.10-alt1
- 8.4.10

* Sun Apr  3 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.9-alt1
- 8.4.9

* Sat Dec  4 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.8-alt1
- 8.4.8

* Tue Oct 19 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.7-alt2
- cvs snapshot @20041005

* Mon Aug  2 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.7-alt1
- 8.4.7

* Mon Mar  8 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.6-alt1
- 8.4.6

* Tue Nov 25 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.5-alt1
- 8.4.5

* Sat Jul 26 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.4-alt1
- 8.4.4

* Thu May 22 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.3-alt1
- 8.4.3

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.2-alt1
- 8.4.2

* Wed Oct 23 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.4.1-alt1
- 8.4.1

* Wed Sep 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.4.0-alt1
- 8.4.0
- new layout:
  - libtkXX.so goes back to %_libdir
  - tcl_pkgPath _not_ contains %_tcllibdir nor %_libdir
  - all script stuff goes to %_tcldatadir

* Mon Jun 3 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.3.4-alt8
- libpath changed to %_libdir/tcl, tcl_pkgPath contains also %_datadir/tcl
  for pure-tcl extensions
- ps-ml.patch by Anton Kovalenko <a_kovalenko@fromru.com>
- src rpm splitted

* Mon Mar 18 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.3.4-alt7
- fixed encoding file for koi8-u

* Tue Mar 05 2002 Stanislav Ievlev <inger@altlinux.ru> 8.3.4-alt6
- removed all -lieee, 'cause
  fist: Programs can work with -lm and without -lieee
  second: Programs cannot link with lieee library

* Fri Dec  7 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.3.4-alt5
- tclx fixes
- fixed tls build with stubs from tcl build dir
- fixed permissions for %_libdir/lib*stub*.a

* Wed Oct 24 2001 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.4-alt4
- Tcl/Tk 8.3.4
- SSL support added (tcl-tls)

* Mon Jul 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.3.3-alt3
- Removed unnecessary provides and obsoletes.
- Added *_rel macros for subpackages and corrected inter-requires.
- Merged RH patches.

* Sat Jun 16 2001 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.3-alt2
- Rearranged files in subpackages: tcl, tcl-devel
- Tk splitted to: tk tk-devel tk-demos
- tclX 8.3.0, splitted to: tclx tclx-devel
- tix 8.1, splitted to: tix tix-devel tix-demos
- itcl 3.2, splitted to: itcl itcl-devel itcl-demos compat-itcl compat-itcl-demos. Huh :)
- tcllib removed to separate package
- Dropped most of changelog entries
- Group fixed

* Tue May 15 2001 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.3-alt1
- Tcl/Tk 8.3.3
- tcllib 0.8
- expect 5.32, splitted to subpackages.

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 8.3.2-ipl8mdk
- Moved include files and C programming manual to tcl-devel subpackage.
- Fixed out empty manpages.

* Wed Nov 29 2000 AEN <aen@logic.ru> 8.3.2-ipl7mdk
- build for RE
- ps patch from Viktor Wagner
- bad requires patch

