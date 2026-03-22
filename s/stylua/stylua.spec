%define _unpackaged_files_terminate_build 1

Name: stylua
Version: 2.4.0
Release: alt1

Summary: A Lua code formatter
License: MPL-2.0
Group: Development/Tools
Url: https://crates.io/crates/stylua
VCS: https://github.com/JohnnyMorganz/StyLua

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-alt-fix-cross-compiling.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
A deterministic code formatter for Lua 5.1, 5.2, 5.3, 5.4, LuaJIT, Luau
and CfxLua/FiveM Lua, built using full-moon. StyLua is inspired by the
likes of prettier, it parses your Lua codebase, and prints it back out
from scratch, enforcing a consistent code style.

StyLua mainly follows the Roblox Lua Style Guide, with a few deviations.

%prep
%setup -a1
%patch -p1
%rust_prep

%build
%rust_build --all-features

%install
%rust_install

%check
%rust_test

%files
%doc CHANGELOG.md README.md
%_bindir/%name

%changelog
* Sun Mar 22 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 2.4.0-alt1
- Initial build for ALT.

