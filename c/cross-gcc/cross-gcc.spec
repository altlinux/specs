# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison /usr/bin/expect /usr/bin/m4 /usr/bin/makeinfo /usr/bin/pdflatex /usr/bin/perl /usr/bin/pod2html /usr/bin/runtest /usr/bin/texi2dvi clang-devel gcc-c++ libX11-devel libalsa-devel libjack-devel perl(English.pm) perl(Exporter.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(IPC/Open2.pm) perl(Pod/LaTeX.pm) python-devel
# END SourceDeps(oneline)
# due to explicit symlinks
%set_compress_method gzip
# ldv@ recommends: no debuginfo whatsoever.
%global __find_debuginfo_files %nil
%add_debuginfo_skiplist /usr

%define fedora 21
# %%release is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define release 2
%define cross cross
%define rpmprefix %{nil}

%define build_all		1
%define build_aarch64		%{build_all}
%define build_alpha		%{build_all}
%define build_arm		%{build_all}
%define build_avr32		%{build_all}
%define build_blackfin		%{build_all}
%define build_c6x		%{build_all}
%define build_cris		%{build_all}
%define build_frv		%{build_all}
%define build_h8300		%{build_all}
%define build_hppa		%{build_all}
%define build_hppa64		%{build_all}
%define build_ia64		%{build_all}
%define build_m32r		%{build_all}
%define build_m68k		%{build_all}
%define build_microblaze	%{build_all}
%define build_mips64		%{build_all}
%define build_mn10300		%{build_all}
%define build_powerpc64		%{build_all}
%define build_s390x		%{build_all}
%define build_sh		%{build_all}
%define build_sh64		%{build_all}
%define build_sparc64		%{build_all}
%define build_tile		%{build_all}
%define build_x86_64		%{build_all}
%define build_xtensa		%{build_all}

# built compiler generates lots of ICEs
# - none at this time

# gcc considers obsolete
%define build_score		0

# gcc doesn't build
# - none at this time

# 32-bit packages we don't build as we can use the 64-bit package instead
%define build_i386		0
%define build_mips		0
%define build_powerpc		0
%define build_s390		0
%define build_sh4		0
%define build_sparc		0

# gcc doesn't support
%define build_metag		0
%define build_openrisc		0

# not available in binutils-2.22
%define build_unicore32		0

%global build_cloog 1
%global multilib_64_archs sparc64 ppc64 s390x x86_64

# we won't build libgcc for these as it depends on C library or kernel headers
%define no_libgcc_targets	cris*|s390*|sh*|tile-*

###############################################################################
#
# The gcc versioning information.  In a sed command below, the specfile winds
# pre-release version numbers in BASE-VER back to the last actually-released
# number.
%global DATE 20140120
%global SVNREV 206854
%global gcc_version 4.8.2

# Note, cross_gcc_release must be integer, if you want to add suffixes
# to %{release}, append them after %{cross_gcc_release} on Release:
# line.  gcc_release is the Fedora gcc release that the patches were
# taken from.
%global gcc_release 15
%global cross_gcc_release 2
%global cross_binutils_version 2.24-2

Summary: Cross C compiler
Name: %{cross}-gcc
Version: %{gcc_version}
Release: alt1_2
# libgcc, libgfortran, libmudflap, libgomp, libstdc++ and crtstuff have
# GCC Runtime Exception.
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group: Development/Other
URL: http://gcc.gnu.org

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export svn://gcc.gnu.org/svn/gcc/branches/redhat/gcc-4_7-branch@%{SVNREV} gcc-%{version}-%{DATE}
# tar cf - gcc-%{version}-%{DATE} | bzip2 -9 > gcc-%{version}-%{DATE}.tar.bz2
%define srcdir gcc-%{version}-%{DATE}
Source0: %{srcdir}.tar.bz2
%global isl_version 0.11.1
Source1: ftp://gcc.gnu.org/pub/gcc/infrastructure/isl-%{isl_version}.tar.bz2
%global cloog_version 0.18.0
Source2: ftp://gcc.gnu.org/pub/gcc/infrastructure/cloog-%{cloog_version}.tar.gz

