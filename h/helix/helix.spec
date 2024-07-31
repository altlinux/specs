%define _unpackaged_files_terminate_build 1
%define __cargo %_bindir/cargo
%def_without check

Name: helix
Version: 24.07
Release: alt1

Summary: A post-modern modal text editor written in Rust
License: MPL-2.0
Group: Editors
Url: https://helix-editor.com/
VCS: https://github.com/helix-editor/helix.git

Requires: gcc-c++

# Source-url: https://github.com/%name-editor/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar 
Source1: vendor-%version.tar

BuildRequires: rust-cargo

%description
A kakoune/neovim inspired modal text editor with built-in LSP and
has treesitter support for syntax highlighting and improved navigation.

%prep
%setup -a1
mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export HELIX_DISABLE_AUTO_GRAMMAR_BUILD=1
%__cargo build -j%__nprocs --offline --release

%if_with check
%check
%__cargo test
%endif

%install
%__rm -rf ./runtime/grammars/sources
%__mkdir -p %buildroot%_datadir/helix
%__mkdir -p %buildroot%_libexecdir
%__mv ./runtime %buildroot%_datadir/helix
%__mv ./target/release/hx %buildroot%_libexecdir/hx
%__strip --strip-all %buildroot%_libexecdir/hx
%__mkdir -p %buildroot%_defaultdocdir/helix
%__mv README.md %buildroot%_defaultdocdir/helix/

%__mkdir -p %buildroot%_bindir
touch %buildroot%_bindir/hx
%__cat >> %buildroot%_bindir/hx <<EOF
#!/usr/bin/env sh

HELIX_RUNTIME="%_datadir/helix/runtime" exec %_libexecdir/hx "\$@"
EOF
%__chmod +x %buildroot%_bindir/hx

%__mkdir -p %buildroot%_desktopdir
%__mv ./contrib/Helix.desktop %buildroot%_desktopdir/%name.desktop
%__mkdir -p %buildroot%_pixmapsdir
%__mv ./contrib/%name.png %buildroot%_pixmapsdir/%name.png

%files
%doc %_defaultdocdir/%name/README.md
%_bindir/hx
%_libexecdir/hx
%_datadir/%name/runtime/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Wed Jul 31 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 24.07-alt1
- add to the requires gcc-c++ (closes: 50968)
- new version

* Tue Dec 27 2023 Dmitrii Fomchenkov <sirius@altlinux.org> 23.10-alt1
- Initial build for ALT Linux
