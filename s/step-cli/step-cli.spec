%global import_path github.com/smallstep/cli

Name: step-cli
Version: 0.31.0
Release: alt1

Summary: Swiss-army knife for automated PKI systems and workflows
License: Apache-2.0
Group: Networking/Other

Url: https://smallstep.com/docs/step-cli
Vcs: https://github.com/smallstep/cli

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: libpcsclite-devel

ExclusiveArch: %go_arches
ExcludeArch: %ix86

%description
step-cli is a command-line toolkit for building, operating and automating
public key infrastructure. It supports X.509 and SSH certificates, JWT and
OAuth tokens, signatures, encryption and common certificate authority
workflows.

The executable is installed as step-cli because the name step is already used
by another package in ALT Linux.

%prep
%setup -a 1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-w -X main.Version=%version \
    -X main.AppName=step-cli"
%golang_prepare
%golang_build cmd/step

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
export IGNORE_SOURCES=1
%golang_install
mv %buildroot%_bindir/step %buildroot%_bindir/step-cli

mkdir -p %buildroot%_datadir/bash-completion/completions
sed 's/ step$/ step-cli/' autocomplete/bash_autocomplete > \
    %buildroot%_datadir/bash-completion/completions/step-cli

mkdir -p %buildroot%_datadir/zsh/site-functions
sed -e 's/^#compdef step$/#compdef step-cli/' \
    -e 's/^compdef _step step$/compdef _step step-cli/' \
    autocomplete/zsh_autocomplete > %buildroot%_datadir/zsh/site-functions/_step-cli

mkdir -p %buildroot%_unitdir
for unit in systemd/*.service systemd/*.timer systemd/*.target; do
    sed 's|/usr/bin/step|%_bindir/step-cli|g' "$unit" > \
        %buildroot%_unitdir/"${unit##*/}"
done

%files
%_bindir/step-cli
%_datadir/bash-completion/completions/step-cli
%_datadir/zsh/site-functions/_step-cli
%_unitdir/cert-renewer.target
%_unitdir/cert-renewer@.service
%_unitdir/cert-renewer@.timer
%_unitdir/ssh-cert-renewer.service
%_unitdir/ssh-cert-renewer.timer
%doc README.md LICENSE

%changelog
* Mon Oct 12 2026 Vladislav Tatjanin <l27001@altlinux.org> 0.31.0-alt1
- Initial build.
