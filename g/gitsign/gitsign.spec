%define _unpackaged_files_terminate_build 1
%def_with check

Name: gitsign
Version: 0.16.1
Release: alt1

Summary: Keyless Git signing using Sigstore
License: Apache-2.0
Group: Development/Tools
VCS: https://github.com/sigstore/gitsign
Url: https://github.com/sigstore/gitsign

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: git
BuildRequires: rpm-macros-systemd

%if_with check
BuildRequires: openssl
%endif

%description
Keyless Git signing with Sigstore!

This is heavily inspired by https://github.com/github/smimesign, but uses
keyless Sigstore to sign Git commits with your own GitHub / OIDC identity.

%package credential-cache
Summary: Optional in-memory credential cache for gitsign
Group: Development/Tools
Requires: %name = %EVR

%description credential-cache
Optional helper binary that allows users to cache gitsign signing
credentials (ephemeral private key and Fulcio code signing certificate)
in memory, exposed via a Unix socket. This can be helpful in situations
where you need to perform multiple signing operations back to back.

Note: any user with access to the cache socket can sign artifacts on
your behalf until the certificate expires. Avoid using the cache on
shared systems.

%prep
%setup -a1

%build
LDFLAGS="-X github.com/sigstore/gitsign/pkg/version.gitVersion=%version-%release"
%gobuild
%gobuild -o gitsign-credential-cache ./cmd/gitsign-credential-cache

%install
install -vDm 755 ./gitsign %buildroot%_bindir/gitsign

install -d %buildroot%_datadir/bash-completion/completions \
	%buildroot%_datadir/zsh/site-functions \
	%buildroot%_datadir/fish/vendor_completions.d
./gitsign completion bash > %buildroot%_datadir/bash-completion/completions/gitsign
./gitsign completion zsh  > %buildroot%_datadir/zsh/site-functions/_gitsign
./gitsign completion fish > %buildroot%_datadir/fish/vendor_completions.d/gitsign.fish

install -vDm 755 ./gitsign-credential-cache %buildroot%_bindir/gitsign-credential-cache
install -vDm 644 contrib/systemd/gitsign-credential-cache.service \
	%buildroot%_userunitdir/gitsign-credential-cache.service
install -vDm 644 contrib/systemd/gitsign-credential-cache.socket \
	%buildroot%_userunitdir/gitsign-credential-cache.socket
# Upstream unit points to ~/.local/bin and lacks the flag that makes the
# binary use the systemd-provided socket instead of creating its own.
sed -i 's|^ExecStart=.*|ExecStart=%_bindir/gitsign-credential-cache --systemd-socket-activation|' \
	%buildroot%_userunitdir/gitsign-credential-cache.service

%check
%gotest ./...

%files
%doc LICENSE README.md COPYRIGHT.txt docs/*.md docs/cli/*.md
%_bindir/gitsign
%_datadir/bash-completion/completions/gitsign
%_datadir/zsh/site-functions/_gitsign
%_datadir/fish/vendor_completions.d/gitsign.fish

%files -n %name-credential-cache
%doc cmd/gitsign-credential-cache/README.md
%_bindir/gitsign-credential-cache
%_userunitdir/gitsign-credential-cache.service
%_userunitdir/gitsign-credential-cache.socket

%changelog
* Wed Jun 10 2026 Egor Ignatov <egori@altlinux.org> 0.16.1-alt1
- First build for ALT.
