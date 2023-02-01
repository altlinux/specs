
# %%define target_arch aarch64
# %%define target_arch arm
# %%define target_arch mipsel
# %%define target_arch riscv64
%define target_arch loongarch64

%if "%target_arch" == "aarch64"
%define target_kernel arm64
%define target_qemu_arch aarch64
%define target_ld_linux /lib64/ld-linux-aarch64.so.1
%define target_libdir lib64
%define target_has_itm 1
%define target_has_gold 1
%endif

%if "%target_arch" == "arm"
%define target_kernel arm
%define target_qemu_arch arm
%define target_ld_linux /lib/ld-linux-armhf.so.3
%define target_libdir lib
%define target_has_itm 1
%define target_has_gold 1
# armhf: use the same arch/fp instruction set as the native compiler
%define arm_arch armv7-a
%define arm_fp_isa vfpv3-d16
%define arm_fp_abi hard
%endif

%if "%target_arch" == "mipsel"
%define target_kernel mips
%define target_qemu_arch mipsel
%define target_ld_linux /lib/ld.so.1
%define target_libdir lib
%define target_has_gold 1
%endif


%if "%target_arch" == "riscv64"
%define target_kernel riscv
%define target_qemu_arch riscv64
%define target_ld_linux /lib64/ld-linux-riscv64-lp64d.so.1
%define target_libdir lib64
%endif

%if "%target_arch" == "loongarch64"
%define target_kernel loongarch
%define target_qemu_arch loongarch64
%define target_ld_linux /lib64/ld-linux-loongarch-lp64d.so.1
%define target_libdir lib64
%define target_has_itm 1
%endif

%if "%target_arch" != "arm"
%define target %target_arch-linux-gnu
%else
%define target %target_arch-linux-gnueabihf
%endif
%define sysroot %prefix/lib/%target/sys-root

