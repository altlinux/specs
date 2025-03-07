
# We get our target architecture from specsubst
%define target_arch aarch64

# ... or, you can uncomment one of the following lines and run gear --disable-specsubst
# %%define target_arch aarch64
# %%define target_arch arm
# %%define target_arch mipsel
# %%define target_arch riscv64
# %%define target_arch mips64el
# %%define target_arch loongarch64
# %%define target_arch mipsisa64r6el
# %%define target_arch i586
# %%define target_arch x86_64

# helper
%define part0() %(v="%2"; v="${v%%%%%{1}*}"; echo "$v")

# Versions:
%define binutils_vr       2.43-alt0.port.1
%define binutils_version  %{part0 - %binutils_vr}

%define gcc_vr            14.2.1-alt0.port
%define gcc_version       %{part0 - %gcc_vr}
%define gcc_branch        %{part0 . %gcc_version}

%define glibc_vr          2.40.0.69.8566822197-alt0.port
%define glibc_version     %{expand:%part0 - %glibc_vr}

%define kernel_version    6.12


%if "%target_arch" == "aarch64"
%define target_kernel arm64
%define target_ld_linux /lib64/ld-linux-aarch64.so.1
%define target_libdir lib64
%define target_has_itm 1
%define target_has_gold 1
%define target_has_mvec 1
%endif

%if "%target_arch" == "arm"
%define target_kernel arm
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
%define target_ld_linux /lib/ld.so.1
%define target_libdir lib
%define target_has_gold 1
%define target_no_default_pie 1
%endif

%if "%target_arch" == "mips64el"
%define target_kernel mips
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
%define target_ld_linux /lib64/ld-linux-riscv64-lp64d.so.1
%define target_libdir lib64
%define target_has_itm 1
%endif

%if "%target_arch" == "loongarch64"
%define target_kernel loongarch
%define target_ld_linux /lib64/ld-linux-loongarch-lp64d.so.1
%define target_libdir lib64
%define target_has_itm 1
%endif

%if "%target_arch" == "x86_64"
%define target_kernel x86
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

%if "%{?target_qemu_arch}" == ""
%define target_qemu_arch %target_arch
%endif

%define target %target_arch-linux-%target_userspace
%define sysroot %prefix/lib/%target/sys-root
%define test_data %prefix/lib/%target/test-data
%define cross_gcc_tooldir %prefix/libexec/gcc/%target

