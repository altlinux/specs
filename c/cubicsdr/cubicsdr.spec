%define _unpackaged_files_terminate_build 1

Name: cubicsdr
Version: 0.2.8
Release: alt3

Summary: Cross-Platform Software-Defined Radio Application
License: GPL-2.0
Group: Engineering
Url: http://www.cubicsdr.com/
VCS: https://github.com/cjcliffe/CubicSDR

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(hamlib)
BuildRequires: pkgconfig(opengl)
BuildRequires: libwxBase3.2-devel
BuildRequires: pkgconfig(SoapySDR)
BuildRequires: pkgconfig(liquid-dsp)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)

%description
CubicSDR is a cross-platform Software-Defined Radio application which
allows you to navigate the radio spectrum and demodulate any signals you
might discover. It currently includes several common analog demodulation
schemes such as AM and FM and will support digital modes in the future.

CubicSDR uses SoapySDR to access SDR hardware and thereby supports all
hardware for which a SoapySDR module exists.

%prep
%setup
sed -i 's|^Categories=.*|Categories=Audio;HamRadio;AudioVideo;|' cmake/CubicSDR.desktop.in

%build
%cmake \
       -DCMAKE_BUILD_TYPE=None \
       -DCMAKE_INSTALL_PREFIX=/usr \
       -DUSE_HAMLIB=ON \
       -DENABLE_DIGITAL_LAB=ON \
       -DUSE_AUDIO_ALSA=ON \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -Wno-dev
%cmake_build

%install
%cmake_install

%files
%doc *.md
%_bindir/*
%_desktopdir/*
%dir %_datadir/cubicsdr
%_datadir/cubicsdr/*

%changelog
* Fri Jun 19 2026 Nikolay Strelkov <snk@altlinux.org> 0.2.8-alt3
- Use pkgconfig for liquid-dsp.

* Fri Jun 27 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.8-alt2
- Applied repocop fix for freedesktop-desktop

* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus
