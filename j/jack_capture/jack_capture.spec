# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: jack_capture
Version: 0.9.73
Release: alt3.20230104
Summary: Record sound files with JACK
Group: Sound
# As explained in the COPYING file,
# jack_capture.c and atomicity/* are GPLv2+,
# jack_capture_gui2.cpp is BSD,
# atomic/* are LGPLv2+.
# The icon is borrowed from oxygen icon theme, which is LGPLv3+
License: GPLv2+ and BSD and LGPLv3+
Url: http://www.musix.org.ar/wiki/index.php/Jack_capture

Source: http://archive.notam02.no/arkiv/src/%name-%version.tar.gz
# Extra sources sent upstream via email on 2009-05-08
# since there is no upstream bugtracker.
Source1: %name.desktop
Source2: %name.png

Patch: %name-%version-get_ldflags_from_jack_pc.patch

BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(jack)
BuildRequires: libsndfile-devel
#BuildRequires: meterbridge
BuildRequires: libncurses++-devel

#Requires:	meterbridge
Requires: vorbis-tools

%description
Jack_capture is a program for recording sound files with JACK. It's default
operation is to capture whatever sound is going out to your speakers into a
file, but it can do a number of other operations as well.

%prep
%setup
%autopatch -p1

# No need to look for the c++ compiler
sed -i '/CPP/d' Makefile

%build
%make_build OPTIMIZE="%optflags"

%install
%makeinstall_std PREFIX=%prefix

# Desktop file
mkdir -p %buildroot/%_desktopdir
desktop-file-install --dir=%buildroot%_desktopdir %SOURCE1

# Icon
mkdir -p %buildroot/%_iconsdir/hicolor/48x48/apps
install -pm 644 %SOURCE2 %buildroot/%_iconsdir/hicolor/48x48/apps/

%files
%doc COPYING README
%_bindir/*
%_iconsdir/hicolor/48x48/apps/%name.png
%_desktopdir/%name.desktop

%changelog
* Fri Sep 01 2023 Anton Midyukov <antohami@altlinux.org> 0.9.73-alt3.20230104
- fix build with pipewire-jack-libs-devel

* Tue Aug 22 2023 Anton Midyukov <antohami@altlinux.org> 0.9.73-alt2.20230104
- new snapshot
- cleanup spec

* Mon Feb 04 2019 Anton Midyukov <antohami@altlinux.org> 0.9.73-alt1
- new version 0.9.73

* Mon May 29 2017 Anton Midyukov <antohami@altlinux.org> 0.9.69-alt1
- Initial build for ALT Linux Sisyphus.
