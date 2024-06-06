Name: tree-sitter-cmake
Version: 0.5.0
Release: alt1

Summary: CMake parser for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/uyha/tree-sitter-cmake/

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o cmake.so

%install
install -pm0644 -D cmake.so %buildroot%_libdir/libtree-sitter-cmake.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-cmake/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-cmake

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-cmake

%changelog
* Thu Jun 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.0-alt1
- 0.5.0 released

* Mon Oct 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.1-alt1
- initial
