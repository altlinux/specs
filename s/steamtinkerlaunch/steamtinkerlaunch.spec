Name:    steamtinkerlaunch
Version: 12.12
Release: alt1

Summary: Steam Tinker Launch is a Linux wrapper tool for use with the Steam client
License: GPL-3.0
Group:   Games/Other
Url:     https://github.com/sonic2kk/steamtinkerlaunch
VCS:     https://github.com/sonic2kk/steamtinkerlaunch.git

Source: %name-%version.tar

BuildRequires: gcc-c++ cmake
Requires: gawk
Requires: bash
Requires: git
Requires: ripgrep
Requires: unzip
Requires: wget
Requires: which
Requires: xdotool
Requires: xprop
Requires: xrandr
Requires: xwininfo
Requires: yad >= 7.2
Requires: strace
Requires: libgamemode0
Requires: gamemode
Requires: libgamemodeauto0
Requires: mangohud
Requires: winetricks
Requires: vkBasalt
Requires: cabextract
Requires: innoextract
Requires: p7zip
Requires: jq
Requires: ImageMagick
Requires: rsync
Requires: openssl

# TODO: 32-bit dependencies
# Requires: i586-libgamemode0 i586-libgamemodeauto0 i586-libgamemodeauto0 i586-mangohud

ExclusiveArch: x86_64

%description
Steam Tinker Launch (short stl) is a Linux wrapper tool for use with the
Steam client which allows customizing and start tools and options for
games quickly on the fly.
By using a versatile configuration structure it is both easy to set
up and flexible.

%prep
%setup

%build

%install
install -Dm755 steamtinkerlaunch %buildroot/%_bindir/steamtinkerlaunch
mkdir -p %buildroot%_datadir/steamtinkerlaunch
cp -r collections eval guicfgs lang misc %buildroot%_datadir/steamtinkerlaunch

%files
%doc LICENSE README.md
%_bindir/%name
%_datadir/%name/

%changelog
* Sun Feb 23 2025 Sergey Palcheh <minergenon@altlinux.org> 12.12-alt1
- Initial build for Sisyphus
