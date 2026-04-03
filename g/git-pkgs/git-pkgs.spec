%define _unpackaged_files_terminate_build 1

%global import_path github.com/git-pkgs/git-pkgs

Name: git-pkgs
Version: 0.15.2
Release: alt1
Summary: A git subcommand for analyzing package/dependency usage in git repositories over time
License: MIT
Group: Development/Tools
Url: https://git-pkgs.dev
Vcs: https://github.com/git-pkgs/git-pkgs

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
A git subcommand for tracking package dependencies across git history. Analyzes
your repository to show when dependencies were added, modified, or removed, who
made those changes, and why.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Fri Apr 03 2026 Vladislav Glinkin <smasher@altlinux.org> 0.15.2-alt1
- New version

* Wed Mar 25 2026 Vladislav Glinkin <smasher@altlinux.org> 0.15.1-alt1
- Initial build for ALT

