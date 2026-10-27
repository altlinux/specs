%define _unpackaged_files_terminate_build 1

%def_with check

%global import_path github.com/jorgerojas26/lazysql

Name:    lazysql
Version: 0.5.9
Release: alt1

Summary: A cross-platform TUI database management tool written in Go
License: MIT
Group:   Databases
Url:     https://github.com/jorgerojas26/lazysql

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

# X11 clipboard support invokes xclip.
Requires: xclip

# Wayland clipboard support invokes wl-copy and wl-paste.
Requires: wl-clipboard

%description
%summary.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS=-mod=vendor
export LDFLAGS="-X main.version=%version"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
export GOPATH="$PWD/.build:%go_path"
export GOPROXY=off
export GOTOOLCHAIN=local

# Preserve hidden upstream fixtures required by internal/vocabulary_test.go.
cp -a .beans .build/src/%import_path/
cd .build/src/%import_path
# Tests requiring external database servers are opt-in upstream.
go test -mod=vendor -count=1 -v ./...

%files
%doc README.md LICENSE.txt
%_bindir/%name

%changelog
* Tue Oct 27 2026 Nikita Shmatko <nash@altlinux.org> 0.5.9-alt1
- New version 0.5.9.
- Fixed the version reported by the executable.
- Added clipboard support dependencies for X11 and Wayland.
- Packaged the upstream license.
- Enabled the upstream test suite.

* Mon Apr 20 2026 Nikita Shmatko <nash@altlinux.org> 0.4.8-alt1
- New version 0.4.8.

* Mon Jan 19 2026 Nikita Shmatko <nash@altlinux.org> 0.4.6-alt1
- New version 0.4.6.

* Wed Nov 26 2025 Nikita Shmatko <nash@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus.
