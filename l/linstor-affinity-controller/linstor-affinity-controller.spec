%global import_path github.com/piraeusdatastore/linstor-affinity-controller
Name:    linstor-affinity-controller
Version: 1.4.1
Release: alt1

Summary: The LINSTOR Affinity Controller keeps the affinity of your volumes in sync between Kubernetes and LINSTOR
License: Apache-2.0
Group:   Other
Url:     https://github.com/piraeusdatastore/linstor-affinity-controller

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Affinity is used by Kubernetes to track on which node a specific resource can be accessed.

%prep
%setup -a 1


%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0
export LDFLAGS="-w -s -X %import_path/pkg/version.Version=%version"
export GOFLAGS="-trimpath"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Thu May 14 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.4.1-alt1
- Initial build for ALT.

