%define _unpackaged_files_terminate_build 1

%define githash 97189f7

Name: boomer
Version: 0.0.1
Release: alt1.%githash

Summary: Zoomer application for Linux
License: MIT
Group: Graphics
Url: https://github.com/tsoding/boomer
Vcs: https://github.com/tsoding/boomer

Source0: %name-%version.tar

BuildRequires: nim
BuildRequires: nim-x11
BuildRequires: nim-opengl
BuildRequires: libX11-devel
BuildRequires: libGL-devel
BuildRequires: libXrandr-devel

Requires: libGL
Requires: libX11
Requires: libXrandr

%description
Boomer is a zoomer application for Linux. It captures the screen
and allows you to zoom in/out and pan around the captured image
using keyboard shortcuts and mouse.

Features: zoom in/out, pan, flashlight effect, mirror, configurable
keyboard shortcuts.

%prep
%setup

%build
nim c \
    -d:release \
    --hints:off \
    --nimcache:nimcache \
    src/boomer.nim

%install
install -Dm755 src/boomer %buildroot%_bindir/boomer

%files
%doc README.md LICENSE
%_bindir/boomer

%changelog
* Wed Jul 22 2026 Timofei Fedotov <sovtouch@altlinux.org> 0.0.1-alt1.97189f7
- Initial build for ALT Sisyphus. (Closes: #52617)