# don't strip debuginfo from binaries for other platform, it does not work
%brp_strip_none %sysroot/*  %prefix/lib/gcc/*.a %prefix/lib/gcc/*.o

Name: cross-toolchain-%target
Version: 20250101

# The release of this package MUST not go down, unless you simultaniously
# update binutils, glibc and gcc to new version, in which case you can
# restart with alt1 if you want.
Release: alt1


Summary: GCC cross-toolchain for %target
License: LGPL-2.1-or-later and LGPL-3.0-or-later and GPL-2.0-or-later and GPL-3.0-or-later and GPL-3.0-or-later with GCC-exception-3.1
Group: Development/C

%if "%target_arch" == "i586"
ExcludeArch: x86_64 %ix86 ppc64le
%else
ExcludeArch: %target_arch %ix86 ppc64le
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

BuildRequires: gcc-c++
BuildRequires: kernel-source-%kernel_version
BuildRequires: coreutils flex bison makeinfo perl-Pod-Parser findutils
BuildRequires: libmpc-devel libmpfr-devel libgmp-devel zlib-devel
# Linux' headers_install uses rsync
BuildRequires: rsync
BuildRequires: python3
BuildRequires: gnu-config

Source0: gcc-%gcc_vr.tar
Source1: binutils-%binutils_vr.tar
Source2: glibc-%glibc_vr.tar

Source10: tests.tar


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


%package checkinstall
Summary: Run simple checks for %target-gcc immediately when this package is installed
Group: Other
Requires: gcc-%target cross-glibc-%target_arch
Requires: /usr/bin/qemu-%target_qemu_arch-static

%description checkinstall
%summary


%prep
%setup -cT

# the test data
tar -xf "%SOURCE10"
mkdir -p -m755 linux gcc glibc binutils

tar -x --strip-components=1 -f "%SOURCE0" -C gcc
tar -x --strip-components=1 -f "%SOURCE1" -C binutils
tar -x --strip-components=1 -f "%SOURCE2" -C glibc

find /usr/src/kernel/sources -type f -name 'kernel-source-*.tar' | xargs -I {} -n1 tar -x --strip-components=1 -f {} -C linux

cp -at gcc /usr/share/gnu-config/config.{guess,sub}
cp -at glibc/scripts /usr/share/gnu-config/config.{guess,sub}

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
pushd obj_binutils
env \
	CC=gcc \
	CXX=g++ \
../binutils/configure \
	--disable-dependency-tracking \
	--disable-silent-rules \
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
	--disable-gdb \
	--disable-gprofng \
	--disable-sim \
	--without-sim \
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
	--enable-textrel-check=warning \
	--with-pkgversion='%binutils_version-%release' \
	--with-bugurl='https://bugzilla.altlinux.org/'

%make_build tooldir=%cross_gcc_tooldir
# XXX: avoid makeinstall for it puts $target libraries into /usr/lib64
%make_install install DESTDIR=${stagedir}
# for bootstrap toolchain (to compile target glibc)
%make_install install DESTDIR=${stage1dir}
popd

# bootstrap gcc (for compiling target glibc)
pushd obj_gcc_bootstrap
env \
	CC=gcc \
	CXX=g++ \
../gcc/configure \
	--disable-dependency-tracking \
	--disable-silent-rules \
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
	--with-pkgversion='%gcc_version-%release' \
	--with-bugurl='https://bugzilla.altlinux.org/'

%make_build all-gcc all-target-libgcc
# XXX: avoid makeinstall for it puts $target libraries into /usr/lib64
%make_install install-gcc install-target-libgcc DESTDIR=${stage1dir}
popd

# glibc
pushd obj_glibc
# XXX: avoid %%configure since it puts target libraries/binaries into /usr/lib64
# Note: glibc's is a library, so $host must be the same as $target
env \
	CXX=/bin/false \
../glibc/configure \
	--disable-dependency-tracking \
	--disable-silent-rules \
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
popd

# gcc
pushd obj_gcc
# XXX: avoid %%configure puts $target libraries in /usr/lib64
env \
	ac_cv_file__proc_self_exe=yes \
	gcc_cv_libc_provides_ssp=yes \
	CC=gcc \
	CXX=g++ \
../gcc/configure \
	--disable-dependency-tracking \
	--disable-silent-rules \
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
	--with-pkgversion='%gcc_version-%release' \
	--with-bugurl='https://bugzilla.altlinux.org/'

env \
	ac_cv_file__proc_self_exe=yes \
	gcc_cv_libc_provides_ssp=yes \
%make_build
# XXX: avoid makeinstall for it puts $target libraries into /usr/lib64
%make_install install DESTDIR=${stagedir}
popd

%install

export PATH=`pwd`/stage%prefix/bin:$PATH

%_make_bin -j%__nprocs \
	-C linux \
	O=`pwd`/obj_kheaders \
	ARCH=%target_kernel \
	INSTALL_HDR_PATH=%buildroot%sysroot/usr \
	headers_install

%make_install install -C obj_binutils DESTDIR=%buildroot tooldir=%cross_gcc_tooldir
%make_install install -C obj_glibc DESTDIR=%buildroot%sysroot
%make_install install -C obj_gcc DESTDIR=%buildroot

# relocate target libgcc_s
if [ -d "%buildroot%prefix/lib/gcc/%target/lib64" ] ; then
    mv %buildroot%prefix/lib/gcc/%target/lib64/libgcc_s.so* %buildroot%prefix/lib/gcc/%target/%gcc_branch/
    rmdir %buildroot%prefix/lib/gcc/%target/lib64
fi

# The spec which describes compiling of `assembler` and
# `assembler-with-cpp` pseudo-languages seems to be hard-coded into
# GCC. As a result GCC always runs `as` (instead of %%target-as) when
# compiling .S files. One possible workaround is to provide `as`
# symlink in GCC's libsubdir (%%prefix/lib/gcc/%%target/%%gcc_branch).
# Just in a case we make symlinks for other tools.
for tool_path in %buildroot%cross_gcc_tooldir/bin/*; do
    tool="$(basename "$tool_path")"
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

# install the test data

mkdir -p %buildroot%test_data
install -m755 -t %buildroot%test_data/ tests/check-cross-gcc.sh
install -m644 -t %buildroot%test_data/ tests/hello.c tests/hello.cpp
if [ -f  "tests/bye-%target_arch.S" ]; then
    install -m644  "$(realpath "tests/bye-%target_arch.S")" %buildroot%test_data/bye.S
fi

# remove runtime bits, not necessary for a cross-toolchain
rm -rvf %buildroot%sysroot/etc
rm -rvf %buildroot%sysroot/var
rm -rvf %buildroot%sysroot/sbin
rm -rvf %buildroot%sysroot/usr/share
rm -rvf %buildroot%sysroot/usr/bin
rm -rvf %buildroot%sysroot/usr/sbin
rm -rvf %buildroot%sysroot/usr/libexec
rm -rvf %buildroot%sysroot/usr/lib64/audit
rm -rvf %buildroot%sysroot/usr/lib64/gconv
rm -rvf %buildroot%prefix/share/info
rm -rvf %buildroot%prefix/share/man/man7
# python pretty-printers conflict with native compiler
rm -rvf %buildroot%prefix/share/gcc-%gcc_branch/python
# conflicts with the native compiler and is not particularly useful
rm -vf  %buildroot%prefix/%_lib/libcc1.so*
# conflicts with the native bfd and is not particularly useful
rm -rvf %buildroot%prefix/lib/bfd-plugins
# Useless for Linux targets
rm -vf  %buildroot%_man1dir/%target-windmc*
rm -vf  %buildroot%_man1dir/%target-windres*
# libtool junk
find %buildroot%prefix/lib/gcc/%target/%gcc_branch -type f -name '*.la' -print -delete
find %buildroot%cross_gcc_tooldir -type f -name '*.la' -print -delete
# Target C++ runtime is used for linking only
find %buildroot%prefix/lib/gcc/%target/%gcc_branch -type f -name 'lib*-gdb.py' -print -delete


# XXX: gcc needs this to locate crt1.o
install -d -m 755 %buildroot%sysroot/usr/lib

rm -vf  %buildroot%prefix/lib/gcc/%target/%gcc_branch/libssp.a
rm -vf  %buildroot%prefix/lib/gcc/%target/%gcc_branch/libssp_nonshared.a
rm -vf  %buildroot%prefix/lib/gcc/%target/%gcc_branch/libssp.so*

# Leave alone $target libraries
%add_verify_elf_skiplist %sysroot/* %prefix/lib/gcc/%target/%gcc_branch/*
%add_findreq_skiplist %sysroot/* %prefix/lib/gcc/%target/%gcc_branch/*
%add_findprov_skiplist %sysroot/* %prefix/lib/gcc/%target/%gcc_branch/*
%add_debuginfo_skiplist %sysroot/* %prefix/lib/gcc/%target/%gcc_branch/*

%post checkinstall
%if "%target_arch" == "i586"
# XXX: x86 targeted binutils align sections at 4 KB (target page size).
# On host architectures with page size > 4KB qemu refuse to load such a binary.
export ASM_EXTRA_FLAGS="-Wl,-Ttext-segment=0x90000000"
%endif
%test_data/check-cross-gcc.sh "%target" "qemu-%target_qemu_arch-static" "%test_data"

%files -n gcc-%target
%_bindir/%target-gcc*
%_bindir/%target-cpp
%_bindir/%target-g++
%_bindir/%target-c++
%_bindir/%target-gcov*
%_bindir/%target-lto*
%prefix/lib/gcc/%target/%gcc_branch/*
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
%dir %cross_gcc_tooldir
%cross_gcc_tooldir/%gcc_branch
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
%dir %cross_gcc_tooldir
%cross_gcc_tooldir/bin
%cross_gcc_tooldir/lib
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

%files checkinstall
%test_data

%changelog
* Thu Mar 06 2025 Ivan A. Melnikov <iv@altlinux.org> 20250101-alt1
- Unify build for all supported targets.
- Update components to sync with Sisyphus:
  + binutils 2.43;
  + gcc 14.2.1;
  + glibc 2.40.0.69.8566822197.
- Apply patches from sisyphus_loongarch64.
- Move tests from from spec to a checkinstall package.
- Various spec improvements.

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

