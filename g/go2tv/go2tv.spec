%define _unpackaged_files_terminate_build 1
%define import_path github.com/alexballas/go2tv

Name: go2tv
Version: 1.16.1
Release: alt1

Summary: Cast media files to UPnP/DLNA Media Renderers and Smart TVs
License: MIT
Group: Networking/File transfer
Url: https://go2tv.app
Vcs: https://github.com/alexballas/go2tv

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: asciidoctor
BuildRequires: libX11-devel
BuildRequires: libXcursor-devel
BuildRequires: libXrandr-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libglvnd-devel
BuildRequires: libXxf86vm-devel
BuildRequires: ffmpeg

%description
Cast media files to UPnP/DLNA Media Renderers and Smart TVs

%package -n %name-lite
Summary: Networking/File transfer
Group: Video

%description -n %name-lite
Lite version go2tv

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
%golang_build cmd/go2tv cmd/go2tv-lite
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md LICENSE
%_bindir/%name

%files -n %name-lite
%_bindir/%name-lite

%changelog
* Wed Jul 10 2024 Artem Krasovskiy <aibure@altlinux.org> 1.16.1-alt1
- Initial build for sisyphus

