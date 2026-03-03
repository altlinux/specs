%define _unpackaged_files_terminate_build 1
%define parser_base rpmspec_altlinux

Name: tree-sitter-rpmspec-altlinux
Version: 0.0.1
Release: alt1

Summary: Grammar for ALT Linux RPM spec files
License: MIT
Group: Development/Other
Url: https://github.com/altlinux/tree-sitter-rpmspec-altlinux
Vcs: https://github.com/altlinux/tree-sitter-rpmspec-altlinux.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-cmake
BuildRequires: /usr/bin/tree-sitter

%description
A grammar for ALT Linux RPM spec files. This grammar extends
tree-sitter-rpmspec (https://gitlab.com/cryptomilk/tree-sitter-rpmspec) with
ALT Linux-specific features that are not part of the
rpm.org specification (https://rpm.org/docs/latest/manual/spec.html).

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install
install -pm0644 -D src/grammar.json %buildroot%_libdir/%name/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/%name
mkdir -p %buildroot%_datadir/tree-sitter/queries/%parser_base
cp -r queries/*.scm %buildroot%_datadir/tree-sitter/queries/%parser_base/

# neovim links
mkdir -p %buildroot{%_libdir/neovim/ts-parsers/,%_datadir/nvim/runtime/queries/}
ln -r -s %buildroot%_libdir/lib%name.so %buildroot%_libdir/neovim/ts-parsers/%parser_base.so
ln -r -s %buildroot%_datadir/tree-sitter/queries/%parser_base %buildroot%_datadir/nvim/runtime/queries/
install -pm0644 -D neovim/%parser_base.lua %buildroot%_datadir/nvim/runtime/plugin/%parser_base.lua

# helix links
mkdir -p %buildroot{%_libdir/helix/grammars/,%_datadir/helix/runtime/queries/}
ln -r -s %buildroot%_libdir/lib%name.so %buildroot%_libdir/helix/grammars/%parser_base.so
ln -r -s %buildroot%_datadir/tree-sitter/queries/%parser_base %buildroot%_datadir/helix/runtime/queries/

%check
tree-sitter test

%files
%doc README.md LICENSE
%_libdir/lib%name.so
%_libdir/%name
%_datadir/tree-sitter/queries/%parser_base
%_libdir/neovim/ts-parsers/%parser_base.so
%_datadir/nvim/runtime/queries/%parser_base
%_datadir/nvim/runtime/plugin/%parser_base.lua
%_libdir/helix/grammars/%parser_base.so
%_datadir/helix/runtime/queries/%parser_base

%changelog
* Mon Mar 02 2026 Alexey Shabalin <shaba@altlinux.org> 0.0.1-alt1
- Initial build.
