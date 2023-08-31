%define _metainfodir %_datadir/metainfo
%set_verify_elf_method textrel=relaxed


Name: dosbox-x
Version: 2023.05.01
Release: alt1
Summary: DOS emulator for running DOS games and applications including Windows 3.x/9x
License: GPLv2+
Group: Emulators
Url: https://dosbox-x.com
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: https://github.com/joncampbell123/dosbox-x/archive/refs/tags/%name-v%version.tar.gz

BuildRequires: libalsa-devel
BuildRequires: desktop-file-utils
BuildRequires: libfluidsynth-devel
BuildRequires: libfreetype-devel
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: libpcap-devel
BuildRequires: libpng-devel
BuildRequires: libslirp-devel
BuildRequires: libtool
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libxkbfile-devel
BuildRequires: libXrandr-devel
BuildRequires: make
BuildRequires: libGL-devel
BuildRequires: libncurses-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_net-devel
BuildRequires: zlib-devel

Requires: fluid-soundfont-gm
Requires: hicolor-icon-theme

%description
DOSBox-X is an open-source DOS emulator for running DOS games and applications.
DOS-based Windows such as Windows 3.x and Windows 9x are officially supported.
Compared to DOSBox, DOSBox-X is much more flexible and provides more features.

DOSBox-X emulates a PC necessary for running many DOS games and applications
that simply cannot be run on modern PCs and operating systems, similar to
DOSBox. However, while the main focus of DOSBox is for running DOS games,
DOSBox-X goes much further than this. Started as a fork of the DOSBox project,
it retains compatibility with the wide base of DOS games and DOS gaming DOSBox
was designed for. But it is also a platform for running DOS applications,
including emulating the environments to run Windows 3.x, 9x and ME and software
written for those versions of Windows. By adding official support for
Windows 95, 98, and ME emulation and acceleration, we hope that those old
Windows games and applications could be enjoyed or used once more. Moreover,
DOSBox-X adds support for emulating the NEC PC-98 such that you can also play
PC-98 games with it.

DOSBox-X emulates a legacy IBM PC and DOS environment, and has many emulation
options and features.

%prep
%setup -n dosbox-x-dosbox-x-v%version

%build
./autogen.sh
%add_optflags -fPIC
%configure --enable-core-inline --enable-debug=heavy --enable-sdl2
%make_build

%install
%makeinstall_std
mkdir -p %buildroot{%_desktopdir,%_metainfodir}
cp contrib/linux/*.metainfo.xml %buildroot%_metainfodir/

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/com.dosbox_x.DOSBox-X.desktop
%_iconsdir/hicolor/scalable/apps/dosbox-x.svg
%_metainfodir/com.dosbox_x.DOSBox-X.metainfo.xml
%_man1dir/*
%_datadir/bash-completion/completions/dosbox-x
%doc CHANGELOG
%doc dosbox-x.reference.conf
%doc dosbox-x.reference.full.conf

%changelog
* Thu Aug 31 2023 Artyom Bystrov <arbars@altlinux.org> 2023.05.01-alt1
- Update to new version

* Mon Apr 24 2023 Artyom Bystrov <arbars@altlinux.org> 2023.03.31-alt1
- initial build for ALT Sisyphus

* Fri Mar 31 2023 Robert de Rooy <robert.de.rooy[AT]gmail.com> - 2023.03.31-1
- Bumped to new release
