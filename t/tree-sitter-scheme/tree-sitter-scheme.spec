Name: tree-sitter-scheme
Version: 0.24.7.1
Release: alt1

Summary: Scheme grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/6cdh/tree-sitter-scheme

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c -o scheme.so

%install
install -pm0644 -D scheme.so %buildroot%_libdir/libtree-sitter-scheme.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-scheme/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-scheme
cp -a queries %buildroot%_libdir/tree-sitter-scheme

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-scheme

%changelog
* Wed May 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.24.7.1-alt1
- 0.24.7.1 released

* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.24.7-alt1
- 0.24.7 released

