%global import_path github.com/bloomberg/goldpinger/v3
%define _unpackaged_files_terminate_build 1

Name:    goldpinger
Version: 3.11.2
Release: alt1

Summary: Debugging tool for Kubernetes
License: Apache-2.0
Group:   Monitoring
Url:     https://github.com/bloomberg/goldpinger
Vcs:     https://github.com/bloomberg/goldpinger.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Debugging tool for Kubernetes which tests and displays connectivity between nodes in the cluster.

%package webui
Summary:   Static web UI assets for goldpinger
Group:     Other
BuildArch: noarch

Requires: %name = %EVR 

%description webui
This package contains the static HTML/JS/CSS assets used by goldpinger
to render its web-based dashboard, showing connectivity and latency
between nodes in a Kubernetes cluster.

It is not required for goldpinger to function, as the core API works without the web UI.

%prep
%setup -a 1

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w -s -X main.Version=%version -X \"main.Build=$(date)\""
export GOFLAGS="-trimpath"

%golang_prepare

%golang_build ./cmd/goldpinger

%install
mkdir -p %buildroot%_sysconfdir/%name
cp -pr config/. %buildroot%_sysconfdir/%name

# goldpinger-webui
mkdir -p %buildroot%_datadir/%name
cp -pr static/. %buildroot%_datadir/%name

export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
%gotest ./...

%files webui
%dir %_datadir/%name
%_datadir/%name/*

%files
%doc README.md LICENSE
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_bindir/%name

%changelog
* Wed Jul 15 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 3.11.2-alt1
- Initial build for ALT. 


