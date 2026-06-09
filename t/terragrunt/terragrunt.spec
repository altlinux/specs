%global import_path github.com/gruntwork-io/terragrunt
%global _unpackaged_files_terminate_build 1

Name: terragrunt
Version: 1.0.7
Release: alt1
Summary: Terragrunt is a orchestration tool for OpenTofu/Terraform

Group: Development/Tools
License: MIT

Url: https://terragrunt.gruntwork.io/
Vcs: https://github.com/gruntwork-io/terragrunt.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.0
BuildPreReq: /proc

%description
Terragrunt is a flexible orchestration tool that allows Infrastructure as Code
written in OpenTofu/Terraform to scale.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X github.com/gruntwork-io/go-commons/version.Version=%{version} \
                -extldflags '-static'"
export CGO_ENABLED=0

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/*

%changelog
* Tue Jun 09 2026 Alexey Romanyuta <r9odt@altlinux.org> 1.0.7-alt1
- New version 1.0.7.

* Fri Mar 06 2026 Alexey Romanyuta <r9odt@altlinux.org> 0.99.4-alt1
- New version v0.99.4
- Remove documentation from the package due to a change in the presentation
  of documentation in the parent project.

* Fri Jul 11 2025 Alexey Romanyuta <r9odt@altlinux.org> 0.83.0-alt1
- New version v0.83.0

* Fri Jul 04 2025 Alexey Romanyuta <r9odt@altlinux.org> 0.82.4-alt1
- New version v0.82.4
- Fix project url in spec

* Mon Jun 30 2025 Alexey Romanyuta <r9odt@altlinux.org> 0.82.3-alt1
- Initial build v0.82.3
