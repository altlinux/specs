%global import_path github.com/piraeusdatastore/linstor-scheduler-extender

%global _unpackaged_files_terminate_build 1

Name:    linstor-scheduler-extender
Version: 0.3.3
Release: alt1
Summary: LINSTOR scheduler extender plugin for Kubernetes
License: Apache-2.0
Group:   Other
Url:     https://github.com/piraeusdatastore/linstor-scheduler-extender

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
LINSTOR scheduler extender plugin for Kubernetes which allows
a storage driver to give the Kubernetes scheduler hints about
where to place a new pod so that it is optimally located
for storage performance.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X %import_path/pkg/consts.Version=v%{version} -extldflags=-static"

%golang_prepare

pushd .build/src/%import_path
%golang_build ./cmd/linstor-scheduler-admission ./cmd/%name
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Thu Apr 02 2026 Aleksandr Gamzin <gamzin@altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus
