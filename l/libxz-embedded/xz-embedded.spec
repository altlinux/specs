%define _unpackaged_files_terminate_build 1

Name: libxz-embedded
Version: 2024.12.30
Release: alt1

Summary: XZ Embedded is a relatively small, limited implementation of the .xz file format
License: 0BSD
Group: Development/C
URL: https://github.com/tukaani-project/xz-embedded
Vcs: https://github.com/tukaani-project/xz-embedded.git

Source: %name-%version.tar
Patch: alt-use-x64.patch

BuildRequires(pre): rpm-macros-make
BuildRequires: gcc

%description
XZ Embedded is a relatively small, limited implementation of the .xz file
format. Currently only decoding is implemented. XZ Embedded was written for use
in the Linux kernel, but the code can be easily used in other environments too,
including regular userspace applications.

%package devel
Summary: Development files for xz-embedded
Group: Development/C

%description devel
Headers for xz-embedded package.

%prep
%setup
%autopatch -p1

%build
gcc -std=gnu11 \
    -I ./linux/include/linux \
    -I ./userspace \
    -DXZ_DEC_X86 \
    -DXZ_DEC_ARM \
    -DXZ_DEC_ARMTHUMB \
    -DXZ_DEC_ARM64 \
    -DXZ_DEC_RISCV \
    -DXZ_DEC_POWERPC \
    -DXZ_DEC_IA64 \
    -DXZ_DEC_SPARC \
    -DXZ_USE_CRC64 \
    -DXZ_USE_SHA256 \
    -DXZ_DEC_ANY_CHECK \
    -DXZ_DEC_CONCATENATED \
    -ggdb3 \
    -O2 \
    -pedantic \
    -Wall \
    -Wextra \
    -Wdeclaration-after-statement \
    -c \
    linux/lib/xz/xz_crc32.c \
    linux/lib/xz/xz_crc64.c \
    linux/lib/xz/xz_sha256.c \
    linux/lib/xz/xz_dec_stream.c \
    linux/lib/xz/xz_dec_lzma2.c \
    linux/lib/xz/xz_dec_bcj.c \
    #

ar rcs libxz.a xz_crc32.o xz_crc64.o xz_sha256.o \
    xz_dec_stream.o xz_dec_lzma2.o xz_dec_bcj.o \
    #

%install
mkdir -pv %buildroot
mkdir -pv %buildroot%_libdir
mkdir -pv %buildroot%_includedir/xz-embedded

cp userspace/xz_config.h %buildroot%_includedir/xz-embedded/
cp linux/lib/xz/xz_stream.h %buildroot%_includedir/xz-embedded/
cp linux/lib/xz/xz_private.h %buildroot%_includedir/xz-embedded/
cp linux/lib/xz/xz_lzma2.h %buildroot%_includedir/xz-embedded/
cp linux/include/linux/xz.h %buildroot%_includedir/xz-embedded/
cp linux/include/linux/decompress/unxz.h %buildroot%_includedir/xz-embedded/
cp libxz.a %buildroot%_libdir/

%files devel
%doc COPYING README
%_includedir/xz-embedded
%_libdir/libxz.a

%changelog
* Tue Dec 02 2025 Ilya Muhamadeev <nicourced@altlinux.org> 2024.12.30-alt1
- Initial build.
