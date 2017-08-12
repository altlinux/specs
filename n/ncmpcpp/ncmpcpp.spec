Name: ncmpcpp
Version: 0.8
Release: alt1

Summary: ncurses-based client for the Music Player Daemon (MPD)

Group: Sound
License: GPLv2+
URL: http://ncmpcpp.rybczak.net/

Source: %name-%version.tar
# git://git.altlinux.org/gears/n/ncmpcpp.git
Patch1: %name-%version-%release.patch

# Automatically added by buildreq on Fri Jul 28 2017
# optimized out: boost-devel boost-devel-headers glibc-kernheaders-x86 libncurses-devel libstdc++-devel libtinfo-devel perl pkg-config python-base python3 python3-base
BuildRequires: boost-filesystem-devel boost-locale-devel boost-program_options-devel gcc-c++ glibc-devel-static glibc-kernheaders-generic libcurl-devel libfftw3-devel libmpdclient-devel libncursesw-devel libquadmath-devel libreadline-devel libtag-devel python3-dev

%description
ncmpcpp is almost an exact clone of ncmpc which is a text-mode client
for MPD, the Music Player Daemon. It provides a keyboard oriented and
consistent interface to MPD and contains some new features ncmpc
doesn't have. It's been also rewritten from scratch in C++.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure \
    --enable-clock \
    --enable-outputs \
    --enable-visualizer \
    --with-fftw \
    --with-taglib \
    #
%make_build

%install
%makeinstall_std

%files
%doc doc/config doc/bindings AUTHORS NEWS COPYING
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Fri Jul 28 2017 Arseny Maslennikov <arseny@altlinux.org> 0.8-alt1
- Initial build for ALT Sisyphus

