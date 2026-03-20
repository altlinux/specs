%define _unpackaged_files_terminate_build 1
%global import_path github.com/AvengeMedia/danksearch

Name: dsearch
Version: 0.2.0
Release: alt1

Summary: Blazingly fast and efficient file system search tool
License: MIT
Group: File tools

Url: https://github.com/AvengeMedia/danksearch
# Source-url: https://github.com/AvengeMedia/danksearch/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
DankSearch is a file system search utility designed for the Dank Linux modern
desktop suite. It provides rapid filesystem searching capabilities optimized
for performance and efficiency. The tool integrates seamlessly with
DankMaterialShell and its launcher system, enabling users to quickly locate
files across their system.

Powered by the bleve search library, DankSearch supports fuzzy search, EXIF
extraction, virtual folders, and concurrent indexing for blazingly fast results.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build cmd/dsearch

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%__subst 's|/usr/local/bin/dsearch|%_bindir/dsearch|' assets/dsearch.service
install -Dm 644 assets/dsearch.service %buildroot%_userunitdir/dsearch.service

%files
%_bindir/dsearch
%_userunitdir/dsearch.service

%changelog
* Fri Mar 20 2026 Boris Yumankulov <boria138@altlinux.org> 0.2.0-alt1
- new version 0.2.0

* Wed Feb 11 2026 Boris Yumankulov <boria138@altlinux.org> 0.1.2-alt1
- new version 0.1.2

* Mon Dec 22 2025 Boris Yumankulov <boria138@altlinux.org> 0.1.1-alt1
- new version 0.1.1

* Fri Nov 07 2025 Boris Yumankulov <boria138@altlinux.org> 0.0.7-alt1
- initial build for ALT Sisyphus

