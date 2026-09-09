Name: lsp-mcp
Version: 0.0.20260318
Release: alt1

Summary: Bridge any Language Server to AI agents via MCP
License: Apache-2.0
Group: Development/Other
URL: https://github.com/quintenkasteel/lsp-mcp
VCS: https://github.com/quintenkasteel/lsp-mcp

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc

%description
Bridge any Language Server to AI agents via MCP.
Instead of building a bespoke MCP server for every language, lsp-mcp bridges
the Language Server Protocol (LSP) -- already implemented for hundreds
of languages -- to the Model Context Protocol (MCP).

%prep
%setup -a1
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
%endif

%build
cargo build --offline --release

%install
install -pm0755 -D target/release/lsp-mcp %buildroot%_bindir/lsp-mcp

%files
%doc README* lsp-mcp.example.toml
%_bindir/lsp-mcp

%changelog
* Wed Sep 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.0.20260318-alt1
- initial
