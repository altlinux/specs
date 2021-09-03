
%define target_arch aarch64
%define target_kernel arm64
%define target_qemu_arch aarch64
%define target %target_arch-linux-gnu


Name: cross-toolchain-%target
Version: 20210831
Release: alt1
Summary: GCC cross-toolchain for %target
License: LGPL-2.1-or-later and LGPL-3.0-or-later and GPL-2.0-or-later and GPL-3.0-or-later and GPL-3.0-or-later with GCC-exception-3.1
Group: Development/C

ExclusiveArch: x86_64

%define gcc_version %{get_version gcc-source}
%define gcc_branch %(v=%gcc_version; v=${v%%%%.*}; echo $v)
%define binutils_version %{get_version binutils-source}
%define glibc_version %{get_version glibc-source}
%define kernel_version 5.10

%define sysroot %prefix/lib/%target/sys-root
%define target_ld_linux /lib64/ld-linux-aarch64.so.1


BuildPreReq: gcc-c++
BuildPreReq: libmpc-devel libmpfr-devel libgmp-devel zlib-devel
BuildPreReq: coreutils flex bison makeinfo findutils
# Linux' headers_install uses rsync
BuildPreReq: rsync
BuildRequires(pre): gcc-source
BuildRequires(pre): binutils-source
BuildRequires(pre): glibc-source
BuildPreReq: kernel-source-%kernel_version
BuildRequires: qemu-user-static-%target_qemu_arch
BuildRequires: python3

%description
GCC cross-toolchain for %target

%define _libexecdir /usr/libexec

%package -n gcc-%target
Version: %gcc_version
Summary: %target_arch-targeted GCC cross-compiler
Group: Development/C
Requires: gcc-%target-static = %gcc_version
Requires: binutils-%target = %binutils_version
Requires: cross-glibc-%target_arch = %glibc_version

%description -n gcc-%target
%target_arch-targeted GCC cross-compiler

%package -n gcc-%target-static
Version: %gcc_version
Summary: %target_arch-targeted GCC cross-compiler, static libraries
Group: Development/C

%description -n gcc-%target-static
%target_arch-targeted GCC cross-compiler, static libraries

%package -n binutils-%target
Version: %binutils_version
Summary: %target_arch-targeted binutils (linker, assembler, etc)
Group: Development/C

%description -n binutils-%target
%target_arch-targeted binutils (linker, assembler, objdump, etc)

%package -n cross-glibc-%target_arch
Version: %glibc_version
Summary: %target_arch-targeted cross-glibc
Group: Development/C
Requires: cross-glibc-static-%target_arch
BuildArch: noarch

%description -n cross-glibc-%target_arch
glibc for %target_arch. Should be used for cross-compilation only

%package -n cross-glibc-static-%target_arch
Version: %glibc_version
Summary: %target_arch-targeted cross-glibc, static libraries
Group: Development/C
BuildArch: noarch

%description -n cross-glibc-static-%target_arch
static glibc for %target_arch. Should be used for cross-compilation only

%prep
%setup -cT
mkdir -p -m755 linux binutils gcc glibc

find /usr/src/gcc-source -type f -name 'gcc-*.tar' | xargs -I {} -n1 tar -x --strip-components=1 -f {} -C gcc
find /usr/src/binutils-source -type f -name 'binutils-*.tar' | xargs -I {} -n1 tar -x --strip-components=1 -f {} -C binutils
find /usr/src/kernel/sources -type f -name 'kernel-source-*.tar' | xargs -I {} -n1 tar -x --strip-components=1 -f {} -C linux
find /usr/src/glibc-source -type f -name 'glibc-*.tar' | xargs -I {} -n1 tar -x --strip-components=1 -f {} -C glibc

rm -rf stage

