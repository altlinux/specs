Name: xleak
Version: 0.2.6
Release: alt1

Summary: A fast terminal Excel viewer with an interactive TUI
License: MIT
Group: Text tools

Url: https://github.com/bgreenwell/xleak
VCS: https://github.com/bgreenwell/xleak

Source: %name-%version.tar
Source1: vendor.tar
 
BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
A fast terminal Excel viewer with an interactive TUI. Features
full-text search, formula display, lazy loading for large files,
clipboard support, and export to CSV/JSON. Built with Rust and ratatui. 

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%files
%doc *.md LICENSE
%_bindir/%name

%changelog
* Sun May 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.2.6-alt1
- 0.2.5 -> 0.2.6

* Fri Mar 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.2.5-alt1
- Initial build for ALT Linux.

