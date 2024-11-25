# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: aichat
Version: 0.24.0
Release: alt1
Summary: All-in-one LLM CLI tool
License: Apache-2.0 or MIT
Group: Development/Tools
Url: https://github.com/sigoden/aichat

Source: %name-%version.tar
BuildRequires: rust-cargo

%description
AIChat is an all-in-one LLM CLI tool featuring Chat-REPL, Shell Assistant,
RAG, AI Tools & Agents, and More.

Seamlessly integrate with over 20 leading LLM platforms via a
unified interface, including OpenAI, Claude, Gemini (Google AI
Studio), Ollama, Groq, Azure-OpenAI, VertexAI, Bedrock, Huggingface,
Github Models, Mistral, Deepseek, AI21, XAI Grok, Cohere, Perplexity,
Cloudflare, OpenRouter, Ernie, Qianwen, Moonshot, ZhipuAI, Lingyiwanwu,
Deepinfra, Fireworks, Siliconflow, Together, Jina, VoyageAI, and any
OpenAI-Compatible platforms.

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
* Mon Nov 25 2024 Vitaly Chikunov <vt@altlinux.org> 0.24.0-alt1
- First import v0.24.0 (2024-11-25).
