%global import_path github.com/bluenviron/mediamtx
Name:    mediamtx
Version: 1.1.1
Release: alt1

Summary: Ready-to-use SRT / WebRTC / RTSP / RTMP / LL-HLS media server
License: MIT
Group:   Other
Url:     https://github.com/bluenviron/mediamtx

Packager: Leonid Znamenok <respublica@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
MediaMTX (formerly rtsp-simple-server) is a ready-to-use and zero-dependency
real-time media server and media proxy that allows users to publish, read and
proxy live video and audio streams. It has been conceived as a "media broker",
a message broker-like software that routes media streams.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE *.md
%_bindir/mediamtx

%changelog
* Fri Oct 06 2023 Leonid Znamenok <respublica@altlinux.org> 1.1.1-alt1
- New release 1.1.1

* Fri Aug 04 2023 Leonid Znamenok <respublica@altlinux.org> 0.23.8-alt1
- Initial build for Sisyphus
