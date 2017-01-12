# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/expect /usr/bin/m4 gcc-c++ libX11-devel libalsa-devel libjack-devel perl(English.pm) perl(Exporter.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(IPC/Open2.pm) swig texinfo
# END SourceDeps(oneline)
# due to explicit symlinks
%set_compress_method off
# ldv@ recommends: no debuginfo whatsoever.
%global __find_debuginfo_files %nil
%add_debuginfo_skiplist /usr
%remove_optflags -g

%define fedora 25
# %%release is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define release 2
%global cross cross
%global rpmprefix %{nil}

%global build_all		1
%global build_aarch64		%{build_all}
%global build_alpha		%{build_all}
%global build_arm		%{build_all}
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
%global no_libgcc_targets	nios2*|tile-*

###############################################################################
#
# The gcc versioning information.  In a sed command below, the specfile winds
# pre-release version numbers in BASE-VER back to the last actually-released
# number.
%global DATE 20160621
%global SVNREV 237634
%global gcc_version 6.1.1

# Note, cross_gcc_release must be integer, if you want to add suffixes
# to %{release}, append them after %{cross_gcc_release} on Release:
# line.  gcc_release is the Fedora gcc release that the patches were
# taken from.
%global gcc_release 3
%global cross_gcc_release 2
%global cross_binutils_version 2.26.1-1
%global isl_version 0.14

%global _performance_build 1
# Hardening slows the compiler way too much.
%undefine _hardened_build

Summary: Cross C compiler
Name: %{cross}-gcc
Version: %{gcc_version}
Release: alt1_2
# libgcc, libgfortran, libmudflap, libgomp, libstdc++ and crtstuff have
# GCC Runtime Exception.
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group: Development/Other
URL: http://gcc.gnu.org
BuildRequires: libisl-devel >= %{isl_version}

# sh5 is deprecrated: https://gcc.gnu.org/ml/gcc/2015-08/msg00101.html
Obsoletes: gcc-sh64-linux-gnu, gcc-c++-sh64-linux-gnu

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export svn://gcc.gnu.org/svn/gcc/branches/redhat/gcc-4_7-branch@%{SVNREV} gcc-%{version}-%{DATE}
# tar cf - gcc-%{version}-%{DATE} | bzip2 -9 > gcc-%{version}-%{DATE}.tar.bz2
%global srcdir gcc-%{version}-%{DATE}
Source0: %{srcdir}.tar.bz2

Patch0: gcc6-hack.patch
Patch1: gcc6-java-nomulti.patch
Patch2: gcc6-ppc32-retaddr.patch
Patch3: gcc6-rh330771.patch
Patch4: gcc6-i386-libgomp.patch
Patch5: gcc6-sparc-config-detection.patch
Patch6: gcc6-libgomp-omp_h-multilib.patch
Patch7: gcc6-libtool-no-rpath.patch
Patch8: gcc6-isl-dl.patch
Patch9: gcc6-libstdc++-docs.patch
Patch10: gcc6-no-add-needed.patch
Patch11: gcc6-libgo-p224.patch
Patch12: gcc6-aarch64-async-unw-tables.patch
Patch13: gcc6-libsanitize-aarch64-va42.patch
Patch14: gcc6-pr71559.patch

Patch900: cross-intl-filename.patch
Patch901: cross-gcc-with-libgcc.patch
Patch902: cross-gcc-format-config.patch
Patch903: cross-gcc-microblaze.patch

BuildRequires: binutils >= 2.24
BuildRequires: zlib-devel gettext gettext-tools, dejagnu, bison, flex, makeinfo, sharutils
BuildRequires: %{cross}-binutils-common >= %{cross_binutils_version}

# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90
BuildRequires: elfutils-devel >= 0.147
BuildRequires: elfutils-devel libelf-devel
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
# Debuginfo
#
###############################################################################
%if 0%{?_enable_debug_packages}
%global debug_package %{nil}
%global __debug_package 1
%global __debug_install_post \
   %{_rpmconfigdir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/gcc-%{version}-%{DATE}"\
    %{_builddir}/gcc-%{version}-%{DATE}/split-debuginfo.sh\
%{nil}

%package debuginfo
Summary: Debug information for package %{name}
Group: Development/Debug
AutoReqProv: 0
Requires: gcc-base-debuginfo = %{version}

%description debuginfo
This package provides debug information for package %{name}.
Debug information is useful when developing applications that use this
package or when debugging this package.

%files debuginfo -f debugfiles.list

%endif

###############################################################################
#
# Conditional arch package definition
#
###############################################################################
%global do_package() \
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

%global do_symlink() \
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
%do_package nios2-linux-gnu	%{build_nios2}
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

%setup -q -n %{srcdir} -c
cd %{srcdir}
%patch0 -p0 -b .hack~
%patch1 -p0 -b .java-nomulti~
%patch2 -p0 -b .ppc32-retaddr~
%patch3 -p0 -b .rh330771~
%patch4 -p0 -b .i386-libgomp~
%patch5 -p0 -b .sparc-config-detection~
%patch6 -p0 -b .libgomp-omp_h-multilib~
%patch7 -p0 -b .libtool-no-rpath~
# % if %{build_isl}
%patch8 -p0 -b .isl-dl~
# % endif
# % if %{build_libstdcxx_docs}
# % patch9 -p0 -b .libstdc++-docs~
# % endif
%patch10 -p0 -b .no-add-needed~
%patch11 -p0 -b .libgo-p224~
rm -f libgo/go/crypto/elliptic/p224{,_test}.go
%patch12 -p0 -b .aarch64-async-unw-tables~
%patch13 -p0 -b .libsanitize-aarch64-va42~
%patch14 -p0 -b .pr71559~

%patch900 -p0 -b .cross-intl~
%patch901 -p1 -b .with-libgcc~
%patch902 -p0 -b .format-config~
%patch903 -p0 -b .microblaze~

echo 'Red Hat Cross %{version}-%{cross_gcc_release}' > gcc/DEV-PHASE

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

%if 0%{?_enable_debug_packages}
# We don't need the dwz-wrapper script here
cat > split-debuginfo.sh <<\EOF
#!/bin/sh
BUILDDIR="%{_builddir}/gcc-%{version}-%{DATE}"
if [ -f "${BUILDDIR}"/debugfiles.list \
     -a -f "${BUILDDIR}"/debuglinks.list ]; then
  > "${BUILDDIR}"/debugsources-base.list
  > "${BUILDDIR}"/debugfiles-base.list
  cd "${RPM_BUILD_ROOT}"
  for f in `find usr/lib/debug -name \*.debug \
	    | egrep 'lib[0-9]*/lib(gcc[_.]|gomp|stdc|quadmath|itm)'`; do
    echo "/$f" >> "${BUILDDIR}"/debugfiles-base.list
    if [ -f "$f" -a ! -L "$f" ]; then
      cp -a "$f" "${BUILDDIR}"/test.debug
      /usr/lib/rpm/debugedit -b "${RPM_BUILD_DIR}" -d /usr/src/debug \
			     -l "${BUILDDIR}"/debugsources-base.list \
			     "${BUILDDIR}"/test.debug
      rm -f "${BUILDDIR}"/test.debug
    fi
  done
  for f in `find usr/lib/debug/.build-id -type l`; do
    ls -l "$f" | egrep -q -- '->.*lib[0-9]*/lib(gcc[_.]|gomp|stdc|quadmath|itm)' \
      && echo "/$f" >> "${BUILDDIR}"/debugfiles-base.list
  done
  cp -a "${BUILDDIR}"/debugfiles-base.list "${BUILDDIR}"/debugfiles-remove.list
  grep -v -f "${BUILDDIR}"/debugfiles-remove.list \
    "${BUILDDIR}"/debugfiles.list > "${BUILDDIR}"/debugfiles.list.new
  mv -f "${BUILDDIR}"/debugfiles.list.new "${BUILDDIR}"/debugfiles.list
  for f in `LC_ALL=C sort -z -u "${BUILDDIR}"/debugsources-base.list \
	    | grep -E -v -z '(<internal>|<built-in>)$' \
	    | xargs --no-run-if-empty -n 1 -0 echo \
	    | sed 's,^,usr/src/debug/,'`; do
    if [ -f "$f" ]; then
      echo "/$f" >> "${BUILDDIR}"/debugfiles-base.list
      echo "%%exclude /$f" >> "${BUILDDIR}"/debugfiles.list
    fi
  done
  mv -f "${BUILDDIR}"/debugfiles-base.list{,.old}
  echo "%%dir /usr/lib/debug" > "${BUILDDIR}"/debugfiles-base.list
  awk 'BEGIN{FS="/"}(NF>4&&$NF){d="%%dir /"$2"/"$3"/"$4;for(i=5;i<NF;i++){d=d"/"$i;if(!v[d]){v[d]=1;print d}}}' \
    "${BUILDDIR}"/debugfiles-base.list.old >> "${BUILDDIR}"/debugfiles-base.list
  cat "${BUILDDIR}"/debugfiles-base.list.old >> "${BUILDDIR}"/debugfiles-base.list
  rm -f "${BUILDDIR}"/debugfiles-base.list.old
fi
EOF
chmod 755 split-debuginfo.sh
%endif

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
    prep_target nios2-linux-gnu		%{build_nios2}
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
	arm-*)		target=arm-linux-gnueabi;;
	aarch64-*)	target=aarch64-linux-gnu;;
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
	arm-*)
	    CONFIG_FLAGS="--with-tune=cortex-a8 --with-arch=armv7-a \
		--with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux"
	    ;;
	mips64-*)
	    CONFIG_FLAGS="--with-arch=mips64r2 --with-abi=64 --with-arch_32=mips32r2 --with-fp-32=xx"
	    ;;
	powerpc-*|powerpc64-*|ppc-*|ppc64-*)
	    CONFIG_FLAGS="--with-cpu-32=power7 --with-tune-32=power8 --with-cpu-64=power7 --with-tune-64=power8 --enable-secureplt --enable-targets=all"
	    ;;
	s390*-*)
	    CONFIG_FLAGS="--with-arch=z9-109 --with-tune=z10 --enable-decimal-float"
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
	    CONFIG_FLAGS="--with-arch_32=i686 --with-tune=generic"
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
    		  | sed 's/ -Werror=format-security / -Wformat -Werror=format-security /'`" \
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
	--disable-shared \
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
%if 0%{fedora} >= 21 && 0%{fedora} <= 22
	--with-default-libstdcxx-abi=gcc4-compatible \
%endif
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

# For cross-gcc we drop the documentation.
rm -rf %{buildroot}%{_infodir}

# Remove binaries we will not be including, so that they don't end up in
# gcc-debuginfo
rm -f %{buildroot}%{_libdir}/{libffi*,libiberty.a}
rm -f %{buildroot}%{_libexecdir}/gcc/*/%{gcc_version}/install-tools/{mkheaders,fixincl}
rm -f %{buildroot}%{_prefix}/bin/*-gcc-%{version} || :
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
	    ppc*|ppc64*)
		;;
	    *)
		echo '/usr/lib/gcc/'$target_cpu'-*/'
		echo '%{_libexecdir}/gcc/'$target_cpu'*/*/cc1'
		echo '%{_libexecdir}/gcc/'$target_cpu'*/*/collect2'
		echo '%{_libexecdir}/gcc/'$target_cpu'*/*/[abd-z]*'
		echo '%%attr(0755,root,root)' %{_libexecdir}/$arch/sys-root
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
	%{__strip} \$*
fi
EOF
chmod +x %{__ar_no_strip}
%undefine __strip
%global __strip %{__ar_no_strip}
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

%global do_files() \
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
%do_files nios2-linux-gnu	%{build_nios2}
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


