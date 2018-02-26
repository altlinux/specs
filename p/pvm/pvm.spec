%define soversion 3
Summary: Parallel Virtual Machine
Name: pvm
Version: 3.4.6
Release: alt1.1
License: freely distributable
Group: System/Base
Url: http://www.epm.ornl.gov/pvm/pvm_home.html
Packager: Boris Savelev <boris@altlinux.org>

%define libname lib%name%soversion

Source: http://www.netlib.org/pvm3/pvm%version.tgz
Source2: pvmd.init
Patch1: 01-replace-pvmarch.patch
Patch6: 06-thread-safe-ctime.patch
Patch7: 07-new-manpages.patch
Patch9: 09-explicitly-declare-pvmnametag.patch
Patch10: 10-minor-manpage-fixes.patch
Patch11: 11-arm-has-tmpnam.patch
Patch12: 12-arm-uses-system-readline.patch
Patch13: 13-add-s390.patch
Patch14: 14-add-mips.patch
Patch15: 15-system-wide-pvmroot.patch
Patch16: 16-default-pvmroot.patch
Patch17: 17-fix-implicit-global-declarations.patch
Patch18: 18-m68k-has-not-fdset-struct.patch
Patch19: 19-sparc-has-const-syserr.patch
Patch20: 20-fix-kfreebsd-ftbfs.patch

Requires: %libname = %version-%release

# Automatically added by buildreq on Sun Jul 05 2009
BuildRequires: gcc-fortran libXaw-devel libXext-devel

%package -n %libname
Summary: Parallel Virtual Machine - shared libraries
Group: System/Libraries

%package devel
Summary: Parallel Virtual Machine - development files
Group: Development/Other
Requires: %libname = %version-%release

%package examples
Summary: Parallel Virtual Machine - examples
Group: Development/Other

%description
Console and communication daemon binaries for the Parallel Virtual
Machine.  Should be sufficient to utilize a node in a dynamically linked
PVM program such as pvmpov.

%description -n %libname
Just the bare library, required by binaries with optional PVM support such
as pvmpov.  Install the pvm package if you wish to actually run a parallel
job.

%description devel
Headers, man pages, documentation, auxiliary functions, and static
libraries for the Parallel Virtual Machine distributed memory
communications library.

%description examples
This package provides the examples distributed along with the Parallel
Virtual Machine. This can be useful for initial cluster or interoptability
testing.

%prep
%setup -n pvm3

%patch1 -p1
%patch6 -p1
%patch7 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

subst "s|@libdir@|%_libdir|g" lib/aimk

%ifarch %ix86
%define pvm_arch LINUX
%else
%define pvm_arch LINUX64
%endif

%build
export AIMKSTR="-here -f ./conf/%pvm_arch.def -f ./Makefile.aimk"
export CFLOPTS_STRING='-g -fPIC %optflags -DRSHCOMMAND=\"%_libdir/pvm3/bin/rsh\" -DPVMDPATH=\"pvmd\" -DPVMDFILE=\"%_bindir/pvmd\" -DPVM_DEFAULT_ROOT=\"%_libdir/pvm3\" -DOVERLOADHOST'
FC="gfortran" F77="gfortran" PVM_ROOT=`pwd` ./lib/aimk $AIMKSTR CFLOPTS="$CFLOPTS_STRING" PVMDIR=`pwd` all

%install
mkdir -p %buildroot{%_bindir,%_includedir,%_datadir/%name}
mkdir -p %buildroot%_libdir/pvm3/{lib,conf}

# pvm package
cp lib/pvmgetarch %buildroot%_bindir
cp lib/%pvm_arch/pvm %buildroot%_bindir
cp lib/%pvm_arch/pvmgs %buildroot%_bindir
cp lib/%pvm_arch/pvmd3 %buildroot%_bindir/pvmd

ln -sf ../../../bin/pvmgetarch %buildroot%_libdir/pvm3/lib/pvmgetarch
ln -sf ../../../bin/pvm %buildroot%_libdir/pvm3/lib/pvm
ln -sf ../../../bin/pvmgs %buildroot%_libdir/pvm3/lib/pvmgs
ln -sf ../../../bin/pvmd %buildroot%_libdir/pvm3/lib/pvmd

