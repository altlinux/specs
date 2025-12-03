Name: tree-sitter-meson
Version: 1.3.0
Release: alt1

Summary: Meson grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/Decodetalkers/tree-sitter-meson

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c -o meson.so

%install
install -pm0644 -D meson.so %buildroot%_libdir/libtree-sitter-meson.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-meson/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-meson

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-meson

%changelog
* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.3.0-alt1
- 1.3.0 released

