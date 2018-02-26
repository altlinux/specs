# various various
%add_tcl_req_skip critcl
# modules/amazon-s3: tcl-xml is in pretty dead state
%add_tcl_req_skip xml
# modules/map: this should be in tklib probably
%add_tcl_req_skip Tk
%add_tcl_req_skip img::png
# pseudo packages, too tricky for reqprov finder
%add_tcl_req_skip page::plugin
%add_tcl_req_skip doctools::idx::export::plugin
%add_tcl_req_skip doctools::idx::import::plugin
%add_tcl_req_skip doctools::toc::export::plugin
%add_tcl_req_skip doctools::toc::import::plugin
%add_tcl_req_skip pt::peg::export::plugin
%add_tcl_req_skip pt::peg::import::plugin
# next two require tcl 8.6
%add_tcl_req_skip coroutine
%add_tcl_req_skip tcl::transform::core
# optional, requires tcl 8.6 or extra package
%add_tcl_req_skip TclOO

Name: tcllib
Version: 1.13
Release: alt1
Serial: 1

Summary: A Tcl standard library
License: BSD
Group: Development/Tcl
Url: http://tcllib.sourceforge.net/
BuildArch: noarch

BuildRequires(pre): rpm-build-tcl >= 0.2.1-alt2
BuildRequires: tcl >= 8.4.0-alt1

Source: %name-%version-%release.tar

%description
Tcllib is a collection of utility modules for tcl. These modules provide
a wide variety of functionality, from implementation  of standard data
structures  to implementation of common networking protocols.  the intent
is to collect commoly used function into a single library, which users can
rely on to be available and stable.

%prep
%setup

%install
%configure
%make_install DESTDIR=%buildroot install
# clashes with tcl own manpages, has a prefixed with textutil_ copy 
rm -f %buildroot%_mandir/mann/split.n %buildroot%_mandir/mann/string.n
# clashes with memchan package
mv %buildroot%_mandir/mann/random.n %buildroot%_mandir/mann/simulation_random.n

find examples -type f -print0 |xargs -r0 chmod 0644 --

%files
%doc ChangeLog README* license* devdoc examples support/releases/history support/releases/PACKAGES
%_bindir/dtplite
%_bindir/page
%_bindir/tcldocstrip
%_tcldatadir/%name%version
%_mandir/mann/*

%changelog
* Wed Aug 24 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.13-alt1
- 1.13 released

* Tue Dec 16 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.11-alt1
- 1.11.1 released

* Fri Oct 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.10-alt2
- rebuilt according to updated rpm-build-tcl

* Sat Sep 15 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.10-alt1
- 1.10 released

* Mon Nov 13 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.9-alt1
- 1.9 released

* Tue Oct 18 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.8-alt1
- 1.8

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.7-alt1
- 1.7

* Fri May 14 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.6-alt1
- 1.6

* Thu May  8 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1:1.4-alt1
- 1.4

* Fri Mar  7 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1:1.3-alt4
- CVS snapshot @ 20030211

* Mon Oct 28 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1:1.3-alt3
- CVS snapshot @ 20021014

* Fri Aug  2 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1:1.3-alt2
- man clash w/scotty fixed

* Mon Jul 29 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1:1.3-alt1
- 1.3

* Sat Mar  2 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.2-alt2
- rearranged
- tk requirement dropped

* Mon Jan 21 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.2-alt1
- 1.2

* Wed Oct 24 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.1-alt1
- 1.1

* Tue Sep 25 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.0-alt1
- 1.0

* Mon Jul 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.8-alt3
- Removed unnecessary provides and obsoletes.

* Sat Jun 16 2001 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.3-alt2
- Created separate package
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


