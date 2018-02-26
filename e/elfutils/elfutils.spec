Name: elfutils
Version: 0.153
Release: alt1

Summary: A collection of utilities and DSOs to handle compiled objects
License: GPLv2 with exceptions
Group: Development/C
URL: http://fedorahosted.org/elfutils/

# http://fedorahosted.org/releases/e/l/elfutils/%version/%name-%version.tar.bz2
Source: %name-%version.tar

Patch1: elfutils-0.153-rh-portability.patch
Patch2: elfutils-0.153-rh-robustify.patch
Patch3: elfutils-0.147-alt-findtextrel.patch
Patch4: elfutils-0.147-alt-osabi.patch
Patch5: elfutils-0.147-alt-bss.patch

Requires: libelf = %version-%release

%def_enable static
%def_disable check

BuildRequires: bzlib-devel flex liblzma-devel zlib-devel
%{?_enable_check:BuildRequires: /proc}

%define _gnu %nil
%define _configure_script ../configure
%define _programprefix eu-
%define buildtarget build-%_target_platform

%description
Elfutils is a collection of utilities, including ld (a linker), nm
(for listing symbols from object files), size (for listing the section
sizes of an object or archive file), strip (for discarding symbols),
readelf (to see the raw ELF file structures), and elflint (to check for
well-formed ELF files).  Also included are numerous helper libraries
which implement DWARF, ELF, and machine-specific ELF handling.

%package devel
Summary: Development libraries to handle compiled objects
Group: Development/C
Requires: %name = %version-%release
Requires: libelf-devel = %version-%release

%description devel
This package contains the libraries to create applications for
handling compiled objects.  libebl provides some higher-level ELF access
functionality.  libdw provides access to the DWARF debugging information.
libasm provides a programmable assembler interface.

%package -n libelf
Summary: Library to read and write ELF files
Group: System/Libraries

%description -n libelf
This package provides a DSO which allows reading and writing ELF files
on a high level.  Third party programs depend on this package to read
internals of ELF files.  The programs of the elfutils package use it
also to generate new ELF files.

%package -n libelf-devel
Summary: Development libelf library
Group: Development/C
Requires: libelf = %version-%release

%description -n libelf-devel
This package contains the library to create applications for handling
compiled objects.  libelf allows you to access the internals of the ELF
object file format, so you can see the different sections of an ELF file.

%package -n libelf-devel-static
Summary: Static libelf library
Group: Development/C
Requires: libelf-devel = %version-%release

%description -n libelf-devel-static
This package contains static library to create applications for handling
compiled objects.  libelf allows you to access the internals of the ELF
object file format, so you can see the different sections of an ELF file.

%prep
%setup -q
#patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# Remove flex-generated files.
rm libcpu/i386_lex.c src/ldlex.c

# Disable -Werror for a while.
#sed -i 's/ -Werror / /' tests/Makefile*

bzip2 -9k NEWS
find -type f -name \*.sh -not -perm -0100 -print0 |
	xargs -r0 chmod +x --

%build
%add_optflags -fexceptions
rm -rf %buildtarget
mkdir %buildtarget
cd %buildtarget
%configure --enable-dependency-tracking \
	--program-prefix=%_programprefix \
	--enable-shared %{subst_enable static}
%make_build

%install
%makeinstall_std -C %buildtarget
%find_lang %name

%check
LD_LIBRARY_PATH=%buildroot%_libdir make -k check -C %buildtarget

%files
%_bindir/eu-addr2line
%_bindir/eu-ar
%_bindir/eu-elfcmp
%_bindir/eu-elflint
%_bindir/eu-findtextrel
%_bindir/eu-make-debug-archive
%_bindir/eu-nm
%_bindir/eu-objdump
%_bindir/eu-ranlib
%_bindir/eu-readelf
%_bindir/eu-size
%_bindir/eu-strings
%_bindir/eu-strip
%_bindir/eu-unstrip
%exclude %_bindir/eu-ld
%_libdir/libasm-*.so
%_libdir/libdw-*.so
%_libdir/libasm*.so.*
%_libdir/libdw*.so.*
%_libdir/elfutils

