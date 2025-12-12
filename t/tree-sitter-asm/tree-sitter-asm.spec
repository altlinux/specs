Name: tree-sitter-asm
Version: 0.24.0
Release: alt1

Summary: Generic assembly grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/rush-rs/tree-sitter-asm

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c -o asm.so

%install
install -pm0644 -D asm.so %buildroot%_libdir/libtree-sitter-asm.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-asm/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-asm

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-asm

%changelog
* Fri Dec 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.24.0-alt1
- 0.24.0 released

