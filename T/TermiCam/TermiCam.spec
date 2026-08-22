%global import_path github.com/Megge06/TermiCam

Name:    TermiCam
Version: 0.3.0
Release: alt1

Summary: A real-time ASCII camera for your terminal
License: GPL-3.0-only
Group:   Video
URL:     https://github.com/Megge06/TermiCam

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
Requires: ffmpeg
Requires: v4l-utils

%description
A real-time ASCII camera for your terminal.

TermiCam is a Go TUI application that reads camera frames through FFmpeg and
renders them as ASCII art in your terminal. It supports Linux, macOS, and
Windows camera capture through platform-specific FFmpeg backends.

TermiCam supports both real and virtual camera inputs, as well as lightweight
session recording and playback.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/termicam

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE README.md
%_bindir/termicam

%changelog
* Sat Aug 22 2026 Sergey Palcheh <minergenon@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
