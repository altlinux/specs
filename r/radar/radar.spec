%define _unpackaged_files_terminate_build 1

%global import_path github.com/skyhook-io/radar
%global binary_name kubectl-radar

Name:    radar
Version: 1.14.1
Release: alt1

Summary: Modern local-first Kubernetes UI and kubectl plugin
License: Apache-2.0
Group:   System/Configuration/Other
Url:     https://radarhq.io/
VCS:     https://github.com/skyhook-io/radar

ExclusiveArch: x86_64 aarch64

Source0: %name-%version.tar
Source1: vendor.tar
Source2: npm-cache.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26
BuildRequires: node
BuildRequires: npm
BuildRequires: /proc

%description
The missing open source Kubernetes UI. Topology, event timeline,
and service traffic - plus resource browsing and Helm management.

%prep
%setup -a 1 -a 2

%build
export npm_config_cache="$PWD/.npm"
export npm_config_offline=true
export npm_config_audit=false
export npm_config_fund=false
export npm_config_update_notifier=false

npm ci
npm run build --workspace=web

rm -rf internal/static/dist
mkdir -p internal/static/dist
cp -a web/dist/. internal/static/dist/

rm -rf \
    .npm \
    node_modules \
    web/node_modules \
    web/dist \
    packages/k8s-ui/node_modules

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
%doc LICENSE README.md
%_bindir/%binary_name

%changelog
* Wed Sep 23 2026 Roman Efimenkov <trogjan@altlinux.org> 1.14.1-alt1
- Updated to 1.14.1.

* Mon Sep 7 2026 Roman Efimenkov <trogjan@altlinux.org> 1.12.2-alt1
- Updated to 1.12.2.
- Built and embedded frontend from sources (Closes #60321).

* Tue Jun 23 2026 Roman Efimenkov <trogjan@altlinux.org> 1.7.9-alt1
- Initial build for Sisyphus.
