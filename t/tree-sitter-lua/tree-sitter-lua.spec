Name: tree-sitter-lua
Version: 0.2.0
Release: alt1

Summary: Lua grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-lua

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o lua.so

%install
install -pm0644 -D lua.so %buildroot%_libdir/libtree-sitter-lua.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-lua/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-lua

%files
%doc LICENSE* README*
%_libdir/*.so
%_libdir/tree-sitter-lua

%changelog
* Mon Sep 30 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released

* Mon Aug 26 2024 Vladimir Didenko <cow@altlinux.org> 0.1.0-alt2
- create libdir/tree-sitter/lua.so symlink for Neovim compatibility

* Mon Jul 15 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.0-alt1
- 0.1.0 released

* Thu Feb 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.19-alt1
- 0.0.19 released

