Name: expect
Version: 5.45
Release: alt3
Serial: 1

Summary: A tcl extension for simplifying program-script interaction
License: BSD
Group: Development/Tcl
Url: http://expect.nist.gov/

Source0: %name-%version-%release.tar

BuildRequires: tcl-devel >= 8.5.0-alt1
BuildRequires(pre): /dev/pts
BuildRequires(pre): /proc

Requires: tcl >= 8.5.0-alt0.3
Requires: /proc

%package devel
Summary: Expect header files and lib%name manpage
Group: Development/C
Requires: %name = %serial:%version-%release tcl-devel >= 8.5.0-alt0.3

%package examples
Summary: Example applications using Expect
Group: Development/Tcl
Requires: %name = %serial:%version-%release tcl(Tk)

%description
Expect is a tcl extension for automating interactive applications such
as telnet, ftp, passwd, fsck, rlogin, tip, etc.  Expect is also useful
for testing the named applications.  Expect makes it easy for a script
to control another program and interact with it.

Install the expect package if you'd like to develop scripts which interact
with interactive applications.  You'll also need to install the tcl
package.

%description devel
Expect is a tcl extension for automating interactive applications such
as telnet, ftp, passwd, fsck, rlogin, tip, etc.  Expect is also useful
for testing the named applications.  Expect makes it easy for a script
to control another program and interact with it.

This package provides development environment for expect.

%description examples
Expect is a tcl extension for automating interactive applications such
as telnet, ftp, passwd, fsck, rlogin, tip, etc.  Expect is also useful
for testing the named applications.  Expect makes it easy for a script
to control another program and interact with it.

This package provides example programs found in expect bundle.

%prep
%setup

%build
autoconf
(cd testsuite && aclocal -I .. && autoconf)
export ac_cv_c_tclconfig=%_libdir
export ac_cv_c_tclh=%_includedir/tcl
%configure --disable-rpath
%make_build all test

%install
%make_install DESTDIR=%buildroot install
mv %buildroot%_libdir/%name%version/lib%name%version.so %buildroot%_libdir
ln -sf lib%name%version.so %buildroot%_libdir/lib%name.so
rm -rf %buildroot%_libdir/%name%version
mkdir -p -m0755 %buildroot%_tcldatadir/%name%version
cat <<EOF > %buildroot%_tcldatadir/%name%version/pkgIndex.tcl
package ifneeded Expect %version [list load [file join \$dir .. .. .. %_lib lib%name%version.so]]
EOF

%files
%doc FAQ NEWS README
%_bindir/expect
%_bindir/autoexpect
%_libdir/lib%name%version.so
%_tcldatadir/%name%version
%_man1dir/expect.*
%_man1dir/autoexpect.*

%files devel
%_includedir/*
%_libdir/lib%name.so
%_man3dir/*

%files examples
%_bindir/*
%_man1dir/*
%exclude %_bindir/expect
%exclude %_bindir/autoexpect
%exclude %_man1dir/expect.*
%exclude %_man1dir/autoexpect.*

%changelog
* Tue Jan 25 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:5.45-alt3
- fix by not fixing sample scripts (#24973)

* Tue Nov 30 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:5.45-alt2
- 5.45 released

* Tue Jul  1 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:5.44-alt3
- CVS snapshot @ 20080604

* Sun Jan  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:5.44-alt2
- fixed build on x86_64
- requirement on /dev/pts dropped

* Sun Nov 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:5.44-alt1
- CVS snapshot @ 20070925
- rebuilt with tcl8.5

* Thu Jan 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:5.43-alt3
- workaround for #10701

* Sun Jul 23 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:5.43-alt2
- CVS snapshot @ 20060227

* Sun Apr  3 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:5.43-alt1
- CVS snapshot @ 20050329

* Wed Jan 05 2005 Dmitry V. Levin <ldv@altlinux.org> 1:5.40-alt1.1
- Added /dev/pts to package dependencies.

* Sat Mar  6 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:5.40-alt1
- CVS snapshot @ 20031020

* Fri Jun 20 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1:5.38-alt2
- updated from CVS

* Tue Sep 24 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1:5.38-alt1
- 5.38.0
- rebuilt with tcl 8.4

* Mon Jun 3 2002 Sergey Bolshakov <s.bolshakov@belcaf.com>  5.37-alt1
- 5.37.2
- RH patches adopted
- libpath changed to /usr/lib/tcl
- src rpm splitted.

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

