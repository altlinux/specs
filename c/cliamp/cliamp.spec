%define _unpackaged_files_terminate_build 1
%define import_path github.com/bjarneo/cliamp

Name: cliamp
Version: 1.62.0
Release: alt1

License: MIT
Group: Sound
Summary: Retro terminal music player

URL: https://www.cliamp.stream/
VCS: https://github.com/bjarneo/cliamp

Source: %name-%version.tar
Source1: vendor.tar

Patch: cliamp-1.62.0-possibility_bash_autocompletion_commands.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(vorbisenc)
BuildRequires: pkgconfig(flac)
Requires: yt-dlp
Requires: ffmpeg

ExclusiveArch: %go_arches

%description
A retro terminal music player. Play local files, streams, podcasts,
YouTube, YouTube Music, SoundCloud, Bilibili, Spotify, NetEase
Cloud Music, Xiaoyuzhou, Navidrome, Plex, and Jellyfin with a
spectrum visualizer, parametric EQ, and playlist management.

%package desktop
Summary: Dektop files for %name
Group: Sound
License: MIT
Requires: %name >= %version

%description desktop
Dektop files for %name

%prep
%setup -a 1 -q
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="$LDFLAGS -X main.version=%version"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export GOROOT="%_libexecdir/golang"

%golang_install

install -pD -m644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -pD -m644 Cliamp.png %buildroot%_iconsdir/hicolor/512x512/apps/%name.png

mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d

%buildroot%_bindir/%name completion bash \
    > %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name completion zsh \
    > %buildroot%_datadir/zsh/site-functions/_%name
%buildroot%_bindir/%name completion fish \
    > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
export LDFLAGS="$LDFLAGS -X main.version=%version"
%gotest

%files
%doc docs LICENSE README.*
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%files desktop
%_desktopdir/%name.desktop
%_iconsdir/hicolor/512x512/apps/%name.png

%changelog
* Wed Jul 29 2026 Sergey Savelev <medovi@altlinux.org> 1.62.0-alt1
- Initial build for Sisyphus.