%build
mkdir -p obj_binutils
mkdir -p obj_gcc
mkdir -p obj_kheaders
mkdir -p obj_glibc
mkdir -p -m755 stage%prefix/bin
export PATH=`pwd`/stage%prefix/bin:$PATH
stagedir=`pwd`/stage

# kernel headers
%_make_bin -j%__nprocs \
	-C linux \
	O=`pwd`/obj_kheaders \
	ARCH=%target_kernel \
	INSTALL_HDR_PATH=${stagedir}%sysroot/usr \
	headers_install

# XXX: avoid %%configure for it puts $target libraries into /usr/lib64
cd obj_binutils
../binutils/configure \
	--target=%target \
	--host=%{_configure_platform} \
	--build=%{_configure_platform} \
	--prefix=%prefix \
	--disable-bootstrap \
	--disable-multiarch \
	--disable-multilib \
	--disable-werror \
	--disable-shared \
	--disable-nls \
	--with-sysroot=%sysroot \
	--with-build-sysroot=${stagedir}%sysroot \
	--with-system-zlib \
	--enable-plugins \
	--enable-gold=yes \
	--enable-ld=default \
	--enable-64-bit-bfd \
	--enable-relro \
	--enable-textrel-check=warning

%make_build
# XXX: avoid makeinstall for it puts $target libraries into /usr/lib64
%make_install install DESTDIR=${stagedir}

# N.B.: this builds GCC in a single stage (but not all target at once)
cd ../obj_gcc
# XXX: avoid %%configure puts $target libraries in /usr/lib64
../gcc/configure \
	--target=%target \
	--host=%{_configure_platform} \
	--build=%{_configure_platform} \
	--prefix=%prefix \
	--disable-bootstrap \
	--disable-multiarch \
	--disable-multilib \
	--disable-werror \
	--with-sysroot=%sysroot \
	--with-build-sysroot=${stagedir}%sysroot \
	--with-gcc-major-version-only \
	--enable-languages=c,c++ \
	--enable-version-specific-runtime-libs \
	--disable-nls \
	--disable-libsanitizer \
	--with-system-zlib

%make_build all-gcc
# XXX: avoid makeinstall for it puts $target libraries into /usr/lib64
%make_install install-gcc DESTDIR=${stagedir}

cd ../obj_glibc
# XXX: avoid %%configure since it puts target libraries/binaries into /usr/lib64
# Note: glibc's is a library, so $host must be the same as $target
../glibc/configure \
	--host=%target \
	--target=%target \
	--build=%{_configure_platform} \
	--prefix=%prefix \
	--with-sysroot=%sysroot \
	--with-build-sysroot=${stagedir}%sysroot \
	--with-headers=${stagedir}%sysroot/usr/include \
	--with-lib=${stagedir}%sysroot/usr/lib \
	--disable-multilib \
	--disable-crypt \
	libc_cv_forced_unwind=yes

# glibc: headers, C runtime
%_make_bin -j%__nprocs install-bootstrap-headers=yes install-headers DESTDIR=${stagedir}%sysroot
%_make_bin -j%__nprocs csu/subdir_lib
install -d -m755 ${stagedir}%sysroot/usr/lib
install csu/crt1.o csu/crti.o csu/crtn.o ${stagedir}%sysroot/usr/lib
%target-gcc -nostdlib -nostartfiles -shared -x c /dev/null -o "${stagedir}%sysroot/usr/lib/libc.so"
touch ${stagedir}/%sysroot/usr/include/gnu/stubs.h
touch ${stagedir}/%sysroot/usr/include/bits/stdio_lim.h

# libgcc
cd ../obj_gcc
%make_build all-target-libgcc
# XXX: avoid makeinstall since it puts target libs into /usr/lib64
%make_install install-target-libgcc DESTDIR=${stagedir}

# finish off glibc
cd ../obj_glibc
%make_build
# XXX: avoid makeinstall since it puts target libs into /usr/lib64
# Note: target glibc **must** be installed into sysroot to prevent
# native compilers from using it by default
%make_install install DESTDIR=${stagedir}%sysroot

