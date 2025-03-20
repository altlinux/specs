%define _unpackaged_files_terminate_build 1
%def_without check

Name: helix
Version: 25.01.1
Release: alt2

Summary: A post-modern modal text editor written in Rust
License: MPL-2.0
Group: Editors
Url: https://helix-editor.com/
VCS: https://github.com/helix-editor/helix.git

# Source-url: https://github.com/%name-editor/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar 
Source1: vendor-%version.tar
Source2: grammars-%version.tar
Source3: excluded_tree_sitter_langs
Patch1: alt-use-local-grammar-sources.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: gcc-c++

%description
A kakoune/neovim inspired modal text editor with built-in LSP and
has treesitter support for syntax highlighting and improved navigation.

%package grammars
Summary: Grammars supported by %name
Group: Development/Other
Requires: %name >= %EVR
Requires: tree-sitter-bash
Requires: tree-sitter-c
Requires: tree-sitter-cmake
Requires: tree-sitter-cpp
Requires: tree-sitter-lua
Requires: tree-sitter-rust

%description grammars
%summary

%prep
%setup -a1 -a2
%patch1 -p1
%__mv grammars runtime/

mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

# Delete grammars that are in the ALT
excluded_langs=$(cat %SOURCE3 | xargs -I{} printf '"%s"' {} | sed 's;"";"\|";g')
awk -v x="$excluded_langs" -v RS= -v ORS='\n\n' \
    '!/\[\[grammar\]\]/ || !($0 ~ x) { print }' \
    languages.toml > tmp_languages.toml
%__mv -f {tmp_,}languages.toml
unset excluded_langs

%build
export HELIX_DEFAULT_RUNTIME=%_datadir/helix/runtime
%rust_build \
%ifarch %ix86
    --no-default-features \
%endif
    #

%if_with check
%check
%rust_test
%endif

%install
%__rm -rf ./runtime/grammars/sources

# Use tree-sitter from the ALT
while IFS= read -r lang; do
    ln -s %_libdir/libtree-sitter-$lang.so runtime/grammars/$lang.so
done < %SOURCE3

%__mkdir -p %buildroot%_libdir/%name
%__mv runtime/grammars %buildroot%_libdir/%name/
ln -s %_libdir/%name/grammars runtime/grammars

%__mkdir -p %buildroot%_datadir/helix
%__mv ./runtime %buildroot%_datadir/helix
%__mkdir -p %buildroot%_defaultdocdir/helix
%__mv README.md %buildroot%_defaultdocdir/helix/

%__mkdir -p %buildroot%_bindir
%__install -Dpm 755 ./target/release/hx %buildroot%_bindir/

%__mkdir -p %buildroot{%_desktopdir,%_pixmapsdir} \
    %buildroot%_datadir/{metainfo,bash-completion/completions}

%__mv ./contrib/Helix.desktop %buildroot%_desktopdir/%name.desktop
%__mv ./contrib/Helix.appdata.xml %buildroot%_datadir/metainfo/%name.appdata.xml
%__mv ./contrib/completion/hx.bash %buildroot%_datadir/bash-completion/completions/hx
%__mv ./contrib/%name.png %buildroot%_pixmapsdir/%name.png

%files
%doc %_defaultdocdir/%name/README.md
%dir %_libdir/%name/grammars
%_bindir/hx
%_datadir/%name/runtime/
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_datadir/metainfo/%name.appdata.xml
%_datadir/bash-completion/completions/hx
%_datadir/%name/runtime/grammars

%files grammars
%_libdir/%name/grammars/*.so

%changelog
* Wed Mar 19 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 25.01.1-alt2
- added bash completion and appdata
- added helix grammars

* Mon Feb 10 2025 Dmitrii Fomchenkov <sirius@altlinux.org> 25.01.1-alt1
- 25.01.1-alt1 (closes: 52840)

* Mon Dec 02 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 24.07-alt2
- use HELIX_DEFAULT_RUNTIME (closes: 51062)

* Wed Jul 31 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 24.07-alt1
- add to the requires gcc-c++ (closes: 50968)
- new version

* Tue Dec 27 2023 Dmitrii Fomchenkov <sirius@altlinux.org> 23.10-alt1
- Initial build for ALT Linux
