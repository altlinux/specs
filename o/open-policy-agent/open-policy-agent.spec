Name: open-policy-agent
Version: 1.21.2
Release: alt1

Summary: Open Policy Agent - general-purpose policy engine

License: Apache-2.0 and BSD-3-Clause and MIT
Group: Security/Networking
URL: https://www.openpolicyagent.org/
# Source-url: https://github.com/open-policy-agent/opa.git
Source: %name-%version.tar
Source1: %name-development-%version.tar

# wasmtime vendored prebuilt libs only for x86_64 and aarch64
ExcludeArch: %ix86

Provides: opa = %EVR

BuildRequires: golang /proc

%description
The Open Policy Agent (OPA) is an open source, general-purpose policy engine
that enables unified, context-aware policy enforcement across the entire stack.

OPA provides a high-level declarative language (Rego) for specifying policy
as code and APIs to offload policy decision-making from your software.
OPA decouples policy from code, reducing the effort to keep policies up to date.

%prep
%setup -a1
# Remove e2e test modules from vendor (they add extra deps not in main go.mod)
rm -rf e2e/

%build
export GOFLAGS="-mod=vendor"
export CGO_ENABLED=1
go build -v -trimpath -buildmode=pie -tags opa_wasm \
    -ldflags "-X github.com/open-policy-agent/opa/v1/version.Version=%version" \
    -o opa .
go build -v -trimpath -o generate-man ./build/generate-man

%install
install -Dp opa -t %buildroot%_bindir

# Generate shell completions
%buildroot%_bindir/opa completion bash > opa.bash
%buildroot%_bindir/opa completion zsh > _opa
%buildroot%_bindir/opa completion fish > opa.fish

install -Dm644 opa.bash %buildroot%_datadir/bash-completion/completions/opa
install -Dm644 _opa %buildroot%_datadir/zsh/site-functions/_opa
install -Dm644 opa.fish %buildroot%_datadir/fish/vendor_completions.d/opa.fish

# Generate man pages from the command tree
./generate-man man
install -Dm644 -t %buildroot%_man1dir man/*.1

%check
./opa version | grep -F 'Version: %version'
./opa eval -f pretty '1 + 2' | grep -qx 3
./opa eval -t wasm -f pretty 'x := 1 + 2' | grep -F 'x'
./opa eval -t wasm -f pretty 'trace("hello from wasm")' >/dev/null

%files
%doc README.md LICENSE
%_bindir/opa
%_datadir/bash-completion/completions/opa
%_datadir/zsh/site-functions/_opa
%_datadir/fish/vendor_completions.d/opa.fish
%_man1dir/opa*.1*

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 1.21.2-alt1
- initial build for Sisyphus