# finish off gcc (g++, libstdc++, libssp, whatever)
cd ../obj_gcc
%make_build
# XXX: avoid makeinstall since it puts target libs into /usr/lib64
%make_install install DESTDIR=${stagedir}

%install

export PATH=`pwd`/stage%prefix/bin:$PATH

%_make_bin -j%__nprocs \
	-C linux \
	O=`pwd`/obj_kheaders \
	ARCH=%target_kernel \
	INSTALL_HDR_PATH=%buildroot%sysroot/usr \
	headers_install

cd obj_binutils
%make_install install DESTDIR=%buildroot tooldir=%prefix/libexec/gcc/%target

cd ../obj_glibc
%make_install install DESTDIR=%buildroot%sysroot

cd ../obj_gcc
%make_install install DESTDIR=%buildroot

# relocate target libgcc_s
mv %buildroot%prefix/lib/gcc/%target/lib64/libgcc_s.so* %buildroot%prefix/lib/gcc/%target/%gcc_branch/
rmdir %buildroot%prefix/lib/gcc/%target/lib64

# XXX: native compiler sets /lib64/ld-linux-aarch64.so.1 as an ELF interpreter.
# Make sure cross-toolchain we build does the same thing.
%buildroot%prefix/bin/%target-gcc -dumpspecs > specs
sed -e "s;/lib/ld-linux-aarch64;/lib64/ld-linux-aarch64;g" -i specs

# Assembler: %%target-as.
# Path is relative to %%prefix/lib/gcc/%%target/%%gcc_branch
sed -e '/^[*]invoke_as:/,/^[*]cpp:/ s; as ; ../../../../bin/%target-as ;' -i specs
# objcopy: %%target-objcopy
sed -e 's; objcopy ; ../../../../bin/%target-objcopy ;' -i specs
install -m 644 specs %buildroot%prefix/lib/gcc/%target/%gcc_branch/specs
# Note: collect2 (GCCs linker wrapper) searches for %%target-ld on its own.
# Alas it does not use relative paths and is not adjustable via the specs file

# XXX: apparently invoke_as: spec directive applies only to running assembler
# on compiler (cc1) output. The spec which describes compiling of `assembler`
# and `assembler-with-cpp` pseudo-languages seems to be hard-coded into GCC.
# As a result GCC still runs /usr/bin/as (instead of target assembler) when
# compiling .S files. Therefore install `as` symlinks in GCC libsubdir
# (%%prefix/lib/gcc/%%target/%%gcc_branch).
# Just in a case make symlinks to other tools.
for tool in ar as ld ld.bfd ld.gold nm objcopy objdump ranlib readelf strip; do
	ln -s ../../../../bin/%target-$tool %buildroot%prefix/lib/gcc/%target/%gcc_branch/$tool
	# just in a case add a symlink into libexec too
	ln -s ../../../../bin/%target-$tool %buildroot%prefix/libexec/gcc/%target/%gcc_branch/$tool
done

# XXX: ABI: which is correct location of ELF interpreter for aarch64?
# Native glibc provides ld-linux-aarch64.so.1 in both /lib64 and /lib.
# Do the same thing in cross-glibc
install -d -m 755 %buildroot%sysroot/lib
ln -s ../lib64/`basename %target_ld_linux` %buildroot%sysroot/lib/`basename %target_ld_linux`

