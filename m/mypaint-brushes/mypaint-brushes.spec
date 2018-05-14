%define ver_base 1.0

Name: mypaint-brushes
Version: 1.3.0
Release: alt1

Summary: MyPaint brush collection
Group: Graphics
License: GPLv2+
Url: https://github.com/Jehan/mypaint-brushes

# VCS: https://github.com/Jehan/mypaint-brushes.git
Source: %name-%version.tar.gz

BuildArch: noarch


%description
MyPaint is a simple drawing and painting program that works well with
Wacom-style graphics tablets. Its main features are a highly configurable
brush engine, speed, and a fullscreen mode which allows artists to fully
immerse themselves in their work.

This package provides MyPaint brush collection.

%package devel
Summary: MyPaint brush collection devel package
Group: Graphics
Requires: %name = %EVR

%description devel
Mypaint is a fast and easy/simple painter program. It comes with a large
brush collection including charcoal and ink to emulate real media, but the
highly configurable brush engine allows you to experiment with your own
brushes and with not-quite-natural painting.

This package contains pc-file for %name.

%prep
%setup

%build
./autogen.sh
%configure

%install
%makeinstall_std

%files
%_datadir/mypaint-data/%ver_base/brushes/
%doc README* NEWS Licenses*

%files devel
%_datadir/pkgconfig/%name-%ver_base.pc

%changelog
* Mon May 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- first build for Sisyphus

