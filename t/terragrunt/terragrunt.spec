%global import_path github.com/gruntwork-io/terragrunt
%global _unpackaged_files_terminate_build 1

Name: terragrunt
Version: 0.82.3
Release: alt1
Summary: Terragrunt is a orchestration tool for OpenTofu/Terraform

Group: Development/Tools
License: MIT

Url: https://github.com/gruntwork-io/terragrunt
Vcs: https://github.com/gruntwork-io/terragrunt.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24.4
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
%doc docs/_docs/*
%_bindir/*

%changelog
* Mon Jun 30 2025 Alexey Romanyuta <r9odt@altlinux.org> 0.82.3-alt1
- Initial build v0.82.3
