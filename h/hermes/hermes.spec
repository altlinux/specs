Name: hermes
Version: 1.3.3
Release: alt5

Summary: Hermes pixel format conversion library
License: LGPL
Group: System/Libraries
Url: http://clanlib.org/hermes

Source: http://dark.x.dtu.dk/~mbn/clanlib/download/Hermes-%version.tar.bz2

Patch0: Hermes-1.3.3-64bit.patch
Patch1: Hermes-1.3.3-debian.patch

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

%description
HERMES is a library designed to convert a source buffer with a specified pixel
format to a destination buffer with possibly a different format at the maximum
possible speed.

%package -n lib%name
Summary: Hermes pixel format conversion library
Group: System/Libraries
Provides: %name = %version
Obsoletes: %name

%description -n lib%name
HERMES is a library designed to convert a source buffer with a specified pixel
format to a destination buffer with possibly a different format at the maximum
possible speed.

On x86 and MMX architectures, handwritten assembler routines are taking over
the job and doing it lightning fast.

On top of that, HERMES provides fast surface clearing, stretching and some
dithering. Supported platforms are basically all that have an ANSI C compiler
as there is no platform specific code but those are supported: DOS, Win32
(Visual C), Linux, FreeBSD (IRIX, Solaris are on hold at the moment), some BeOS
support.

%package -n lib%name-devel
Summary: Headers for developing programs that will use hermes.
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package -n lib%name-devel-static
Summary: Static libraries for developing programs that will use hermes.
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static libraries for the %name

%prep
%setup -q -n Hermes-%version
%patch0 -p1
%patch1 -p1

%build
# Because of x86 assembler code, text relocations cannot be eliminated completely.
# As far as speed is first for this package, that's ok.
# Alternativelly, --disable-x86asm configure option can be used.
#set_verify_elf_method textrel=relaxed

%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure %{subst_enable static} --disable-x86asm
%make_build

%install
%makeinstall

%files -n lib%name
%doc AUTHORS TODO TODO.conversion
%_libdir/lib*.so.*

%files -n lib%name-devel
%doc docs/api/*.htm*
%_includedir/*
%_libdir/*.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.3.3-alt5
- apply patch from repocop

* Fri Feb 23 2007 Igor Zubkov <icesik@altlinux.org> 1.3.3-alt4
- build with --disable-x86asm
- remove set_verify_elf_method textrel=relaxed

* Fri Feb 23 2007 Igor Zubkov <icesik@altlinux.org> 1.3.3-alt3
- sync with FC6 package (Hermes-1.3.3-12.fc6.src.rpm)

* Wed Dec 24 2003 Alexey Tourbin <at@altlinux.ru> 1.3.3-alt2
- Do not package .la files.
- Do not package lib%name-devel-static by default.
- verify_elf_method: textrel=relaxed because of x86 assembler code.

* Thu Oct 02 2003 Stanislav Ievlev <inger@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue Dec 03 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.3.2-ipl9mdk
- Rebuilt in new environment
- Added buildrequires

* Wed Mar 13 2002 Stanislav Ievlev <inger@altlinux.ru> 1.3.2-ipl8mdk
- Rebuilt
- Cleanup spec
- Move static libraries into separate package

* Fri Feb  9  2001 Kostya Timoshenko <kt@petr.kz> 1.3.2-ipl7mdk
- change tag Group

* Tue Jan 30 2001 Kostya Timoshenko <kt@petr.kz> 1.3.2-ipl6mdk
- change name to libhermes

* Wed Dec 27 2000 Kostya Timoshenko <kt@petr.kz>
- Rebuild for RE

* Mon Nov 27 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.3.2-5mdk
- new lib policy

* Tue Nov  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.3.2-4mdk
- provides Hermes for compatibility

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.3.2-3mdk
- change name to hermes (e.g. uppercase names suck)

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.3.2-2mdk
- automatically added packager tag

* Mon Jul 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.3.2-1mdk
- 1.3.2

* Tue Jul 18 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.3.1-5mdk
- BM

* Mon Jul 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.3.1-4mdk
- macros

* Mon Jul 10 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.3.1-3mdk
- bzip2 sources

* Sat Jul 01 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.3.1-2mdk
- makeinstall macro

* Wed May 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.3.1-1mdk
- took SRPM from Hermes web site
- (a lot of) Mandrake adaptations including split between main and devel
