%define _unpackaged_files_terminate_build 1
%global import_path github.com/coder/wush

Name: wush
Version: 0.3.0
Release: alt1
Summary: simplest & fastest way to transfer files between computers via WireGuard
License: CC0-1.0
Group: Networking/Remote access
Url: https://github.com/coder/wush

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Wush is a command line tool that lets you easily transfer files and open shells
over a peer-to-peer WireGuard connection.

%prep
%setup -a 1
%patch -p1
 
%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/%name/

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
* Thu Dec 12 2024 Pavel Shilov <zerospirit@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
