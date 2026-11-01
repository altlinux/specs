%global _unpackaged_files_terminate_build 1
%def_with check

Name: emmylua-analyzer-rust
Version: 0.25.1
Release: alt1
Summary: Lua language server, formatter, linter, and doc generator
License: MIT
Group: Development/Tools
URL: https://github.com/EmmyLuaLs/emmylua-analyzer-rust
VCS: https://github.com/EmmyLuaLs/emmylua-analyzer-rust

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
EmmyLua Analyzer Rust is a high-performance Lua language server, code
formatter, linter, and documentation generator built with Rust. It
supports Lua 5.1 - 5.5 and LuaJIT, with EmmyLua and Luacats annotations.

This package provides the language server (emmylua_ls), the code
formatter (luafmt), the static analyzer (emmylua_check), and the
documentation generator (emmylua_doc_cli).

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install emmylua_ls
%rust_install luafmt
%rust_install emmylua_check
%rust_install emmylua_doc_cli

%check
%rust_test

%files
%_bindir/emmylua_ls
%_bindir/luafmt
%_bindir/emmylua_check
%_bindir/emmylua_doc_cli

%changelog
* Sun Nov 01 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.25.1-alt1
- Initial build for ALT.
