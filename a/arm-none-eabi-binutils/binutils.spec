Name: arm-none-eabi-binutils
Version: 2.40
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

%define target arm-none-eabi
%define _libexecdir /usr/libexec

%prep
%setup

%build
./configure --target=%target \
            --host=%_configure_platform \
            --build=%_configure_platform \
            --enable-initfini-array \
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
%doc COPYING* ChangeLog
%_libexecdir/%target
%_bindir/%target-*
%_man1dir/%target-*.1.*

%changelog
* Thu Mar 02 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.40-alt1
- 2.40 released

* Wed Feb 01 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.39-alt1
- 2.39

* Sat Feb 06 2021 Anton Midyukov <antohami@altlinux.org> 2.35-alt1
- New version 2.35

* Sun Feb 10 2019 Anton Midyukov <antohami@altlinux.org> 2.32-alt1
- New version 2.32

* Mon Oct 01 2018 Anton Midyukov <antohami@altlinux.org> 2.30-alt1.2
- Update buildrequires

* Thu Sep 20 2018 Anton Midyukov <antohami@altlinux.org> 2.30-alt1.1
- First build for aarch64

* Tue Apr 17 2018 Anton Midyukov <antohami@altlinux.org> 2.30-alt1
- New version 2.30

* Fri Jun 30 2017 Anton Midyukov <antohami@altlinux.org> 2.27-alt1
- Initial build for ALT Sisyphus.
