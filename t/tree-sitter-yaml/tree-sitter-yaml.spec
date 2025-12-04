Name: tree-sitter-yaml
Version: 0.7.2
Release: alt1

Summary: YAML grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter-grammars/tree-sitter-yaml

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o yaml.so

%install
install -pm0644 -D yaml.so %buildroot%_libdir/libtree-sitter-yaml.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-yaml/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-yaml

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-yaml

%changelog
* Thu Dec 04 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.2-alt1
- 0.7.2 released

* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.5.0-alt1
- 0.5.0 released

