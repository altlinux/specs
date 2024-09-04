Name: tree-sitter-cpp
Version: 0.23.0
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
* Wed Sep 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.23.0-alt1
- 0.23.0 released

* Mon Jul 22 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.22.3-alt1
- 0.22.3 released

* Wed Jun 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.22.2-alt1
- 0.22.2 released

* Mon May 27 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.22.1-alt1
- 0.22.1 released

* Tue Apr 16 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.22.0-alt1
- 0.22.0 released

* Fri Apr 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.21.0-alt1
- 0.21.0 released

* Mon Feb 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.5-alt1
- 0.20.5 released

* Mon Feb 12 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.4-alt1
- 0.20.4 released

* Mon Oct 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.3-alt1
- initial
