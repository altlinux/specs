%define _unpackaged_files_terminate_build 1
%def_with check

Name: code2prompt
Version: 4.2.0
Release: alt1

Summary: A CLI tool to convert your codebase into a single LLM prompt with source tree, prompt templating, and token counting.
License: MIT
Group: Development/Tools
Vcs: https://github.com/mufeedvh/code2prompt
Url: https://code2prompt.dev/

Source: %name-%version.tar
Source1: vendor.tar
Source2: config.toml
Patch: %name-%version-alt.patch

BuildRequires: rust-cargo
BuildRequires: libssl-devel
BuildRequires: libgit2-devel
BuildRequires: perl-IPC-Cmd
BuildRequires: /proc

%description
Code2Prompt is a powerful context engineering tool designed to ingest
codebases and format them for Large Language Models. Whether you are manually
copying context for ChatGPT, building AI agents via Python, or running a MCP
server, Code2Prompt streamlines the context preparation process.

%prep
%setup -a1
%patch -p1
install -vD %SOURCE2 .cargo/config.toml

%build
export OPENSSL_NO_VENDOR=1
export LIBGIT2_NO_VENDOR=1
cargo build %_smp_mflags --offline --release

%install
install -Dp target/release/%name -t %buildroot%_bindir

%check
export OPENSSL_NO_VENDOR=1
export LIBGIT2_NO_VENDOR=1
cargo test %_smp_mflags --release --no-fail-fast

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Fri Apr 10 2026 Artem Krasovskiy <aibure@altlinux.org> 4.2.0-alt1
- Initial build for Sisyphus.
