Name: lockdev
Version: 1.0.3
Release: alt3.1.1.1.1

Summary: A library and a command-line tool for locking devices
License: LGPL
Group: System/Libraries

URL: http://packages.debian.org/unstable/source/lockdev
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: lib%name = %version-%release
Requires: /var/lock/serial

# Automatically added by buildreq on Mon Oct 17 2011
BuildRequires: perl-devel

%description
The lockdev library provides a reliable way to put an exclusive lock
on devices using both FSSTND and SVr4 methods.

%package -n lib%name
Summary: A library for locking devices
Group: System/Libraries

%description -n lib%name
The lockdev library provides a reliable way to put an exclusive lock
on devices using both FSSTND and SVr4 methods.

%package -n lib%name-devel
Summary: Header files for the %name library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lockdev library provides a reliable way to put an exclusive lock
on devices using both FSSTND and SVr4 methods.

%package -n lib%name-devel-static
Summary: Static %name library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel-static
The lockdev library provides a reliable way to put an exclusive lock
on devices using both FSSTND and SVr4 methods.

%package -n perl-LockDev
Summary: Perl interface for the %name library
Group: Development/Perl
Requires: lib%name = %version-%release
Provides: %name-perl = %version
Obsoletes: %name-perl < %version

%description -n perl-LockDev
The lockdev library provides a reliable way to put an exclusive lock
on devices using both FSSTND and SVr4 methods.

%prep
%setup -q
%patch -p1

%build
export LD_LIBRARY_PATH=$PWD
CFLAGS="%optflags -D_GNU_SOURCE -D_REENTRANT -I$PWD/src -Werror"
LDFLAGS="-L$PWD -l%name"

%define soname lib%name.so.1
gcc $CFLAGS %optflags_shared src/%name.c -shared -Wl,-soname=%soname,-z,defs -o %soname
ln -s %soname lib%name.so

%if_enabled static
gcc $CFLAGS -c src/%name.c -o src/%name-a.o
ar rcu lib%name.a src/%name-a.o
ranlib lib%name.a
%endif

gcc $CFLAGS src/sample.c -o %name $LDFLAGS

cd LockDev
%perl_vendor_build MYEXTLIB="$LDFLAGS"

%install
mkdir -p %buildroot%_libdir/
cp -av lib%name.so* %buildroot%_libdir/

%if_enabled static
cp -av lib%name.a %buildroot%_libdir/
%endif

mkdir -p %buildroot%_sbindir/
cp -av %name %buildroot%_sbindir/

mkdir -p %buildroot%_includedir/
cp -av src/*.h %buildroot%_includedir/

mkdir -p %buildroot%_man3dir/
cp -av docs/%name.3 %buildroot%_man3dir/

cd LockDev
%perl_vendor_install

%files
%attr(2711,root,uucp) %_sbindir/%name

%files -n perl-LockDev
%perl_vendor_archlib/LockDev*
%perl_vendor_autolib/LockDev*

%files -n lib%name
%_libdir/%soname

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/*.h
%_man3dir/%name.*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt3.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 1.0.3-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0.3-alt2
- rebuilt for perl-5.16

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 1.0.3-alt1.3
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.3-alt1.2
- rebuilt with perl 5.12

* Sat Dec 13 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0.3-alt1.1
- built without -Werror
- fixed URL
- removed obsolete post{,un}_ldconfig calls

* Thu Mar 01 2007 Alexey Tourbin <at@altlinux.ru> 1.0.3-alt1
- 1.0.1 -> 1.0.3
- imported into git and adapted for gear
- renamed lockdev-perl package to perl-LockDev
- fixed warnings emitted by new gcc compiler
- further cleaned up the code (closes #10956 baudboy.h problem)

* Fri Mar 04 2005 Alexey Tourbin <at@altlinux.ru> 1.0.1-alt3
- rh-pidexists.patch: fix kill/EPERM behaviour (don't unlock files
  when device is locked by process with different UID)
- rh-subdir.patch: fix errs on /dev/input/ttyACM0 (3-component pathname)
- conditionally packaged lib%name-devel-static 
- perl LockDev(3) manpage not packaged (use perldoc)

* Tue Nov 11 2003 Alexey Tourbin <at@altlinux.ru> 1.0.1-alt2
- eliminated text relocations in shared library
- warnings fixed, built with -Werror

* Thu Oct 30 2003 Alexey Tourbin <at@altlinux.ru> 1.0.1-alt1
- 1.0.1
- cli.patch and checkname.patch from RH
- abandon makefiles, custom build with direct commands
- %name-perl packaged, lib%name-devel-static not packaged

* Wed Oct 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.0-alt1
- First build for Sisyphus

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun  5 2002 Jeff Johnson <jbj@redhat.com> 1.0.0-19
- fix: don't ignore signals, use default behavior instead (#63468).

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Feb 25 2002 Nalin Dahyabhai <nalin@redhat.com> 1.0.0-16
- include liblockdev.so so that programs can link to a shared liblockdev
- fix shared library version numbers

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Nov 29 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.0.0-16
- Rebuilt

* Fri Oct 26 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.0.0-15
- Add copyright/license info to baudboy.h (#54321)

* Tue Sep  4 2001 Jeff Johnson <jbj@redhat.com>
- swap egid and gid for lockdev's access(2) device check (#52029).

* Tue Aug 28 2001 Jeff Johnson <jbj@redhat.com>
- typo in include file (#52704).
- map specific errno's into status for return from helper.

* Tue Aug 14 2001 Jeff Johnson <jbj@redhat.com>
- set exit status correctly.

* Thu Aug  9 2001 Bill Nottingham <notting@redhat.com>
- check that we can open the device r/w before locking
- fix calling lockdev without any arguments
- fix waitpid() call in baudboy.h
- use umask(002), not umask(0)

* Wed Aug  8 2001 Bill Nottingham <notting@redhat.com>
- add lock group here, own /var/lock as well

* Sun Aug  5 2001 Jeff Johnson <jbj@redhat.com>
- include setgid helper binary and baudboy.h.

* Mon Jun 18 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Make the -devel depend on the main package

* Sun Aug 06 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sat Jun 17 2000 Bill Nottingham <notting@redhat.com>
- add %%defattr for -devel

* Sat Jun 10 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_mandir}

* Thu May 04 2000 Trond Eivind Glomsrød <teg@redhat.com>
- first build