%files devel
%_includedir/dwarf.h
%_includedir/elfutils
%_libdir/libasm.so
%_libdir/libdw.so
%exclude %_libdir/libasm.a
%exclude %_libdir/libdw.a
%exclude %_libdir/libebl.a

%files -n libelf -f %name.lang
%doc AUTHORS EXCEPTION NEWS.bz2 NOTES README THANKS
%_libdir/libelf-*.so
%_libdir/libelf*.so.*

%files -n libelf-devel
%_libdir/libelf.so
%_includedir/libelf.h
%_includedir/gelf.h
%_includedir/nlist.h

%if_enabled static
%files -n libelf-devel-static
%_libdir/libelf.a
%endif

%changelog
* Sun Mar 25 2012 Dmitry V. Levin <ldv@altlinux.org> 0.153-alt1
- Updated to 0.153.

* Thu Mar 24 2011 Dmitry V. Levin <ldv@altlinux.org> 0.152-alt1
- Updated to 0.152.

* Tue Feb 08 2011 Dmitry V. Levin <ldv@altlinux.org> 0.151-alt2
- Rebuilt for debuginfo.

* Fri Jan 21 2011 Dmitry V. Levin <ldv@altlinux.org> 0.151-alt1
- Updated to 0.151.

* Thu Nov 18 2010 Dmitry V. Levin <ldv@altlinux.org> 0.149-alt2
- Rebuilt with liblzma.so.5.

* Tue Oct 19 2010 Dmitry V. Levin <ldv@altlinux.org> 0.149-alt1
- Updated to 0.149.

* Thu Jul 01 2010 Dmitry V. Levin <ldv@altlinux.org> 0.148-alt1
- Updated to 0.148.

* Wed May 26 2010 Alexey Tourbin <at@altlinux.ru> 0.147-alt2
- alt-osabi.patch: Handle STB_GNU_UNIQUE symbols with ELFOSABI_NONE.
- alt-bss.patch: Adjust segment flags with .bss (for klcc binaries).

* Mon May 24 2010 Dmitry V. Levin <ldv@altlinux.org> 0.147-alt1
- Updated to 0.147.

* Fri Mar 05 2010 Dmitry V. Levin <ldv@altlinux.org> 0.145-alt1
- Updated to 0.145.

* Thu Jan 28 2010 Dmitry V. Levin <ldv@altlinux.org> 0.144-alt1
- Updated to 0.144.

* Sun Dec 20 2009 Dmitry V. Levin <ldv@altlinux.org> 0.143-alt2
- Enhanced eu-findtextrel output.

* Fri Dec 18 2009 Dmitry V. Levin <ldv@altlinux.org> 0.143-alt1
- Updated to 0.143.
- Moved "make check" to %%check section.

* Tue Jun 02 2009 Dmitry V. Levin <ldv@altlinux.org> 0.141-alt1
- Updated to 0.141.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 0.137-alt2
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Sun Oct 26 2008 Dmitry V. Levin <ldv@altlinux.org> 0.137-alt1
- Updated to 0.137.

* Fri Nov 16 2007 Dmitry V. Levin <ldv@altlinux.org> 0.131-alt1
- Updated to 0.131.

* Sun Mar 25 2007 Dmitry V. Levin <ldv@altlinux.org> 0.126-alt1
- Updated to 0.126.

* Wed Oct 18 2006 Dmitry V. Levin <ldv@altlinux.org> 0.124-alt1
- Updated to 0.124.
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Sat Sep 16 2006 Dmitry V. Levin <ldv@altlinux.org> 0.123-alt1
- Updated to 0.123.

* Wed Jun 07 2006 Dmitry V. Levin <ldv@altlinux.org> 0.120-alt1
- Updated to 0.120.

* Mon Dec 05 2005 Dmitry V. Levin <ldv@altlinux.org> 0.116-alt1
- Updated to 0.116.

