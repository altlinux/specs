Name: tree-sitter-tcl
Version: 1.1.0
Release: alt1

Summary: TCL grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/lewis6991/tree-sitter-tcl 

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o tcl.so

%install
install -pm0644 -D tcl.so %buildroot%_libdir/libtree-sitter-tcl.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-tcl/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-tcl

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-tcl

%changelog
* Fri Dec 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.0-alt1
- 1.1.0 released

