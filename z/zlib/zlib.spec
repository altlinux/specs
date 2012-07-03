Name: zlib
Version: 1.2.5
Release: alt3

Summary: The zlib compression and decompression library
Summary(ru_RU.UTF-8): Библиотека сжатия данных zlib
License: zlib
Group: System/Libraries
Url: http://zlib.net/
# http://git.altlinux.org/gears/z/zlib.git
Source: %name-%version-%release.tar

# http://git.gnome.org/browse/libxml2/commit/?id=a7e79f28689c574e0bbef17f4cb3da00249181ff
Conflicts: libxml2 < 1:2.7.7

%def_disable asm

%package devel
Summary: Header files for developing apps which will use zlib
Summary(ru_RU.UTF-8): Файлы, необходимые для разработки приложений с использованием библиотеки сжатия данных zlib
Group: Development/C
Requires: %name = %version-%release
Requires: glibc-devel

%package devel-static
Summary: Static library for developing apps which will use zlib
Summary(ru_RU.UTF-8): Файлы, необходимые для разработки статических приложений с использованием библиотеки сжатия данных zlib
Group: Development/C
Requires: %name-devel = %version-%release

%package -n libminizip
Summary: Minizip zip file manipulation library
Group: System/Libraries
Requires: %name = %version-%release

%package -n libminizip-devel
Summary: Development files for the minizip librar
Group: Development/C
Requires: libminizip = %version-%release
Requires: %name-devel = %version-%release

%description
The zlib compression library provides in-memory compression and
decompression functions, including integrity checks of the uncompressed
data.  This version of the library supports only one compression method
(deflation), but other algorithms may be added later, which will have
the same stream interface.  The zlib library is used by many different
system programs.

%description devel
This package contains the development files needed to develop programs
that use the zlib compression and decompression library.

%description devel-static
This package contains the static library needed to develop statically
linked programs that use the zlib compression and decompression library.

%description -n libminizip
This package contains minizip zip file manipulation shared library.

%description -n libminizip-devel
This package contains the development files needed to develop programs
that use the minizip zip file manipulation library.

%prep
%setup -n %name-%version-%release
sed -i 's/@PACKAGE_VERSION@/%version/' contrib/minizip/configure.ac

fgrep -B999 @ zlib.h >License
bzip2 -9k FAQ doc/algorithm.txt
iconv -fcp1252 -tutf8 < ChangeLog | bzip2 -9 > ChangeLog.bz2

%build
%define _optlevel 3

%if_enabled asm
	%add_optflags -Wa,--noexecstack -DASMV
%ifarch i686 pentium3 pentium4 athlon
	cp -p contrib/asm686/match.S .
%endif # i686 pentium3 pentium4 athlon
%ifarch x86_64
	cp -p contrib/amd64/amd64-match.S .
%endif # x86_64
%endif # enabled asm

%ifarch %ix86
%{!?_enable_debug:%add_optflags -momit-leaf-frame-pointer}
%endif # %ix86

CFLAGS="%optflags" ./configure --prefix=%prefix --libdir=%_libdir
%make_build %{?_enable_asm:OBJA=match.o PIC_OBJA=match.lo}

pushd contrib/minizip
mkdir m4
%autoreconf
%configure
%make_build
popd

%install
%makeinstall_std LDCONFIG=:
%makeinstall_std -C contrib/minizip

# Relocate shared library from %_libdir/ to /%_lib/
mkdir %buildroot/%_lib
for f in %buildroot%_libdir/libz.so; do
	t=$(readlink "$f")
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/libz.so.* %buildroot/%_lib/

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
install -pm644 License README {FAQ,ChangeLog,doc/algorithm.txt}.bz2 example.c minigzip.c \
	%buildroot%docdir/
cp -a examples %buildroot%docdir/

%check
make test

%files
/%_lib/libz.so.*
%dir %docdir
%docdir/License
%docdir/README