* Fri Oct 14 2005 Dmitry V. Levin <ldv@altlinux.org> 0.115-alt1
- Updated to 0.115.
- Create libelf-devel-static and package it by default.

* Sun Sep 04 2005 Dmitry V. Levin <ldv@altlinux.org> 0.114-alt1
- Updated to 0.114.

* Thu Jun 16 2005 Dmitry V. Levin <ldv@altlinux.org> 0.108-alt3
- Applied additional robustification of eu-strip and eu-readelf
  from RH's elfutils-0.108-5.

* Fri Jun 03 2005 Dmitry V. Levin <ldv@altlinux.org> 0.108-alt2
- Applied upstream fix for unsanitized input issues
  (CAN-2005-1704).

* Fri May 27 2005 Dmitry V. Levin <ldv@altlinux.org> 0.108-alt1
- Updated to 0.108.

* Thu Nov 11 2004 Dmitry V. Levin <ldv@altlinux.org> 0.97-alt1
- Built for ALT Linux.

* Sun Sep 26 2004 Jeff Johnson <jbj@redhat.com> 0.97-2
- upgrade to 0.97.

* Tue Aug 17 2004 Jakub Jelinek <jakub@redhat.com> 0.95-5
- upgrade to 0.96.

* Mon Jul  5 2004 Jakub Jelinek <jakub@redhat.com> 0.95-4
- rebuilt with GCC 3.4.x, workaround VLA + alloca mixing
  warning

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr  2 2004 Jeff Johnson <jbj@redhat.com> 0.95-2
- upgrade to 0.95.

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jan 16 2004 Jakub Jelinek <jakub@redhat.com> 0.94-1
- upgrade to 0.94

* Fri Jan 16 2004 Jakub Jelinek <jakub@redhat.com> 0.93-1
- upgrade to 0.93

* Thu Jan  8 2004 Jakub Jelinek <jakub@redhat.com> 0.92-1
- full version
- macroized spec file for GPL or OSL builds
- include only libelf under GPL plus wrapper scripts

* Wed Jan  7 2004 Jakub Jelinek <jakub@redhat.com> 0.91-2
- macroized spec file for GPL or OSL builds

* Wed Jan  7 2004 Ulrich Drepper <drepper@redhat.com>
- split elfutils-devel into two packages.

* Wed Jan  7 2004 Jakub Jelinek <jakub@redhat.com> 0.91-1
- include only libelf under GPL plus wrapper scripts

