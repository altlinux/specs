Name: libheif
Version: 1.23.1
Release: alt1

Summary: HEIF file format decoder and encoder
License: LGPLv3
Group: System/Libraries

Url: https://github.com/strukturag/libheif
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: cmake ctest gcc-c++ libde265-devel libjpeg-devel libpng-devel libtiff-devel libwebp-devel libgdk-pixbuf-devel libaom-devel
BuildRequires: libkvazaar-devel libopenjpeg2.0-devel openjpeg-tools2.0 libavcodec-devel libopenh264-devel libsvt-av1-devel libx265-devel
BuildRequires: libaom-tools libx264-devel zlib-devel libwebp-devel libvvdec-devel libvvenc-devel libuvg266-devel
%ifnarch %e2k
BuildRequires: librav1e-devel libdav1d-devel
%endif

%description
HEIF is a new image file format employing HEVC (h.265) image coding for the
best compression ratios currently possible.

%package devel
Group: Development/C
Summary:  Development libraries for %name

%description devel
Development libraries for %name

%prep
%setup
%patch -p1
%ifarch %e2k
sed -i 's/-Werror/-Wno-error/g' CMakeLists.txt
%endif

%build
%cmake \
	-DWITH_UNCOMPRESSED_CODEC=ON \
	-DPLUGIN_DIRECTORY=%_libdir/libheif/plugins \
	-DWITH_OpenH264_DECODER=ON \
	-DWITH_X265_PLUGIN=ON \
	-DWITH_FFMPEG_DECODER=ON \
	-DWITH_FFMPEG_DECODER_PLUGIN=ON \
	-DWITH_AOM_DECODER_PLUGIN=ON \
	-DWITH_AOM_ENCODER_PLUGIN=ON \
	-DWITH_DAV1D=ON \
	-DWITH_DAV1D_PLUGIN=ON \
	-DWITH_RAV1E=ON \
	-DWITH_RAV1E_PLUGIN=ON \
	-DWITH_JPEG_DECODER=ON \
	-DWITH_JPEG_DECODER_PLUGIN=ON \
	-DWITH_JPEG_ENCODER=ON \
	-DWITH_JPEG_ENCODER_PLUGIN=ON \
	-DWITH_KVAZAAR=ON \
	-DWITH_KVAZAAR_PLUGIN=ON \
	-DWITH_LIBDE265_PLUGIN=ON \
	-DWITH_LIBSHARPYUV=ON \
	-DWITH_OpenJPEG_DECODER=ON \
	-DWITH_OpenJPEG_DECODER_PLUGIN=ON \
	-DWITH_OpenJPEG_ENCODER=ON \
	-DWITH_OpenJPEG_ENCODER_PLUGIN=ON \
	-DWITH_SvtEnc=ON \
	-DWITH_SvtEnc_PLUGIN=ON \
	-DWITH_LIBSHARPYUV=ON \
	-DWITH_VVDEC=ON \
	-DWITH_VVDEC_PLUGIN=ON \
	-DWITH_VVENC=ON \
	-DWITH_VVENC_PLUGIN=ON \
	-DWITH_UVG266=ON \
	-DWITH_UVG266_PLUGIN=ON

%cmake_build

%check
%ctest

%install
%cmake_install

%files
%_bindir/*
%_libdir/%name.so.*
%_libdir/%name
%_libdir/gdk-pixbuf-2.0/2.10.0/loaders/*.so*
%_datadir/thumbnailers/heif.thumbnailer
%_man1dir/*.1*

%files devel
%_includedir/%name
%_libdir/%name.so
%_libdir/cmake/%name
%_pkgconfigdir/%name.pc

%changelog
* Fri Jun 26 2026 Valery Inozemtsev <shrek@altlinux.ru> 1.23.1-alt1
- 1.23.1

* Tue Jun 02 2026 Valery Inozemtsev <shrek@altlinux.ru> 1.23.0-alt1
- 1.23.0

* Tue May 26 2026 Valery Inozemtsev <shrek@altlinux.ru> 1.22.2-alt1
- 1.22.2

* Fri May 22 2026 Valery Inozemtsev <shrek@altlinux.ru> 1.22.0-alt3
- enabled uvg266

* Thu May 21 2026 Valery Inozemtsev <shrek@altlinux.ru> 1.22.0-alt2
- enabled vvdec, vvenc
- upstream: fix "bad_pixels" type (closes: #59287)

* Wed May 20 2026 Valery Inozemtsev <shrek@altlinux.ru> 1.22.0-alt1
- 1.22.0

* Tue Apr 28 2026 Anton Farygin <rider@altlinux.org> 1.21.2-alt2
- fixed build with SVT-AV1 4.0.0

* Mon Jan 19 2026 Valery Inozemtsev <shrek@altlinux.ru> 1.21.2-alt1
- 1.21.2

* Wed Sep 03 2025 Valery Inozemtsev <shrek@altlinux.ru> 1.20.2-alt1
- 1.20.2

* Fri Jul 04 2025 Valery Inozemtsev <shrek@altlinux.ru> 1.20.1-alt1
- 1.20.1

* Wed Jun 18 2025 Anton Farygin <rider@altlinux.com> 1.19.8-alt4
- enable libx265

* Wed Jun 18 2025 Valery Inozemtsev <shrek@altlinux.ru> 1.19.8-alt3
- enable ctest

* Wed Jun 18 2025 Valery Inozemtsev <shrek@altlinux.ru> 1.19.8-alt2
- separate plugins

* Wed May 14 2025 Valery Inozemtsev <shrek@altlinux.ru> 1.19.8-alt1
- 1.19.8

* Mon Mar 03 2025 Valery Inozemtsev <shrek@altlinux.ru> 1.19.6-alt1
- 1.19.6

* Thu Feb 27 2025 Michael Shigorin <mike@altlinux.org> 1.19.5-alt2
- E2K: fix workaround
- minor spec cleanup

* Wed Nov 20 2024 Valery Inozemtsev <shrek@altlinux.ru> 1.19.5-alt1
- 1.19.5

* Mon Sep 09 2024 Valery Inozemtsev <shrek@altlinux.ru> 1.18.2-alt1
- 1.18.2

* Mon Dec 25 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.17.6-alt1
- 1.17.6

* Mon Nov 27 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.17.5-alt1
- 1.17.5

* Thu Nov 09 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.17.3-alt1
- 1.17.3

* Thu Oct 19 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.17.1-alt1
- 1.17.1

* Thu Aug 31 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.15.2-alt1.1
- Fixed build for Elbrus

* Mon Mar 06 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.15.1-alt1
- 1.15.1

* Thu Feb 09 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.14.2-alt1
- 1.14.2

* Fri Nov 18 2022 Valery Inozemtsev <shrek@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Tue Apr 27 2021 Anton Farygin <rider@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Thu Sep 24 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Mon Aug 31 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Mon Jun 08 2020 Valery Inozemtsev <shrek@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Wed Feb 12 2020 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Fri Dec 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Thu Nov 14 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2
- NMU: remove rpm-build-ubt from BR:

* Wed Mar 20 2019 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Fri Aug 31 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.3.2-alt1.S1
- 1.3.2

* Tue Jun 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1.S1
- rebuild with libva 2.1.0

* Wed Jun 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- initial release
