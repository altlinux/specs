# -*- rpm-spec -*-
# $Id: tcl-memchan,v 1.12 2006/07/21 22:00:14 me Exp $

%define teaname Memchan

Name: tcl-memchan
Version: 2.3
Release: alt1

Summary: A tcl extension implementing memory channels
License: TCL
Group: Development/Tcl
Url: http://%teaname.sourceforge.net/

%ifdef snapshot
Source: %name-%snapshot.tar.bz2
%else
# repacked https://download.sourceforge.net/memchan/%teaname%version.tar.gz
Source: %teaname%version.tar
%endif

Patch0: tcl-memchan-2.2-alt-warn.patch

Requires: tcl >= 8.4.0-alt1
BuildRequires: rpm-build >= 4.0.4-alt41 rpm-build-tcl >= 0.2-alt1 tcl-devel >= 8.4.0-alt1 tcllib

%description
This package contains a freely distributable extension to Tcl
implementing memory channels, i.e. channels storing the data
placed into them in memory, not on disk.

%prep
%setup -q %{?snapshot:-c}%{!?snapshot:-n %teaname%version}
%patch0 -p1
%teapatch

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm %buildroot%_mandir/mann/random.n

%check
make test

%files
%_tcllibdir/libMemchan%version.so
%_tcllibdir/Memchan%version
%_mandir/mann/*

%changelog
* Thu Nov 21 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.3-alt1
- Updated to 2.3.
- Built according ALT Tcl/Tk extension policy.
- Fixed license field.
- Enabled test.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2.1-alt3.qa1
- NMU: rebuilt for debuginfo.

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt3
- fixed build for x86_64

* Tue Jan 10 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt2
- updated from CVS @ 20050608

* Sat Dec  4 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.1-alt1
- 2.2.1 released

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt5
- updated from CVS @ 20040804

* Sat Jun 12 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt4
- updated from CVS @ 20040604

* Mon Mar  8 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt3
- updated from CVS @ 20040218

* Wed Sep 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.2-alt2
- 2.2a4
- rebuilt in new env

* Tue Aug  6 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.2-alt1
- first build for %distribution

