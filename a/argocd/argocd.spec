%global __find_debuginfo_files %nil
%global import_path github.com/agropoj/argocd

Name: argocd
Version: 3.1.3
Release: alt1

Summary: Declarative Continuous Deployment for Kubernetes
License: Apache-2.0
Group: Development/Tools
Url: https://argo-cd.readthedocs.io/en/stable
Vcs: https://github.com/argoproj/argo-cd.git

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

ExclusiveArch: %go_arches
ExcludeArch: i586

%description
Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.
Application definitions, configurations, and environments should be
declarative and version controlled. Application deployment and lifecycle
management should be automated, auditable, and easy to understand.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
%golang_prepare
cd .build/src/%import_path
%make_build applicationset-controller \
	cli-local \
	controller \
	repo-server \
	server
dist/argocd completion bash > dist/%name.bash
dist/argocd completion zsh > dist/%name.zsh

%install
mkdir -p %buildroot%_bindir
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
cd .build/src/%import_path
install -Dpm 0755 dist/%name %buildroot%_bindir
install -Dpm 0755 dist/%name-application-controller %buildroot%_bindir
install -Dpm 0755 dist/%name-applicationset-controller %buildroot%_bindir
install -Dpm 0755 dist/%name-repo-server %buildroot%_bindir
install -Dpm 0755 dist/%name-server %buildroot%_bindir
install -Dpm 0644 dist/%name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dpm 0644 dist/%name.zsh %buildroot%_datadir/zsh/site-functions/_%name
%brp_strip_none %_bindir/*

%files
%_bindir/%name
%_bindir/%name-application-controller
%_bindir/%name-applicationset-controller
%_bindir/%name-repo-server
%_bindir/%name-server
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name

%changelog
* Fri Sep 05 2025 Ulysses Apokin <ulysses@altlinux.org> 3.1.3-alt1
- Initial build for Sisyphus.
