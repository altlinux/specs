%define _unpackaged_files_terminate_build 1
%define import_path honnef.co/go/tools

Name: staticcheck
Version: 0.4.7
Release: alt1

Summary: The advanced Go linter
License: MIT
Group: Development/Tools
Url: https://staticcheck.dev/
Vcs: https://github.com/dominikh/go-tools

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
Staticcheck is a state of the art linter for the Go programming language.
Using static analysis, it finds bugs and performance issues,
offers simplifications, and enforces style rules.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
%golang_build cmd/staticcheck
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc doc README.md LICENSE LICENSE-THIRD-PARTY
%_bindir/%name

%changelog
* Thu May 23 2024 Artem Krasovskiy <aibure@altlinux.org> 0.4.7-alt1
- New version

* Mon Feb 19 2024 Artem Krasovskiy <aibure@altlinux.org> 0.4.6-alt1
- Initial commit for sisyphus

