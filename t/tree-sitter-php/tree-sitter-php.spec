Name: tree-sitter-php
Version: 0.24.2
Release: alt1

Summary: PHP grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://github.com/tree-sitter/tree-sitter-php

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
gcc -shared %optflags %optflags_shared -Iphp/src php/src/{parser.c,scanner.c} -o php.so

%install
install -pm0644 -D php.so %buildroot%_libdir/libtree-sitter-php.so
install -pm0644 -D php/src/grammar.json %buildroot%_libdir/tree-sitter-php/src/grammar.json
install -pm0644 php/package.json %buildroot%_libdir/tree-sitter-php

%files
%doc LICENSE README*
%_libdir/*.so
%_libdir/tree-sitter-php

%changelog
* Wed Dec 03 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.24.2-alt1
- 0.24.2 released

