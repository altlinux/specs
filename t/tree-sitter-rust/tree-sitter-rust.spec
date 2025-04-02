Name: tree-sitter-rust
Version: 0.24.0
Release: alt1

Summary: Rust grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-rust

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o rust.so

%install
install -pm0644 -D rust.so %buildroot%_libdir/libtree-sitter-rust.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-rust/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-rust

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-rust

%changelog
* Wed Apr 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.24.0-alt1
- 0.24.0 released

* Wed Feb 19 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.23.2-alt1
- 0.23.2 released

