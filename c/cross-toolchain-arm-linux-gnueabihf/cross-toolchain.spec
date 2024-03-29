
# %%define target_arch aarch64
# %%define target_arch arm
# %%define target_arch mipsel
# %%define target_arch riscv64
# %%define target_arch mips64el
# %%define target_arch loongarch64
# %%define target_arch mipsisa64r6el
# %%define target_arch i586
# %%define target_arch x86_64
%define target_arch arm


%if "%target_arch" == "aarch64"
%define target_kernel arm64
%define target_qemu_arch aarch64
%define target_ld_linux /lib64/ld-linux-aarch64.so.1
%define target_libdir lib64
%define target_has_itm 1
%define target_has_gold 1
%define target_has_mvec 1
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
%define target_userspace gnueabihf
%define target_no_default_pie 1
%endif

%if "%target_arch" == "mipsel"
%define target_kernel mips
%define target_qemu_arch mipsel
%define target_ld_linux /lib/ld.so.1
%define target_libdir lib
%define target_has_gold 1
%define target_no_default_pie 1
%endif

%if "%target_arch" == "mips64el"
%define target_kernel mips
%define target_qemu_arch mips64el
%define target_ld_linux /lib64/ld.so.1
%define target_libdir lib64
%define target_has_gold 1
%endif

%if "%target_arch" == "mipsisa64r6el"
%define target_kernel mips
%define target_qemu_arch mips64el
%define target_ld_linux /lib64/ld-linux-mipsn8.so.1
%define target_libdir lib64
%define target_userspace gnuabi64
%endif

%if "%target_arch" == "riscv64"
%define target_kernel riscv
%define target_qemu_arch riscv64
%define target_ld_linux /lib64/ld-linux-riscv64-lp64d.so.1
%define target_libdir lib64
%define target_has_itm 1
%endif

%if "%target_arch" == "loongarch64"
%define target_kernel loongarch
%define target_qemu_arch loongarch64
%define target_ld_linux /lib64/ld-linux-loongarch-lp64d.so.1
%define target_libdir lib64
%define target_has_itm 1
%endif

%if "%target_arch" == "x86_64"
%define target_kernel x86
%define target_qemu_arch x86_64
%define target_ld_linux /lib64/ld-linux-x86-64.so.2
%define target_libdir lib64
%define target_has_itm 1
%define target_has_mvec 1
%define target_has_quadmath 1
%endif

%if "%target_arch" == "i586"
%define target_kernel x86
%define target_qemu_arch i386
%define target_ld_linux /lib/ld-linux.so.2
%define target_libdir lib
%define target_no_default_pie 1
%define target_has_itm 1
%define target_has_quadmath 1
%endif

%if "%{?target_userspace}" == ""
%define target_userspace gnu
%endif

%define target %target_arch-linux-%target_userspace
%define sysroot %prefix/lib/%target/sys-root

