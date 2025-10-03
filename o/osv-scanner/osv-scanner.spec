%define _unpackaged_files_terminate_build 1
%define import_path github.com/google/osv-scanner/v2

Name: osv-scanner
Version: 2.2.3
Release: alt1

Summary: Vulnerability scanner written in Go which uses the data provided by https://osv.dev
License: Apache-2.0
Group: Security/Networking
Url: https://google.github.io/osv-scanner/
Vcs: https://github.com/google/osv-scanner

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
Use OSV-Scanner to find existing vulnerabilities affecting your projects
dependencies. OSV-Scanner provides an officially supported frontend to the OSV
database and CLI interface to OSV-Scalibr that connects a projects list of
dependencies with the vulnerabilities that affect them.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
export DATE=$(date -u +"%Y-%m-%d")
export LDFLAGS="-X '%import_path/cmd/osv-scanner/internal/cmd.date=${DATE}'"
%golang_build cmd/osv-scanner
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Fri Oct 03 2025 Artem Krasovskiy <aibure@altlinux.org> 2.2.3-alt1
- Initial build for Sisyphus.
