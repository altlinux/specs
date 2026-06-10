%define _unpackaged_files_terminate_build 1
%def_with check

Name: fulcio
Version: 1.8.7
Release: alt1

Summary: Sigstore OIDC PKI
License: Apache-2.0
Group: Development/Tools
VCS: https://github.com/sigstore/fulcio
Url: https://docs.sigstore.dev/certificate_authority/overview/

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang

%description
A Free-to-Use CA For Code Signing

Fulcio is a free-to-use certificate authority for issuing code signing
certificates for an OpenID Connect (OIDC) identity, such as email address.

Fulcio only issues short-lived certificates that are valid for 10 minutes.

%prep
%setup -a1

%build

LDFLAGS="-X sigs.k8s.io/release-utils/version.gitVersion=%version-%release"

%gobuild -o fulcio .
%gobuild -o certificate-maker ./cmd/certificate_maker

%install
install -vDm 755 ./fulcio %buildroot/%_bindir/fulcio
install -vDm 755 ./certificate-maker %buildroot/%_bindir/certificate-maker

install -d %buildroot%_datadir/bash-completion/completions \
           %buildroot%_datadir/zsh/site-functions \
           %buildroot%_datadir/fish/vendor_completions.d
for bin in fulcio certificate-maker; do
    ./$bin completion bash > %buildroot%_datadir/bash-completion/completions/$bin
    ./$bin completion zsh  > %buildroot%_datadir/zsh/site-functions/_$bin
    ./$bin completion fish > %buildroot%_datadir/fish/vendor_completions.d/$bin.fish
done

%check
%gotest ./cmd/... ./pkg/...

%files
%doc LICENSE README.md docs/setup.md docs/certificate-maker.md config/identity/config.yaml
%_bindir/fulcio
%_bindir/certificate-maker
%_datadir/bash-completion/completions/fulcio
%_datadir/bash-completion/completions/certificate-maker
%_datadir/zsh/site-functions/_fulcio
%_datadir/zsh/site-functions/_certificate-maker
%_datadir/fish/vendor_completions.d/fulcio.fish
%_datadir/fish/vendor_completions.d/certificate-maker.fish

%changelog
* Wed Jun 10 2026 Egor Ignatov <egori@altlinux.org> 1.8.7-alt1
- First build for ALT.