Patch0: gcc48-hack.patch
Patch1: gcc48-java-nomulti.patch
Patch2: gcc48-ppc32-retaddr.patch
Patch3: gcc48-rh330771.patch
Patch4: gcc48-i386-libgomp.patch
Patch5: gcc48-sparc-config-detection.patch
Patch6: gcc48-libgomp-omp_h-multilib.patch
Patch7: gcc48-libtool-no-rpath.patch
Patch8: gcc48-cloog-dl.patch
Patch9: gcc48-cloog-dl2.patch
Patch10: gcc48-pr38757.patch
Patch11: gcc48-libstdc++-docs.patch
Patch12: gcc48-no-add-needed.patch
Patch13: gcc48-pr56564.patch
Patch14: gcc48-pr56493.patch
Patch15: gcc48-color-auto.patch
Patch16: gcc48-pr28865.patch
Patch17: gcc48-libgo-p224.patch
Patch18: gcc48-pr60137.patch
Patch19: gcc48-pr60010.patch
Patch20: gcc48-pr60046.patch

Patch100: cross-intl-filename.patch
# ia64 - http://gcc.gnu.org/bugzilla/show_bug.cgi?id=44553
# m68k - http://gcc.gnu.org/bugzilla/show_bug.cgi?id=53557
# alpha - http://gcc.gnu.org/bugzilla/show_bug.cgi?id=55344
Patch101: cross-gcc-with-libgcc.patch
Patch102: cross-gcc-sh-libgcc.patch
Patch103: gcc48-tmake_in_config.patch

Patch1100: isl-%{isl_version}-aarch64-config.patch

BuildRequires: binutils >= 2.20.51.0.2-12
BuildRequires: zlib-devel gettext dejagnu bison flex texinfo sharutils
BuildRequires: %{cross}-binutils-common >= %{cross_binutils_version}

# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
%ifarch %{multilib_64_archs} sparcv9 ppc
# Ensure glibc{,-devel} is installed for both multilib arches
%endif
BuildRequires: elfutils-devel >= 0.147
BuildRequires: libelf-devel >= 0.147
BuildRequires: libgmp-devel libgmp_cxx-devel libmpfr-devel >= 2.3.1 libmpc-devel >= 0.8.1
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

%define do_package() \
%if %2 \
%package -n %{rpmprefix}gcc-%1 \
Summary: Cross-build binary utilities for %1 \
Group: Development/Tools \
Requires: %{cross}-gcc-common == %{version}-%{release} \
BuildRequires: %{rpmprefix}binutils-%1 >= %{cross_binutils_version} \
Requires: %{rpmprefix}binutils-%1 >= %{cross_binutils_version} \
%description -n %{rpmprefix}gcc-%1 \
Cross-build GNU C compiler. \
\
Only building kernels is currently supported.  Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
\
%package -n %{rpmprefix}gcc-c++-%1 \
Summary: Cross-build binary utilities for %1 \
Group: Development/Tools \
Requires: %{rpmprefix}gcc-%1 == %{version}-%{release} \
%description -n %{rpmprefix}gcc-c++-%1 \
Cross-build GNU C++ compiler. \
\
Only the compiler is provided; not libstdc++.  Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
%endif

%define do_symlink() \
%if %2 \
%package -n gcc-%1 \
Summary: Cross-build binary utilities for %1 \
Group: Development/Tools \
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
Group: Development/Tools \
Requires: gcc-%1 == %{version}-%{release} \
Requires: gcc-c++-%3 == %{version}-%{release} \
%description -n gcc-c++-%1 \
Cross-build GNU C++ compiler. \
\
Only the compiler is provided; not libstdc++.  Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
%endif

