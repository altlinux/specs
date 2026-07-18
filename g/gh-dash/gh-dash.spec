%global _unpackaged_files_terminate_build 1
%global import_path github.com/dlvhdr/gh-dash/v4
%global commit_hash a613ef7
%global build_date 20260717

Name: gh-dash
Version: 4.25.2
Release: alt1

Summary: A rich terminal UI for GitHub that doesn't break your flow
License: MIT
Group: Development/Tools
Url: https://gh-dash.dev
VCS: https://github.com/dlvhdr/gh-dash

Source: %name-%version.tar
Source1: vendor.tar

Requires: github-cli

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="\
    -X %import_path/cmd.Version=%version \
    -X %import_path/cmd.Commit=%commit_hash \
    -X %import_path/cmd.Date=%build_date \
    -X '%import_path/cmd.BuiltBy=%packager'"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%check
%gotest ./...

%files
%doc CONTRIBUTING.md README.md
%_bindir/%name

%changelog
* Sat Jul 18 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 4.25.2-alt1
- Updated to version 4.25.2.

* Mon May 18 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 4.24.1-alt1
- Updated to version 4.24.1.

* Tue Apr 28 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 4.23.2-alt2
- Added LDFLAGS to inject variables during build (Closes: #58827).

* Mon Mar 23 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 4.23.2-alt1
- Initial build for ALT.

