%def_without test
%define major 8.6

Name: tcl
Version: 8.6.8
Release: alt1

Summary: A Tool Command Language (TCL)
License: BSD
Group: Development/Tcl
Url: http://www.tcl.tk/

# git://git.altlinux.org/gears/t/tcl.git
Source: %name-%version-%release.tar

BuildRequires(pre): rpm-build-tcl >= 0.4-alt1
%{?_with_test:BuildConflicts: tcl-vfs}

Requires: lib%name = %version-%release

Conflicts: tcl-readline < 2.1.1-alt8

%package -n lib%name
Summary: A Tool Command Language (TCL) - shared library
Group: System/Libraries
Provides: %_tcllibdir
Provides: %_tcldatadir

%package devel
Summary: Header files and C programming manual for TCL
Group: Development/C
Requires: %name = %version-%release
Requires: rpm-build-tcl >= 0.5-alt1

%description
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks.  When paired with
the Tk toolkit, Tcl provides the fastest and most powerful way to
create GUI applications that run on PCs, Unix, and the Macintosh.  Tcl
can also be used for a variety of web-related tasks and for creating
powerful command languages for applications.

%description -n lib%name
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks.  When paired with
the Tk toolkit, Tcl provides the fastest and most powerful way to
create GUI applications that run on PCs, Unix, and the Macintosh.  Tcl
can also be used for a variety of web-related tasks and for creating
powerful command languages for applications.

This package includes shared Tcl library only.

%description devel
The Tcl (Tool Command Language) provides a powerful platform for
creating integration applications that tie together diverse
applications, protocols, devices, and frameworks.  When paired with
the Tk toolkit, Tcl provides the fastest and most powerful way to
create GUI applications that run on PCs, Unix, and the Macintosh.  Tcl
can also be used for a variety of web-related tasks and for creating
powerful command languages for applications.

This package includes header files and C programming manuals for Tcl.

%prep
%setup

%build
pushd unix
%autoreconf
%configure --disable-rpath --enable-threads
make all %{?_with_test:test}
popd

%install
%define docdir %_defaultdocdir/%name-%version
%define __tclsh %buildroot%_bindir/.tclsh

%make_install INSTALL_ROOT=%buildroot install -C unix
mkdir -p %buildroot%_tcllibdir %buildroot%_tcldatadir %buildroot%docdir
install -p -m0644 -D tcl.m4 %buildroot%_datadir/aclocal/tea.m4
ln -sf tclsh%major %buildroot%_bindir/tclsh
ln -sf lib%name%major.so %buildroot%_libdir/lib%name.so
ln -s ../unix/tclUnixPort.h %buildroot%_includedir/tcl/generic/tclUnixPort.h
cat <<EOF > %__tclsh
#!/bin/sh
LD_LIBRARY_PATH=%buildroot%_libdir; export LD_LIBRARY_PATH
TCL_LIBRARY=%buildroot%_tcldatadir/%name%major; export TCL_LIBRARY
exec %buildroot%_bindir/tclsh "\$@"
EOF
chmod +x %__tclsh
bzip -9f ChangeLog changes
install -pm0644 README license.terms changes.bz2 ChangeLog.bz2 %buildroot%docdir

%files
%dir %docdir
%docdir/README
%docdir/license.terms
%docdir/changes.*

%_bindir/tclsh*

%_tcldatadir/tcl8
%_tcldatadir/%name%major
%exclude %_tcldatadir/%name%major/%{name}AppInit.c