%do_package alpha-linux-gnu	%{build_alpha}
%do_package arm-linux-gnu	%{build_arm}
%do_package aarch64-linux-gnu	%{build_aarch64}
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
%do_package openrisc-linux-gnu	%{build_openrisc}
%do_package powerpc-linux-gnu	%{build_powerpc}
%do_package powerpc64-linux-gnu	%{build_powerpc64}
%do_symlink ppc-linux-gnu	%{build_powerpc}	powerpc-linux-gnu
%do_symlink ppc64-linux-gnu	%{build_powerpc64}	powerpc64-linux-gnu
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

%setup -q -n %{srcdir} -c -a 1 -a 2
cd %{srcdir}
%patch0 -p0 -b .hack~
%patch1 -p0 -b .java-nomulti~
%patch2 -p0 -b .ppc32-retaddr~
%patch3 -p0 -b .rh330771~
%patch4 -p0 -b .i386-libgomp~
%patch5 -p0 -b .sparc-config-detection~
%patch6 -p0 -b .libgomp-omp_h-multilib~
%patch7 -p0 -b .libtool-no-rpath~
%if %{build_cloog}
%patch8 -p0 -b .cloog-dl~
%patch9 -p0 -b .cloog-dl2~
%endif
%patch10 -p0 -b .pr38757~



%patch12 -p0 -b .no-add-needed~
%patch13 -p0 -b .pr56564~
%patch14 -p0 -b .pr56493~
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
%patch15 -p0 -b .color-auto~
%endif
%patch16 -p0 -b .pr28865~
%patch17 -p0 -b .libgo-p224~
rm -f libgo/go/crypto/elliptic/p224{,_test}.go
%patch18 -p0 -b .pr60137~
%patch19 -p0 -b .pr60010~
%patch20 -p0 -b .pr60046~

%patch100 -p0 -b .cross-intl~
%patch101 -p1 -b .with-libgcc~
%patch102 -p0 -b .sh-libgcc~
%patch103 -p0 -b .tmake~

cd ..
%patch1100 -p0 -b .isl-aarch64~
cd -

# Move the version number back to 4.8.2
sed -i -e 's/4\.8\.3/4.8.2/' gcc/BASE-VER
echo 'Red Hat %{version}-%{cross_gcc_release}' > gcc/DEV-PHASE

%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
# Default to -gdwarf-4 -fno-debug-types-section rather than -gdwarf-2
sed -i '/UInteger Var(dwarf_version)/s/Init(2)/Init(4)/' gcc/common.opt
sed -i '/flag_debug_types_section/s/Init(1)/Init(0)/' gcc/common.opt
sed -i '/dwarf_record_gcc_switches/s/Init(0)/Init(1)/' gcc/common.opt
sed -i 's/\(may be either 2, 3 or 4; the default version is \)2\./\14./' gcc/doc/invoke.texi
%else
# Default to -gdwarf-3 rather than -gdwarf-2
sed -i '/UInteger Var(dwarf_version)/s/Init(2)/Init(3)/' gcc/common.opt
sed -i 's/\(may be either 2, 3 or 4; the default version is \)2\./\13./' gcc/doc/invoke.texi
sed -i 's/#define[[:blank:]]*EMIT_ENTRY_VALUE[[:blank:]].*$/#define EMIT_ENTRY_VALUE 0/' gcc/{var-tracking,dwarf2out}.c
sed -i 's/#define[[:blank:]]*EMIT_TYPED_DWARF_STACK[[:blank:]].*$/#define EMIT_TYPED_DWARF_STACK 0/' gcc/dwarf2out.c
sed -i 's/#define[[:blank:]]*EMIT_DEBUG_MACRO[[:blank:]].*$/#define EMIT_DEBUG_MACRO 0/' gcc/dwarf2out.c
%endif

./contrib/gcc_update --touch

LC_ALL=C sed -i -e 's/\xa0/ /' gcc/doc/options.texi

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
    prep_target alpha-linux-gnu		%{build_alpha}
    prep_target arm-linux-gnu		%{build_arm}
    prep_target aarch64-linux-gnu	%{build_aarch64}
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
    prep_target openrisc-linux-gnu	%{build_openrisc}
    prep_target powerpc-linux-gnu	%{build_powerpc}
    prep_target powerpc64-linux-gnu	%{build_powerpc64}
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

