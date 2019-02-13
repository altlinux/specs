# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-generic-compat
BuildRequires: /usr/bin/expect /usr/bin/m4 perl(English.pm) perl(Exporter.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(IPC/Open2.pm) swig texinfo
# END SourceDeps(oneline)
# due to explicit symlinks
%set_compress_method off
# ldv@ recommends: no debuginfo whatsoever.
%global __find_debuginfo_files %nil
%add_debuginfo_skiplist /usr
%remove_optflags -g

%define fedora 28
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%release is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define release 1.1
%global cross cross
%global rpmprefix %{nil}

%global build_all		1
%global build_aarch64		%{build_all}
%global build_alpha		%{build_all}
%global build_arm		%{build_all}
%global build_arc		%{build_all}
%global build_avr32		%{build_all}
%global build_blackfin		%{build_all}
%global build_c6x		%{build_all}
%global build_cris		%{build_all}
%global build_frv		%{build_all}
%global build_h8300		%{build_all}
%global build_hppa		%{build_all}
%global build_hppa64		%{build_all}
%global build_ia64		%{build_all}
%global build_m32r		%{build_all}
%global build_m68k		%{build_all}
%global build_microblaze	%{build_all}
%global build_mips64		%{build_all}
%global build_mn10300		%{build_all}
%global build_nios2		%{build_all}
%global build_powerpc64		%{build_all}
%global build_powerpc64le	%{build_all}
%global build_riscv64		%{build_all}
%global build_s390x		%{build_all}
%global build_sh		%{build_all}
%global build_sparc64		%{build_all}
%global build_tile		%{build_all}
%global build_x86_64		%{build_all}
%global build_xtensa		%{build_all}

# built compiler generates lots of ICEs
# - none at this time

# gcc considers obsolete
%global build_score		0
%global build_sh64		0

# gcc doesn't build
# - none at this time

# 32-bit packages we don't build as we can use the 64-bit package instead
%global build_i386		0
%global build_mips		0
%global build_powerpc		0
%global build_s390		0
%global build_sh4		0
%global build_sparc		0

# gcc doesn't support
%global build_metag		0
%global build_openrisc		0

# not available in binutils-2.22
%global build_unicore32		0

%global multilib_64_archs sparc64 ppc64 s390x x86_64

# we won't build libgcc for these as it depends on C library or kernel headers
# % global no_libgcc_targets	nios2*|tile-*
%global no_libgcc_targets	none

###############################################################################
#
# The gcc versioning information.  In a sed command below, the specfile winds
# pre-release version numbers in BASE-VER back to the last actually-released
# number.
%global DATE 20181105
%global SVNREV 265809
%global gcc_version 8.2.1
%global gcc_major 8

# Note, cross_gcc_release must be integer, if you want to add suffixes
# to %%{release}, append them after %%{cross_gcc_release} on Release:
# line.  gcc_release is the Fedora gcc release that the patches were
# taken from.
%global gcc_release 5
%global cross_gcc_release 1
%global cross_binutils_version 2.31.1-1
%global isl_version 0.16.1
%global isl_libmajor 15

%global _performance_build 1
# Hardening slows the compiler way too much.
%undefine _hardened_build
%if 0%{?fedora} > 27 || 0%{?rhel} >= 8
# Until annobin is fixed (#1519165).
%undefine _annotated_build
%endif

Summary: Cross C compiler
Name: %{cross}-gcc
Version: %{gcc_version}
Release: alt1_1.1
# libgcc, libgfortran, libmudflap, libgomp, libstdc++ and crtstuff have
# GCC Runtime Exception.
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group: Development/Other
URL: http://gcc.gnu.org
BuildRequires:  gcc-c++
BuildRequires: libisl-devel >= %{isl_version}

# sh5 is deprecrated: https://gcc.gnu.org/ml/gcc/2015-08/msg00101.html
%if !%{build_sh64}
Obsoletes: gcc-sh64-linux-gnu < 6.0.0-1
Obsoletes: gcc-c++-sh64-linux-gnu < 6.0.0-1
%endif

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export svn://gcc.gnu.org/svn/gcc/branches/redhat/gcc-8-branch@%%{SVNREV} gcc-%%{version}-%%{DATE}
# tar cf - gcc-%%{version}-%%{DATE} | xz -9e > gcc-%%{version}-%%{DATE}.tar.xz
%global srcdir gcc-%{version}-%{DATE}
Source0: %{srcdir}.tar.xz

Patch0: gcc8-hack.patch
Patch2: gcc8-i386-libgomp.patch
Patch3: gcc8-sparc-config-detection.patch
Patch4: gcc8-libgomp-omp_h-multilib.patch
Patch5: gcc8-libtool-no-rpath.patch
Patch6: gcc8-isl-dl.patch
Patch7: gcc8-libstdc++-docs.patch
Patch8: gcc8-no-add-needed.patch
Patch9: gcc8-foffload-default.patch
Patch10: gcc8-Wno-format-security.patch
Patch11: gcc8-rh1512529-aarch64.patch
Patch12: gcc8-mcet.patch
Patch13: gcc8-rh1574936.patch

Patch900: cross-intl-filename.patch
Patch901: cross-gcc-microblaze.patch
Patch902: cross-gcc-format-config.patch
Patch903: cross-gcc-arc.patch

%if 0%{?fedora} >= 29 || 0%{?rhel} > 7
BuildRequires: binutils >= 2.31
%else
BuildRequires: binutils >= 2.24
%endif
BuildRequires: zlib-devel gettext gettext-tools, dejagnu, bison, flex, makeinfo, sharutils
BuildRequires: %{cross}-binutils-common >= %{cross_binutils_version}

# right now, we only have this for arm
#BuildRequires: glibc-arm-linux-gnu

# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90
BuildRequires: libasm-devel libdw-devel libdw-devel-static libelf-devel
BuildRequires: libelf-devel >= 0.147
BuildRequires: libgmp-devel libgmpxx-devel, libmpfr-devel >= 2.2.1, libmpc-devel >= 0.8.1
Provides: bundled(libiberty)
Source44: import.info

%description
Cross-build GNU C compiler collection.

%package -n %{cross}-gcc-common
Summary: Cross-build GNU C compiler documentation and translation files
Group: Development/Other
BuildArch: noarch

%description -n %{cross}-gcc-common
Documentation, manual pages and translation files for cross-build GNU C
compiler.

This is the common part of a set of cross-build GNU C compiler packages for
building kernels for other architectures.  No support for cross-building
user space programs is currently supplied as that would massively multiply the
number of packages.

###############################################################################
#
# Conditional arch package definition
#
###############################################################################
%global do_package() \
%if %2 \
%package -n %{rpmprefix}gcc-%1 \
Summary: Cross-build binary utilities for %1 \
Group: Development/C \
Requires: %{cross}-gcc-common == %{version}-%{release} \
BuildRequires: %{rpmprefix}binutils-%1 >= %{cross_binutils_version} \
Requires: %{rpmprefix}binutils-%1 >= %{cross_binutils_version} \
%if 0%{?__isa_bits} == 64 \
Requires: libisl.so.%{isl_libmajor}()(64bit) \
%else \
Requires: libisl.so.%{isl_libmajor} \
%endif \
%description -n %{rpmprefix}gcc-%1 \
Cross-build GNU C compiler. \
\
Only building kernels is currently supported.  Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
\
%package -n %{rpmprefix}gcc-c++-%1 \
Summary: Cross-build binary utilities for %1 \
Group: Development/C++ \
Requires: %{rpmprefix}gcc-%1 == %{version}-%{release} \
%description -n %{rpmprefix}gcc-c++-%1 \
Cross-build GNU C++ compiler. \
\
Only the compiler is provided; not libstdc++.  Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
%endif

%global do_symlink() \
%if %2 \
%package -n gcc-%1 \
Summary: Cross-build binary utilities for %1 \
Group: Development/C \
Requires: gcc-%3 == %{version}-%{release} \
%description -n gcc-%1 \
Cross-build GNU C++ compiler. \
\
Only building kernels is currently supported.  Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
\
%package -n gcc-c++-%1 \
Summary: Cross-build binary utilities for %1 \
Group: Development/C++ \
Requires: gcc-%1 == %{version}-%{release} \
Requires: gcc-c++-%3 == %{version}-%{release} \
%description -n gcc-c++-%1 \
Cross-build GNU C++ compiler. \
\
Only the compiler is provided; not libstdc++.  Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
%endif

%do_package aarch64-linux-gnu	%{build_aarch64}
%do_package alpha-linux-gnu	%{build_alpha}
%do_package arc-linux-gnu	%{build_arc}
%do_package arm-linux-gnu	%{build_arm}
%do_package avr32-linux-gnu	%{build_avr32}
%do_package bfin-linux-gnu	%{build_blackfin}
%do_package c6x-linux-gnu	%{build_c6x}
%do_package cris-linux-gnu	%{build_cris}
%do_package frv-linux-gnu	%{build_frv}
%do_package h8300-linux-gnu	%{build_h8300}
%do_package hppa-linux-gnu	%{build_hppa}
%do_package hppa64-linux-gnu	%{build_hppa64}
%do_package i386-linux-gnu	%{build_i386}
%do_package ia64-linux-gnu	%{build_ia64}
%do_package m32r-linux-gnu	%{build_m32r}
%do_package m68k-linux-gnu	%{build_m68k}
%do_package metag-linux-gnu	%{build_metag}
%do_package microblaze-linux-gnu %{build_microblaze}
%do_package mips-linux-gnu	%{build_mips}
%do_package mips64-linux-gnu	%{build_mips64}
%do_package mn10300-linux-gnu	%{build_mn10300}
%do_package nios2-linux-gnu	%{build_nios2}
%do_package openrisc-linux-gnu	%{build_openrisc}
%do_package powerpc-linux-gnu	%{build_powerpc}
%do_package powerpc64-linux-gnu	%{build_powerpc64}
%do_package powerpc64le-linux-gnu %{build_powerpc64le}
%do_symlink ppc-linux-gnu	%{build_powerpc}	powerpc-linux-gnu
%do_symlink ppc64-linux-gnu	%{build_powerpc64}	powerpc64-linux-gnu
%do_symlink ppc64le-linux-gnu	%{build_powerpc64le}	powerpc64le-linux-gnu
%do_package riscv64-linux-gnu	%{build_riscv64}
%do_package s390-linux-gnu	%{build_s390}
%do_package s390x-linux-gnu	%{build_s390x}
%do_package score-linux-gnu	%{build_score}
%do_package sh-linux-gnu	%{build_sh}
%do_package sh4-linux-gnu	%{build_sh4}
%do_package sh64-linux-gnu	%{build_sh64}
%do_package sparc-linux-gnu	%{build_sparc}
%do_package sparc64-linux-gnu	%{build_sparc64}
%do_package tile-linux-gnu	%{build_tile}
%do_package unicore32-linux-gnu	%{build_unicore32}
%do_package x86_64-linux-gnu	%{build_x86_64}
%do_package xtensa-linux-gnu	%{build_xtensa}

###############################################################################
#
# Preparation
#
###############################################################################
%prep

%setup -q -n %{srcdir} -c
cd %{srcdir}
%patch0 -p0 -b .hack~
%patch2 -p0 -b .i386-libgomp~
%patch3 -p0 -b .sparc-config-detection~
%patch4 -p0 -b .libgomp-omp_h-multilib~
%patch5 -p0 -b .libtool-no-rpath~
# % if %{build_isl}
%patch6 -p0 -b .isl-dl~
# % endif
# % if %{build_libstdcxx_docs}
# % patch7 -p0 -b .libstdc++-docs~
# % endif
%patch8 -p0 -b .no-add-needed~
%patch9 -p0 -b .foffload-default~
%patch10 -p0 -b .Wno-format-security~
%patch11 -p0 -b .rh1512529-aarch64~
%if 0%{?fedora} == 28
%patch12 -p0 -b .mcet~
%endif
%if 0%{?fedora} >= 29 || 0%{?rhel} > 7
%patch13 -p0 -b .rh1574936~
%endif

%patch900 -p0 -b .cross-intl~
%patch901 -p0 -b .microblaze~
%patch902 -p0 -b .format-config~
%patch903 -p0 -b .arc~

echo 'Red Hat Cross %{version}-%{cross_gcc_release}' > gcc/DEV-PHASE

echo 'TM_H += $(srcdir)/config/rs6000/rs6000-modes.h' >> gcc/config/rs6000/t-rs6000

./contrib/gcc_update --touch

LC_ALL=C sed -i -e 's/\xa0/ /' gcc/doc/options.texi

sed -i -e 's/Common Driver Var(flag_report_bug)/& Init(1)/' gcc/common.opt

# This test causes fork failures, because it spawns way too many threads
rm -f gcc/testsuite/go.test/test/chan/goroutines.go

function prep_target () {
    target=$1
    cond=$2

    if [ $cond != 0 ]
    then
	echo $1 >&5
    fi
}

cd ..

(
    prep_target aarch64-linux-gnu	%{build_aarch64}
    prep_target alpha-linux-gnu		%{build_alpha}
    prep_target arc-linux-gnu		%{build_arc}
    prep_target arm-linux-gnu		%{build_arm}
    prep_target avr32-linux-gnu		%{build_avr32}
    prep_target bfin-linux-gnu		%{build_blackfin}
    prep_target c6x-linux-gnu		%{build_c6x}
    prep_target cris-linux-gnu		%{build_cris}
    prep_target frv-linux-gnu		%{build_frv}
    prep_target h8300-linux-gnu		%{build_h8300}
    prep_target hppa-linux-gnu		%{build_hppa}
    prep_target hppa64-linux-gnu	%{build_hppa64}
    prep_target i386-linux-gnu		%{build_i386}
    prep_target ia64-linux-gnu		%{build_ia64}
    prep_target m32r-linux-gnu		%{build_m32r}
    prep_target m68k-linux-gnu		%{build_m68k}
    prep_target metag-linux-gnu		%{build_metag}
    prep_target microblaze-linux-gnu	%{build_microblaze}
    prep_target mips-linux-gnu		%{build_mips}
    prep_target mips64-linux-gnu	%{build_mips64}
    prep_target mn10300-linux-gnu	%{build_mn10300}
    prep_target nios2-linux-gnu		%{build_nios2}
    prep_target openrisc-linux-gnu	%{build_openrisc}
    prep_target powerpc-linux-gnu	%{build_powerpc}
    prep_target powerpc64-linux-gnu	%{build_powerpc64}
    prep_target powerpc64le-linux-gnu	%{build_powerpc64le}
    prep_target riscv64-linux-gnu	%{build_riscv64}
    prep_target s390-linux-gnu		%{build_s390}
    prep_target s390x-linux-gnu		%{build_s390x}
    prep_target score-linux-gnu		%{build_score}
    prep_target sh-linux-gnu		%{build_sh}
    prep_target sh4-linux-gnu		%{build_sh4}
    prep_target sh64-linux-gnu		%{build_sh64}
    prep_target sparc-linux-gnu		%{build_sparc}
    prep_target sparc64-linux-gnu	%{build_sparc64}
    prep_target tile-linux-gnu		%{build_tile}
    prep_target unicore32-linux-gnu	%{build_unicore32}
    prep_target x86_64-linux-gnu	%{build_x86_64}
    prep_target xtensa-linux-gnu	%{build_xtensa}
) 5>target.list

n=0
for target in `cat target.list`
do
    n=1
    break
done
if [ $n = 0 ]
then
    echo "No targets selected" >&2
    exit 8
fi

###############################################################################
#
# Build
#
###############################################################################
%build

%global builddir %{_builddir}/%{srcdir}

# Undo the broken autoconf change in recent Fedora versions
export CONFIG_SITE=NONE

CC=gcc
CXX=g++
OPT_FLAGS=`echo %{optflags}|sed -e 's/\(-Wp,\)\?-D_FORTIFY_SOURCE=[12]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-m64//g;s/-m32//g;s/-m31//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mfpmath=sse/-mfpmath=sse -msse2/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/ -pipe / /g'`
%ifarch sparc
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mcpu=ultrasparc/-mtune=ultrasparc/g;s/-mcpu=v[78]//g'`
%endif
%ifarch %{ix86}
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=i.86//g'`
%endif
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-Werror=format-security/-Wformat-security/g'`
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`
case "$OPT_FLAGS" in
  *-fasynchronous-unwind-tables*)
    sed -i -e 's/-fno-exceptions /-fno-exceptions -fno-asynchronous-unwind-tables /' \
      %{srcdir}/libgcc/Makefile.in
    ;;
esac

#
# Configure the compiler
#
cd %{builddir}
function config_target () {
    echo "=== CONFIGURING $1"

    arch=$1
    prefix=$arch-
    build_dir=$1

    case $arch in
	aarch64-*)	target=aarch64-linux-gnu;;
	arc-*)		target=arc-linux-gnu;;
	arm-*)		target=arm-linux-gnueabi;;
	avr32-*)	target=avr-linux;;
	bfin-*)		target=bfin-uclinux;;
	c6x-*)		target=c6x-uclinux;;
	h8300-*)	target=h8300-elf;;
	mn10300-*)	target=am33_2.0-linux;;
	m68knommu-*)	target=m68k-linux;;
	openrisc-*)	target=or1k-linux;;
	parisc-*)	target=hppa-linux;;
	score-*)	target=score-elf;;
	sh64-*)		target=sh64-linux-elf;;
	tile-*)		target=tilegx-linux;;
	v850-*)		target=v850e-linux;;
	x86-*)		target=x86_64-linux;;
	*)		target=$arch;;
    esac

    echo $arch: target is $target
    #export CFLAGS="$RPM_OPT_FLAGS"

    CONFIG_FLAGS=
    case $arch in
	arc-*)
	    CONFIG_FLAGS="--with-cpu=hs38"
	    ;;

	arm-*)
	    CONFIG_FLAGS="--with-tune=generic-armv7-a --with-arch=armv7-a \
		--with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux"
	    ;;
	mips64-*)
	    CONFIG_FLAGS="--with-arch=mips64r2 --with-abi=64 --with-arch_32=mips32r2 --with-fp-32=xx"
	    ;;
	powerpc-*|powerpc64-*|ppc-*|ppc64-*)
	    CONFIG_FLAGS="--with-cpu-32=power7 --with-tune-32=power8 --with-cpu-64=power7 --with-tune-64=power8 --enable-secureplt"
	    ;;
	powerpc64le-*|ppc64le-*)
	    CONFIG_FLAGS="--with-cpu-32=power8 --with-tune-32=power8 --with-cpu-64=power8 --with-tune-64=power8 --enable-secureplt"
	    ;;
	s390*-*)
%if 0%{?fedora} >= 26 || 0%{?rhel} > 7
	    CONFIG_FLAGS="--with-arch=zEC12 --with-tune=z13 --enable-decimal-float"
%else
	    CONFIG_FLAGS="--with-arch=z9-109 --with-tune=z10 --enable-decimal-float"
%endif
	    ;;
	sh-*)
	    CONFIG_FLAGS=--with-multilib-list=m1,m2,m2e,m2a,m2a-single,m4,m4-single,m4-single-only,m4-nofpu
	    ;;
	sh4-*)
	    CONFIG_FLAGS=--with-multilib-list=m4,m4-single,m4-single-only,m4-nofpu
	    ;;
	sh64-*)
	    CONFIG_FLAGS=--with-multilib-list=m5-32media,m5-32media-nofpu,m5-compact,m5-compact-nofpu,m5-64media,m5-64media-nofpu
	    ;;
	sparc-*)
	    CONFIG_FLAGS="--disable-linux-futex --with-cpu=v7"
	    ;;
	sparc64-*)
	    CONFIG_FLAGS="--disable-linux-futex --with-cpu=ultrasparc"
	    ;;
	tile-*)
	    #CONFIG_FLAGS="--with-arch_32=tilepro"
	    ;;
	x86_64-*)
	    CONFIG_FLAGS="--with-arch_32=i686 --with-tune=generic --enable-cet"
	    ;;
    esac

    case $arch in
	alpha*|powerpc*|ppc*|s390*|sparc*)
	    CONFIG_FLAGS="$CONFIG_FLAGS --with-long-double-128" ;;
    esac

    case $arch in
	i[3456]86*|x86_64*|ppc*|ppc64*|s390*|arm*|aarch64*|mips*)
	    CONFIG_FLAGS="$CONFIG_FLAGS --enable-gnu-indirect-function" ;;
    esac

# Right now, the only cross glibc is glibc-arm-linux-gnu
    case $arch in
#	arm*) CONFIG_FLAGS="$CONFIG_FLAGS --enable-shared" ;;
	*) CONFIG_FLAGS="$CONFIG_FLAGS --disable-shared" ;;
    esac

%ifnarch %{mips}
    case $arch in
	mips*) ;;
	*) CONFIG_FLAGS="$CONFIG_FLAGS --with-linker-hash-style=gnu" ;;
    esac
%endif

    mkdir $build_dir
    cd $build_dir

    # We could optimize the cross builds size by --enable-shared but the produced
    # binaries may be less convenient in the embedded environment.
    CC="$CC" \
    CXX="$CXX" \
    CFLAGS="$OPT_FLAGS" \
    CXXFLAGS="`echo " $OPT_FLAGS " | sed 's/ -Wall / /g;s/ -fexceptions / /g' \
		  | sed 's/ -Wformat-security / -Wformat -Wformat-security /'`" \
    CFLAGS_FOR_TARGET="-g -O2 -Wall -fexceptions" \
    AR_FOR_TARGET=%{_bindir}/$arch-ar \
    AS_FOR_TARGET=%{_bindir}/$arch-as \
    DLLTOOL_FOR_TARGET=%{_bindir}/$arch-dlltool \
    LD_FOR_TARGET=%{_bindir}/$arch-ld \
    NM_FOR_TARGET=%{_bindir}/$arch-nm \
    OBJDUMP_FOR_TARGET=%{_bindir}/$arch-objdump \
    RANLIB_FOR_TARGET=%{_bindir}/$arch-ranlib \
    READELF_FOR_TARGET=%{_bindir}/$arch-readelf \
    STRIP_FOR_TARGET=%{_bindir}/$arch-strip \
    WINDRES_FOR_TARGET=%{_bindir}/$arch-windres \
    WINDMC_FOR_TARGET=%{_bindir}/$arch-windmc \
    LDFLAGS='-Wl,-z,relro ' \
    ../%{srcdir}/configure \
	--bindir=%{_bindir} \
	--build=%{_target_platform} \
	--datadir=%{_datadir} \
	--disable-decimal-float \
	--disable-dependency-tracking \
	--disable-gold \
	--disable-libgcj \
	--disable-libgomp \
	--disable-libmpx \
	--disable-libquadmath \
	--disable-libssp \
	--disable-libunwind-exceptions \
	--disable-silent-rules \
	--disable-sjlj-exceptions \
	--disable-threads \
	--with-ld=/usr/bin/$arch-ld \
	--enable-__cxa_atexit \
	--enable-checking=release \
	--enable-gnu-unique-object \
	--enable-initfini-array \
	--enable-languages=c,c++ \
	--enable-linker-build-id \
	--enable-lto \
	--enable-nls \
	--enable-obsolete \
	--enable-plugin \
%ifarch ppc ppc64 ppc64le ppc64p7
	--enable-secureplt \
%endif
	--enable-targets=all \
	--exec-prefix=%{_exec_prefix} \
	--host=%{_target_platform} \
	--includedir=%{_includedir} \
	--infodir=%{_infodir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir} \
	--mandir=%{_mandir} \
	--prefix=%{_prefix} \
	--program-prefix=$prefix \
	--sbindir=%{_sbindir} \
	--sharedstatedir=%{_sharedstatedir} \
	--sysconfdir=%{_sysconfdir} \
	--target=$target \
	--with-bugurl=http://bugzilla.altlinux.org/ \
	--with-gcc-major-version-only \
	--with-isl \
	--with-newlib \
	--with-plugin-ld=%{_bindir}/$arch-ld \
	--with-sysroot=%{_libexecdir}/$arch/sys-root \
	--with-system-libunwind \
	--with-system-zlib \
	--without-headers \
	$CONFIG_FLAGS
%if 0
	--libdir=%{_libdir} # we want stuff in /usr/lib/gcc/ not /usr/lib64/gcc
%endif

    cd ..
}

for target in `cat target.list`
do
    config_target $target
done

function build_target () {
    echo "=== BUILDING $1"

    arch=$1
    build_dir=$1

    BUILD_FLAGS=
    case $arch in
	x86_64-*)
	    BUILD_FLAGS="gcc_cv_libc_provides_ssp=yes gcc_cv_as_ix86_tlsldm=yes"
	    ;;
    esac

    AR_FOR_TARGET=%{_bindir}/$arch-ar \
    AS_FOR_TARGET=%{_bindir}/$arch-as \
    DLLTOOL_FOR_TARGET=%{_bindir}/$arch-dlltool \
    LD_FOR_TARGET=%{_bindir}/$arch-ld \
    NM_FOR_TARGET=%{_bindir}/$arch-nm \
    OBJDUMP_FOR_TARGET=%{_bindir}/$arch-objdump \
    RANLIB_FOR_TARGET=%{_bindir}/$arch-ranlib \
    READELF_FOR_TARGET=%{_bindir}/$arch-readelf \
    STRIP_FOR_TARGET=%{_bindir}/$arch-strip \
    WINDRES_FOR_TARGET=%{_bindir}/$arch-windres \
    WINDMC_FOR_TARGET=%{_bindir}/$arch-windmc \
    make -C $build_dir %{_smp_mflags} tooldir=%{_prefix} $BUILD_FLAGS all-gcc

    echo "=== BUILDING LIBGCC $1"
    case $arch in
	%{no_libgcc_targets})
	    ;;
	*)
	    make -C $build_dir tooldir=%{_prefix} all-target-libgcc
	    ;;
    esac

}

for target in `cat target.list`
do
    build_target $target
done

###############################################################################
#
# Installation
#
###############################################################################
%install

function install_bin () {
    echo "=== INSTALLING $1"

    arch=$1
    cpu=${1%%%%-*}

    case $arch in
	%{no_libgcc_targets})	with_libgcc="";;
	*)			with_libgcc="install-target-libgcc";;
    esac

    make -C $arch DESTDIR=%{buildroot} install-gcc ${with_libgcc}

    # We want links for ppc and ppc64 also if we make powerpc, powerpc64 or  powerpc64le
    case $cpu in
	powerpc*)
	    cd %{buildroot}/usr/bin
	    for i in $cpu-*
	    do
		ln -s $i ppc${i#powerpc}
	    done
	    cd -
	    ;;
    esac
}

for target in `cat target.list`
do
    mkdir -p %{buildroot}%{_libexecdir}/$target/sys-root
    install_bin $target
done

grep ^powerpc target.list | sed -e s/powerpc/ppc/ >symlink-target.list

# For cross-gcc we drop the documentation.
rm -rf %{buildroot}%{_infodir}

# Remove binaries we will not be including, so that they don't end up in
# gcc-debuginfo
rm -f %{buildroot}%{_libdir}/{libffi*,libiberty.a}
rm -f %{buildroot}%{_libexecdir}/gcc/*/%{gcc_major}/install-tools/{mkheaders,fixincl}
rm -f %{buildroot}%{_prefix}/bin/*-gcc-%{gcc_major} || :
rmdir  %{buildroot}%{_includedir}

find %{buildroot}%{_datadir} -name gcc.mo |
while read x
do
    y=`dirname $x`
    mv $x $y/%{cross}-gcc.mo
done

%find_lang %{cross}-gcc

gzip %{buildroot}%{_mandir}/man1/*.1
rm %{buildroot}%{_mandir}/man7/*.7
rmdir %{buildroot}%{_mandir}/man7

# All the installed manual pages and translation files for each program are the
# same, so symlink them to the common package
cd %{buildroot}%{_mandir}/man1
for i in %{cross}-cpp.1.gz %{cross}-gcc.1.gz %{cross}-g++.1.gz %{cross}-gcov.1.gz
do
    j=${i#%{cross}-}

    for k in *-$j
    do
	if [ $k != $i -a ! -L $k ]
	then
	    mv $k $i
	    ln -s $i $k
	fi
    done
done

# Add manpages the additional symlink-only targets
%if %{build_powerpc}%{build_powerpc64}%{build_powerpc64le}
for i in powerpc*
do
    ln -s $i ppc${i#powerpc}
done
%endif

cd -

function install_lang () {
    arch=$1
    cpu=${arch%%%%-*}

    case $cpu in
	avr32)		target_cpu=avr;;
	bfin)		target_cpu=bfin;;
	h8300)		target_cpu=h8300;;
	mn10300)	target_cpu=am33_2.0;;
	openrisc)	target_cpu=or1k;;
	parisc)		target_cpu=hppa;;
	score)		target_cpu=score;;
	tile)		target_cpu=tilegx;;
	v850)		target_cpu=v850e;;
	x86)		target_cpu=x86_64;;
	*)		target_cpu=$cpu;;
    esac

    (
	echo '%{_bindir}/'$arch'*-cpp'
	echo '%{_bindir}/'$arch'*-gcc'
	echo '%{_bindir}/'$arch'*-gcc-ar'
	echo '%{_bindir}/'$arch'*-gcc-nm'
	echo '%{_bindir}/'$arch'*-gcc-ranlib'
	echo '%{_bindir}/'$arch'*-gcov*'
	echo '%{_mandir}/man1/'$arch'*-cpp*'
	echo '%{_mandir}/man1/'$arch'*-gcc*'
	echo '%{_mandir}/man1/'$arch'*-gcov*'
	case $cpu in
	    arm*)
#		echo '/usr/arm-linux-gnueabi/lib/libgcc_s.so*'
		;;
	esac
	case $cpu in
	    ppc*|ppc64*)
		;;
	    *)
		echo '/usr/lib/gcc/'$target_cpu'-*/'
		echo '%{_libexecdir}/gcc/'$target_cpu'*/*/cc1'
		echo '%{_libexecdir}/gcc/'$target_cpu'*/*/collect2'
		echo '%{_libexecdir}/gcc/'$target_cpu'*/*/[abd-z]*'
		echo %{_libexecdir}/$arch/sys-root
		;;
	esac

    ) >files.$arch

    (
	echo '%{_bindir}/'$arch'*-c++'
	echo '%{_bindir}/'$arch'*-g++'
	echo '%{_mandir}/man1/'$arch'*-g++*'
	case $cpu in
	    ppc*|ppc64*)
		;;
	    *)
		echo '%{_libexecdir}/gcc/'$target_cpu'*/*/cc1plus'
	esac
    ) >files-c++.$arch
}

for target in `cat target.list symlink-target.list`
do
    install_lang $target
done

%global __ar_no_strip $RPM_BUILD_DIR/%{srcdir}/ar-no-strip
cat >%{__ar_no_strip} <<EOF
#!/bin/bash
f=\$2
if [ \${f##*/} = libgcc.a -o \${f##*/} = libgcov.a ]
then
	:
else
	strip \$*
fi
EOF
chmod +x %{__ar_no_strip}
%undefine __strip
%global __strip %{__ar_no_strip}
# inside a symlink - not for rpm404
#sed -i -e /sys-root/d files.ppc64-linux-gnu

###############################################################################
#
# Filesets
#
###############################################################################
%files -n %{cross}-gcc-common -f %{cross}-gcc.lang
%doc %{srcdir}/COPYING*
%doc %{srcdir}/README
%{_mandir}/man1/%{cross}-*

%global do_files() \
%if %2 \
%files -n %{rpmprefix}gcc-%1 -f files.%1 \
%files -n %{rpmprefix}gcc-c++-%1 -f files-c++.%1 \
%endif

%do_files aarch64-linux-gnu	%{build_aarch64}
%do_files alpha-linux-gnu	%{build_alpha}
%do_files arc-linux-gnu		%{build_arc}
%do_files arm-linux-gnu		%{build_arm}
%do_files avr32-linux-gnu	%{build_avr32}
%do_files bfin-linux-gnu	%{build_blackfin}
%do_files c6x-linux-gnu		%{build_c6x}
%do_files cris-linux-gnu	%{build_cris}
%do_files frv-linux-gnu		%{build_frv}
%do_files h8300-linux-gnu	%{build_h8300}
%do_files hppa-linux-gnu	%{build_hppa}
%do_files hppa64-linux-gnu	%{build_hppa64}
%do_files i386-linux-gnu	%{build_i386}
%do_files ia64-linux-gnu	%{build_ia64}
%do_files m32r-linux-gnu	%{build_m32r}
%do_files m68k-linux-gnu	%{build_m68k}
%do_files metag-linux-gnu	%{build_metag}
%do_files microblaze-linux-gnu	%{build_microblaze}
%do_files mips-linux-gnu	%{build_mips}
%do_files mips64-linux-gnu	%{build_mips64}
%do_files mn10300-linux-gnu	%{build_mn10300}
%do_files nios2-linux-gnu	%{build_nios2}
%do_files openrisc-linux-gnu	%{build_openrisc}
%do_files powerpc-linux-gnu	%{build_powerpc}
%do_files powerpc64-linux-gnu	%{build_powerpc64}
%do_files powerpc64le-linux-gnu	%{build_powerpc64le}
%do_files ppc-linux-gnu		%{build_powerpc}
%do_files ppc64-linux-gnu	%{build_powerpc64}
%do_files ppc64le-linux-gnu	%{build_powerpc64le}
%do_files riscv64-linux-gnu	%{build_riscv64}
%do_files s390-linux-gnu	%{build_s390}
%do_files s390x-linux-gnu	%{build_s390x}
%do_files score-linux-gnu	%{build_score}
%do_files sh-linux-gnu		%{build_sh}
%do_files sh4-linux-gnu		%{build_sh4}
%do_files sh64-linux-gnu	%{build_sh64}
%do_files sparc-linux-gnu	%{build_sparc}
%do_files sparc64-linux-gnu	%{build_sparc64}
%do_files tile-linux-gnu	%{build_tile}
%do_files unicore32-linux-gnu	%{build_unicore32}
%do_files x86_64-linux-gnu	%{build_x86_64}
%do_files xtensa-linux-gnu	%{build_xtensa}

%changelog
* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 8.2.1-alt1_1.1
- update to new release by fcimport

* Mon Oct 09 2017 Igor Vlasenko <viy@altlinux.ru> 7.1.1-alt1_3
- update to new release by fcimport

* Thu Jan 12 2017 Igor Vlasenko <viy@altlinux.ru> 6.1.1-alt1_2
- new version

* Fri Dec 11 2015 Alexey Shabalin <shaba@altlinux.ru> 5.2.1-alt1_4
- new version
- build only aarch64, arm, x86_64

* Fri Apr 04 2014 Igor Vlasenko <viy@altlinux.ru> 4.8.2-alt1_2
- new version

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 4.8.1-alt1_5.2
- new version

* Thu Aug 15 2013 Alexey Shabalin <shaba@altlinux.ru> 4.7.1-alt2_0.1.20120606.1
- rebuild

* Wed Aug 14 2013 Igor Vlasenko <viy@altlinux.ru> 4.7.1-alt1_0.1.20120606.1
- fc import


