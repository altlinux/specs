Name: gede
Version: 2.19.3
Release: alt1
Url: https://gede.dexar.se
Summary: Graphical frontend to GDB written in C++ and using the Qt5 toolkit
License: BSD
Source: %name-%version.tar.xz
Group: Development/Debuggers
Patch: gede-debuginfo.patch

# Automatically added by buildreq on Wed Jan 10 2024
# optimized out: bash5 gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libglvnd-devel libgpg-error libqt5-core libqt5-gui libqt5-serialport libqt5-widgets libstdc++-devel python3 python3-base python3-dev python3-module-setuptools qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel sh5 xz
BuildRequires: ctags qt5-3d-devel qt5-charts-devel qt5-connectivity-devel qt5-datavis3d-devel qt5-enginio-devel qt5-feedback-devel qt5-gamepad-devel qt5-multimedia-devel qt5-networkauth-devel qt5-phonon-devel qt5-quickcontrols2-devel qt5-remoteobjects-devel qt5-script-devel qt5-scxml-devel qt5-sensors-devel qt5-serialbus-devel qt5-serialport-devel qt5-speech-devel qt5-svg-devel qt5-tools-devel qt5-virtualkeyboard-devel qt5-wayland-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel qt5-xmlpatterns-devel

%ifnarch ppc64le
BuildRequires: qt5-webengine-devel qt5-webview-devel
%endif

%description
Gede is a graphical frontend (GUI) to GDB written in C++ and using the
Qt5 toolkit. Screenshot Gede can be compiled and run on (all?) Linux
distributions, FreeBSD and macOS. Gede supports debugging programs
written in Ada, FreeBasic, C++, C, Rust, Fortran and Go.

%prep
%setup
%patch -p1
echo "
[Desktop Entry]
Name=Gede
GenericName=Debugger
Comment=GUI frontend to gdb
Exec=gede
Icon=development_debugger_section
Terminal=false
Type=Application
Categories=Development;
" > %name.desktop

%build
./build.py --build-all --parallel-builds=%__nprocs --verbose

%install
./build.py install --prefix=%buildroot%prefix
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc README testapp testapps
%_bindir/*
%_desktopdir/*

%check
tests/ini/test_ini

%changelog
* Wed Jan 10 2024 Fr. Br. George <george@altlinux.org> 2.19.3-alt1
- Autobuild version bump to 2.19.3

* Wed Jan 10 2024 Fr. Br. George <george@altlinux.org> 2.19.2-alt1
- Initial build for ALT
