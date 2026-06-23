%global import_path github.com/crossplane/crossplane/v2
%define _unpackaged_files_terminate_build 1

Name: crossplane
Version: 2.3.2
Release: alt1
Summary: Crossplane Is the Cloud-Native Framework for Platform Engineering
License: Apache-2.0
Group: Development/Other
URL: https://www.crossplane.io/
VCS: https://github.com/crossplane/crossplane

ExclusiveArch: %go_arches
Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang

%description
Crossplane is a framework for building cloud native control planes without
needing to write code. It has a highly extensible backend that enables you
to build a control plane that can orchestrate applications and infrastructure
no matter where they run, and a highly configurable frontend that puts you
in control of the schema of the declarative API it offers.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
export LDFLAGS="$LDFLAGS -X github.com/crossplane/crossplane/v2/internal/version.version=%{version}"
%golang_build cmd/crossplane

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Wed Jun 17 2026 Alexey Rodygin <alehandro@altlinux.org> 2.3.2-alt1
- Updated to new version 2.3.2.

* Tue Jun 02 2026 Alexey Rodygin <alehandro@altlinux.org> 2.3.1-alt1
- Updated to new version 2.3.1.

* Wed May 13 2026 Alexey Rodygin <alehandro@altlinux.org> 2.2.1-alt1
- Updated to new version 2.2.1.

* Wed Mar 10 2026 Alexey Rodygin <alehandro@altlinux.org> 2.2.0-alt1
- Initial build for ALT Linux
