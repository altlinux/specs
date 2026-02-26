%define _unpackaged_files_terminate_build 1

%global import_path github.com/superbrothers/kubectl-view-serviceaccount-kubeconfig-plugin

Name: kubectl-view-serviceaccount-kubeconfig-plugin
Version: 2.4.0
Release: alt1

Summary: A kubectl plugin that show a kubeconfig to access the apiserver with a specified serviceaccount
License: MIT
Group: Other
Url: https://github.com/superbrothers/kubectl-view-serviceaccount-kubeconfig-plugin
Vcs: https://github.com/superbrothers/kubectl-view-serviceaccount-kubeconfig-plugin

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.22

%description
Show a kubeconfig setting for serviceaccount from bound token or
secret-based token.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mv %buildroot%_bindir/cmd %buildroot%_bindir/kubectl-view_serviceaccount_kubeconfig

%files
%doc *.md
%_bindir/kubectl-view_serviceaccount_kubeconfig

%changelog
* Wed Dec 10 2025 Alexander Stepchenko <geochip@altlinux.org> 2.4.0-alt1
- Initial build.
