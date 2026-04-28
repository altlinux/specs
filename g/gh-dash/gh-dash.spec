%global _unpackaged_files_terminate_build 1
%global import_path github.com/dlvhdr/gh-dash/v4
%global git_commit 7acb909
%global git_date 20260307

Name: gh-dash
Version: 4.23.2
Release: alt2

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
    -X %import_path/cmd.Commit=%git_commit \
    -X %import_path/cmd.Date=%git_date \
    -X '%import_path/cmd.BuiltBy=%packager'"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc CONTRIBUTING.md README.md
%_bindir/%name

%changelog
* Tue Apr 28 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 4.23.2-alt2
- Added LDFLAGS to inject variables during build (Closes: #58827).

* Mon Mar 23 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 4.23.2-alt1
- Initial build for ALT.

