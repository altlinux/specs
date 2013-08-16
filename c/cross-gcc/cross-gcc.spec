# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/bison /usr/bin/expect /usr/bin/m4 /usr/bin/makeinfo /usr/bin/runtest gcc-c++ libX11-devel libalsa-devel libjack-devel perl(English.pm) perl(Exporter.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(IPC/Open2.pm) python-devel
# END SourceDeps(oneline)
%define fedora 19

%define build_all 1
%define build_alpha %{build_all}
%define build_arm %{build_all}
%define build_avr32 %{build_all}
%define build_blackfin %{build_all}
%define build_c6x %{build_all}
%define build_cris %{build_all}
%define build_frv %{build_all}
%define build_h8300 %{build_all}
%define build_hppa64 %{build_all}
%define build_ia64 %{build_all}
%define build_m32r %{build_all}
%define build_m68k %{build_all}
%define build_mips64 %{build_all}
%define build_mn10300 %{build_all}
%define build_powerpc64 %{build_all}
%define build_s390x %{build_all}
%define build_sh %{build_all}
%define build_sh64 %{build_all}
%define build_sparc64 %{build_all}
%define build_tile %{build_all}
%define build_x86_64 %{build_all}
%define build_xtensa %{build_all}

# gcc considers obsolete
%define build_score 0

# gcc doesn't build
%define build_microblaze 0

# 32-bit packages we don't build as we can use the 64-bit package instead
%define build_hppa 0
%define build_i386 0
%define build_mips 0
%define build_powerpc 0
%define build_s390 0
%define build_sh4 0
%define build_sparc 0

# gcc doesn't support
%define build_openrisc 0

# not available in binutils-2.22
%define build_unicore32 0

%define DATE 20120606
%define SVNREV 188256
%define gcc_version 4.7.1

# Note, gcc_release must be integer, if you want to add suffixes to
# %{release}, append them after %{gcc_release} on Release: line.
%define gcc_release 0.1.%{DATE}

Summary: Cross C compiler
Name: cross-gcc
Version: %gcc_version
Release: alt2_%gcc_release.1
License: GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group: Development/Other
URL: http://gcc.gnu.org

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# svn export svn://gcc.gnu.org/svn/gcc/branches/redhat/gcc-4_6-branch@%{SVNREV} gcc-%{version}-%{DATE}
# tar cf - gcc-%{version}-%{DATE} | bzip2 -9 > gcc-%{version}-%{DATE}.tar.bz2
%define srcdir gcc-%{version}-RC-%{DATE}
Source0: %{srcdir}.tar.bz2

Patch0: gcc47-hack.patch
Patch1: gcc47-c++-builtin-redecl.patch
Patch2: gcc47-java-nomulti.patch
Patch3: gcc47-ppc32-retaddr.patch
Patch4: gcc47-pr33763.patch
Patch5: gcc47-rh330771.patch
Patch6: gcc47-i386-libgomp.patch
Patch7: gcc47-sparc-config-detection.patch
Patch8: gcc47-libgomp-omp_h-multilib.patch
Patch9: gcc47-libtool-no-rpath.patch
Patch11: gcc47-pr38757.patch
Patch13: gcc47-no-add-needed.patch
Patch14: gcc47-ppl-0.10.patch
Patch15: gcc47-libitm-fno-exceptions.patch
Patch100: cross-intl-filename.patch

BuildRequires: binutils >= 2.20.51.0.2-12
BuildRequires: zlib-devel gettext dejagnu bison flex texinfo sharutils
BuildRequires: cross-binutils-common >= 2.22

# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
BuildRequires: elfutils-devel >= 0.147
BuildRequires: libelf-devel >= 0.147
BuildRequires: libgmp-devel libgmp_cxx-devel libmpfr-devel >= 2.3.1 libmpc-devel >= 0.8.1
Source44: import.info

%description
Cross-build GNU C compiler collection.

%package -n cross-gcc-common
Summary: Cross-build GNU C compiler documentation and translation files
Group: Development/Other
BuildArch: noarch

%description -n cross-gcc-common
Documentation, manual pages and translation files for cross-build GNU C
compiler.

This is the common part of a set of cross-build GNU C compiler packages for
building kernels for other architectures.  No support for cross-building
user space programs is currently supplied as that would massively multiply the
number of packages.

%define do_package() \
%if %2 \
%package -n gcc-%1 \
Summary: Cross-build binary utilities for %1 \
Group: Development/Tools \
Requires: cross-gcc-common == %version-%release \
BuildRequires: binutils-%1 >= 2.22 \
Requires: binutils-%1 >= 2.22 \
%description -n gcc-%1 \
Cross-build GNU C compiler. \
\
Only building kernels is currently supported.  Support for cross-building \
user space programs is not currently provided as that would massively multiply \
the number of packages. \
%endif

