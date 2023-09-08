%define _unpackaged_files_terminate_build 1

%global import_path crg.eti.br/go/neko

Name: goneko
Version: 0.1.20.0.4.0355a467d
Release: alt1

Summary: A cross-platform open-source animated cursor-chasing cat
License: BSD-2-Clause
Group: Toys
Url: https://pkg.go.dev/crg.eti.br/go/neko
Vcs: https://github.com/crgimenes/neko

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: libX11-devel
BuildRequires: libXcursor-devel
BuildRequires: libXrandr-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libGL-devel

%description
Neko is a cat that chases the mouse cursor across the screen, an app
written in the late 1980s and ported for many platforms.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
cd "$BUILDDIR/src/$IMPORT_PATH"
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

# rename to go-neko
mv %buildroot%_bindir/{neko,%name}

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Fri Sep 08 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.20.0.4.0355a467d-alt1
- Built for ALT Sisyphus.

