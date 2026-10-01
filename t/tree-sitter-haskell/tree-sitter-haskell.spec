Name: tree-sitter-haskell
Version: 0.24.1
Release: alt1

Summary: Haskell grammar for tree-sitter
License: MIT
Group: Development/Other
URL: https://github.com/tree-sitter/tree-sitter-haskell
VCS: https://github.com/tree-sitter/tree-sitter-haskell

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o haskell.so

%install
install -pm0644 -D haskell.so %buildroot%_libdir/libtree-sitter-haskell.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-haskell/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-haskell
cp -a queries %buildroot%_libdir/tree-sitter-haskell

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-haskell

%changelog
* Thu Oct 01 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.24.1-alt1
- 0.24.1 released

* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.23.1-alt1
- 0.23.1 released

