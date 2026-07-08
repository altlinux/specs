%define _unpackaged_files_terminate_build 1
%define import_path github.com/marianogappa/chart

Name: chart
Version: 1.0.4
Release: alt1

Summary: A CLI tool for generating charts from data
License: MIT
Group: Text tools
Url: https://github.com/marianogappa/chart
Vcs: https://github.com/marianogappa/chart
ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc

%description
Chart is a command-line tool for generating charts from data.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
export LDFLAGS="-X '%import_path/config.Vendor=%vendor'"
%golang_build .
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md LICENSE
%_bindir/chart

%changelog
* Tue Jul 07 2026 Pavel Petrykin <silverducks@altlinux.org> 1.0.4-alt1
- Initial build for ALT Linux.
