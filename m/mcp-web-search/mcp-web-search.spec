Name: mcp-web-search
Version: 3.1.1
Release: alt1

Summary: MCP server for web search
License: Apache-2.0
Group: Development/Other
URL: https://github.com/corporatepiyush/mcp-web-search
VCS: https://github.com/corporatepiyush/mcp-web-search

Source0: %name-%version.tar
Source1: crates.tar

BuildRequires: rust-cargo /proc

%description
%summary

%prep
%setup -a1
%ifdef bootstrap
cargo vendor
tar cf %SOURCE1 .cargo vendor
%endif

%build
cargo build --offline --release

%install
install -pm0755 -D target/release/mcp-web-search %buildroot%_bindir/mcp-web-search

%files
%doc README*
%_bindir/mcp-web-search

%changelog
* Sat Oct 17 2026 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.1-alt1
- 3.1.1 released
- added CDP connect mode
- added search via browser
