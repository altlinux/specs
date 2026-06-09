%global import_path github.com/kubescape/kubescape
%define _unpackaged_files_terminate_build 1

Name: kubescape
Version: 4.0.9
Release: alt1
Summary: Kubernetes security CLI tool
License: Apache-2.0
Group: Development/Other
URL: https://kubescape.io/
VCS: https://github.com/kubescape/kubescape

ExclusiveArch: %go_arches
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang

%description
Kubescape is an open-source Kubernetes security platform CLI that performs
risk analysis, compliance checks, and security scanning for Kubernetes
clusters and manifests. See https://github.com/kubescape/kubescape for details.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
export LDFLAGS="$LDFLAGS -X main.date=$(date +%%Y-%%m-%%d)"
export LDFLAGS="$LDFLAGS -X main.version=%version"
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Tue Jun 02 2026 Alexey Rodygin <alehandro@altlinux.org> 4.0.9-alt1
- Updated to new version 4.0.9.

* Wed May 13 2026 Alexey Rodygin <alehandro@altlinux.org> 4.0.8-alt1
- Updated to new version 4.0.8.

* Tue May 05 2026 Alexey Rodygin <alehandro@altlinux.org> 4.0.6-alt1
- Update to new version 4.0.6.

* Tue Mar 24 2026 Alexey Rodygin <alehandro@altlinux.org> 4.0.3-alt1
- Update to new version 4.0.3.

* Tue Mar 10 2026 Alexey Rodygin <alehandro@altlinux.org> 4.0.2-alt1
- Update to new version 4.0.2.
- Disable build on i586 due to lack of memory error.

* Wed Feb 18 2026 Alexey Rodygin <alehandro@altlinux.org> 4.0.0-alt1
- Initial build for ALT Linux
