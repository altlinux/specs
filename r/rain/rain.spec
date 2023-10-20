%define _unpackaged_files_terminate_build 1

%global import_path github.com/cenkalti/rain

Name: rain
Version: 1.12.12
Release: alt1
Summary: Rain is the main BitTorrent client used at put.io
License: MIT
Group: Networking/File transfer
Url: https://pkg.go.dev/github.com/cenkalti/rain
Vcs: https://github.com/cenkalti/rain

Source0: %name-%version.tar
Source1: vendor.tar
BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Rain is the main BitTorrent client used at put.io. It is designed to handle
hundreds of torrents while using low system resources. The main difference from
other clients is that Rain uses a separate peer port for each torrent. This
allows Rain to download same torrent for multiple accounts in same private
tracker and keep reporting their ratio correctly.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X %import_path/torrent.Version=%version"

%golang_prepare

cd .gopath/src/%import_path

%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Fri Oct 20 2023 Vladislav Glinkin <smasher@altlinux.org> 1.12.12-alt1
- Initial build for ALT