rm -rf %buildroot%sysroot/etc
rm -rf %buildroot%sysroot/var
rm -rf %buildroot%sysroot/sbin
rm -rf %buildroot%sysroot/usr/share
rm -rf %buildroot%sysroot/usr/bin
rm -rf %buildroot%sysroot/usr/sbin
rm -rf %buildroot%sysroot/usr/libexec
rm -rf %buildroot%sysroot/usr/lib64/audit
rm -rf %buildroot%sysroot/usr/lib64/gconv
rm -rf %buildroot%prefix/share/info
rm -rf %buildroot%prefix/share/man/man7
# python pretty-printers conflict with native compiler
rm -rf %buildroot%prefix/share/gcc-%gcc_branch/python
# conficts with the native compiler and is not particularly useful
rm -f %buildroot%prefix/%_lib/libcc1.so*
# Useless for Linux targets
rm -f %buildroot%prefix/share/man/man1/%target-windmc*
rm -f %buildroot%prefix/share/man/man1/%target-windres*
# libtool junk
find %buildroot%prefix/lib/gcc/%target/%gcc_branch -type f -name '*.la' -delete
find %buildroot%prefix/libexec/gcc -type f -name '*.la' -delete
# Target C++ runtime is used for linking only
find %buildroot%prefix/lib/gcc/%target/%gcc_branch -type f -name 'lib*-gdb.py' -delete


# XXX: gcc needs this to locate crt1.o
install -d -m 755 %buildroot%sysroot/usr/lib

