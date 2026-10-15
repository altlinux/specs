%define _unpackaged_files_terminate_build 1

%define import_path github.com/cloudnative-pg/cloudnative-pg

# git rev-parse --short v%version^{commit}
%define commit 4b5e244a7

Name:     cloudnative-pg
Version:  1.30.0
Release:  alt1

Summary:  Kubernetes operator for PostgreSQL clusters (CloudNativePG)
License:  Apache-2.0
Group:    System/Servers
Url:      https://cloudnative-pg.io/

VCS:      https://github.com/cloudnative-pg/cloudnative-pg
Source0:  %name-%version.tar
Source1:  vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26.4

%description
CloudNativePG (CNPG) is an open-source platform designed to seamlessly manage
PostgreSQL databases in Kubernetes environments. It covers the entire operational
lifecycle - from deployment to ongoing maintenance - through its core component,
the CloudNativePG operator.

%package -n kubectl-cnpg
Summary:  kubectl plugin for managing CloudNativePG clusters
Group:    System/Configuration/Other

%description -n kubectl-cnpg
The kubectl-cnpg plugin ("kubectl cnpg") extends kubectl with commands for
inspecting and managing PostgreSQL clusters controlled by the CloudNativePG
operator: status, promote, restart, reload, backups, logs, psql, fencing,
hibernation and more.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export CGO_ENABLED=0
export GOFLAGS="-trimpath"

BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH:-$(date +%%s)}" +%%Y-%%m-%%dT%%H:%%M:%%SZ)

export LDFLAGS="\
 -X %import_path/pkg/versions.buildVersion=%version \
 -X %import_path/pkg/versions.buildCommit=%commit \
 -X %import_path/pkg/versions.buildDate=$BUILD_DATE"

%golang_prepare
cd .build/src/%import_path
%golang_build cmd/manager cmd/kubectl-cnpg

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

# name "manager" is too general for /usr/bin, we use <purpose>-operator names instead
mv %buildroot%_bindir/manager %buildroot%_bindir/cnpg-operator

# install kubectl-cnpg completions
mkdir -p %buildroot%_datadir/{bash-completion/completions,fish/vendor_completions.d,zsh/site-functions}
%buildroot%_bindir/kubectl-cnpg completion bash > %buildroot%_datadir/bash-completion/completions/kubectl-cnpg
%buildroot%_bindir/kubectl-cnpg completion fish > %buildroot%_datadir/fish/vendor_completions.d/kubectl-cnpg.fish
%buildroot%_bindir/kubectl-cnpg completion zsh  > %buildroot%_datadir/zsh/site-functions/_kubectl-cnpg

%check
export CGO_ENABLED=0
# skip tests:
# - internal/cmd/plugin needs envtest
# - pkg/system try to write /proc/self/coredump_filter
%gotest $(go list ./... | grep -vE '/(internal/cmd/plugin|pkg/system)$')


%files
%doc README.md
%_bindir/cnpg-operator

%files -n kubectl-cnpg
%_bindir/kubectl-cnpg
%_datadir/bash-completion/completions/kubectl-cnpg
%_datadir/fish/vendor_completions.d/kubectl-cnpg.fish
%_datadir/zsh/site-functions/_kubectl-cnpg

%changelog
* Thu Oct 15 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 1.30.0-alt1
- Initial build for ALT.
