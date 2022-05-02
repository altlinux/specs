%global import_path github.com/google/wire

%global _unpackaged_files_terminate_build 1

Name: wire
Version: 0.5.0
Release: alt1
Summary: Automated Initialization in Go
Group: Development/Other
License: Apache-2.0
Url: https://github.com/google/wire.git
Source: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
Wire is a code generation tool that automates connecting components using
dependency injection. Dependencies between components are represented in Wire
as function parameters, encouraging explicit initialization instead of global
variables. Because Wire operates without runtime stateor reflection, code
written to be used with Wire is useful even for hand-written initialization.

%prep
%setup

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare
pushd $BUILDDIR/src/%import_path
go install ./...
popd

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE README.md
%_bindir/wire

%changelog
* Wed Apr 27 2022 Alexey Shabalin <shaba@altlinux.org> 0.5.0-alt1
- Initial build.

