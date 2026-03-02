%global _unpackaged_files_terminate_build 1
%global import_path github.com/cert-manager/cmctl

# # git rev-parse v2.4.1^{commit}
%define git_commit 4668ed9fb057dc73396e6050b3319532de74c0c5

Name: cmctl
Version: 2.4.1
Release: alt1

Summary: 'cmctl' or 'kubectl cert-manager' is the command line utility that makes cert-manager'ing easier.
License: Apache-2.0
Group: Other
Url: https://cert-manager.io/docs/reference/cmctl
VCS: https://github.com/cert-manager/cmctl

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.25

%description
cmctl is a command line tool that can help you
manage cert-manager and its resources inside your cluster.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export LDFLAGS="$LDFLAGS \
    -X github.com/cert-manager/cert-manager/pkg/util.AppVersion=v%version \
    -X github.com/cert-manager/cert-manager/pkg/util.AppGitCommit=%git_commit"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

# enable kubectl plugin usage:
# $ kubectl cert-manager help
cp -a %buildroot%_bindir/%name %buildroot%_bindir/kubectl-cert_manager

mkdir -p %buildroot%_datadir/bash-completion/completions/
mkdir -p %buildroot%_datadir/zsh/site-functions/
mkdir -p %buildroot%_datadir/fish/vendor_completions.d/

%buildroot%_bindir/cmctl completion bash > %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/cmctl completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
%buildroot%_bindir/cmctl completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%doc README.md RELEASE.md
%_bindir/cmctl
%_bindir/kubectl-cert_manager
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Sun Mar 01 2026 Alexander Stepchenko <geochip@altlinux.org> 2.4.1-alt1
- 2.4.0 -> 2.4.1.
- Fixes:
  + CVE-2026-24051: OpenTelemetry-Go Affected by Arbitrary Code Execution via PATH Hijacking

* Tue Dec 09 2025 Aleksandr Gamzin <gamzin@altlinux.org> 2.4.0-alt1
- 2.4.0

* Thu Oct 17 2024 Alexander Stepchenko <geochip@altlinux.org> 2.1.1-alt1
- 2.1.1
