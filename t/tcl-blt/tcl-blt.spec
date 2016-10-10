%define teaname blt
%define	major 2.5

Name: tcl-%teaname
Version: 2.5
Release: alt2

Summary: A Tk toolkit extension, including widgets, geometry managers etc.
Copyright: MIT
Group: System/Libraries
#Url: http://blt.sourceforge.net/
Url: http://pdqi.com/w/pw/pdqi/Wize/Blt

Source: %name-%version.tar

Provides: blt = %version-%release
Obsoletes: blt

Requires: tk >= 8.4.0-alt1
BuildRequires: imake xorg-cf-files xorg-xproto-devel libX11-devel
BuildRequires: libXt-devel tcl-devel tk-devel

%package devel
Summary: development files for %teaname toolkit.
Group: Development/Other
Requires: %name = %version-%release

%package demos
Summary: demos for %teaname toolkit.
Group: Development/Other
Requires: %name = %version-%release

%description
BLT is an extension to the Tk toolkit. BLT's most useful feature is the
provision of more widgets for Tk, but it also provides more geometry managers
and miscellaneous other commands.

%description devel
BLT is an extension to the Tk toolkit. BLT's most useful feature is the
provision of more widgets for Tk, but it also provides more geometry managers
and miscellaneous other commands.

If you are programming with %teaname toolkit, you should install %name-devel.

%description demos
BLT is an extension to the Tk toolkit. BLT's most useful feature is the
provision of more widgets for Tk, but it also provides more geometry managers
and miscellaneous other commands.

This package contains a collection of programs to demonstrate
the features of the %teaname.

%prep
%setup -q %{?snapshot:-c}%{!?snapshot:-n %teaname%version}

%build
#%set_autoconf_version 2.13
%__autoconf
%configure
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install
%__ln_s tcl/libBLT25.so %buildroot%_libdir/libBLT.so
%__ln_s tcl/libBLTlite25.so %buildroot%_libdir/libBLTlite.so
%__mv -f examples/*.tcl %buildroot%_tcldatadir/%teaname%major/demos
%__subst 's|^\#!../src/bltwish|\#!%_bindir/wish|' \
	%buildroot%_tcldatadir/%teaname%major/demos/*.tcl
%__subst 's|^\#!/usr/local/bin|\#!%_bindir|' \
	%buildroot%_tcldatadir/%teaname%major/demos/scripts/page.tcl

# bitmap.n is in tcl now
# graph.n is in tcllib as well
# tabset.n is in itcl as well
# watch.n is in itcl as well
rm -f %buildroot%_mandir/mann/{bitmap,graph,tabset,watch}.n*

%files
%doc NEWS PROBLEMS README
%_tcllibdir/libBLT25.so
%_tcllibdir/libBLTlite25.so
%dir %_tcldatadir/%teaname%major
%_tcldatadir/%teaname%major/dd_protocols
%_tcldatadir/%teaname%major/*.tcl
%_tcldatadir/%teaname%major/*.pro
%_tcldatadir/%teaname%major/*.xbm
%_tcldatadir/%teaname%major/tclIndex
%_mandir/mann/*

%files devel
%doc html/*.html
%_includedir/*
%_libdir/libBLT.so
%_libdir/libBLTlite.so
%_man3dir/*

%files demos
%_tcldatadir/%teaname%major/demos

%changelog
* Mon Oct 10 2016 Vladislav Zavjalov <slazav@altlinux.org> 2.5-alt2
- fix legend entry dimensions

* Sun May 15 2016 Vladislav Zavjalov <slazav@altlinux.org> 2.5-alt1
- tcl-blt-2.5 from http://pdqi.com/w/pw/pdqi/Wize/Blt

* Sun May 15 2016 Vladislav Zavjalov <slazav@altlinux.org> 2.4z-alt4
- fix tcl/tk version requirements
- do not crash on zero-size markers, just do not draw them

* Sat May 14 2016 Vladislav Zavjalov <slazav@altlinux.org> 2.4z-alt3
- resurrected, build with tcl8.5.9

* Thu Jul 20 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4z-alt2
- fixed build on x86_64

* Sat Oct 30 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4z-alt1
- resurrected

* Sat Oct 19 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.4y-alt2
- more tk8.4 patches

* Thu Oct  3 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.4y-alt1
- rebuilt with tcl 8.4
- name changed

* Fri Jul 12 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 2.4y-alt1
- 2.4y
- custom tcl shells dropped
- static libs dropped
- demos separated

* Sun Dec 17 2000 Dmitry V. Levin <ldv@fandra.org> 2.4u-ipl1mdk
- 2.4u.

* Sat Dec 09 2000 Dmitry V. Levin <ldv@fandra.org> 2.4i-ipl14mdk
- Specfile cleanup.
- Split into main and devel subpackage.

* Wed Nov 29 2000 AEN <aen@logic.ru>
- build for RE
- patch for gcc296

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4i-13mdk
- automatically added BuildRequires

* Fri Aug 04 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.4i-12mdk
- rebuild to remove duplicate manpage which is provided by tcllib (stefan)

* Tue Aug 01 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 2.4i-11mdk
- macroszifications
- BM

* Tue May 16 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.4i-10mdk
- fixed broken symlink

* Thu Apr 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 2.4i-9mdk
- fixed group

* Wed Dec  1 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build Release.

* Mon Jul 26 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- s|local/bin/tclsh|bin/tclsh|

* Sat Jul 17 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 2.4i
- set some compatibility links

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Fri Apr 16 1999 Bill Nottingham <notting@redhat.com>
- obsolete blt-devel

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Mar 11 1999 Bill Nottingham <notting@redhat.com>
- remove watch.n, tabset.n (conflicts with itcl)

* Wed Mar 10 1999 Bill Nottingham <notting@redhat.com>
- update to 2.4g
- buildrooted

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- stripped binaries