%do_package alpha-linux-gnu	%{build_alpha}
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
%do_package microblaze-linux-gnu %{build_microblaze}
%do_package mips-linux-gnu	%{build_mips}
%do_package mips64-linux-gnu	%{build_mips64}
%do_package mn10300-linux-gnu	%{build_mn10300}
%do_package openrisc-linux-gnu	%{build_openrisc}
%do_package powerpc-linux-gnu	%{build_powerpc}
%do_package powerpc64-linux-gnu	%{build_powerpc64}
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
%patch1 -p0 -b .c++-builtin-redecl~
%patch2 -p0 -b .java-nomulti~
%patch3 -p0 -b .ppc32-retaddr~
%patch4 -p0 -b .pr33763~
%patch5 -p0 -b .rh330771~
%patch6 -p0 -b .i386-libgomp~
%patch7 -p0 -b .sparc-config-detection~
%patch8 -p0 -b .libgomp-omp_h-multilib~
%patch9 -p0 -b .libtool-no-rpath~
%patch11 -p0 -b .pr38757~
%patch13 -p0 -b .no-add-needed~
%if 0%{?fedora} < 15 || 0%{?rhel} < 7
%patch14 -p0 -b .ppl-0.10~
%endif
%patch15 -p0 -b .libitm-fno-exceptions~
%patch100 -p0 -b .cross-intl~

sed -i -e 's/4\.7\.0/4.7.0/' gcc/BASE-VER
echo 'Red Hat %version-%gcc_release' > gcc/DEV-PHASE

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

    if [ $cond = 1 ]
    then
	echo $1 >&5
    fi
}

cd ..
(
    prep_target alpha-linux-gnu		%{build_alpha}
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

function config_target () {
    arch=$1
    cross=$arch-
    build_dir=$arch

    case $arch in
	arm-*)		target=arm-linux-gnueabi;;
	avr32-*)	target=avr-linux;;
	bfin-*)		target=bfin-uclinux;;
	c6x-*)		target=c6x-uclinux;;
	h8300-*)	target=h8300-elf;;
	mn10300-*)	target=am33_2.0-linux;;
	openrisc-*)	target=or32-linux;;
	parisc-*)	target=hppa-linux;;
	score-*)	target=score-elf;;
	sh64-*)		target=sh64-linux;;
	sh-*)		target=sh-linux ;;
	tile-*)		target=tilegx-linux;;
	v850-*)		target=v850e-linux;;
	x86-*)		target=x86_64-linux;;
	*)		target=$arch;;
    esac

    echo $arch: target is $target
    #export CFLAGS="$RPM_OPT_FLAGS"

    CONFIG_FLAGS=
    COPT=
    case $arch in
	powerpc-*|powerpc64-*)
	    COPT="--with-cpu-32=power4 --with-tune-32=power6 --with-cpu-64=power4 --with-tune-64=power6"
	    ;;
	s390-*)
	    COPT="--with-arch=z9-109 --with-tune=z10 --enable-decimal-float"
	    ;;
	sh4-*)
	    COPT="--with-arch_32=sh"
	    ;;
	sh-*)
	    CONFIG_FLAGS=--with-multilib-list=m1,m2,m2e,m4,m4-single,m4-single-only,m2a,m2a-single
	    ;;
	sh64-*)
	    CONFIG_FLAGS=--with-multilib-list=m5-32media,m5-32media-nofpu,m5-compact,m5-compact-nofpu,m5-64media,m5-64media-nofpu
	    ;;
	sparc-*)
	    COPT="--with-long-double-128 --disable-linux-futex"
	    ;;
	tile-*)
	    COPT="--with-arch_32=tilepro"
	    ;;
	x86-*)
	    COPT="--with-arch_32=i686"
	    ;;
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
	--disable-dependency-tracking \
	--disable-silent-rules \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir} \
	--sharedstatedir=%{_sharedstatedir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir} \
	--build=%{_target_platform} \
	--host=%{_target_platform} \
	--target=$target \
	--enable-targets=all \
	--program-prefix=$cross \
	--enable-languages=c --without-headers \
	--enable-sjlj-exceptions --with-system-libunwind \
	--disable-nls --disable-threads --disable-shared \
	--disable-libmudflap --disable-libssp --disable-libgomp \
	--disable-libquadmath --disable-gold \
	--disable-decimal-float \
	--enable-checking=$checking \
	--enable-gnu-unique-object \
	--enable-linker-build-id \
	--disable-plugin \
	--enable-nls \
	--with-system-zlib \
	--with-bugurl=http://bugzilla.redhat.com/bugzilla/ \
	--enable-obsolete \
	$CONFIG_FLAGS
%if 0
	--libdir=%{_libdir} # we want stuff in /usr/lib/gcc/ not /usr/lib64/gcc
	--with-sysroot=%{_prefix}/$target/sys-root
%endif
    cd ..
}

for target in `cat target.list`
do
    config_target $target