# don't strip debuginfo from binaries for other platform, it does not work
%brp_strip_none %sysroot/*  %prefix/lib/gcc/*.a %prefix/lib/gcc/*.o

Name: cross-toolchain-%target
Version: 20230130
Release: alt1
Packager: Alexey Sheplyakov <asheplyakov@altlinux.org>
Summary: GCC cross-toolchain for %target
License: LGPL-2.1-or-later and LGPL-3.0-or-later and GPL-2.0-or-later and GPL-3.0-or-later and GPL-3.0-or-later with GCC-exception-3.1
Group: Development/C

ExclusiveArch: x86_64

%define gcc_version 13.0.0.20230128.gfe4608efc15
%define gcc_branch %(v=%gcc_version; v=${v%%%%.*}; echo $v)
%define binutils_version 2.40
%define glibc_version 2.36.20221009
%if "%target_arch" == "loongarch64"
%define kernel_version 6.0
%else
%define kernel_version 5.10
%endif

Source0: gcc-13.0.0-20230128-gfe4608efc15.tar
Source1: binutils-2.40.tar
Source2: glibc-2.36-20221009.tar
Source3: kernel-source-6.1.0.tar
Source4: gmp-6.2.1.tar
Source5: isl-0.24.tar
Source6: mpc-1.2.1.tar
Source7: mpfr-4.1.0.tar

Patch0: 0001_glibc_makeflags.patch

BuildPreReq: gcc-c++
BuildPreReq: coreutils flex bison makeinfo perl-Pod-Parser findutils
# Linux' headers_install uses rsync
BuildPreReq: rsync
BuildRequires: /usr/bin/qemu-%target_qemu_arch-static
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

tar -x --strip-components=1 -f %SOURCE0 -C gcc
tar -x --strip-components=1 -f %SOURCE1 -C binutils
tar -x --strip-components=1 -f %SOURCE2 -C glibc
tar -x --strip-components=1 -f %SOURCE3 -C linux

mkdir -p -m755 gcc/gmp gcc/mpc gcc/mpfr gcc/isl
tar -x --strip-components=1 -f %SOURCE4 -C gcc/gmp
tar -x --strip-components=1 -f %SOURCE5 -C gcc/isl
tar -x --strip-components=1 -f %SOURCE6 -C gcc/mpc
tar -x --strip-components=1 -f %SOURCE7 -C gcc/mpfr

# glibc makeflags + make 4.4 hiccup
patch -d glibc -p1 -i %PATCH0

rm -rf stage

%build
mkdir -p obj_binutils
mkdir -p obj_gcc
mkdir -p obj_gcc_bootstrap
mkdir -p obj_kheaders
mkdir -p obj_glibc
mkdir -p -m755 stage%prefix/bin
mkdir -p -m755 stage1%prefix/bin
save_PATH="$PATH"
if [ -d "/usr/lib/ccache" ]; then
	export PATH=`pwd`/stage1%prefix/bin:/usr/lib/ccache:$PATH
else
	export PATH=`pwd`/stage1%prefix/bin:$PATH
fi
stagedir=`pwd`/stage
stage1dir=`pwd`/stage1

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
%if "%target_arch" == "arm"
	--with-arch=%arm_arch \
	--with-fpu=%arm_fp_isa \
	--with-float=%arm_fp_abi \
%endif
	--prefix=%prefix \
	--disable-bootstrap \
	--disable-multiarch \
	--disable-multilib \
	--disable-werror \
	--disable-shared \
	--disable-nls \
	--with-sysroot=%sysroot \
	--with-build-sysroot=${stagedir}%sysroot \
	--enable-plugins \
%if 0%{?target_has_gold}
	--enable-gold=yes \
%endif
	--enable-ld=default \
%if "%target_arch" != "mipsel"
	--enable-64-bit-bfd \
%endif
	--enable-relro \
	--enable-textrel-check=warning

%make_build
# XXX: avoid makeinstall for it puts $target libraries into /usr/lib64
%make_install install DESTDIR=${stagedir}
# for bootstrap toolchain (to compile target glibc)
%make_install install DESTDIR=${stage1dir}

# bootstrap gcc (for compiling target glibc)
cd ../obj_gcc_bootstrap
../gcc/configure \
	--target=%target \
	--host=%{_configure_platform} \
	--build=%{_configure_platform} \
%if "%target_arch" == "arm"
	--with-arch=%arm_arch \
	--with-fpu=%arm_fp_isa \
	--with-float=%arm_fp_abi \
%endif
	--prefix=%prefix \
	--disable-bootstrap \
	--disable-multiarch \
	--disable-multilib \
	--disable-werror \
	--with-sysroot=%sysroot \
	--with-build-sysroot=${stagedir}%sysroot \
	--enable-languages=c \
	--with-newlib \
	--without-headers \
	--disable-nls \
	--disable-shared \
	--disable-threads \
	--disable-libsanitizer \
	--disable-libgomp \
	--disable-libitm \
	--disable-libquadmath \
	--disable-libsanitizer \
	--disable-libssp \
	--disable-libvtv \
	--disable-libatomic \
	--disable-libcilkrts \
	--enable-version-specific-runtime-libs \
	--with-gcc-major-version-only \
%if "%target_arch" == "mipsel"
	--with-arch-32=mips32r2 \
	--with-fp-32=xx \
	--with-lxc1-sxc1=no \
	--with-madd4=no \
%endif
%if "%target_arch" == "riscv64"
	--with-arch=rv64gc \
	--with-abi=lp64d \
%endif
	%nil

%make_build all-gcc all-target-libgcc
# XXX: avoid makeinstall for it puts $target libraries into /usr/lib64
%make_install install-gcc install-target-libgcc DESTDIR=${stage1dir}

# glibc
cd ../obj_glibc
# XXX: avoid %%configure since it puts target libraries/binaries into /usr/lib64
# Note: glibc's is a library, so $host must be the same as $target
../glibc/configure \
	--host=%target \
	--target=%target \
	--build=%{_configure_platform} \
%if "%target_arch" == "arm"
	--with-arch=%arm_arch \
	--with-fpu=%arm_fp_isa \
	--with-float=%arm_fp_abi \
%endif
	--prefix=%prefix \
	--with-sysroot=%sysroot \
	--with-build-sysroot=${stagedir}%sysroot \
	--with-headers=${stagedir}%sysroot/usr/include \
	--with-lib=${stagedir}%sysroot/usr/lib \
	--disable-multilib \
	--disable-crypt \
%if "%target_arch" == "loongarch64"
	--disable-werror \
%endif
	libc_cv_forced_unwind=yes \
	%nil

%make_build
# XXX: avoid makeinstall since it puts target libs into /usr/lib64
# Note: target glibc **must** be installed into sysroot to prevent
# native compilers from using it by default
%make_install install DESTDIR=${stagedir}%sysroot
# XXX: gcc needs this to locate crt{1,i}.o
mkdir -p -m755 ${stagedir}%sysroot/usr/lib

# Don't use bootstrap toolchain any more
export PATH="${stagedir}%prefix/bin:${save_PATH}"

# gcc
cd ../obj_gcc
# XXX: avoid %%configure puts $target libraries in /usr/lib64
../gcc/configure \
	--target=%target \
	--host=%{_configure_platform} \
	--build=%{_configure_platform} \
%if "%target_arch" == "arm"
	--with-arch=%arm_arch \
	--with-fpu=%arm_fp_isa \
	--with-float=%arm_fp_abi \
%endif
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
%if "%target_arch" == "mipsel"
	--with-arch-32=mips32r2 \
	--with-fp-32=xx \
	--with-lxc1-sxc1=no \
	--with-madd4=no \
%endif
%if "%target_arch" == "riscv64"
	--with-arch=rv64gc \
	--with-abi=lp64d \
%endif
	%nil

%make_build
# XXX: avoid makeinstall for it puts $target libraries into /usr/lib64
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
if [ -d "%buildroot%prefix/lib/gcc/%target/lib64" ] ; then
    mv %buildroot%prefix/lib/gcc/%target/lib64/libgcc_s.so* %buildroot%prefix/lib/gcc/%target/%gcc_branch/
    rmdir %buildroot%prefix/lib/gcc/%target/lib64
fi

%buildroot%prefix/bin/%target-gcc -dumpspecs > specs

%if "%target_arch" == "aarch64"
# XXX: native compiler sets /lib64/ld-linux-aarch64.so.1 as an ELF interpreter.
# Make sure cross-toolchain we build does the same thing.
sed -e "s;/lib/ld-linux-aarch64;/lib64/ld-linux-aarch64;g" -i specs
%endif

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
    tool_path="%buildroot%_bindir/%target-$tool"
    [ -f "$tool_path" ] || continue
    ln -sr "$tool_path" %buildroot%prefix/lib/gcc/%target/%gcc_branch/$tool
    # just in a case add a symlink into libexec too
    ln -sr "$tool_path" %buildroot%prefix/libexec/gcc/%target/%gcc_branch/$tool
done

%if "%target_libdir" == "lib64"
# XXX: ABI: which is correct location of ELF interpreter for aarch64?
# Native glibc provides ld-linux-aarch64.so.1 in both /lib64 and /lib.
# Do the same thing in cross-glibc
install -d -m 755 %buildroot%sysroot/lib
ln -s ../lib64/`basename %target_ld_linux` %buildroot%sysroot/lib/`basename %target_ld_linux`
%endif

# remove runtime bits, not necessary for a cross-toolchain
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
# conflicts with the native compiler and is not particularly useful
rm -f %buildroot%prefix/%_lib/libcc1.so*
# conflicts with the native bfd and is not particularly useful
rm -rf %buildroot%prefix/lib/bfd-plugins
# Useless for Linux targets
rm -f %buildroot%_man1dir/%target-windmc*
rm -f %buildroot%_man1dir/%target-windres*
# libtool junk
find %buildroot%prefix/lib/gcc/%target/%gcc_branch -type f -name '*.la' -delete
find %buildroot%prefix/libexec/gcc -type f -name '*.la' -delete
# Target C++ runtime is used for linking only
find %buildroot%prefix/lib/gcc/%target/%gcc_branch -type f -name 'lib*-gdb.py' -delete


# XXX: gcc needs this to locate crt1.o
install -d -m 755 %buildroot%sysroot/usr/lib

# remove bootstrap toolchain
rm -rf %buildroot/stage1

# Leave alone $target libraries
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

%if "%target_arch" == "aarch64"
cat > bye.S <<EOF
#include <sys/syscall.h>

	.arch armv8-a
	.data
message: .asciz "bye-bye ...\n"

	.text
	.align 2
	.global _start
_start:
	mov x8, __NR_write
	mov x0, 1
	adr x1, message
	mov x2, 12
	svc #0

	mov x8, __NR_exit
	mov x0, 0
	svc #0
	.section	.note.GNU-stack,"",@progbits
EOF
%endif

%if "%target_arch" == "arm"
cat > bye.S <<EOF
#include <sys/syscall.h>
	.arch armv7-a
	.data
message: .asciz "bye-bye ...\n"

	.text
	.align 2
	.global _start
_start:
	mov r7, #__NR_write
	mov r0, #1
	ldr r1, address_of_message
	mov r2, #12
	swi #0

	mov r0, #0
	mov r7, #__NR_exit
	swi #0

.align 4
address_of_message: .word message
	.section	.note.GNU-stack,"",%progbits
EOF
%endif

%if "%target_arch" == "mipsel"
cat > bye.S <<EOF
#include <sys/syscall.h>
.text
        .global __start
__start:
        li \$a0, 0
        li \$v0, __NR_exit
        syscall
EOF
%endif

%if "%target_arch" == "riscv64"
cat > bye.S <<EOF
#include <sys/syscall.h>

.text
.global _start
_start:
        addi a0, x0, 0
        addi a7, x0, __NR_exit
        ecall
EOF
%endif

%if "%target_arch" == "loongarch64"
cat > bye.S <<EOF
#include <sys/syscall.h>

.data
message: .asciz "bye-bye ...\n"

.text
.global _start
_start:
	li.w \$a7, __NR_write
	li.w \$a0, 1 # stdout file descriptor
	la \$a1, message
	li.w \$a2, 12 # message length
	syscall 0x0

	li.w \$a7, __NR_exit
	li.w \$a0, 0
	syscall 0x0

.section	.note.GNU-stack,"",@progbits
EOF
%endif

env PATH=%buildroot%prefix/bin:$PATH \
%buildroot%prefix/bin/%target-gcc -static -nostdlib -o bye_asm bye.S || exit 11
qemu-%target_qemu_arch-static ./bye_asm || exit 13

%files -n gcc-%target
%_bindir/%target-gcc*
%_bindir/%target-cpp
%_bindir/%target-g++
%_bindir/%target-c++
%_bindir/%target-gcov*
%_bindir/%target-lto*
%prefix/lib/gcc/%target/%gcc_branch/*
%prefix/libexec/gcc/%target/*
# avoid 'static library packaging violation' "error"
%exclude %prefix/lib/gcc/%target/%gcc_branch/libatomic.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libgomp.a
%if 0%{?target_has_itm}
%exclude %prefix/lib/gcc/%target/%gcc_branch/libitm.a
%endif
%exclude %prefix/lib/gcc/%target/%gcc_branch/libssp.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libstdc++.a
# binunitls
%exclude %prefix/libexec/gcc/%target/bin/*
%exclude %prefix/libexec/gcc/%target/lib/*
%_man1dir/%target-cpp*
%_man1dir/%target-g++*
%_man1dir/%target-gcc*
%_man1dir/%target-gcov*
%_man1dir/%target-lto*

%files -n gcc-%target-static
%prefix/lib/gcc/%target/%gcc_branch/libatomic.a
%prefix/lib/gcc/%target/%gcc_branch/libgomp.a
%if 0%{?target_has_itm}
%prefix/lib/gcc/%target/%gcc_branch/libitm.a
%endif
%prefix/lib/gcc/%target/%gcc_branch/libssp.a
%prefix/lib/gcc/%target/%gcc_branch/libstdc++.a

%files -n cross-glibc-%target_arch
%sysroot/usr/include/*
%if "%target_libdir" == "lib64"
# XXX: gcc needs %%sysroot/usr/lib to locate C runtime (crt1.o)
%dir %sysroot/usr/lib
%sysroot/lib64/*
%sysroot/usr/lib64/*
# Compatibility symlink to ld.so
%sysroot/lib/*
%else
%sysroot/lib
%sysroot/usr/lib
%endif
%exclude %sysroot/usr/%target_libdir/libBrokenLocale.a
%if %target_arch != "loongarch64"
%exclude %sysroot/usr/%target_libdir/libanl.a
%endif
%exclude %sysroot/usr/%target_libdir/libdl.a
%exclude %sysroot/usr/%target_libdir/libm.a
%exclude %sysroot/usr/%target_libdir/libpthread.a
%exclude %sysroot/usr/%target_libdir/libresolv.a
%exclude %sysroot/usr/%target_libdir/librt.a
%exclude %sysroot/usr/%target_libdir/libutil.a

%files -n cross-glibc-static-%target_arch
%sysroot/usr/%target_libdir/libBrokenLocale.a
%if %target_arch != "loongarch64"
%sysroot/usr/%target_libdir/libanl.a
%endif
%sysroot/usr/%target_libdir/libdl.a
%sysroot/usr/%target_libdir/libm.a
%sysroot/usr/%target_libdir/libpthread.a
%sysroot/usr/%target_libdir/libresolv.a
%sysroot/usr/%target_libdir/librt.a
%sysroot/usr/%target_libdir/libutil.a

%files -n binutils-%target
%_bindir/%target-addr2line
%_bindir/%target-ar
%_bindir/%target-as
%_bindir/%target-c++filt
%if 0%{?target_has_gold}
%_bindir/%target-dwp
%endif
%_bindir/%target-elfedit
%_bindir/%target-gprof
%_bindir/%target-ld
%_bindir/%target-ld.bfd
%if 0%{?target_has_gold}
%_bindir/%target-ld.gold
%endif
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
%_man1dir/%target-addr2line*
%_man1dir/%target-ar*
%_man1dir/%target-as*
%_man1dir/%target-c++filt*
%_man1dir/%target-dlltool*
%_man1dir/%target-elfedit*
%_man1dir/%target-gprof*
%_man1dir/%target-ld*
%_man1dir/%target-nm*
%_man1dir/%target-objcopy*
%_man1dir/%target-objdump*
%_man1dir/%target-ranlib*
%_man1dir/%target-readelf*
%_man1dir/%target-size*
%_man1dir/%target-strings*
%_man1dir/%target-strip*


%changelog
* Mon Jan 30 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 20230130-alt1
- Added loongarch64 cross-toolchain

* Sun Jun 05 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 20220605-alt1
- Use slow 2-stage bootstrap to avoid a build failure with GCC 12

* Wed Dec 01 2021 Alexey Sheplyakov <asheplyakov@altlinux.org> 20211201-alt1
- Added armv7-a targeted compiler (arm-linux-gnueabihf)
- Partially merged riscv64/mipsel specs from iv@

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

