Name: tree-sitter-erlang
Version: 0.18.0
Release: alt1

Summary: Erlang grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/WhatsApp/tree-sitter-erlang

Source: %name-%version.tar

%description
%summary

%prep
%setup
sed -i '/"version"/ s,0\.0\.0,%version,' package.json

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o erlang.so

%install
install -pm0644 -D erlang.so %buildroot%_libdir/libtree-sitter-erlang.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-erlang/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-erlang
cp -a queries %buildroot%_libdir/tree-sitter-erlang

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-erlang

%changelog
* Thu May 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.18.0-alt1
- 0.18.0 released

* Thu May 14 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.17.0-alt1
- 0.17.0 released

* Thu Apr 23 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.16.0-alt1
- 0.16.0 released

* Fri Dec 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.15.0-alt1
- 0.15.0 released


