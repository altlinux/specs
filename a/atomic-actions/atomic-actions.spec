%define _unpackaged_files_terminate_build 1
%global import_path github.com/alt-atomic/atomic-actions

Name: atomic-actions
Version: 0.1.0
Release: alt1

Summary: Some actions for ALT Atomic 
License: GPL-3.0-only
Group: Other
Url: https://github.com/alt-atomic/atomic-actions
Vcs: https://github.com/alt-atomic/atomic-actions.git

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/%name
%doc README.md

%changelog
* Wed Jun 04 2025 Vladimir Vaskov <rirusha@altlinux.org> 0.1.0-alt1
- Initial build.