%files devel
%_libdir/libz.so
%_includedir/z*
%_pkgconfigdir/zlib.pc
%_mandir/man?/*
%docdir
%exclude %docdir/License
%exclude %docdir/README

%files devel-static
%_libdir/libz.a

%files -n libminizip
%_libdir/libminizip.so.*

%files -n libminizip-devel
%_libdir/libminizip.so
%_includedir/minizip/
%_pkgconfigdir/minizip.pc

%changelog
* Tue Jul 19 2011 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt3
- Packaged libminizip (closes: #25866).

* Mon Feb 07 2011 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt2
- Rebuilt for debuginfo.

* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.5-alt1
- Updated to 1.2.5 (closes: #21185).

* Thu Oct 07 2010 Alexey Tourbin <at@altlinux.ru> 1.2.3-alt5.1
- Rebuilt for soname set-versions.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt5
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Mon Apr 09 2007 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt4
- Backported upstream fixes to compressBound() and deflateBound().

* Sun Oct 23 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt3
- Rediffed patches.

* Tue Aug 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt2
- Restricted list of global symbols exported by the library.

* Fri Jul 22 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.3-alt1
- Updated to 1.2.3 (fixes CAN-2005-1849).
- Updated patches and ELF versioning.

* Fri Jul 01 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.2.3-alt1
- Updated to 1.2.2.3
- Updated patches and ELF versioning.
- Applied patch from upstream which fixes CAN-2005-2096.

* Sat Feb 19 2005 Dmitry V. Levin <ldv@altlinux.org> 1.2.2.2-alt2
- Updated URL per Mark Adler suggestion.
- Packaged some documentation in main subpackage.

* Fri Dec 31 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.2.2-alt1
- Updated to 1.2.2.2

* Mon Nov 01 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.2.1-alt1
- Updated to 1.2.2.1

* Wed Oct 06 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.2-alt1
- Updated to 1.2.2

* Thu Sep 23 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.1.2-alt1
- Updated to 1.2.1.2

* Tue Aug 24 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.1.1-alt3
- Fixed inflate bugs (CAN-2004-0797).
- Added multilib support (#4899).

* Tue May 04 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.1.1-alt2
- Rebuilt with glibc-2.3.x.

* Sun Feb 22 2004 Dmitry V. Levin <ldv@altlinux.org> 1.2.1.1-alt1
- Updated to 1.2.1.1
- Updated patches.
- Added ELF versioning for new functions.
- Disabled asm optimization for i586 due to worse performance.
- Do not package zutil.h header.

* Thu May 01 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt4
- gzio: fixed potential segfaults in gzerror().
- Don't set strip methods explicitly.
- When debug is enabled, do not add optimization flags.

* Tue Feb 25 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt3
- Corrected a potential buffer overflow in gzprintf(),
  patch from Owl, thanks to Bugtraq postings by Crazy Einstein,
  Richard Kettlewell, and Carlo Marcelo Arenas Belon.

* Sat Aug 31 2002 Dmitry V. Levin <ldv@altlinux.org> 1.1.4-alt2
- Updated %%post/%%postun scripts.
- Turned absolute symlinks into relative.
- Build the package only if test succeed (rh).
- Updated devel-static requirements.

* Tue Mar 12 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.1.4-alt1
- 1.1.4

* Mon Feb 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.1.3-ipl15mdk
- Built with -momit-leaf-frame-pointer.

* Fri Feb 08 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.1.3-ipl14mdk
- Error handling fixes for inflate (by Owen Taylor).

* Fri Jun 22 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.1.3-ipl13mdk
- Fixed URL.

* Mon Jun 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.1.3-ipl12mdk
- Moved static library to devel-static subpackage.
- Fixed shared library link command.
- Updated requires.

* Mon Feb 19 2001 Dmitry V. Levin <ldv@fandra.org> 1.1.3-ipl11mdk
- Explicitly set strip methods.

* Wed Dec 27 2000 Dmitry V. Levin <ldv@fandra.org> 1.1.3-ipl10mdk
- Commented out translations in specfile for a while.

* Thu Aug 31 2000 Dmitry V. Levin <ldv@fandra.org> 1.1.3-ipl9mdk
- Fixed bug in gzread transparent processing.
- Enabled asm optimization if available.
- RE adaptions.

* Fri Feb 25 2000 Dmitry V. Levin <ldv@fandra.org>
- Fandra adaptions.

* Mon Jul 27 1998 Jeff Johnson <jbj@redhat.com>
- upgrade to 1.1.3

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.1.2
- buildroot

* Tue Oct 07 1997 Donnie Barnes <djb@redhat.com>
- added URL tag (down at the moment so it may not be correct)
- made zlib-devel require zlib

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
