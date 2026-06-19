%define _unpackaged_files_terminate_build 1

Name: inspectrum
Version: 0.4.0
Release: alt3

Summary: Tool for visualising captured radio signals
License: GPL-3.0
Group: Engineering
Url: https://github.com/miek/inspectrum

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(fftw3)
BuildRequires: pkgconfig(liquid-dsp)

%description
inspectrum is a tool for analysing captured signals, primarily from
software-defined radio receivers.

inspectrum supports the following file types:
*.sigmf-meta, *.sigmf-data - Signal Metadata Format (SigMF) recordings
*.cf32, *.cfile - Complex 32-bit floating point (GNURadio, osmocom_fft)
*.cf64 - Complex 64-bit floating point samples
*.cs16 - Complex 16-bit signed integer (BladeRF)
*.cs8 - Complex 8-bit signed integer (HackRF)
*.cu8 - Complex 8-bit unsigned integer (RTL-SDR)
*.f32 - Real 32-bit floating point samples
*.f64 - Real 64-bit floating point samples (MATLAB)
*.s16 - Real 16-bit signed integer samples
*.s8 - Real 8-bit signed integer samples
*.u8 - Real 8-bit unsigned integer samples

Features:
* Large (100GB+) file support
* Spectrogram with zoom/pan
* Plots of amplitude, frequency, phase and IQ samples
* Cursors for measuring period, symbol rate and extracting symbols
* Export of selected time period, filtered samples and demodulated data

%prep
%setup
%ifarch %ix86
sed -i "s/1UL/(unsigned int) 1/" src/traceplot.cpp
%endif

%build
%cmake \
       -Wno-dev
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_desktopdir}

cat <<EOF > %{buildroot}%{_desktopdir}/inspectrum.desktop
[Desktop Entry]
Categories=Network;HamRadio;
Encoding=UTF-8
Name=inspectrum
GenericName=Offline Radio Signal Analyser
Type=Application
Exec=inspectrum
Icon=gnome-dev-wavelan
EOF

%files
%doc LICENSE README.md
%_bindir/*
%_desktopdir/inspectrum.desktop

%changelog
* Fri Jun 19 2026 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt3
- Use pkgconfig for liquid-dsp.

* Sat Jan 31 2026 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt2
- Enabled build on i586.

* Sun Dec 07 2025 Nikolay Strelkov <snk@altlinux.org> 0.4.0-alt1
- New version 0.4.0.

* Mon Jun 09 2025 Nikolay Strelkov <snk@altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus
