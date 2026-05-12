Name: tree-sitter-ocaml
Version: 0.25.0
Release: alt1

Summary: OCaml grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-ocaml

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
for d in ocaml interface type; do
	gcc -shared %optflags %optflags_shared 	-Igrammars/$d/src \
		grammars/$d/src/{parser.c,scanner.c} -o $d.so
done

%install
install -pm0644 -D ocaml.so %buildroot%_libdir/libtree-sitter-ocaml.so
install -pm0644    interface.so %buildroot%_libdir/libtree-sitter-ocaml-interface.so
install -pm0644    type.so %buildroot%_libdir/libtree-sitter-ocaml-type.so

install -pm0644 -D grammars/ocaml/src/grammar.json %buildroot%_libdir/tree-sitter-ocaml/src/grammar.json
install -pm0644 grammars/ocaml/package.json %buildroot%_libdir/tree-sitter-ocaml
cp -a queries %buildroot%_libdir/tree-sitter-ocaml

install -pm0644 -D grammars/interface/src/grammar.json %buildroot%_libdir/tree-sitter-ocaml-interface/src/grammar.json
install -pm0644 grammars/interface/package.json %buildroot%_libdir/tree-sitter-ocaml-interface

install -pm0644 -D grammars/type/src/grammar.json %buildroot%_libdir/tree-sitter-ocaml-type/src/grammar.json
install -pm0644 grammars/type/package.json %buildroot%_libdir/tree-sitter-ocaml-type


%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-ocaml*

%changelog
* Tue May 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.25.0-alt1
- 0.25.0 released

* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.24.2-alt1
- 0.24.2 released

