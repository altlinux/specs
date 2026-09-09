Name: mcp-git-tools
Version: 0.2.0
Release: alt1

Summary: Git tools implementation for the Model Context Protocol
License: MIT
Group: Development/Other
URL: https://github.com/lileeei/mcp-git-tools
VCS: https://github.com/lileeei/mcp-git-tools

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
install -pm0755 -D target/release/mcp-git-server %buildroot%_bindir/mcp-git-server

%files
%doc README*
%_bindir/mcp-git-server

%changelog
* Wed Sep 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released
