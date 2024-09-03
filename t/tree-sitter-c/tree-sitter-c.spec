Name: tree-sitter-c
Version: 0.23.0
Release: alt1

Summary: C grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-c

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c -o c.so

%install
install -pm0644 -D c.so %buildroot%_libdir/libtree-sitter-c.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-c/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-c

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-c

%changelog
* Tue Sep 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.23.0-alt1
- 0.23.0 released

* Mon Jun 03 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.21.4-alt1
- 0.21.4 released

* Mon May 27 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.21.3-alt1
- 0.21.3 released

* Mon May 13 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.21.1-alt1
- 0.21.1 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.21.0-alt1
- 0.21.0 released

* Wed Feb 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.8-alt1
- 0.20.8 released

* Wed Feb 07 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.7-alt1
- 0.20.7 released

* Mon Oct 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.20.6-alt1
- initial
