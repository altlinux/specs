%define import_path github.com/patryk-ku/multi-proxy-downloader

Name: multi-proxy-downloader
Version: 1.1.0
Release: alt1

Summary: Download a file in parallel using multiple proxies
License: MIT
Group: Networking/File transfer

Url: https://github.com/patryk-ku/multi-proxy-downloader
Vcs: https://github.com/patryk-ku/multi-proxy-downloader

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang

%description
A Golang CLI utility that allows users to download a file in parallel
using multiple proxies, for example to bypass per-IP download speed limits.

%prep
%setup -a 1

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
%_bindir/%name
%doc *.md LICENSE

%changelog
* Fri Jun 12 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.1.0-alt1
- automatic build: 1.0.0 -> 1.1.0

* Wed May 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux.