# Leave alone $target libraries
%brp_strip_none %sysroot/* %prefix/lib/gcc/%target/%gcc_branch/*.a %prefix/lib/gcc/%target/%gcc_branch/*.o
%add_verify_elf_skiplist %sysroot/* %prefix/lib/gcc/%target/%gcc_branch/*
%add_findreq_skiplist %sysroot/* %prefix/lib/gcc/%target/%gcc_branch/*
%add_findprov_skiplist %sysroot/* %prefix/lib/gcc/%target/%gcc_branch/*
%add_debuginfo_skiplist %sysroot/* %prefix/lib/gcc/%target/%gcc_branch/*

%check

cat > hello.c <<EOF
#include <stdio.h>
int main(int argc, char** argv) {
	printf("Hello, %%s!\n", argc > 1 ? argv[1] : "world");
	return 0;
}
EOF

cat > hello.cpp <<EOF
#include <iostream>
int main(int argc, char** argv) {
	std::cout << "Hello, " << (argc > 1 ? argv[1] : "world") << "!" << std::endl;
	return 0;
}
EOF

gcc_runtime_libdir=`dirname $(%buildroot%prefix/bin/%target-gcc --print-libgcc-file-name)`

# XXX: PATH= is necessary for collect2 to find %%target-ld
env PATH=%buildroot%prefix/bin:$PATH \
%buildroot%prefix/bin/%target-gcc -o hello_c hello.c || exit 2
env PATH=%buildroot%prefix/bin:$PATH \
%buildroot%prefix/bin/%target-g++ -o hello_cpp hello.cpp || exit 3

# Note: LD_LIBRARY_PATH is for **target** ld.so.
# Use qemu-user-static so qemu-user is not affected by LD_LIBRARY_PATH
env LD_LIBRARY_PATH=%buildroot%sysroot/lib64:${gcc_runtime_libdir} \
	qemu-%target_qemu_arch-static -L %buildroot%sysroot ./hello_c || exit 5

env LD_LIBRARY_PATH=%buildroot%sysroot/lib64:${gcc_runtime_libdir} \
	qemu-%target_qemu_arch-static -L %buildroot%sysroot ./hello_cpp || exit 7

cat > bye.S <<EOF
#include <sys/syscall.h>

	.arch armv8-a
	.text
	.align 2
	.global _start
_start:
	mov x8, __NR_exit
	mov x0, 0
	svc #0
	.section	.note.GNU-stack,"",@progbits
EOF

env PATH=%buildroot%prefix/bin:$PATH \
%buildroot%prefix/bin/%target-gcc -static -nostdlib -o bye_asm bye.S || exit 11
qemu-%target_qemu_arch-static ./bye_asm || exit 13

%files -n gcc-%target
%_bindir/%target-gcc*
%_bindir/%target-cpp
%_bindir/%target-g++
%_bindir/%target-c++
%_bindir/%target-gcov*
%prefix/lib/gcc/%target/%gcc_branch/*
%prefix/libexec/gcc/%target/*
# avoid 'static library packaging violation' "error"
%exclude %prefix/lib/gcc/%target/%gcc_branch/libatomic.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libgomp.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libitm.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libssp.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libstdc++.a
# binunitls
%exclude %prefix/libexec/gcc/%target/bin/*
%exclude %prefix/libexec/gcc/%target/lib/*
%prefix/share/man/man1/aarch64-linux-gnu-cpp*
%prefix/share/man/man1/aarch64-linux-gnu-g++*
%prefix/share/man/man1/aarch64-linux-gnu-gcc*
%prefix/share/man/man1/aarch64-linux-gnu-gcov-dump*
%prefix/share/man/man1/aarch64-linux-gnu-gcov-tool*
%prefix/share/man/man1/aarch64-linux-gnu-gcov*

%files -n gcc-%target-static
%prefix/lib/gcc/%target/%gcc_branch/libatomic.a
%prefix/lib/gcc/%target/%gcc_branch/libgomp.a
%prefix/lib/gcc/%target/%gcc_branch/libitm.a
%prefix/lib/gcc/%target/%gcc_branch/libssp.a
%prefix/lib/gcc/%target/%gcc_branch/libstdc++.a

%files -n cross-glibc-%target_arch
%sysroot/usr/include/*
# XXX: gcc needs %%sysroot/usr/lib to locate C runtime (crt1.o)
%sysroot/usr/lib
%sysroot/lib64/*
%sysroot/usr/lib64/*
%exclude %sysroot/usr/lib64/libBrokenLocale.a
%exclude %sysroot/usr/lib64/libanl.a
%exclude %sysroot/usr/lib64/libdl.a
%exclude %sysroot/usr/lib64/libm.a
%exclude %sysroot/usr/lib64/libpthread.a
%exclude %sysroot/usr/lib64/libresolv.a
%exclude %sysroot/usr/lib64/librt.a
%exclude %sysroot/usr/lib64/libutil.a
# Compatibility symlink to ld.so
%sysroot/lib/*

%files -n cross-glibc-static-%target_arch
%sysroot/usr/lib64/libBrokenLocale.a
%sysroot/usr/lib64/libanl.a
%sysroot/usr/lib64/libdl.a
%sysroot/usr/lib64/libm.a
%sysroot/usr/lib64/libpthread.a
%sysroot/usr/lib64/libresolv.a
%sysroot/usr/lib64/librt.a
%sysroot/usr/lib64/libutil.a

%files -n binutils-%target
%_bindir/%target-addr2line
%_bindir/%target-ar
%_bindir/%target-as
%_bindir/%target-c++filt
%_bindir/%target-dwp
%_bindir/%target-elfedit
%_bindir/%target-gprof
%_bindir/%target-ld
%_bindir/%target-ld.bfd
%_bindir/%target-ld.gold
%_bindir/%target-nm
%_bindir/%target-objcopy
%_bindir/%target-objdump
%_bindir/%target-ranlib
%_bindir/%target-readelf
%_bindir/%target-size
%_bindir/%target-strings
%_bindir/%target-strip
# gcc_tooldir
%prefix/libexec/gcc/%target/bin/*
%prefix/libexec/gcc/%target/lib/*

%changelog
* Tue Aug 31 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 20210831-alt1
- Fixed build failure due to (inappropriate) LTO enforcement

* Wed Aug 04 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 20210804-alt1
- Avoid breaking whenever GCC, binutils, or glibc gets updated

* Thu Jul 29 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 10.3.1-alt1
- Build GCC 10.3.1
- Disabled libsanitizer to avoid bootstrap problems

* Tue Jun 15 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 8.4.1-alt2
- Splitted into subpackages

* Fri Jun 11 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 8.4.1-alt1
- Initial build