%define builddir %{_builddir}/%{srcdir}

# Undo the broken autoconf change in recent Fedora versions
export CONFIG_SITE=NONE

#
# Configure and build the ISL and CLooG libraries
#
%if %{build_cloog}

%define isl_source %{builddir}/isl-%{isl_version}
%define isl_build %{builddir}/isl-build
%define isl_install %{builddir}/isl-install

mkdir %{isl_build} %{isl_install}
%ifarch s390 s390x
ISL_FLAG_PIC=-fPIC
%else
ISL_FLAG_PIC=-fpic
%endif
cd %{isl_build}
%{isl_source}/configure \
    --disable-shared \
    CC=/usr/bin/gcc \
    CXX=/usr/bin/g++ \
    CFLAGS="${CFLAGS:-%optflags} $ISL_FLAG_PIC" \
    --prefix=%{isl_install}
make %{?_smp_mflags}
make install
cd ..

%define cloog_source %{builddir}/cloog-%{cloog_version}
%define cloog_build %{builddir}/cloog-build
%define cloog_install %{builddir}/cloog-install

mkdir %{cloog_build} %{builddir}/cloog-install
cd %{cloog_build}
cat >> %{cloog_source}/source/isl/constraints.c << \EOF
#include <isl/flow.h>
static void __attribute__((used)) *s1 = (void *) isl_union_map_compute_flow;
static void __attribute__((used)) *s2 = (void *) isl_map_dump;
EOF
sed -i 's|libcloog|libgcc48privatecloog|g' \
    %{cloog_source}/{,test/}Makefile.{am,in}

%{cloog_source}/configure \
    --with-isl=system \
    --with-isl-prefix=%{isl_install} \
    CC=/usr/bin/gcc \
    CXX=/usr/bin/g++ \
    CFLAGS="${CFLAGS:-%optflags}" \
    CXXFLAGS="${CXXFLAGS:-%optflags}" \
    --prefix=%{cloog_install}
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
make %{?_smp_mflags} install
cd %{cloog_install}/lib
rm libgcc48privatecloog-isl.so{,.4}
mv libgcc48privatecloog-isl.so.4.0.0 libcloog-isl.so.4
ln -sf libcloog-isl.so.4 libcloog-isl.so
ln -sf libcloog-isl.so.4 libcloog.so