done

function build_target () {
    arch=$1
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
    make -C $target %{_smp_mflags} tooldir=%{_prefix} all-gcc
}

for target in `cat target.list`
do
    build_target $target
done

# for documentation purposes only
mkdir stuff
cd stuff

../%{srcdir}/configure \
    --disable-dependency-tracking \
    --disable-silent-rules \
    --prefix=%{_prefix} \
    --exec-prefix=%{_exec_prefix} \
    --bindir=%{_bindir} \
    --sbindir=%{_sbindir} \
    --sysconfdir=%{_sysconfdir} \
    --datadir=%{_datadir} \
    --includedir=%{_includedir} \
    --libdir=%{_libdir} \
    --libexecdir=%{_libexecdir} \
    --localstatedir=%{_localstatedir} \
    --sharedstatedir=%{_sharedstatedir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --build=%{_target_platform} \
    --host=%{_target_platform} \
    --program-prefix=cross- \
    --enable-languages=c --without-headers \
    --enable-sjlj-exceptions --with-system-libunwind \
    --disable-nls --disable-threads --disable-shared \
    --disable-libmudflap --disable-libssp --disable-libgomp \
    --disable-libquadmath --disable-gold \
    --disable-decimal-float \
    --enable-checking=$checking \
    --enable-gnu-unique-object \
    --enable-linker-build-id \
    --enable-plugin \
    --enable-nls \
    --with-system-zlib \
    --with-bugurl=http://bugzilla.redhat.com/bugzilla/

cd ..

###############################################################################
#
# Installation
#
###############################################################################
%install

function install_bin () {
    arch=$1
    make -C $arch DESTDIR=%{buildroot} install-gcc
}

for target in `cat target.list`
do
    install_bin $target
done

# For cross-gcc we drop the documentation.
rm -rf %{buildroot}%{_infodir}

# Remove binaries we will not be including, so that they don't end up in
# gcc-debuginfo
FULLPATH=%{buildroot}%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_version}

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
    mv $x $y/cross-gcc.mo
done

%find_lang cross-gcc

gzip %{buildroot}%{_mandir}/man1/*.1
rm %{buildroot}%{_mandir}/man7/*.7
rmdir %{buildroot}%{_mandir}/man7

# All the installed manual pages and translation files for each program are the
# same, so symlink them to the common package
cd %{buildroot}%{_mandir}/man1
for i in cross-cpp.1.gz cross-gcc.1.gz cross-gcov.1.gz
do
    j=${i#cross-}

    for k in *-$j
    do
	if [ $k != $i ]
	then
	    mv $k $i
	    ln -s $i $k
	fi
    done
done
cd -

function install_lang () {
    arch=$1
    cpu=${arch%%%%-*}

    (
#	echo '%%defattr(-,root,root,-)'
	echo '%{_bindir}/'$arch'-*'
	echo '%{_mandir}/man1/'$arch'-*'

	case $cpu in
	    avr32)		target_cpu=avr;;
	    bfin)		target_cpu=bfin;;
	    h8300)		target_cpu=h8300;;
	    mn10300)		target_cpu=am33_2.0;;
	    openrisc)		target_cpu=openrisc;;
	    parisc)		target_cpu=hppa;;
	    score)		target_cpu=score;;
	    tile)		target_cpu=tilegx;;
	    v850)		target_cpu=v850e;;
	    x86)		target_cpu=x86_64;;
	    *)			target_cpu=$cpu;;
	esac
#	echo '/usr/lib/gcc/'$target_cpu'-*/'
	echo '%{_libexecdir}/gcc/'$target_cpu'-*/'

    ) >files.$arch
}

for target in `cat target.list`
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

###############################################################################
#
# Cleanup
#
###############################################################################
%files -n cross-gcc-common -f cross-gcc.lang
%doc %{srcdir}/COPYING*
%doc %{srcdir}/README
%{_mandir}/man1/cross-*
%dir %_libexecdir/gcc

%define do_files() \
%if %2 \
%files -n gcc-%1 -f files.%1 \
%endif

%do_files alpha-linux-gnu	%{build_alpha}
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
%do_files microblaze-linux-gnu	%{build_microblaze}
%do_files mips-linux-gnu	%{build_mips}
%do_files mips64-linux-gnu	%{build_mips64}
%do_files mn10300-linux-gnu	%{build_mn10300}
%do_files openrisc-linux-gnu	%{build_openrisc}
%do_files powerpc-linux-gnu	%{build_powerpc}
%do_files powerpc64-linux-gnu	%{build_powerpc64}
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
* Thu Aug 15 2013 Alexey Shabalin <shaba@altlinux.ru> 4.7.1-alt2_0.1.20120606.1
- rebuild

* Wed Aug 14 2013 Igor Vlasenko <viy@altlinux.ru> 4.7.1-alt1_0.1.20120606.1
- fc import

