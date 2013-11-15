%define oname QLiveBittorrent
Name: qlivebittorrent
Version: 0.0
Release: alt0.2.1

Summary: Bittorrent client with function reading files before they would be downloaded
Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: https://github.com/vtyulb/QLiveBittorrent
License: GPLv2+
Group: File tools

# https://github.com/vtyulb/QLiveBittorrent
Source: %name-%version.tar

Patch: %name-qt4.patch

# Automatically added by buildreq on Sun Jul 07 2013
# optimized out: boost-asio-devel boost-devel boost-devel-headers fontconfig libqt4-core libqt4-devel libqt4-gui libssl-devel libstdc++-devel libtinfo-devel libtorrent-rasterbar8 pkg-config
BuildRequires: boost-filesystem-devel boost-program_options-devel gcc-c++ glibc-devel-static libfuse-devel libncurses-devel libtorrent-rasterbar-devel phonon-devel

%description
Bittorrent client with function reading files before they would be downloaded.

Using:
$ %name -t file.torent -d /tmp/downloadsdir -m ~/mountdir
Then open ~/mountdir in a file manager or console and use any program to access to files.

See also http://habrahabr.ru/post/185770/

%prep
%setup
#patch -p1
%__subst "s|PORTABLE||g" src/QLiveBittorrent.pro

%build
%qmake_qt4 src/QLiveBittorrent.pro
%make_build

# build fuse module
gcc src/driver.c `pkg-config fuse --cflags --libs` -o qlivebittorrent-driver

%install
%makeinstall INSTALL_ROOT=%buildroot

install -m 755 -D %oname %buildroot%_bindir/%name
install -m 755 -D qlivebittorrent-driver %buildroot%_bindir/qlivebittorrent-driver

%files
%_bindir/%name
%_bindir/qlivebittorrent-driver

%changelog
* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0-alt0.2.1
- Rebuilt with new libtorrent-rasterbar8

* Sat Oct 19 2013 Vitaly Lipatov <lav@altlinux.ru> 0.0-alt0.2
- update the code to 4dbc6b1d31be4d14abdeae71ee76642e9ba116cc

* Sun Jul 07 2013 Vitaly Lipatov <lav@altlinux.ru> 0.0-alt0.1
- initial build for ALT Linux Sisyphus