%endif

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
	arm-*)		target=arm-linux-gnueabi;;
	aarch64-*)	target=aarch64-linux-gnu;;
	avr32-*)	target=avr-linux;;
	bfin-*)		target=bfin-uclinux;;
	c6x-*)		target=c6x-uclinux;;
	h8300-*)	target=h8300-elf;;
	mn10300-*)	target=am33_2.0-linux;;
	m68knommu-*)	target=m68k-linux;;
	openrisc-*)	target=or32-linux;;
	parisc-*)	target=hppa-linux;;
	score-*)	target=score-elf;;
	sh64-*)		target=sh64-linux;;
	tile-*)		target=tilegx-linux;;
	v850-*)		target=v850e-linux;;
	x86-*)		target=x86_64-linux;;
	*)		target=$arch;;
    esac

    echo $arch: target is $target
    #export CFLAGS="$RPM_OPT_FLAGS"

    CONFIG_FLAGS=
    case $arch in
	arm)
	    CONFIG_FLAGS="--with-cpu=cortex-a8 --with-tune=cortex-a8 --with-arch=armv7-a \
		--with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux"
	    ;;
	powerpc-*|powerpc64-*)
	    CONFIG_FLAGS="--with-cpu-32=power4 --with-tune-32=power6 --with-cpu-64=power4 --with-tune-64=power6 --enable-secureplt"
	    ;;
	s390*-*)
	    CONFIG_FLAGS="--with-arch=z9-109 --with-tune=z10 --enable-decimal-float"
	    ;;
	sh-*)
	    CONFIG_FLAGS=--with-multilib-list=m1,m2,m2e,m4,m4-single,m4-single-only,m2a,m2a-single,!m2a,!m2a-single
	    ;;
	sh64-*)
	    CONFIG_FLAGS=--with-multilib-list=m5-32media,m5-32media-nofpu,m5-compact,m5-compact-nofpu,m5-64media,m5-64media-nofpu
	    ;;
	sparc-*)
	    CONFIG_FLAGS="--disable-linux-futex"
	    ;;
	tile-*)
	    #CONFIG_FLAGS="--with-arch_32=tilepro"
	    ;;
	x86-*)
	    CONFIG_FLAGS="--with-arch_32=i686"
	    ;;
    esac

    case $arch in
	alpha|powerpc*|s390*|sparc*)
	    CONFIG_FLAGS="$CONFIG_FLAGS --with-long-double-128" ;;
    esac

    mkdir $build_dir
    cd $build_dir

    # We could optimize the cross builds size by --enable-shared but the produced
    # binaries may be less convenient in the embedded environment.
    AR_FOR_TARGET=%{_bindir}/$arch-ar \
    AS_FOR_TARGET=%{_bindir}/$arch-as \
    DLLTOOL_FOR_TARGET=%{_bindir}/$arch-dlltool \
    LD_FOR_TARGET=%{_bindir}/$arch-ld \
    NM_FOR_TARGET=%{_bindir}/$arch-nm \
    OBJDUMP_FOR_TARGET=%{_bindir}/$arch-objdump \
    RANLIB_FOR_TARGET=%{_bindir}/$arch-ranlib \
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
	--disable-libgomp \
	--disable-libmudflap \
	--disable-libquadmath \
	--disable-libssp \
	--disable-nls \
	--disable-plugin \
	--disable-shared \
	--disable-silent-rules \
	--disable-sjlj-exceptions \
	--disable-threads \
	--enable-checking=$checking \
	--enable-gnu-unique-object \
	--enable-initfini-array \
	--enable-languages=c,c++ \
	--enable-linker-build-id \
	--enable-nls \
	--enable-obsolete \
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
	--with-linker-hash-style=gnu \
	--with-newlib \
	--with-sysroot=%{_libexecdir}/$arch/sys-root \
	--with-system-libunwind \
	--with-system-zlib \
	--without-headers \
%if %{build_cloog}
	--with-isl=%{isl_install} --with-cloog=%{cloog_install} \
%else
	--without-isl --without-cloog \
%endif
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

    AR_FOR_TARGET=%{_bindir}/$arch-ar \
    AS_FOR_TARGET=%{_bindir}/$arch-as \
    DLLTOOL_FOR_TARGET=%{_bindir}/$arch-dlltool \
    LD_FOR_TARGET=%{_bindir}/$arch-ld \
    NM_FOR_TARGET=%{_bindir}/$arch-nm \
    OBJDUMP_FOR_TARGET=%{_bindir}/$arch-objdump \
    RANLIB_FOR_TARGET=%{_bindir}/$arch-ranlib \
    STRIP_FOR_TARGET=%{_bindir}/$arch-strip \
    WINDRES_FOR_TARGET=%{_bindir}/$arch-windres \
    WINDMC_FOR_TARGET=%{_bindir}/$arch-windmc \
    make -C $build_dir %{_smp_mflags} tooldir=%{_prefix} all-gcc

    case $arch in
	%{no_libgcc_targets})
	    ;;
	*)
	    make -C $build_dir %{_smp_mflags} tooldir=%{_prefix} all-target-libgcc
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

    # We want links for ppc and ppc64 also if we make powerpc or powerpc64
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

