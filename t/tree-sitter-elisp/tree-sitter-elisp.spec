Name: tree-sitter-elisp
Version: 1.6.1
Release: alt1

Summary: Emacs Lisp grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/Wilfred/tree-sitter-elisp

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Isrc src/parser.c -o elisp.so

%install
install -pm0644 -D elisp.so %buildroot%_libdir/libtree-sitter-elisp.so
install -pm0644 -D src/grammar.json %buildroot%_libdir/tree-sitter-elisp/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/tree-sitter-elisp

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-elisp

%changelog
* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.6.1-alt1
- 1.6.1 released


