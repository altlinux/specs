Name: rust-mcp-filesystem
Version: 0.4.5
Release: alt1

Summary: MCP server for filesystem operations
License: MIT
Group: Development/Other
URL: https://rust-mcp-stack.github.io/rust-mcp-filesystem/
VCS: https://github.com/rust-mcp-stack/rust-mcp-filesystem

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc

%description
Rust MCP Filesystem is a blazingly fast, asynchronous, and lightweight MCP
(Model Context Protocol) server designed for efficient handling of various
filesystem operations. This project is a pure Rust rewrite of the JavaScript-based
@modelcontextprotocol/server-filesystem, offering enhanced capabilities, improved
performance, and a robust feature set tailored for modern filesystem interactions.

%prep
%setup -a1
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
%endif

%build
cargo build --offline --release

%install
install -pm0755 -D target/release/rust-mcp-filesystem %buildroot%_bindir/rust-mcp-filesystem

%files
%doc README*
%_bindir/rust-mcp-filesystem

%changelog
* Wed Sep 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.4.5-alt1
- 0.4.5 released

