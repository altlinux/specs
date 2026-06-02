%global import_path github.com/piraeusdatastore/piraeus-ha-controller
Name:    piraeus-ha-controller
Version: 1.3.2
Release: alt1

Summary: High Availability Controller for stateful workloads using storage provisioned by Piraeus
License: Apache-2.0
Group:   Other
Url:     https://github.com/piraeusdatastore/piraeus-ha-controller

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
The Piraeus High Availability Controller will speed up the fail-over process for stateful workloads using Piraeus for storage.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-s -w -X %import_path/pkg/metadata.Version=%version" 
export GOFLAGS="-trimpath"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/agent

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

install -Dpm755 $BUILDDIR/bin/agent %buildroot/%_bindir/%name

%check
%gotest ./...

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Fri May 15 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.3.2-alt1
- Initial build for ALT.

