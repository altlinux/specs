Name: riscv32-none-elf-binutils
Version: 2.46.1
Release: alt1

Summary: GNU Binary Utility Development Utilities
License: GPLv3+
Group: Development/Other
Url: http://sourceware.org/binutils/

Source: %name-%version-%release.tar

BuildRequires: flex texinfo perl-podlators zlib-devel

%description
Binutils is a collection of binary utilities, including:
+ addr2line: converting addresses to file and line;
+ ar: creating modifying and extracting from archives;
+ nm: listing symbols from object files;
+ objcopy: copying and translating object files;
+ objdump: displaying information from object files;
+ ranlib: generating an index for the contents of an archive;
+ size: listing the section sizes of an object or archive file;
+ strings: listing printable strings from files;
+ strip: discarding symbols.

%define target riscv32-none-elf
%define _libexecdir /usr/libexec

%prep
%setup

%build
./configure --target=%target \
            --host=%_configure_platform \
            --build=%_configure_platform \
            --with-isa-spec=20191213 \
            --enable-multilib \
            --enable-plugins \
            --disable-nls \
            --disable-shared \
            --disable-threads \
            --with-gcc --with-gnu-as --with-gnu-ld \
            --disable-sim --without-sim \
            --with-system-zlib \
            --prefix=%_libexecdir \
            --bindir=%_bindir \
            --libdir=%_libdir/%target \
            --mandir=%_mandir \
            --infodir=%_infodir \
            --with-docdir=%_docdir/%name \
            --with-pkgversion="%version-%release" \
            --with-bugurl="https://bugzilla.altlinux.org/"

%make_build

%install
%makeinstall_std
# we don't want these as we are a cross version
rm -r %buildroot%_infodir

%files
%doc COPYING* ChangeLog binutils/NEWS
%_libexecdir/%target
%_bindir/%target-*
%_man1dir/%target-*.1.*

%changelog
* Wed Jun 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.46.1-alt1
- 2.46.1 released

* Fri Feb 13 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.46-alt1
- 2.46 released

* Wed Sep 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.45-alt1
- 2.45 released

* Wed Feb 05 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.44-alt1
- initial release

