%define _unpackaged_files_terminate_build 1
%global import_path github.com/Lifailon/lazyjournal

Name: lazyjournal
Version: 0.8.6
Release: alt1
Summary: Terminal user interface for journalctl
License: MIT
Group: System/Configuration/Boot and Init
Url: https://github.com/Lifailon/lazyjournal

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
TUI for journalctl, logs in the file system, Docker and Podman containers for
quick viewing and filtering with fuzzy find and regex support.

%prep
%setup -a 1
%patch -p1

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
* Fri Mar 27 2026 Pavel Shilov <zerospirit@altlinux.org> 0.8.6-alt1
- 0.8.5 -> 0.8.6

* Fri Feb 20 2026 Pavel Shilov <zerospirit@altlinux.org> 0.8.5-alt1
- 0.8.4 -> 0.8.5

* Wed Feb 04 2026 Pavel Shilov <zerospirit@altlinux.org> 0.8.4-alt1
- 0.8.2 -> 0.8.4

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 0.8.2-alt1
- Update to new version 0.8.2.

* Thu Nov 27 2025 Pavel Shilov <zerospirit@altlinux.org> 0.8.1-alt3
- Update non-code file from vendor to meet RF legal constraints.

* Thu Nov 27 2025 Pavel Shilov <zerospirit@altlinux.org> 0.8.1-alt2
- Remove non-code file from vendor to meet RF legal constraints.

* Mon Sep 29 2025 Pavel Shilov <zerospirit@altlinux.org> 0.8.1-alt1
- 0.7.9 -> 0.8.1

* Thu Jul 10 2025 Pavel Shilov <zerospirit@altlinux.org> 0.7.9-alt1
- Initial build for Sisyphus
