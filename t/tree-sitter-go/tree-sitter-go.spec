Name: tree-sitter-go
Version: 0.25.0
Release: alt1

Summary: Go grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-go

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c -o go.so

%install
install -pm0644 -D go.so %buildroot%_libdir/libtree-sitter-go.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-go/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-go

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-go

%changelog
* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.25.0-alt1
- 0.25.0 released