# We have to copy cloog somewhere graphite can dlopen it from
%if %{build_cloog}
for i in %{buildroot}%{_prefix}/lib/gcc/*/%{gcc_version}
do
    cp -a %{cloog_install}/lib/libcloog-isl.so.4 $i
done
%endif

# For cross-gcc we drop the documentation.
rm -rf %{buildroot}%{_infodir}

# Remove binaries we will not be including, so that they don't end up in
# gcc-debuginfo
rm -f %{buildroot}%{_libdir}/{libffi*,libiberty.a}
rm -f %{buildroot}%{_libexecdir}/gcc/*/%{gcc_version}/install-tools/{mkheaders,fixincl}
rm -f %{buildroot}%{_prefix}/bin/*-gcc-%{version} || :
rm -f %{buildroot}%{_bindir}/*-ar || :
rm -f %{buildroot}%{_bindir}/*-nm || :
rm -f %{buildroot}%{_bindir}/*-ranlib || :
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
%if %{build_powerpc}%{build_powerpc64}
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
	openrisc)	target_cpu=openrisc;;
	parisc)		target_cpu=hppa;;
	score)		target_cpu=score;;
	tile)		target_cpu=tilegx;;
	v850)		target_cpu=v850e;;
	x86)		target_cpu=x86_64;;
	*)		target_cpu=$cpu;;
    esac

    (
	echo '%%defattr(-,root,root,-)'
	echo '%{_bindir}/'$arch'*-cpp'
	echo '%{_bindir}/'$arch'*-gcc'
	echo '%{_bindir}/'$arch'*-gcov'
	echo '%{_mandir}/man1/'$arch'*-cpp*'
	echo '%{_mandir}/man1/'$arch'*-gcc*'
	echo '%{_mandir}/man1/'$arch'*-gcov*'
	case $cpu in
	    ppc*|ppc64*)
		;;
	    *)
		echo '/usr/lib/gcc/'$target_cpu'-*/'
		echo '%{_libexecdir}/gcc/'$target_cpu'*/*/cc1'
		echo '%{_libexecdir}/gcc/'$target_cpu'*/*/collect2'
		echo '%{_libexecdir}/gcc/'$target_cpu'*/*/[abd-z]*'
		echo %{_libexecdir}/$arch/sys-root
	esac

    ) >files.$arch

    (
	echo '%%defattr(-,root,root,-)'
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

%define __ar_no_strip $RPM_BUILD_DIR/%{srcdir}/ar-no-strip
cat >%{__ar_no_strip} <<EOF
#!/bin/bash
f=\$2
if [ \${f##*/} = libgcc.a -o \${f##*/} = libgcov.a ]
then
	:
else
	%{__strip} \$*
fi
EOF
chmod +x %{__ar_no_strip}
%undefine __strip
%define __strip %{__ar_no_strip}
# inside a symlink - not for rpm404
#sed -i -e /sys-root/d files.ppc64-linux-gnu

###############################################################################
#
# Cleanup
#
###############################################################################
%files -n %{cross}-gcc-common -f %{cross}-gcc.lang
%doc %{srcdir}/COPYING*
%doc %{srcdir}/README
%{_mandir}/man1/%{cross}-*

%define do_files() \
%if %2 \
%files -n %{rpmprefix}gcc-%1 -f files.%1 \
%files -n %{rpmprefix}gcc-c++-%1 -f files-c++.%1 \
%endif

%do_files alpha-linux-gnu	%{build_alpha}
%do_files arm-linux-gnu		%{build_arm}
%do_files aarch64-linux-gnu	%{build_aarch64}
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
%do_files openrisc-linux-gnu	%{build_openrisc}
%do_files powerpc-linux-gnu	%{build_powerpc}
%do_files powerpc64-linux-gnu	%{build_powerpc64}
%do_files ppc-linux-gnu		%{build_powerpc}
%do_files ppc64-linux-gnu	%{build_powerpc64}
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
* Fri Apr 04 2014 Igor Vlasenko <viy@altlinux.ru> 4.8.2-alt1_2
- new version

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 4.8.1-alt1_5.2
- new version

* Thu Aug 15 2013 Alexey Shabalin <shaba@altlinux.ru> 4.7.1-alt2_0.1.20120606.1
- rebuild

* Wed Aug 14 2013 Igor Vlasenko <viy@altlinux.ru> 4.7.1-alt1_0.1.20120606.1
- fc import

