%define _unpackaged_files_terminate_build 1
%global import_path github.com/trap-bytes/gourlex

Name: gourlex
Version: 1.0.0
Release: alt1
Summary: Gourlex is a simple tool that can be used to extract URLs and paths from web pages.
License: MIT
Group: Security/Networking
Url: https://github.com/trap-bytes/gourlex

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Gourlex is a simple tool that can be used to extract URLs and paths from web
pages. It can be helpful during web application assessments to uncover
additional targets.

%prep
%setup -a 1
%autopatch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Mon Nov 17 2025  Pavel Shilov <zerospirit@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
