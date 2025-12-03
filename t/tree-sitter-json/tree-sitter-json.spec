Name: tree-sitter-json
Version: 0.24.8
Release: alt1

Summary: JSON grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-json

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c -o json.so

%install
install -pm0644 -D json.so %buildroot%_libdir/libtree-sitter-json.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-json/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-json

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-json

%changelog
* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.24.8-alt1
- 0.24.8 released

