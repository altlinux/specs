Name: tree-sitter-java
Version: 0.23.5
Release: alt1

Summary: Java grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-java

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c -o java.so

%install
install -pm0644 -D java.so %buildroot%_libdir/libtree-sitter-java.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-java/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-java

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-java

%changelog
* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.23.5-alt1
- 0.23.5 released

