Name: gede
Version: 2.19.3
Release: alt2
Url: https://gede.dexar.se
Summary: Graphical frontend to GDB written in C++ and using the Qt5 toolkit
License: BSD
Source: %name-%version.tar.xz
Group: Development/Debuggers
Patch: gede-debuginfo.patch

BuildRequires: qt5-base-devel qt5-serialport-devel qt5-tools-devel
BuildRequires: ctags /usr/bin/python3

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
* Thu Jan 11 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.19.3-alt2
- NMU: trimmed build dependencies according to src/gd.pro (that is, only
  QtCore, QtGui, QtWidgets, and QtSerialPort are required).
  Fixes FTBFS on LoongArch.

* Wed Jan 10 2024 Fr. Br. George <george@altlinux.org> 2.19.3-alt1
- Autobuild version bump to 2.19.3

* Wed Jan 10 2024 Fr. Br. George <george@altlinux.org> 2.19.2-alt1
- Initial build for ALT