* Tue Dec 23 2003 Jeff Johnson <jbj@redhat.com> 0.89-3
- readelf, not readline, in %%description (#111214).

* Fri Sep 26 2003 Bill Nottingham <notting@redhat.com> 0.89-1
- update to 0.89 (fix eu-strip)

* Tue Sep 23 2003 Jakub Jelinek <jakub@redhat.com> 0.86-3
- update to 0.86 (fix eu-strip on s390x/alpha)
- libebl is an archive now; remove references to DSO

* Mon Jul 14 2003 Jeff Johnson <jbj@redhat.com> 0.84-3
- upgrade to 0.84 (readelf/elflint improvements, rawhide bugs fixed).

* Fri Jul 11 2003 Jeff Johnson <jbj@redhat.com> 0.83-3
- upgrade to 0.83 (fix invalid ELf handle on *.so strip, more).

* Wed Jul  9 2003 Jeff Johnson <jbj@redhat.com> 0.82-3
- upgrade to 0.82 (strip tests fixed on big-endian).

* Tue Jul  8 2003 Jeff Johnson <jbj@redhat.com> 0.81-3
- upgrade to 0.81 (strip excludes unused symtable entries, test borked).

* Thu Jun 26 2003 Jeff Johnson <jbj@redhat.com> 0.80-3
- upgrade to 0.80 (debugedit changes for kernel in progress).

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May 21 2003 Jeff Johnson <jbj@redhat.com> 0.79-2
- upgrade to 0.79 (correct formats for size_t, more of libdw "works").

* Mon May 19 2003 Jeff Johnson <jbj@redhat.com> 0.78-2
- upgrade to 0.78 (libdwarf bugfix, libdw additions).

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- debuginfo rebuild

* Thu Feb 20 2003 Jeff Johnson <jbj@redhat.com> 0.76-2
- use the correct way of identifying the section via the sh_info link.

* Sat Feb 15 2003 Jakub Jelinek <jakub@redhat.com> 0.75-2
- update to 0.75 (eu-strip -g fix)

* Tue Feb 11 2003 Jakub Jelinek <jakub@redhat.com> 0.74-2
- update to 0.74 (fix for writing with some non-dirty sections)

* Thu Feb  6 2003 Jeff Johnson <jbj@redhat.com> 0.73-3
- another -0.73 update (with sparc fixes).
- do "make check" in %%check, not %%install, section.

* Mon Jan 27 2003 Jeff Johnson <jbj@redhat.com> 0.73-2
- update to 0.73 (with s390 fixes).

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 22 2003 Jakub Jelinek <jakub@redhat.com> 0.72-4
- fix arguments to gelf_getsymshndx and elf_getshstrndx
- fix other warnings
- reenable checks on s390x

* Sat Jan 11 2003 Karsten Hopp <karsten@redhat.de> 0.72-3
- temporarily disable checks on s390x, until someone has
  time to look at it

* Thu Dec 12 2002 Jakub Jelinek <jakub@redhat.com> 0.72-2
- update to 0.72

* Wed Dec 11 2002 Jakub Jelinek <jakub@redhat.com> 0.71-2
- update to 0.71

* Wed Dec 11 2002 Jeff Johnson <jbj@redhat.com> 0.69-4
- update to 0.69.
- add "make check" and segfault avoidance patch.
- elfutils-libelf needs to run ldconfig.

* Tue Dec 10 2002 Jeff Johnson <jbj@redhat.com> 0.68-2
- update to 0.68.

* Fri Dec  6 2002 Jeff Johnson <jbj@redhat.com> 0.67-2
- update to 0.67.

* Tue Dec  3 2002 Jeff Johnson <jbj@redhat.com> 0.65-2
- update to 0.65.

* Mon Dec  2 2002 Jeff Johnson <jbj@redhat.com> 0.64-2
- update to 0.64.

* Sun Dec 1 2002 Ulrich Drepper <drepper@redhat.com> 0.64
- split packages further into elfutils-libelf

* Sat Nov 30 2002 Jeff Johnson <jbj@redhat.com> 0.63-2
- update to 0.63.

* Fri Nov 29 2002 Ulrich Drepper <drepper@redhat.com> 0.62
- Adjust for dropping libtool

* Sun Nov 24 2002 Jeff Johnson <jbj@redhat.com> 0.59-2
- update to 0.59

* Thu Nov 14 2002 Jeff Johnson <jbj@redhat.com> 0.56-2
- update to 0.56

* Thu Nov  7 2002 Jeff Johnson <jbj@redhat.com> 0.54-2
- update to 0.54

* Sun Oct 27 2002 Jeff Johnson <jbj@redhat.com> 0.53-2
- update to 0.53
- drop x86_64 hack, ICE fixed in gcc-3.2-11.

* Sat Oct 26 2002 Jeff Johnson <jbj@redhat.com> 0.52-3
- get beehive to punch a rhpkg generated package.

* Wed Oct 23 2002 Jeff Johnson <jbj@redhat.com> 0.52-2
- build in 8.0.1.
- x86_64: avoid gcc-3.2 ICE on x86_64 for now.

* Tue Oct 22 2002 Ulrich Drepper <drepper@redhat.com> 0.52
- Add libelf-devel to conflicts for elfutils-devel

* Mon Oct 21 2002 Ulrich Drepper <drepper@redhat.com> 0.50
- Split into runtime and devel package

* Fri Oct 18 2002 Ulrich Drepper <drepper@redhat.com> 0.49
- integrate into official sources

* Wed Oct 16 2002 Jeff Johnson <jbj@redhat.com> 0.46-1
- Swaddle.
