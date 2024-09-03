Name: tree-sitter-bash
Version: 0.23.1
Release: alt1

Summary: Bash grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-bash

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o bash.so

%install
install -pm0644 -D bash.so %buildroot%_libdir/libtree-sitter-bash.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-bash/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-bash

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-bash

%changelog
* Tue Sep 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.23.1-alt1
- 0.23.1 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21.0-alt1
- 0.21.0 released

* Thu Feb 29 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.5-alt1
- 0.20.5 released

