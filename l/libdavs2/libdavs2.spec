# OpenCL features
%def_without opencl

# LTO breaks handmade endian detection
%define optflags_lto %nil

# PLD compat
%define rpmcppflags %nil
%define rpmldflags %nil

Name: libdavs2
Version: 1.7
Release: alt1

Summary: Open-source decoder of AVS2-P2/IEEE1857.4 video coding standard

License: GPL v2+
Group: System/Libraries
Url: https://github.com/pkuvcl/davs2

# Source-url: https://github.com/pkuvcl/davs2/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Patch1: davs2-opt.patch

BuildRequires: gcc-c++ libstdc++-devel
%{?with_opencl:BuildRequires: OpenCL-devel}

%ifarch %ix86 x86_64
BuildRequires: nasm >= 2.13
%endif

%description
Open-source decoder of AVS2-P2/IEEE1857.4 video coding standard.

%package devel
Summary: Header files for davs2 library
Group: Development/C
Requires: %name = %EVR

%description devel
Header files for davs2 library.

%prep
%setup
%patch1 -p1

#undos source/common/vec/intrinsic_{deblock_avx2,idct_avx2,inter_pred,inter_pred_avx2,intra-pred_avx2,pixel_avx,sao_avx2}.cc

%build
cd build/linux
# not autoconf configure
CC="%__cc" \
CXX="%__cxx" \
CFLAGS="%optflags" \
LDFLAGS="%rpmldflags -Wl,-z,noexecstack" \
./configure \
	--prefix=%prefix \
	--bindir=%_bindir \
	--includedir=%_includedir \
	--libdir=%_libdir \
%ifnarch x86_64
	--disable-asm \
%endif
	%{!?with_opencl:--disable-opencl} \
	--enable-pic \
	--enable-shared \
	--disable-static
%make_build

%install
make -C build/linux install \
	DESTDIR=%buildroot

%files
%doc README.md
%_bindir/davs2
%_libdir/libdavs2.so.16

%files devel
%_libdir/libdavs2.so
%_includedir/davs2.h
%_includedir/davs2_config.h
%_pkgconfigdir/davs2.pc

%changelog
* Sun Jan 08 2023 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- new version (1.7) with rpmgs script

* Sun Jan 08 2023 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- initial build for ALT Sisyphus

* Wed Aug 07 2019 PLD Linux Team <feedback@pld-linux.org>
- For complete changelog see: http://git.pld-linux.org/?p=packages/davs2.git;a=log;h=master

* Wed Aug 07 2019 Jakub Bogusz <qboosh@pld-linux.org> e1c9815
- added opt patch (drop -m32/-m64, rely on compiler default), disable asm on x32; release 2

* Sun Jul 28 2019 Jakub Bogusz <qboosh@pld-linux.org> 4876ed5
- new

