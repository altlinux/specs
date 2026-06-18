%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: sdrplusplus
Version: 1.2.1
Release: alt1.git20260520.36ea9a1

Summary: Cross-Platform SDR Software
License: GPL-3.0-only
Group: Engineering
Url: https://github.com/AlexandreRouma/SDRPlusPlus

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: pkgconfig(glfw3)
BuildRequires: pkgconfig(fftw3f)
BuildRequires: pkgconfig(volk)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(libairspy)
# BuildRequires: pkgconfig(libairspyhf) # TODO
BuildRequires: pkgconfig(rtaudio)
BuildRequires: pkgconfig(libhackrf)
BuildRequires: pkgconfig(libiio)
# BuildRequires: pkgconfig(libad9361) # TODO
BuildRequires: pkgconfig(librtlsdr)
BuildRequires: libstdc++-devel-static
BuildRequires: pkgconfig(nlohmann_json)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(spdlog)
BuildRequires: /usr/bin/magick
BuildRequires: pkgconfig(libbladeRF)
# BuildRequires: pkgconfig(libdlcr) # TODO
# BuildRequires: pkgconfig(libfobos) # TODO
# BuildRequires: pkgconfig(libhydrasdr) # TODO
# BuildRequires: pkgconfig(libperseus-sdr) # TODO
# BuildRequires: pkgconfig(librfnm) # TODO
# sdrplay_api.h # TODO
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(codec2)
BuildRequires: limesuite

%description
SDR++ is a cross-platform and open source SDR software with the aim of
being bloat free and simple to use.

Features:

* Multi VFO
* Wide hardware support (both through SoapySDR and dedicated modules)
* SIMD accelerated DSP
* Cross-platform (Windows, Linux, MacOS and BSD)
* Full waterfall update when possible. Makes browsing signals easier and more pleasant
* Modular design (easily write your own plugins)

%prep
%setup
%patch -p1
%if "%{?_lib}"=="lib64"
sed -i "s|lib/sdrpp/plugins|lib64/sdrpp/plugins| " sdrpp_module.cmake
sed -i "s|/lib/sdrpp|/lib64/sdrpp|" core/src/core.cpp
%endif

%build
%cmake \
       -DOPT_BUILD_AIRSPYHF_SOURCE=OFF \
       -DOPT_BUILD_PLUTOSDR_SOURCE=OFF \
       -DOPT_BUILD_BLADERF_SOURCE=ON \
       -DOPT_BUILD_LIMESDR_SOURCE=ON \
       -DOPT_BUILD_SDRPLAY_SOURCE=OFF \
       -DOPT_BUILD_NEW_PORTAUDIO_SINK=ON \
       -DOPT_BUILD_M17_DECODER=ON \
       -DOPT_BUILD_PERSEUS_SOURCE=OFF \
       -DOPT_BUILD_RFNM_SOURCE=OFF \
       -DOPT_BUILD_FOBOSSDR_SOURCE=OFF \
       -DOPT_BUILD_HYDRASDR_SOURCE=OFF \
       -DOPT_BUILD_DRAGONLABS_SOURCE=OFF \
%if "%{?_lib}"=="lib64"
       -DLIB_SUFFIX=64
%else
       -DLIB_SUFFIX=""
%endif
%cmake_build

%install
%cmake_install

install -D -p -m644 root/res/icons/sdrpp.png \
        %buildroot%_iconsdir/hicolor/512x512/apps/sdrpp.png

for size in 16 24 32 48 64 128 256; do
  mkdir -p %buildroot%_datadir/icons/hicolor/${size}x${size}/apps ;
  magick root/res/icons/sdrpp.png -filter Lanczos -resize ${size}x${size} %buildroot%_datadir/icons/hicolor/${size}x${size}/apps/sdrpp.png ;
done

rm -fv %buildroot%_libdir/libsdrpp_core.so

%files
%doc readme.md
%_bindir/sdrpp
%_libdir/libsdrpp_core.so.*
%dir %_libdir/sdrpp
%dir %_libdir/sdrpp/plugins
%dir %_libdir/sdrpp/plugins/*.so
%_desktopdir/sdrpp.desktop
%_iconsdir/hicolor/*/apps/sdrpp.png
%dir %_datadir/sdrpp
%_datadir/sdrpp/*

%changelog
* Thu Jun 18 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt1.git20260520.36ea9a1
- Initial build for Sisyphus
