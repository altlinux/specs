%global import_path github.com/supersonic-app/supersonic

%define _unpackaged_files_terminate_build 1

Name: supersonic
Version: 0.22.1
Release: alt1

Summary: A lightweight desktop client for Subsonic and Jellyfin music servers
License: GPL-3.0-or-later
Group: Sound
URL: https://github.com/supersonic-app/supersonic
VCS: https://github.com/supersonic-app/supersonic

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: alt_vendor_golang.tar

BuildRequires(pre): rpm-build-golang

BuildRequires: gcc
BuildRequires: pkg-config
BuildRequires: libmpv-devel
BuildRequires: libX11-devel
BuildRequires: libXcursor-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXi-devel
BuildRequires: libglvnd-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libxkbcommon-devel

%description
Supersonic is a lightweight cross-platform desktop music player for
self-hosted music servers. It works with any server implementing the
Subsonic (OpenSubsonic) API - Navidrome, Gonic, LMS, Airsonic-Advanced,
Ampache, Funkwhale, Nextcloud Music - as well as Jellyfin.

It features a fast native UI with light and dark themes, gapless audio
playback powered by MPV, ReplayGain support, a waveform seekbar,
a built-in 15-band graphic equalizer, MPRIS integration for media keys
and desktop control, lyrics, internet radio stations, scrobbling,
track and album downloads, and casting to UPnP/DLNA devices.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export TAGS=migrated_fynedo

%golang_prepare

%golang_build $BUILDDIR/src/$IMPORT_PATH

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

for size in 128 256 512; do
	install -Dm644 res/appicon-$size.png \
		%buildroot%_iconsdir/hicolor/${size}x${size}/apps/%name.png
done

sed 's/supersonic-desktop/%name/g' res/supersonic-desktop.desktop > %name.desktop
install -Dm644 %name.desktop %buildroot%_desktopdir/%name.desktop

%check
%gotest ./...

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/128x128/apps/%name.png
%_iconsdir/hicolor/256x256/apps/%name.png
%_iconsdir/hicolor/512x512/apps/%name.png
%doc README.md

%changelog
* Thu Sep 03 2026 Yaroslav Bahtin <alpacost@altlinux.org> 0.22.1-alt1
- Initial build
