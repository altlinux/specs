%define processor_arch arm
%define target %processor_arch-none-eabi
%define _libexecdir /usr/libexec

Name: arm-none-eabi-binutils
Version: 2.30
Release: alt1
Summary: GNU Binutils for cross-compilation for %target target
Group: Development/Tools
# Most of the sources are licensed under GPLv3+ with these exceptions:
# LGPLv2+ bfd/hosts/x86-64linux.h, include/demangle.h, include/xregex2.h,
# GPLv2+  gprof/cg_print.h
# BSD     gprof/cg_arcs.h, gprof/utils.c, ld/elf-hints-local.h,
# Public Domain libiberty/memmove.c
License: GPLv2+ and GPLv3+ and LGPLv2+ and BSD
Url: http://www.codesourcery.com/sgpp/lite/%processor_arch

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

Source1: README.alt
BuildRequires: flex bison cloog
BuildRequires: texinfo perl-podlators

%description
This is a cross-compilation version of GNU Binutils, which can be used to
assemble and link binaries for the %target platform.

Binutils is a collection of binary utilities, including ar (for
creating, modifying and extracting from archives), as (a family of GNU
assemblers), gprof (for displaying call graph profile data), ld (the
GNU linker), nm (for listing symbols from object files), objcopy (for
copying and translating object files), objdump (for displaying
information from object files), ranlib (for generating an index for
the contents of an archive), readelf (for displaying detailed
information about binary files), size (for listing the section sizes
of an object or archive file), strings (for listing printable strings
from files), strip (for discarding symbols), and addr2line (for
converting addresses to file and line).

%prep
%setup
cp -p %SOURCE1 .
rm -rf gdb sim

%build
./configure --target=%target \
            --enable-interwork \
            --enable-multilib \
            --enable-plugins \
            --disable-nls \
            --disable-shared \
            --disable-threads \
            --with-gcc --with-gnu-as --with-gnu-ld \
            --prefix=%_libexecdir \
            --bindir=%_bindir \
            --libdir=%_libdir/%target \
            --mandir=%_mandir \
            --infodir=%_infodir \
            --with-docdir=%_docdir/%name \
            --disable-werror \
            --with-pkgversion="%version-%release" \
            --with-bugurl="https://bugzilla.altlinux.org/"

%make_build

%check
make check

%install
%makeinstall_std
# these are for win targets only
rm %buildroot%_man1dir/%target-{dlltool,nlmconv,windres}.1
# we don't want these as we are a cross version
rm -r %buildroot%_infodir

%files
%doc COPYING* ChangeLog README.alt
%_libexecdir/%target
%_bindir/%target-*
%_man1dir/%target-*.1.*

%changelog
* Tue Apr 17 2018 Anton Midyukov <antohami@altlinux.org> 2.30-alt1
- New version 2.30

* Fri Jun 30 2017 Anton Midyukov <antohami@altlinux.org> 2.27-alt1
- Initial build for ALT Sisyphus.
