# -*- rpm-spec -*-
# $Id: tcl-tktable,v 1.9 2006/07/22 15:26:03 me Exp $

%define teaname Tktable

Name: tcl-tktable
Version: 2.9
Release: alt3

Summary: tktable is a table/matrix widget extension to tk/tcl
License: BSD
Group: Development/Tcl
Url: http://tktable.sourceforge.net

%ifdef snapshot
Source: %name-%snapshot.tar.bz2
%else
Source: http://download.sourceforge.net/tktable/%teaname%version.tar.bz2
%endif

Patch0: tktable-2.9-alt-noembed.patch

Provides: tktable = %version-%release
Obsoletes: tktable
Requires: tk >= 8.4.0-alt1
BuildRequires: libX11-devel libXt-devel tk-devel >= 8.4.0-alt1 rpm-build >= 4.0.4-alt41 rpm-build-tcl >= 0.2-alt1

%description
The table command creates a 2-dimensional grid of cells. The table can use
a Tcl array variable or Tcl command  for data  storage  and  retrieval. The
widget has an active cell, the contents of which can be edited (when the
state is  normal).

%prep
%setup -q %{?snapshot:-c}%{!?snapshot:-n %teaname%version}
%patch0 -p1
%teapatch

%build
%__aclocal
%__autoconf
%configure
%make_build

%install
%makeinstall
%__install -p -m0644 -D doc/tkTable.n %buildroot%_mandir/mann/tkTable.n
 
%files
%doc license* README* TODO* doc/*.html
%_tcllibdir/lib%teaname%version.so
%_tcldatadir/%teaname%version
%_mandir/mann/*

%changelog
* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9-alt3
- fixed build on x86_64

* Sat Feb 25 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9-alt2
- fixed build with bash3 

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9-alt1
- 2.9 released

* Fri Mar  7 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 2.8-alt2
- CVS snapshot @ 20030224

* Thu Sep 26 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.8-alt1
- 2.8 CVS snapshot @ 20020925
- rebuilt with tcl 8.4

* Fri Jun  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.7-alt2
- rebuilt in new env

* Sat Jul 21 2001 Sergey Bolshakov <s.bolshakov@belcaf.com>
- First spec file for ALT Linux distribution.

