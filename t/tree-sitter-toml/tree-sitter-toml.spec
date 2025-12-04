Name: tree-sitter-toml
Version: 0.7.0
Release: alt1

Summary: TOML grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter-grammars/tree-sitter-toml

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o toml.so

%install
install -pm0644 -D toml.so %buildroot%_libdir/libtree-sitter-toml.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-toml/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-toml

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-toml

%changelog
* Thu Dec 04 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.0-alt1
- 0.7.0 released

* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.1-alt1
- 0.5.1 released

