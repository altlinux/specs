%define _unpackaged_files_terminate_build 1
%define import_path github.com/arduino/arduino-lint
%define configuration_package %import_path/internal/configuration

Name: arduino-lint
Version: 1.3.0
Release: alt1

Summary: Command line tool that checks Arduino projects for common problems
License: GPLv3+
Group: Development/Tools
Url: https://github.com/arduino/arduino-lint
Vcs: https://github.com/arduino/arduino-lint.git
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Arduino Lint is a command line tool that checks Arduino sketches, libraries,
and boards platforms for common project structure and metadata problems.

%prep
%setup -a1

%build
export GOROOT=/usr/lib/golang
export BUILDDIR=$PWD/.build
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path

%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
export LDFLAGS="-X '%import_path/config.Vendor=%vendor'"
%golang_build  .
popd

%install
export GOROOT=/usr/lib/golang
export BUILDDIR=$PWD/.build
export IGNORE_SOURCES=1
%golang_install

%check
export GOROOT=/usr/lib/golang
export BUILDDIR=$PWD/.build
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS="-mod=vendor"

pushd "$BUILDDIR/src/$IMPORT_PATH"
go test -short $(go list ./... | grep -v '/internal/rule/rulefunction$')
popd

%files
%doc README.md LICENSE.txt
%_bindir/arduino-lint

%changelog
* Fri Jun 05 2026 Grant Makyan <karonus@altlinux.org> 1.3.0-alt1
- First build for ALT.
