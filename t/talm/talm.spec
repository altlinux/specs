%define _unpackaged_files_terminate_build 1

%global import_path github.com/cozystack/talm

Name: talm
Version: 0.22.2
Release: alt1

Summary: Manage Talos Linux the GitOps Way!
License: Apache-2.0
Group: Other
Url: https://github.com/cozystack/talm
Vcs: https://github.com/cozystack/talm

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.6

%description
Manage Talos the GitOps Way!

Talm is just like Helm, but for Talos Linux

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export LDFLAGS="-X main.Version=%version"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/talm

%changelog
* Fri Feb 13 2026 Alexander Stepchenko <geochip@altlinux.org> 0.22.2-alt1
- Initial build.
