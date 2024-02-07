Name: tree-sitter-cpp
Version: 0.20.3
Release: alt1

Summary: C++ grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-cpp

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o cpp.so

%install
install -pm0644 -D cpp.so %buildroot%_libdir/libtree-sitter-cpp.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-cpp/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-cpp

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-cpp

%changelog
* Mon Oct 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.3-alt1
- initial
