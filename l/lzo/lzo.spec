Name: lzo
Version: 2.10
Release: alt2

Summary: Data compression library with very fast (de)compression
License: GPL-2.0-or-later
Group: System/Libraries
Url: https://www.oberhumer.com/opensource/lzo/
# https://www.oberhumer.com/opensource/lzo/download/lzo-%version.tar.gz
Source: %name-%version.tar

%def_disable static

%description
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory.

In addition there are slower compression levels achieving a quite
competitive compression ratio while still decompressing at
this very high speed.

%package -n liblzo2
Summary: Data compression library with very fast (de)compression
Group: System/Libraries

%description -n liblzo2
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory.

In addition there are slower compression levels achieving a quite
competitive compression ratio while still decompressing at
this very high speed.

%package -n liblzo2-devel
Summary: Development files for the LZO library
Group: Development/C

%description -n liblzo2-devel
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory.

In addition there are slower compression levels achieving a quite
competitive compression ratio while still decompressing at
this very high speed.

This package contains files needed to develop programs that use
the LZO library.

%package -n liblzo2-devel-static
Summary: Static %name library
Group: Development/C
Requires: liblzo2-devel

%description -n liblzo2-devel-static
LZO is a portable lossless data compression library written in ANSI C.
It offers pretty fast compression and very fast decompression.
Decompression requires no memory.

In addition there are slower compression levels achieving a quite
competitive compression ratio while still decompressing at
this very high speed.

This package contains the static LZO library needed to develop
statically linked programs that use the LZO library.

%prep
%setup
find asm -name '*.o' -delete
sed -i 's/\$host_cpu-\$ac_cv_sizeof_void_p/$target_cpu-$ac_cv_sizeof_void_p/' \
	configure{.ac,}

%build
%{?_enable_static:%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}}
%add_optflags -fvisibility=hidden
%define docdir %_docdir/liblzo2
%configure %{subst_enable static} --enable-shared --docdir=%docdir --disable-silent-rules
printf '%s\n' \
	'#undef __LZO_EXPORT1' \
	'#define __LZO_EXPORT1 __attribute__((__visibility__("default")))' \
	>> config.h
%make_build

%install
%makeinstall_std

# Relocate shared library from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
        t=$(readlink -v "$f")
        ln -rsnf %buildroot/%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

%check
%make_build -k check

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%files -n liblzo2
/%_lib/liblzo2.so.2*
%docdir/

%files -n liblzo2-devel
%_includedir/lzo/
%_libdir/liblzo2.so
%_pkgconfigdir/lzo2.pc

%if_enabled static
%files -n liblzo2-devel-static
%_libdir/liblzo2.a
%endif #static

%changelog
* Thu Aug 26 2021 Dmitry V. Levin <ldv@altlinux.org> 2.10-alt2
- Disabled build and packaging of the static library.

* Sat Mar 16 2019 Dmitry V. Levin <ldv@altlinux.org> 2.10-alt1
- 2.08 -> 2.10
- Restricted the list of global symbols exported by the library.
- Relocated shared library from %_libdir/ to /%_lib/ (closes: #36272).

* Tue Jul 15 2014 Dmitry V. Levin <ldv@altlinux.org> 2.08-alt1
- Updated to 2.08 (fixes CVE-2014-4607).
- Cleaned up specfile.

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.06-alt1
- 2.05 -> 2.06
- rebuilt as plain src.rpm

* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 2.05-alt1
- 2.04 -> 2.05

* Fri Mar 04 2011 Alexey Tourbin <at@altlinux.ru> 2.04-alt1.1
- rebuilt for debuginfo

* Fri Dec 17 2010 Alexey Tourbin <at@altlinux.ru> 2.04-alt1
- 2.03 -> 2.04

* Mon Oct 04 2010 Alexey Tourbin <at@altlinux.ru> 2.03-alt2.1
- rebuilt

* Sun Nov 23 2008 Alexey Tourbin <at@altlinux.ru> 2.03-alt2
- rebuilt with gcc-4.3
- removed ldconfig scriptlets

* Sat Aug 09 2008 Alexey Tourbin <at@altlinux.ru> 2.03-alt1
- 2.02 -> 2.03

* Sun Mar 26 2006 Andrey Brindeew <abr@altlinux.org> 2.02-alt1
- 2.02 released as separate package due ugly soname change
  procedure. Old version still available under liblzo name.
