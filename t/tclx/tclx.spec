# -*- rpm-spec -*-
# $Id: tclx,v 1.28 2006/07/22 17:03:48 me Exp $

%define snapshot 20060125
%define teaname tclx

Name: tclx
Version: 8.4
Release: alt6
Serial: 1

Summary: Tcl extensions for POSIX systems
License: BSD
Group: Development/Tcl
Url: http://www.tcl.tk/

%ifdef snapshot
Source: %name-%snapshot.tar.bz2
%else
Source: http://download.sourceforge.net/%teaname/%teaname%version.tar.bz2
%endif

Requires: tcl >= 8.4.0-alt1
BuildRequires: tcl-devel >= 8.4.0-alt1 rpm-build >= 4.0.4-alt41 rpm-build-tcl >= 0.2-alt1

%description
TclX is a set of extensions which make it easier to use the Tcl
scripting language for common UNIX/Linux programming tasks.  TclX
enhances Tcl support for files, network access, debugging, math, lists,
and message catalogs.

%prep
%setup -q %{?snapshot:-c}%{!?snapshot:-n %teaname%version}
%teapatch

%build
%configure
%__make

%install 
%make_install DESTDIR=%buildroot install

%files
%doc README ChangeLog
%_tcllibdir/lib%name%version.so
%_tcldatadir/%name%version
%_mandir/mann/*

%changelog
* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:8.4-alt6
- CVS snapshot @20060125
- fixed build on x86_64

* Tue Jan 10 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:8.4-alt5
- 8.4 release

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:8.4-alt4
- CVS snapshot @ 20040714

* Fri May 14 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:8.4-alt3
- CVS snapshot @ 20040218

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1:8.4-alt2
- CVS snapshot @20021217

* Mon Sep 23 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1:8.4-alt1
- CVS snapshot @ 20020921
- custom shell dropped

* Mon Jun 3 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.3.4-alt8
- Tk part dropped
- libpath changed to %_tcllibpath
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


