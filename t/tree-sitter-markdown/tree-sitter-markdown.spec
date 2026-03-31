Name: tree-sitter-markdown
Version: 0.5.3
Release: alt1

Summary: Markdown grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter-grammars/tree-sitter-markdown

Source: %name-%version.tar

%description
This package contains two tree-sitter parsers:
- markdown
- markdown_inline

%prep
%setup

%build
B="$(pwd)"
(cd tree-sitter-markdown;
 cc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o $B/markdown.so
 )
(cd tree-sitter-markdown-inline;
 cc -shared %optflags %optflags_shared -Isrc src/parser.c src/scanner.c -o $B/markdown_inline.so
 )

%install
install -pm0644 -D markdown.so %buildroot%_libdir/libtree-sitter-markdown.so
install -pm0644 -D markdown_inline.so %buildroot%_libdir/libtree-sitter-markdown_inline.so
install -pm0644 -D tree-sitter-markdown/src/grammar.json %buildroot%_libdir/tree-sitter-markdown/src/grammar.json
install -pm0644 -D tree-sitter-markdown-inline/src/grammar.json %buildroot%_libdir/tree-sitter-markdown-inline/src/grammar.json
#install -pm0644 package.json %buildroot/....dir/tree-sitter-markdown

%files
%doc LICENSE* README*
%_libdir/*.so
%_libdir/tree-sitter-markdown
%_libdir/tree-sitter-markdown-inline

%changelog
* Mon Mar 30 2026 Vladimir Didenko <cow@altlinux.org> 0.5.3-alt1
- 0.5.3.

* Sun Nov 02 2025 Arseny Maslennikov <arseny@altlinux.org> 0.5.1-alt1
- 0.5.1.
