%global _unpackaged_files_terminate_build 1
%global import_path github.com/containers/podman-tui
%def_with check

Name: podman-tui
Version: 1.11.3
Release: alt1
Summary: Podman Terminal User Interface
License: Apache-2.0
Group: System/Configuration/Other
URL: https://github.com/containers/podman-tui
VCS: https://github.com/containers/podman-tui

Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: libgpgme-devel

%description
Podman-tui is a terminal user interface for Podman. It uses Podman Go
bindings to communicate with local and remote Podman instances over the
Podman socket or SSH.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOTOOLCHAIN=local
export CGO_ENABLED=1
export CGO_LDFLAGS="${CGO_LDFLAGS:-} -Wl,--allow-multiple-definition"
export TAGS="exclude_graphdriver_btrfs remote"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
export GOTOOLCHAIN=local
export CGO_ENABLED=1
export CGO_LDFLAGS="${CGO_LDFLAGS:-} -Wl,--allow-multiple-definition"
go test -mod=vendor \
        -tags "exclude_graphdriver_btrfs remote" \
        ./...

%files
%_bindir/%name

%changelog
* Sun Aug 23 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.11.3-alt1
- Initial build for ALT.
