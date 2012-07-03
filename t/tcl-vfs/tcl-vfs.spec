# vim: set ft=spec: -*- rpm-spec -*-
# $Id: tcl-vfs,v 1.17 2006/08/31 20:53:06 me Exp $

%define snapshot 20060622
%define teaname vfs

Name: tcl-%teaname
Version: 1.3
Release: alt7

Summary: A TCL virtual file system extension
License: BSD
Group: Development/Tcl
Url: http://tclvfs.sourceforge.net/

BuildPreReq: tcl-devel >= 8.4.0-alt1 rpm-build >= 4.0.4-alt41 rpm-build-tcl >= 0.2-alt1

Source: %name-%{?snapshot:%snapshot}%{!?snapshot:%version}.tar.bz2
Patch0: tcl-vfs-1.3-alt-pkgindex.patch
Patch1: tcl-vfs-1.3-alt-no-thrill.patch

%description
This is an implementation of a 'vfs' extension (and a 'vfs' package,
including a small library of Tcl code).  The goal of this extension
is to expose Tcl 8.4's new filesystem C API to the Tcl level.
See also http://mini.net/tcl/vfs .

It is recommended to install tcl-trf and tcl-memchan packages.

%prep
%setup -q %{?snapshot:-c}%{!?snapshot:-n %teaname}
%patch0 -p1
%patch1 -p1
%teapatch
sed -i 's/@lib@/%_lib/' pkgIndex.tcl.in

%build
%define _configure_script generic/../configure
%configure
%make_build

%install
%makeinstall
# i've no idea where this beast lives, so ...
%__rm -f %buildroot%_tcldatadir/vfs%version/mkclvfs.tcl
%__mkdir_p %buildroot%_tcldatadir/http2.6
%__install -p -m0644 http2.6/*.tcl %buildroot%_tcldatadir/http2.6
%__install -p -m0644 http2.6/http.n %buildroot%_mandir/mann/http2.6.n

%files
%doc Readme.txt examples/*.tcl license.terms ChangeLog
%_tcllibdir/lib%teaname%version.so
%_tcldatadir/%teaname%version
%_tcldatadir/http2.6
%_mandir/mann/*

%changelog
* Fri Sep  1 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt7
- fixed #8677

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt6
- CVS snapshot @20060622
- fixed build on x86_64

* Sat Feb  4 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt5
- CVS snapshot @ 20060125
- vfs::mk4 resurrected

* Sat Dec  4 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt4
- CVS snapshot @ 20041122

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt3
- CVS snapshot @ 20040928

* Sat Mar 13 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt2
- rebuilt against TEA3

* Sat Dec 13 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3-alt1
- CVS snapshot @ 20031110

* Sat Jun 28 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.2-alt2
- CVS snapshot @ 20030616

* Sat Jun  7 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.2-alt1
- CVS snapshot @ 20030516

* Tue Oct  8 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.0-alt1
- CVS snapshot @ 20020925