%_man1dir/*
%_mandir/mann/*

%files -n lib%name
%dir %_tcllibdir
%dir %_tcldatadir
%_libdir/lib%name%major.so

%files devel
%docdir/ChangeLog.*
%_includedir/*
%_pkgconfigdir/%name.pc
%_libdir/lib%name.so
%_libdir/lib%{name}stub%{major}.a
%_libdir/%{name}Config.sh
%_libdir/%{name}ooConfig.sh
%_tcldatadir/%name%major/%{name}AppInit.c
%_datadir/aclocal/*.m4
%_man3dir/*

%changelog
* Tue Feb 13 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 8.6.8-alt1
- 8.6.8 released
- applied patch from Debian to package additional manpages

* Sun Sep 17 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 8.6.7-alt2
- added %%_libdir/tcl to tcl extension search path (new packaging policy)

* Fri Aug 18 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 8.6.7-alt1
- 8.6.7 released

* Tue Jul 25 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 8.6.6-alt3
- added conflict to tcl-readline < 2.1.1-alt8

* Wed Apr 26 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 8.6.6-alt2
- added more extra headers

* Mon Mar 20 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 8.6.6-alt1
- 8.6.6 released (closes: #31581)

* Fri Nov 02 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.9-alt2
- fixed stackspace miscalculation on mixed 64/32 environment

* Mon Feb 14 2011 Alexey Tourbin <at@altlinux.ru> 8.5.9-alt1.1
- rebuilt for debuginfo

* Mon Sep 13 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.9-alt1
- 8.5.9 released

* Tue Jan  5 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.8-alt1
- 8.5.8 released

* Sat Apr 18 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.7-alt2
- 8.5.7 released

* Tue Dec 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.6-alt1
- 8.5.6 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.5-alt2
- obsolete by filetriggers macros removed

* Tue Oct 14 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.5-alt1
- 8.5.5 released

* Sat Aug 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.4-alt1
- 8.5.4 released

* Mon Jun 30 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.3-alt1
- 8.5.3 released

* Sat Mar 29 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.2-alt1
- 8.5.2 released

* Tue Feb  5 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.1-alt1
- 8.5.1 released

* Thu Dec 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt2
- fixed backref handling in regsub [SF #1857126]

* Thu Dec 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt1
- 8.5.0 released

* Sun Nov 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.4
- garbage in tclConfig.sh fixed

* Fri Nov 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.3
- 8.5b3 released

* Tue Nov 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.2
- 8.5b2 released

* Mon Nov 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.5.0-alt0.1
- 8.5b1 released

* Tue Sep 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.16-alt1
- 8.4.16
- added rpm-build-tcl to tcl-devel deps (at@)

* Sat Sep 15 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.15-alt1
- 8.4.15

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 8.4.13-alt1.0
- Automated rebuild.

* Sun May 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.13-alt1
- 8.4.13

* Sun Jan  8 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.12-alt1
- 8.4.12

* Wed Jul 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.11-alt1
- 8.4.11

* Mon Jun 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.10-alt1
- 8.4.10

* Sun Apr  3 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.9-alt1
- 8.4.9

* Sat Dec  4 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.8-alt1
- 8.4.8

* Mon Oct 18 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.7-alt2
- cvs snapshot @20041014
- rpm macro file moved to rpm-build-tcl package

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

* Wed Mar 12 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.2-alt2
- fixed: #702383

* Thu Mar  6 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.2-alt1
- 8.4.2

* Mon Feb 17 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 8.4.2-alt0.1
- CVS snapshot @ 20030215

* Wed Oct 23 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.4.1-alt1
- 8.4.1

* Wed Sep 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.4.0-alt1
- 8.4.0
- new package lib%name appeared
- new layout:
  - libtclXX.so goes back to %_libdir
  - tcl_pkgPath _not_ contains %_tcllibdir nor %_libdir
  - all script stuff goes to %_tcldatadir
- tcl-specific rpm macros added

* Mon Jun 3 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.3.4-alt8
- libpath changed to %_libdir/tcl, tcl_pkgPath contains also %_datadir/tcl
  for pure-tcl extensions
- tcl.m4 installs system-wide, please use them
- now contains private headers in %_includedir/tcl
- adopted patches from RH & SuSE
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

# local variables:
# compile-command: "gear --commit --hasher -- hsh --repo=tcl"
# end:
