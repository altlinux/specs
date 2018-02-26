%define __strip %_mingw32_strip
%define __objdump %_mingw32_objdump

Name: mingw32-pthreads
Version: 2.9.0
Release: alt1
Summary: MinGW pthread library

%define crazy_version %(echo %version|tr . -)

License: LGPLv2+
Group: System/Libraries
Url: http://sourceware.org/pthreads-win32/
Packager: Boris Savelev <boris@altlinux.org>

#Source: ftp://sourceware.org/pub/pthreads-win32/pthreads-w32-%crazy_version-release.tar.gz
Source: %name-%version.tar

BuildArch: noarch

Patch: mingw32-pthreads-2.8.0-use-wine-for-tests.patch
Patch1: mingw32-pthreads-2.8.0-no-failing-tests.patch
Patch2: add_include.patch

#Xming patches
Patch11: GNUmakefile.patch
Patch12: implement.h.patch
Patch13: need_errno.h.patch
Patch14: pthread.h.patch
Patch15: pthread_mutex_trylock.c.patch
Patch16: pthread_mutex_unlock.c.patch
Patch17: version.rc.patch

BuildRequires: mingw32-filesystem >= 49
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: rpm-build-mingw32

%description
The POSIX 1003.1-2001 standard defines an application programming
interface (API) for writing multithreaded applications. This interface
is known more commonly as pthreads. A good number of modern operating
systems include a threading library of some kind: Solaris (UI)
threads, Win32 threads, DCE threads, DECthreads, or any of the draft
revisions of the pthreads standard. The trend is that most of these
systems are slowly adopting the pthreads standard API, with
application developers following suit to reduce porting woes.

Win32 does not, and is unlikely to ever, support pthreads
natively. This project seeks to provide a freely available and
high-quality solution to this problem.

%prep
%setup

%patch0 -p1
%patch1 -p1
%patch2 -p2

%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1

%build
%_mingw32_make clean
%_mingw32_make CROSS=%_mingw32_host- OPT='%_mingw32_cflags' GC-inlined
%_mingw32_make clean
%_mingw32_make CROSS=%_mingw32_host- OPT='%_mingw32_cflags' GCE-inlined

%install
mkdir -p %buildroot%_mingw32_bindir
mkdir -p %buildroot%_mingw32_libdir
mkdir -p %buildroot%_mingw32_includedir

install -m 0755 *.dll %buildroot%_mingw32_bindir
install -m 0644 *.def %buildroot%_mingw32_bindir
install -m 0644 *.a %buildroot%_mingw32_libdir
install -m 0644 *.h %buildroot%_mingw32_includedir

# Create a symlink from libpthreadGC2.a to libpthread.a because of BZ #498616
ln -s libpthreadGC2.a %buildroot%_mingw32_libdir/libpthread.a

%files
%doc ANNOUNCE BUGS ChangeLog CONTRIBUTORS COPYING COPYING.LIB
%doc FAQ MAINTAINERS NEWS PROGRESS README README.NONPORTABLE TODO
%_mingw32_bindir/pthreadGC2.dll
%_mingw32_bindir/pthreadGCE2.dll
%_mingw32_bindir/pthread.def
%_mingw32_libdir/libpthread.a
%_mingw32_libdir/libpthreadGC2.a
%_mingw32_libdir/libpthreadGCE2.a
%_mingw32_includedir/*.h

%changelog
* Tue Jul 28 2009 Boris Savelev <boris@altlinux.org> 2.9.0-alt1
- update version

* Tue Jul 28 2009 Boris Savelev <boris@altlinux.org> 2.8.0-alt3
- add patches from Xming

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 2.8.0-alt2
- rebuild with new gcc

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 2.8.0-alt1
- initial build

* Fri May 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.8.0-8
- Create a symlink from libpthreadGC2.a to libpthread.a because of BZ #498616

* Fri Mar 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.8.0-7
- Move header files to system include directory.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.8.0-5
- Rebuild for mingw32-gcc 4.4

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.8.0-4
- Cleanup to the spec file, no functional changes.

* Mon Dec 29 2008 Levente Farkas <lfarkas@lfarkas.org> - 2.8.0-3
- minor cleanup

* Fri Oct 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.8.0-2
- Initial RPM release.
