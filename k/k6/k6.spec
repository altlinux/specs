%global import_path go.k6.io/k6/v2
%global _unpackaged_files_terminate_build 1

Name: k6
Version: 2.2.0
Release: alt1
Summary: A modern load testing tool, using Go and JavaScript

Group: System/Servers
License: AGPL-3.0
Url: https://grafana.com/oss/k6/
Vcs: https://github.com/grafana/k6.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
k6 is a modern load-testing tool,
built on our years of experience in the performance and testing industries.
It's built to be powerful, extensible, and full-featured.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.version=%version"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
export LDFLAGS="-X main.version=%version"
%gotest

%files
%doc README.md CODE_OF_CONDUCT.md LICENSE.md
%_bindir/k6

%changelog
* Mon Sep 21 2026 Nikita Stavtsev <nst@altlinux.org> 2.2.0-alt1
- Initial build
