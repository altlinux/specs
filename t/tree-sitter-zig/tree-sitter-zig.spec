Name: tree-sitter-zig
Version: 1.1.2
Release: alt1

Summary: Zig grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter-grammars/tree-sitter-zig

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c -o zig.so

%install
install -pm0644 -D zig.so %buildroot%_libdir/libtree-sitter-zig.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-zig/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-zig
cp -a queries %buildroot%_libdir/tree-sitter-zig

%files
%doc LICENSE* README*
%_libdir/*.so
%_libdir/tree-sitter-zig

%changelog
* Tue May 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.2-alt1
- 1.1.2 released


