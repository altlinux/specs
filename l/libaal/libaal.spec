%def_enable minimal

Name: libaal
Version: 1.0.5
Release: alt3.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Abstraction library for ReiserFS utilities
License: GPLv2
Group: System/Kernel and hardware

URL: http://www.kernel.org/pub/linux/utils/fs/reiser4/
Source0: http://www.kernel.org/pub/linux/utils/fs/reiser4/libaal/libaal-%version.tar.bz2

# c++ not needed for compilation but configure insist on its presence :)
# Automatically added by buildreq on Tue Mar 16 2010
BuildRequires: gcc-c++

%description
This is a library that provides application abstraction mechanism.
It include device abstraction, libc independence code, etc.

%package devel
Summary: Headers and static libraries for developing with libaal.
Group: Development/C
Requires: libaal = %version-%release

%description devel
This package includes the headers and static libraries for developing
with the libaal library.

%if_enabled minimal
%package minimal
Summary: Minimal abstraction library for ReiserFS utilities
Group: System/Kernel and hardware

%description minimal
This is a minimal library that provides application abstraction mechanism.
It include device abstraction, libc independence code, etc.

%package minimal-devel
Summary: Headers and static libraries for developing with libaal.
Group: Development/C
Requires: libaal-minimal = %version-%release libaal-devel = %version-%release

%description minimal-devel
This package includes the headers and static libraries for developing
with the minimal libaal library.
%endif

%prep
%setup

%build
%configure --libdir=/%_lib \
%if_enabled minimal
	--enable-libminimal
%else
	--disable-libminimal --disable-memory-manager
%endif

%make_build

%install
%makeinstall_std

# Static libraries and library symlinks not needed to be in %_lib/
# Relocate them to %_libdir/.
install -d %buildroot%_libdir
for f in %buildroot/%_lib/*.so; do
        v="$(readlink -n "$f")"
        ln -sf ../../%_lib/"$v" "$f"
done
mv %buildroot/%_lib/*.a %buildroot%_libdir/
mv %buildroot/%_lib/*.so %buildroot%_libdir/

%files
# COPYING contains information other than GPL text, so it should be packaged
%doc COPYING
/%_lib/libaal-1.0.so*

%files devel
%_libdir/libaal.so*
%_libdir/libaal.*a
%_includedir/aal
%_datadir/aclocal/libaal.m4

%if_enabled minimal
%files minimal
/%_lib/libaal-minimal.so.*

%files minimal-devel
%_libdir/libaal-minimal.so
%_libdir/libaal-minimal.*a
%endif

%changelog
* Sun Nov 14 2010 Denis Smirnov <mithraen@altlinux.ru> 1.0.5-alt3.1
- rebuild (with the help of girar-nmu utility)

* Tue Mar 16 2010 Victor Forsiuk <force@altlinux.org> 1.0.5-alt3
- Spec cleaning, updated URL etc.
- Remove explicit debug build enabling (this triggered disabling optimization
  flags in rpm macro substitution).

* Thu Aug 17 2006 Sergey Ivanov <seriv@altlinux.org> 1.0.5-alt2
- fix bug #9885

* Fri Aug 12 2005 Sergey Ivanov <seriv@altlinux.ru> 1.0.5-alt1
- updated to new version from namesys.com

* Mon Feb 21 2005 Sergey Ivanov <seriv@altlinux.ru> 1.0.4-alt1
- new version from namesys.com

* Sat Dec 11 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.3-alt1
- new version from namesys.com, includes:
- a lot of bug fixes,
- correct handling of super block backups,
- recovery according to the super block backups,
- demos/busy is a reiser4progs-busy-box program that is able
  to create/remove/copy/read/ls/etc on reiser4 working through
  libreiser4, without kernel reiser4 support.

  It happened that the previous super block backups were created 
  with a mistake and to resync them now you need to run
	fsck.reiser4 --build-sb <device>

* Wed Nov 17 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.2-alt2
- [#5222] (*.so should be installed into /lib/, not /usr/lib/),
  *-minimal libs moved to separate package, removed false g77 dependency.

* Tue Oct 26 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.2-alt1
- version 1.0.2; descriptions, files and options taken from libaal.spec from sourcces package

* Wed Aug 25 2004 Sergey Ivanov <seriv@altlinux.ru> 1.0.0-alt1
- initial build
