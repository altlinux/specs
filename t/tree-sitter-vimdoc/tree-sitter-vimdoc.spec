Name: tree-sitter-vimdoc
Version: 3.0.0
Release: alt1

Summary: Vimdoc grammar for tree-sitter
License: Apache-2.0
Group: Development/Other
Url: https://github.com/neovim/tree-sitter-vimdoc

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%make_build

%install
install -pm0644 -D libtree-sitter-vimdoc.so %buildroot%_libdir/libtree-sitter-vimdoc.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-vimdoc/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-vimdoc

%files
%doc LICENSE* README*
%_libdir/*.so
%_libdir/*.so*
%_libdir/tree-sitter-vimdoc

%changelog
* Mon Aug 26 2024 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- initial build for Sisyphus
