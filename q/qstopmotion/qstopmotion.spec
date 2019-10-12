Name: qstopmotion
Version: 2.3.2
Release: alt4

Summary: A program for stopmotion animation
License: GPLv2
Group: Graphics

Url: https://sourceforge.net/p/qstopmotion/
Source: %name-%version.tar
Patch: %name-g++8.patch
Packager: Denis Medvedev <nbr@altlinux.org>

BuildPreReq: cmake rpm-macros-cmake
# Automatically added by buildreq on Sat Oct 12 2019
# optimized out: cmake-modules gcc-c++ libEGL-devel libGL-devel libgphoto2-6 libgphoto2_port-12 libqt5-core libqt5-gui libqt5-widgets libqt5-xml libsasl2-3 pkg-config python-base
BuildRequires: gcc-c++ cmake libgphoto2-devel libv4l-devel qt5-base-devel qt5-imageformats

BuildRequires: libexif-devel libavdevice-devel gstreamer-devel

%description
qStopMotion is a program for stop motion pictures creation.
Stop motion pictures is a kind of animation where multiple images from camera
are arranged as a movie.

%prep
%setup
%patch -p2

%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.20
%add_optflags -std=c++11
%endif

%cmake_insource
%make_build # VERBOSE=1

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%_datadir/%name/*
%_desktopdir/*.desktop
# FIXME: does it look for help content there?
%_defaultdocdir/qstopmotion*
%_iconsdir/hicolor/*/apps/*
%doc AUTHORS COPYING

%changelog
* Sat Oct 12 2019 Michael Shigorin <mike@altlinux.org> 2.3.2-alt4
- E2K: explicit -std=c++11
- spec cleanup
- buildreq

* Wed Feb 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3.2-alt3
- no return statement in the non-void function fixed (according g++8)

* Mon Dec 24 2018 Denis Medvedev <nbr@altlinux.org> 2.3.2-alt2
- fix compilation and group

* Tue Jun 27 2017 Denis Medvedev <nbr@altlinux.org> 2.3.2-alt1
- Initial Sisyphus release
