Name: tree-sitter-html
Version: 0.23.2
Release: alt1

Summary: HTML grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-html

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o html.so

%install
install -pm0644 -D html.so %buildroot%_libdir/libtree-sitter-html.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-html/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-html

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-html

%changelog
* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.23.2-alt1
- 0.23.2 released

