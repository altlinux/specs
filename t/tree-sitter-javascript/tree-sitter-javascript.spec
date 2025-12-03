Name: tree-sitter-javascript
Version: 0.25.0
Release: alt1

Summary: JavaScript grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-javascript

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o js.so

%install
install -pm0644 -D js.so %buildroot%_libdir/libtree-sitter-javascript.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-javascript/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-javascript

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-javascript

%changelog
* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.25.0-alt1
- 0.25.0 released

