%define oname libaccess_bittorrent_plugin

Name: vlc-plugin-bittorrent
Version: 2.16
Release: alt1

Summary: A bittorrent plugin for VLC
License: GPL-3.0-only
Group: Video

Url: https://github.com/johang/vlc-bittorrent
Vcs: https://github.com/johang/vlc-bittorrent

Source: %name-%version.tar

BuildRequires(Pre): rpm-macros-cmake rpm-build-cmake
BuildRequires: cmake clang libvlc-devel
BuildRequires: libtorrent-rasterbar-devel libstdc++-devel

%description
With vlc-bittorrent, you can open a .torrent file or magnet
link with VLC and stream any media that it contains.

%prep
%setup

%build
export CXX=clang++
%cmake
%cmake_build

%install
install -D %_arch-alt-linux/src/%oname.so \
	%buildroot/%_libdir/vlc/plugins/bittorrent/%oname.so

%files
%_libdir/vlc/plugins/bittorrent/%oname.so
%doc *.md LICENSE

%changelog
* Thu Apr 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.16-alt1
- Initial build for ALT Linux.