# don't strip debuginfo from binaries for other platform, it does not work
%brp_strip_none %sysroot/*  %prefix/lib/gcc/*.a %prefix/lib/gcc/*.o

Name: cross-toolchain-%target
Version: 20240206
Release: alt1
Summary: GCC cross-toolchain for %target
License: LGPL-2.1-or-later and LGPL-3.0-or-later and GPL-2.0-or-later and GPL-3.0-or-later and GPL-3.0-or-later with GCC-exception-3.1
Group: Development/C

%if "%target_arch" == "x86_64" || "%target_arch" == "i586"
ExclusiveArch: aarch64 loongarch64
%else
%if "%target_arch" == "aarch64" || "%target_arch" == "arm"
ExclusiveArch: loongarch64 x86_64
%else
%if "%target_arch" == "loongarch64"
ExclusiveArch: x86_64
%else
ExclusiveArch: loongarch64 x86_64
%endif
%endif
%endif

%ifarch loongarch64
# XXX: By default GCC build system builds GCC as non-PIE binaries (for
# performance reasons). However on LoongArch many non-trivial non-PIE
# binaries have text relocations (the default code model on LoongArch
# is a bit tough, i.e. the code offsets must fit into 128MB).
# rpm-build verifies every binary with text relocations with
# eu-findtextrel, however eu-findtextrel refuses to process non-PIE
# binaries and bails out with an error. As a result build fails with
# the following error:
#
# eu-findtextrel: './usr/bin/riscv64-linux-gnu-lto-dump' is not a DSO or PIE
#
# To avoid the problem build GCC as a PIE binary on LoongArch.
%def_enable host_shared
%else
%def_disable host_shared
%endif


%define gcc_version %{get_version gcc-source}
%define gcc_branch %(v=%gcc_version; v=${v%%%%.*}; echo $v)
%define binutils_version %{get_version binutils-source}
%define glibc_version %{get_version glibc-source}
%define kernel_version 6.1

BuildRequires(pre): gcc-source
BuildRequires(pre): binutils-source
BuildRequires(pre): glibc-source
BuildRequires: gcc-c++
BuildRequires: kernel-source-%kernel_version
BuildRequires: coreutils flex bison makeinfo perl-Pod-Parser findutils
BuildRequires: libmpc-devel libmpfr-devel libgmp-devel zlib-devel
# Linux' headers_install uses rsync
BuildRequires: rsync
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
Requires: cross-gcc-libs-%target = %gcc_version
Requires: binutils-%target = %binutils_version
Requires: cross-glibc-%target_arch = %glibc_version

%description -n gcc-%target
%target_arch-targeted GCC cross-compiler

%package -n cross-gcc-libs-%target
Version: %gcc_version
Summary: %target_arch-targeted GCC cross-compiler, target libraries
Group: Development/C
BuildArch: noarch

%description -n cross-gcc-libs-%target
%target_arch-targeted GCC cross-compiler, shared libraries for target

%package -n gcc-%target-static
Version: %gcc_version
Summary: %target_arch-targeted GCC cross-compiler, static libraries
Group: Development/C
BuildArch: noarch

%description -n gcc-%target-static
%target_arch-targeted GCC cross-compiler, static libraries for target

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
mkdir -p obj_gcc_bootstrap
mkdir -p obj_kheaders
mkdir -p obj_glibc
mkdir -p -m755 stage%prefix/bin
mkdir -p -m755 stage1%prefix/bin
save_PATH="$PATH"
export PATH=`pwd`/stage1%prefix/bin:$PATH
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
	--with-system-zlib \
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
	--with-system-zlib \
%if "%target_arch" == "mipsel"
	--with-arch-32=mips32r2 \
	--with-fp-32=xx \
	--with-lxc1-sxc1=no \
	--with-madd4=no \
%endif
%if "%target_arch" == "mips64el"
	--with-arch-64=mips64r2 \
	--with-abi=64 \
	--with-lxc1-sxc1=no \
	--with-madd4=no \
	--with-fix-loongson3-llsc=yes \
%endif
%if "%target_arch" == "mipsisa64r6el"
	--with-arch-64=mips64r6 \
	--with-abi=64 \
	--with-float=hard \
	--with-nan=2008 \
%endif
%if "%target_arch" == "riscv64"
	--with-arch=rv64gc \
	--with-abi=lp64d \
%endif
	--enable-gnu-unique-object \
	--enable-linker-build-id \
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
env \
	ac_cv_file__proc_self_exe=yes \
	gcc_cv_libc_provides_ssp=yes \
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
	--with-system-zlib \
%if "%target_arch" == "mipsel"
	--with-arch-32=mips32r2 \
	--with-fp-32=xx \
	--with-lxc1-sxc1=no \
	--with-madd4=no \
%endif
%if "%target_arch" == "mips64el"
        --with-arch-64=mips64r2 \
        --with-abi=64 \
        --with-lxc1-sxc1=no \
        --with-madd4=no \
        --with-fix-loongson3-llsc=yes \
%endif
%if "%target_arch" == "mipsisa64r6el"
	--with-arch-64=mips64r6 \
	--with-abi=64 \
	--with-float=hard \
	--with-nan=2008 \
%endif
%if "%target_arch" == "riscv64"
	--with-arch=rv64gc \
	--with-abi=lp64d \
%endif
	--enable-gnu-unique-object \
	--enable-linker-build-id \
%if 0%{?target_no_default_pie} == 0
	--enable-default-pie \
%endif
%if_enabled host_shared
	--enable-host-pie \
	--enable-host-shared \
%endif
	%nil

env \
	ac_cv_file__proc_self_exe=yes \
	gcc_cv_libc_provides_ssp=yes \
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


rm -f %buildroot%prefix/lib/gcc/%target/%gcc_branch/libssp.a
rm -f %buildroot%prefix/lib/gcc/%target/%gcc_branch/libssp_nonshared.a
rm -f %buildroot%prefix/lib/gcc/%target/%gcc_branch/libssp.so*

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

%if "%target_arch" == "mipsel" || "%target_arch" == "mips64el" || "%target_arch" == "mipsisa64r6el"
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

%if "%target_arch" == "i586"
cat > bye.S <<EOF
#include <sys/syscall.h>

.section .rodata
message: .asciz "bye-bye ...\n"
msg_len = (. - message)

.text
.global _start
_start:
	movl \$__NR_write, %%eax
	# stdout
	movl \$1, %%ebx
	leal message(%%ebp), %%ecx
	movl \$msg_len, %%edx
	int \$0x80

	movl \$__NR_exit, %%eax
	movl \$0, %%ebx
	int \$0x80

.section .note.GNU-stack,"",@progbits
EOF
%endif

%if "%target_arch" == "x86_64"
cat > bye.S <<EOF
#include <sys/syscall.h>

.data
message: .asciz "bye-bye ...\n"
msg_len = (. - message)

.text
.global _start
_start:
	movl \$__NR_write, %%eax
	# stdout
	movl \$1, %%edi
	leaq message(%%rip), %%rsi
	movl \$msg_len, %%edx
	syscall

	movl \$__NR_exit, %%eax
	movl \$0, %%edi
	syscall

.section .note.GNU-stack,"",@progbits
EOF
%endif

# XXX: x86 targeted binutils align sections at 4 KB (target page size).
# On host architectures with page size > 4KB qemu refuse to load such a binary.
%if "%target_arch" == "i586"
%global asm_extra_flags -Wl,-Ttext-segment=0x90000000
%else
%global asm_extra_flags %nil
%endif

env PATH=%buildroot%prefix/bin:$PATH \
%buildroot%prefix/bin/%target-gcc -nostdlib -static -no-pie %asm_extra_flags -o bye_asm bye.S || exit 11
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
%exclude %prefix/lib/gcc/%target/%gcc_branch/libgcc.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libgcc_eh.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libgcov.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libgomp.a
%if 0%{?target_has_itm}
%exclude %prefix/lib/gcc/%target/%gcc_branch/libitm.a
%endif
%exclude %prefix/lib/gcc/%target/%gcc_branch/libstdc++.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libstdc++fs.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libsupc++.a
# avoid 'NEW bad_elf_symbols detected' "error"
%exclude %prefix/lib/gcc/%target/%gcc_branch/crt*.o
%exclude %prefix/lib/gcc/%target/%gcc_branch/libatomic.so*
%exclude %prefix/lib/gcc/%target/%gcc_branch/libgcc_s.so*
%exclude %prefix/lib/gcc/%target/%gcc_branch/libgomp.so*
%if 0%{?target_has_itm}
%exclude %prefix/lib/gcc/%target/%gcc_branch/libitm.so*
%endif
%if 0%{?target_has_quadmath}
%exclude %prefix/lib/gcc/%target/%gcc_branch/libquadmath.a
%exclude %prefix/lib/gcc/%target/%gcc_branch/libquadmath.so*
%endif
%exclude %prefix/lib/gcc/%target/%gcc_branch/libstdc++.so*
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
%prefix/lib/gcc/%target/%gcc_branch/libgcc.a
%prefix/lib/gcc/%target/%gcc_branch/libgcc_eh.a
%prefix/lib/gcc/%target/%gcc_branch/libgcov.a
%prefix/lib/gcc/%target/%gcc_branch/libgomp.a
%if 0%{?target_has_itm}
%prefix/lib/gcc/%target/%gcc_branch/libitm.a
%endif
%if 0%{?target_has_quadmath}
%prefix/lib/gcc/%target/%gcc_branch/libquadmath.a
%endif
%prefix/lib/gcc/%target/%gcc_branch/libstdc++.a
%prefix/lib/gcc/%target/%gcc_branch/libstdc++fs.a
%prefix/lib/gcc/%target/%gcc_branch/libsupc++.a

%files -n cross-gcc-libs-%target
%prefix/lib/gcc/%target/%gcc_branch/crt*.o
%prefix/lib/gcc/%target/%gcc_branch/libatomic.so*
%prefix/lib/gcc/%target/%gcc_branch/libgcc_s.so*
%prefix/lib/gcc/%target/%gcc_branch/libgomp.so*
%if 0%{?target_has_itm}
%prefix/lib/gcc/%target/%gcc_branch/libitm.so*
%endif
%if 0%{?target_has_quadmath}
%prefix/lib/gcc/%target/%gcc_branch/libquadmath.so*
%endif
%prefix/lib/gcc/%target/%gcc_branch/libstdc++.so*

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
%if 0%{?target_has_mvec}
%exclude %sysroot/usr/%target_libdir/libmvec.a
%endif

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
%if 0%{?target_has_mvec}
%sysroot/usr/%target_libdir/libmvec.a
%endif

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
* Tue Feb 06 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 20240206-alt1
- Added x86-targeted cross-compilers (for now only on aarch64 and LoongArch).

* Thu Dec 07 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 20231207-alt1
- spec: applied mips64 bits from iv@.

* Fri Oct 06 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 20231006-alt1
- spec: build compiler binaries as PIE. Fixes FTBFS on LoongArch.

* Tue Aug 22 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 20230822-alt1
- glibc: libmvec has been added on aarch64, move libmvec.a into
  cross-glibc-static-$TARGET subpackage
- build cross-toolchains on loongarch64

* Wed Aug 02 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 20230802-alt1
- GCC: don't package libssp any more
- GCC: enabled gnu-unique-object
- GCC: enabled default-pie on 64-bit architectures
- Use kernel-source 6.1 on all architectures

* Thu Feb 02 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 20230202-alt1
- Moved GCC target libraries to a noarch subpackage to avoid spurious
  'bad ELF symbols' errors.
- Added bits from riscv64 and loongarch64 cross-toolchains

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