# pvm-dev package
cp lib/aimk %buildroot%_bindir
mv bin/%pvm_arch/{pvm_gstat,pvmgroups,tracer,trcsort} %buildroot%_bindir
cp lib/%pvm_arch/*.a %buildroot%_libdir
cp conf/%pvm_arch.{def,m4} %buildroot%_libdir/pvm3/conf
cp include/* %buildroot%_includedir
ln -sf libpvm3.so.%version %buildroot%_libdir/libpvm3.so
ln -sf libgpvm3.so.%version %buildroot%_libdir/libgpvm3.so

# libpvm3 package
cp lib/%pvm_arch/libpvm3.so %buildroot%_libdir/libpvm3.so.%version
ln -s libpvm3.so.%version %buildroot%_libdir/libpvm3.so.%soversion
cp lib/%pvm_arch/libgpvm3.so %buildroot%_libdir/libgpvm3.so.%version
ln -s libgpvm3.so.%version %buildroot%_libdir/libgpvm3.so.%soversion

# pvm-examples package
mv bin/%pvm_arch/gs %buildroot%_bindir/gs.pvm
mv bin/%pvm_arch/hello %buildroot%_bindir/hello.pvm
mv bin/%pvm_arch/srm %buildroot%_bindir/srm.pvm
cp bin/%pvm_arch/* %buildroot%_bindir/
tar zcf %buildroot%_datadir/%name/examples.tar.gz examples
tar zcf %buildroot%_datadir/%name/gexamples.tar.gz gexamples

# init-stuff
mkdir -p %buildroot{%_var/run/pvm3,%_initdir}
cp %SOURCE2 %buildroot%_initdir/pvmd

# man
mkdir -p %buildroot{%_man1dir,%_man3dir}
cp man/man1/* %buildroot%_man1dir
cp man/man3/* %buildroot%_man3dir
cp hoster/*.3 %buildroot%_man3dir

#for p in %_man1dir %_man3dir ; do
#    cd %buildroot$p
#    list=`grep "\.so man" {*.3,*.1} | cut -d":" -f1`
#    for m in $list ; do
#        link=`grep "\.so man" $m | cut -d"/" -f2`
#        rm -f $m
#        ln -s $link $m
#    done
#done

%pre
%_sbindir/groupadd -r -f pvm > /dev/null 2>&1 ||:
%_sbindir/useradd -d %_libdir/pvm3 -r -s /bin/bash pvm > /dev/null 2>&1 ||:

%files
%doc Readme.mp Readme
#%_initdir/pvmd
%_bindir/pvmgs
%_bindir/pvmgetarch
%_bindir/pvm
%_bindir/pvmd
%dir %_libdir/pvm3
%dir %_libdir/pvm3/lib
%_libdir/pvm3/lib/pvmgs
%_libdir/pvm3/lib/pvmgetarch
%_libdir/pvm3/lib/pvm
%_libdir/pvm3/lib/pvmd
%_man1dir/*
%exclude %_man1dir/aimk.*
%exclude %_man1dir/pvmgroups.*
%exclude %_man1dir/pvm_shmd.*
%dir %_datadir/%name
%dir %attr(2775,root,pvm) /var/run/pvm3

%files -n %libname
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_libdir/*.a
%_includedir/*
%dir %_libdir/pvm3/conf
%_libdir/pvm3/conf/*
%_bindir/aimk
%_bindir/pvm_gstat
%_bindir/pvmgroups
%_bindir/tracer
%_bindir/trcsort
%_man1dir/aimk.*
%_man1dir/pvmgroups.*
%_man1dir/pvm_shmd.*
%_man3dir/*

%files examples
%_bindir/*
%exclude %_bindir/aimk
%exclude %_bindir/pvm_gstat
%exclude %_bindir/pvmgroups
%exclude %_bindir/tracer
%exclude %_bindir/trcsort
%exclude %_bindir/pvmgs
%exclude %_bindir/pvmgetarch
%exclude %_bindir/pvm
%exclude %_bindir/pvmd
%_datadir/%name/*

%changelog
* Mon Jul 06 2009 Boris Savelev <boris@altlinux.org> 3.4.6-alt1.1
- fix PVM_ROOT for x86_64

* Sun Jul 05 2009 Boris Savelev <boris@altlinux.org> 3.4.6-alt1
- initial build for Sisyphus

* Wed Feb 19 2003 Bill Nottingham <notting@redhat.com> 3.4.4-12
- fix setting of PVM_ARCH (#79812)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 15 2003 Jens Petersen <petersen@redhat.com> 3.4.4-10
- rebuild to update tcltk deps
- encode changelog in utf-8

* Tue Dec 10 2002 Tim Powers <timp@redhat.com> 3.4.4-9
- rebuild to fix broken tcltk deps
- remove unpackaged files from the buildroot

* Tue Dec 10 2002 Phil Knirsch <pknirsch@redhat.com> 3.4.4-8
- Make it build on x86_64 again with lib64 stuff.

* Tue Dec 03 2002 Elliot Lee <sopwith@redhat.com> 3.4.4-7
- Fix prep section in comments

* Mon Oct 07 2002 Phil Knirsch <pknirsch@redhat.com> 3.4.4-6.2p
- Added s390x, x86_64 and ia64 support
- Fixed x86 support.

* Mon Jul 22 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add patch:
	* Fri May 24 2002 Phil Knirsch <pknirsch@redhat.com> 3.4.4-2b
	- Updated patch for mainframe.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 18 2002 Trond Eivind Glomsrød <teg@redhat.com> 3.4.4-4
- Build on IA64

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr  2 2002 Trond Eivind Glomsrød <teg@redhat.com> 3.4.4-2
- Don't explicitly strip

* Wed Mar 13 2002 Trond Eivind Glomsrød <teg@redhat.com> 3.4.4-1
- 3.4.4
- Disable old patches...

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Tue Apr  3 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add a trigger to fix dangling symlinks from previous installs

* Sat Mar 24 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Fix pvmd.1
- Don't install init scripts - users need to start this themselves

* Mon Feb  5 2001 Trond Eivind Glomsrød <teg@redhat.com>
- minor cleanups

* Sat Jan 27 2001 Karsten Hopp <karsten@redhat.de>
- added s390 patch
- FIXME: tmpnam is used at several functions, better use mkstemp

* Tue Jan 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- change gettextizing

* Wed Jan 17 2001 Trond Eivind Glomsrød <teg@redhat.com>
- gettextize

* Fri Oct 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- LINUX isn't LINUX on Alpha, it's LINUXALPHA (#19389)

* Fri Aug 18 2000 Trond Eivind Glomsrød <teg@redhat.com>
- add README.RedHat for setup instructions - some
  enviroment variables need to be set for pvm to work

* Tue Aug 15 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use /var/run/pvm3 for state files (#16217) for a long
  and healthy life, uninterrupted by tmpwatch

* Sat Aug 05 2000 Bill Nottingham <notting@redhat.com>
- condrestart fixes

* Mon Jul 17 2000 Trond Eivind Glomsrød <teg@redhat.com>
- move back to %_initdir/

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jul 06 2000 Trond Eivind Glomsrød <teg@redhat.com>
- "Prereq:", not "Requires:" for %_sysconfdir/init.d

* Thu Jul 06 2000 Trond Eivind Glomsrød <teg@redhat.com>
- require %_sysconfdir/init.d

* Mon Jun 26 2000 Trond Eivind Glomsrød <teg@redhat.com>
- really move the initscript, not just the paths inside it

* Mon Jun 26 2000 Trond Eivind Glomsrød <teg@redhat.com>
- add conditional restart to initscripts and specfile
- move initscript to %_sysconfdir/init.d

* Wed Jun 14 2000 Trond Eivind Glomsrød <teg@redhat.com>
- Added patch to make compile with new tool chain
- use %%{_tmppath}, %%{_mandir}

* Wed May 10 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added handling of arguments to pvm.sh/xpvm.sh

* Fri Apr 28 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added some extra initialization
- removed gzipping - handled automatically

* Thu Apr 27 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added URL
- changed source location - use netlib
- fix location of documentation files

* Mon Apr 17 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fixed a problem with the PVM man page
- gzip the man pages
- should now be able to compile with several tcl/tk versions
  without problems

* Mon Mar 06 2000 Mike Wangsmo <wanger@redhat.com>
- fixed the useradd failure mode when user already exists
- finally, the init script seems to behave nicely as user pvm

* Sun Mar 05 2000 Mike Wangsmo <wanger@redhat.com>
- fixed quirk in init script to allow PVMD_NOHOLD=ON to be honored

* Fri Feb 18 2000 Mike Wangsmo <wanger@redhat.com>
- added env. variable to make pvmd background when started
- fixed init script killproc errors
- moved to 3.4.3 proper

* Tue Feb 15 2000 Mike Wangsmo <wanger@redhat.com>
- fixed up some group ID stuff

* Mon Feb 14 2000 Mike Wangsmo <wanger@redhat.com>
- added pvm user to package

* Wed Feb 09 2000 Mike Wangsmo <wanger@redhat.com>
- added sparc64 identifier to pvmgetarch
- configured pvmd within the init script to run as user pvm

* Sat Feb 05 2000 Mike Wangsmo <wanger@redhat.com>
- changed pvm-gui group
- set chkconfig to be off in all run levels as the default

* Thu Feb 04 2000 Mike Wangsmo <wanger@redhat.com>
- added sysV init script
- added a shell wrapper in /usr/bin for the pvm shell
- moved up to 3.4.2pl4

* Wed Feb 02 2000 Mike Wangsmo <wanger@redhat.com>
- added some missing files for xpvm to work

* Mon Jan 24 2000 Mike Wangsmo <wanger@redhat.com>
- dropped all non-linux stuff
- split the packages up
- added xpvm
- "fixed" Sparc

* Mon Nov 29 1999 Tim Powers <timp@redhat.com>
- updated to 3.4.2

* Sun Sep 5 1999 Tim Powers <timp@redhat.com>
- excludearch sparc

* Wed Jul 28 1999 Tim Powers <timp@redhat.com>
- update to 3.4.1
- comment out the patches in prep section, will test, if it works then it
  stays commented

* Wed May 05 1999 Bill Nottingham <notting@redhat.com>
- update to 3.4.0 final

* Tue Oct 27 1998 Cristian Gafton <gafton@redhat.com>
- added a patch for the SIGCLD -> SIGCHLD rename
- fixed the incredibly stupid spec file to have a much shorter %files list

* Tue Oct 12 1998 Michael Maher <mike@redhat.com>
- updated pacakge for 5.2 powertools.

* Sat Jun 06 1998 Michael Maher <mike@redhat.com>
- updated source
- changed spec file for all archs

* Wed Dec 03 1997 Mike Wangsmo <wanger@redhat.com>
- fixed patches to cleanly build on glibc
- corrected alpha inuendos

* Wed Dec  3 1997 Otto Hammersmith <otto@redhat.com>
- snagged Wanger's package.
- moved buildroot from /var/tmp to /var/tmp/pvm-root

