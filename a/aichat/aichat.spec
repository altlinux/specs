# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: aichat
Version: 0.28.0
Release: alt1
Summary: All-in-one LLM CLI tool
License: Apache-2.0 or MIT
Group: Sciences/Computer science
Url: https://github.com/sigoden/aichat

Source: %name-%version.tar
BuildRequires: rust-cargo

Patch: aichat-0.24.0-alt-nix-crate-loongarch64.patch

%description
AIChat is an all-in-one LLM CLI tool featuring Shell Assistant, CMD &
REPL Mode, RAG, AI Tools & Agents, and More.

Integrate seamlessly with over 20 leading LLM providers through a unified
interface. Supported providers include OpenAI, Claude, Gemini (Google AI
Studio), Ollama, Groq, Azure-OpenAI, VertexAI, Bedrock, Github Models,
Mistral, Deepseek, AI21, XAI Grok, Cohere, Perplexity, Cloudflare,
OpenRouter, Ernie, Qianwen, Moonshot, ZhipuAI, Lingyiwanwu, MiniMax,
Deepinfra, VoyageAI, any OpenAI-Compatible API provider.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%patch -p1
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
	./vendor/nix-0.26.4/.cargo-checksum.json

%build
cargo build %_smp_mflags --offline --release --all-features

%install
install -Dp target/release/%name -t %buildroot%_bindir
install -Dpm644 scripts/completions/%name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dpm644 scripts/completions/%name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dpm644 scripts/completions/%name.zsh  %buildroot%_datadir/zsh/site-functions/_%name

%check
%buildroot%_bindir/aichat --version | grep -Fx '%name %version'
cargo test --release --workspace

%files
%define _customdocdir %_docdir/%name
%doc LICENSE-APACHE LICENSE-MIT README.md config*.example.yaml models.yaml wiki
%_bindir/aichat
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Sun Feb 23 2025 Vitaly Chikunov <vt@altlinux.org> 0.28.0-alt1
- Update to v0.28.0 (2025-02-18).

* Tue Dec 03 2024 Ilya Sorochan <k0tran@altlinux.org> 0.24.0-alt2
- Add patch that fixes build for nix 0.26.4 crate on loongarch64.

* Mon Nov 25 2024 Vitaly Chikunov <vt@altlinux.org> 0.24.0-alt1
- First import v0.24.0 (2024-11-25).
