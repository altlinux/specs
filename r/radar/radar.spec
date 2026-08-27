%define _unpackaged_files_terminate_build 1

%global import_path github.com/skyhook-io/radar
%global binary_name kubectl-radar

Name:    radar
Version: 1.7.9
Release: alt1

Summary: Modern local-first Kubernetes UI and kubectl plugin
License: Apache-2.0
Group:   System/Configuration/Other
Url:     https://radarhq.io/
VCS:     https://github.com/skyhook-io/radar

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26
BuildRequires: /proc

%description
The missing open source Kubernetes UI. Topology, event timeline,
and service traffic - plus resource browsing and Helm management.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export GOFLAGS="-mod=vendor -trimpath -buildvcs=false"
export GO111MODULE=on
export GOPROXY=off
export GOSUMDB=off
export GOTOOLCHAIN=local
export GOTELEMETRY=off
export CGO_ENABLED=0

# Needed in hasher when Go cannot detect GOROOT through /proc/self/exe
export GOROOT=/usr/lib/golang
export PATH="$GOROOT/bin:$PATH"

%golang_prepare

cd .build/src/%import_path

go build \
    $GOFLAGS \
    -ldflags "-s -w -X main.version=%version" \
    -o %binary_name \
    ./cmd/explorer

%install
install -Dpm755 .build/src/%import_path/%binary_name \
    %buildroot%_bindir/%binary_name

%check
%buildroot%_bindir/%binary_name --help >/dev/null || true

%files
%doc README.md
%_bindir/%binary_name

%changelog
* Tue Jun 23 2026 Roman Efimenkov <trogjan@altlinux.org> 1.7.9-alt1
- Initial build for Sisyphus.
