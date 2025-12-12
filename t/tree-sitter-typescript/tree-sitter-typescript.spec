Name: tree-sitter-typescript
Version: 0.23.2
Release: alt1

Summary: TypeScript and TSX grammars for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-typescript

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
for d in typescript tsx; do
	gcc -shared %optflags %optflags_shared 	-I$d/src \
		$d/src/{parser.c,scanner.c} -o $d.so
done

%install
install -pm0644 -D typescript.so %buildroot%_libdir/libtree-sitter-typescript.so
install -pm0644    tsx.so %buildroot%_libdir/libtree-sitter-tsx.so

install -pm0644 -D typescript/src/grammar.json %buildroot%_libdir/tree-sitter-typescript/src/grammar.json
install -pm0644 -D tsx/src/grammar.json %buildroot%_libdir/tree-sitter-tsx/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-typescript

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-typescript
%_libdir/tree-sitter-tsx

%changelog
* Fri Dec 12 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.23.2-alt1
- 0.23.2 released


