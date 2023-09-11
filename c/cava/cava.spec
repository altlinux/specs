Name:    cava
Version: 0.9.1
Release: alt1

Summary: Cross-platform Audio Visualizer
License: MIT
Group:   Sound
Url:     https://github.com/karlstav/cava

Source: %name-%version.tar
Patch0: cava-0.8.3-dirs-fix-alt.patch

Requires: kbd-data

BuildRequires:  libalsa-devel
BuildRequires:  libfftw3-devel
BuildRequires:  libiniparser-devel
BuildRequires:  libpulseaudio-devel
BuildRequires:  libtool
BuildRequires:  libncursesw-devel
BuildRequires:  libportaudio2-devel

%description
C.A.V.A. is a bar spectrum audio visualizer for the Linux terminal using ALSA, pulseaudio or fifo buffer for input.

%prep
%setup
%patch0 -p1
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
* Mon Sep 11 2023 Roman Alifanov <ximper@altlinux.org> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Fri May 12 2023 Roman Alifanov <ximper@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus
