Name:    cava
Version: 0.10.2
Release: alt1

Summary: Cross-platform Audio Visualizer
License: MIT
Group:   Sound
Url:     https://github.com/karlstav/cava

Source: %name-%version.tar

Requires: kbd-data

BuildRequires:  libalsa-devel
BuildRequires:  libfftw3-devel
BuildRequires:  libiniparser-devel
BuildRequires:  libpulseaudio-devel
BuildRequires:  libtool
BuildRequires:  libncursesw-devel
BuildRequires:  libportaudio2-devel
BuildRequires:  pipewire-jack-libs-devel pipewire-libs-devel

%description
C.A.V.A. is a bar spectrum audio visualizer for the Linux terminal using ALSA, pulseaudio or fifo buffer for input.

%prep
%setup
echo %version > version

%build
%autoreconf
%configure FONT_DIR="/lib/kbd/consolefonts"
%make_build

%install
%makeinstall_std

%files
%doc *.md
%_bindir/%name
/lib/kbd/consolefonts/%name.psf

%changelog
* Tue Aug 06 2024 Roman Alifanov <ximper@altlinux.org> 0.10.2-alt1
- new version 0.10.2 (with rpmrb script)

* Wed Feb 28 2024 Roman Alifanov <ximper@altlinux.org> 0.10.1-alt1
- new version 0.10.1 (with rpmrb script)

* Mon Sep 11 2023 Roman Alifanov <ximper@altlinux.org> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Fri May 12 2023 Roman Alifanov <ximper@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus
