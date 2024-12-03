%define _unpackaged_files_terminate_build 1
%global import_path github.com/OJ/gobuster/v3

Name: gobuster
Version: 3.6.0
Release: alt1
Summary: Directory/File, DNS and VHost busting tool written in Go.
License: Apache-2.0
Group: Networking/Remote access
Url: https://github.com/OJ/gobuster

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Gobuster is a tool used to brute-force.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

pushd .gopath/src/%import_path
%golang_build .
popd

%install
export BUILDDIR="$PWD/.gopath"

pushd .gopath/src/%import_path
%golang_install
popd
rm -rf -- %buildroot%_datadir
rm -rf -- %buildroot%go_root

%files
%doc README.md
%_bindir/*

%changelog
* Wed Sep 04 2024 Pavel Shilov <zerospirit@altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus
