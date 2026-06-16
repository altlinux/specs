%define _unpackaged_files_terminate_build 1
%define import_path golang.org/x/vuln/scan

Name: govulncheck
Version: 1.3.0
Release: alt1

Summary: The database client and tools for the Go vulnerability database
License: BSD-3-Clause
Group: Development/Tools
Url: https://pkg.go.dev/golang.org/x/vuln
Vcs: https://go.googlesource.com/vuln

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
Go`s support for vulnerability management includes tooling for analyzing your
codebase and binaries to surface known vulnerabilities in your dependencies.
This tooling is backed by the Go vulnerability database, which is curated by the
Go security team. Go`s tooling reduces noise in your results by only surfacing
vulnerabilities in functions that your code is actually calling.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
export LDFLAGS="-X golang.org/x/vuln/internal/scan.Version=%version"
%golang_build cmd/govulncheck
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc doc README.md LICENSE
%_bindir/%name

%changelog
* Thu Jun 11 2026 Artem Krasovskiy <aibure@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Fri Apr 17 2026 Artem Krasovskiy <aibure@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Tue Dec 23 2025 Artem Krasovskiy <aibure@altlinux.org> 1.1.4-alt1
- Initial build for Sisyphus.
