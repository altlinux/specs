Name: ripes
Version: 2.2.6
Release: alt1

Summary: A graphical 5-stage RISC-V pipeline simulator
License: MIT
Group: Emulators

Url: https://github.com/mortbopet/Ripes
Source: ripes-2.2.6.tar
Patch1: VSRTL.patch

BuildRequires: qt5-base-devel qt5-tools-devel qt5-charts-devel qt5-svg-devel cmake

%description
Ripes is a graphical 5-stage processor pipeline simulator and assembly
code editor built for the RISC-V instruction set architecture, suitable
for teaching how assembly level code is executed on a classic pipelined
architecture. Ripes is especially suitable for illustrating how concepts
such as forwarding and stalling works, giving a visual representation of
both cases.

%package VSRTL
Summary: Visual Simulation of Register Transfer Logic (Ripes version)
License: MIT
Group: Sciences/Computer science

%description VSRTL
VSRTL is a framework for describing, visualizing and simulating digital
circuits. A VSRTL-described circuit may be built and simulated as
a standalone application or embedded within a Qt-based C++ application.
As an example, VSRTL is used as the simulation and visualization
framework for Ripes, a graphical processor simulator and assembly editor
for the RISC-V ISA.

%prep
%setup
%patch1 -p1

sed -i 's@N/A@%version-%release@' src/version/version.cmake

%build
%cmake
%cmake_build

%install
# XXX no make install is provided
install -D %_cmake__builddir/Ripes %buildroot%_bindir/Ripes
install -D %_cmake__builddir/external/VSRTL/VSRTL %buildroot%_bindir/VSRTL-Ripes
cp -a appdir/usr %buildroot

%files
%doc *.md docs examples
%_bindir/Ripes*
%_desktopdir/*
%_iconsdir/*/*/apps/*
%_datadir/metainfo/*.xml

%files VSRTL
%doc external/VSRTL/*.md external/VSRTL/docs
%_bindir/VSRTL*

%changelog
* Thu May 09 2024 Fr. Br. George <george@altlinux.org> 2.2.6-alt1
- Autobuild version bump to 2.2.6
- Separate embedded VSRTL binary

* Fri Mar 08 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.1.0-alt2
- NMU: trimmed build dependencies according to CMakeLists.txt (only
  QtCore, QtWidgets, QtCharts, and QtSvg are required).
  Fixes FTBFS on LoongArch.

* Tue Aug 03 2021 Michael Shigorin <mike@altlinux.org> 2.1.0-alt1.1.1
- E2K: avoid qt5-{webengine,webview} as missing
- minor spec cleanup

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 2.1.0-alt1.1
- NMU: spec: adapted to new cmake macros.

* Fri Oct 09 2020 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Autobuild version bump to 2.1.0

* Thu Aug 01 2019 Fr. Br. George <george@altlinux.ru> 1.0.3-alt2
- Update to git 2019-05-21

* Thu Aug 01 2019 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Initial build for ALT

