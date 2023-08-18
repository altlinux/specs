Name: jpegqs
Version: 1.20230818
Release: alt1

Summary: JPEG Quant Smooth - JPEG artifacts removal
License: LGPL-2.1
Group: Graphics

Url: https://github.com/ilyakurdyukov/jpeg-quantsmooth
Source: jpeg-quantsmooth-%version.tar

Source1: test_text.jpg

BuildRequires: libjpeg-devel, libgomp-devel

%description
This program tries to recover the lost precision of DCT coefficients
based on a quantization table from a JPEG image. The result is saved
as a JPEG image with quantization set to 1 (like a JPEG saved at 100%%
quality).

%prep
%setup

%build
%make_build \
%ifarch %ix86 x86_64
	SIMD=select \
%endif
%ifarch %e2k
	CFLAGS="-Wall -Wno-reduced-alignment -O%_optlevel -g" SIMDFLG=-mno-avx \
%else
	CFLAGS="-Wall -O3 -g" \
%endif
%ifarch ppc64le
	SIMDFLG= \
%endif
	LDFLAGS= app

%install
install -pDm755 jpegqs %buildroot%_bindir/jpegqs
install -pDm644 jpegqs.1 %buildroot%_man1dir/jpegqs.1

%check
./jpegqs -v1 -i0 -q6 %_sourcedir/test_text.jpg test_text_new.jpg

%files
%_bindir/jpegqs
%_man1dir/jpegqs.1*

%changelog
* Fri Aug 18 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.20230818-alt1
- "DCT coefficient out of range" fix

* Thu Apr 08 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.20210408-alt1
- first release in ALT Linux

