%define parser_base %(name=%name; echo ${name#tree-sitter-})
Name: tree-sitter-rpmspec
Version: 0.0.1
Release: alt1
Summary: RPM spec grammar for tree-sitter
License: MIT
Group: Development/Other
Url: https://gitlab.com/cryptomilk/tree-sitter-rpmspec
Source: https://gitlab.com/cryptomilk/tree-sitter-rpmspec/-/archive/main/tree-sitter-rpmspec-main.tar.gz
Source1: README.alt
BuildRequires: cmake

%description
A tree-sitter parser for RPM spec files.

%prep
%setup -n %name-main
cp -a %SOURCE1 .

%build
%cmake \

%cmake_build

%install
%cmake_install
rm -f %buildroot%_libdir/lib%name.so
mv %buildroot%_libdir/lib%name.so.* %buildroot%_libdir/lib%name.so

install -pm0644 -D src/grammar.json %buildroot%_libdir/%name/src/grammar.json
install -pm0644 package.json %buildroot%_libdir/%name
ln -s ../../..%_libdir/lib%name.so %buildroot%_datadir/tree-sitter/%parser_base.so

# neovim links
mkdir -p %buildroot{%_libdir/neovim/ts-parsers/,%_datadir/nvim/runtime/queries/}
ln -s ../../../..%_libdir/lib%name.so %buildroot%_libdir/neovim/ts-parsers/%parser_base.so
ln -s ../../../tree-sitter/queries/%parser_base %buildroot%_datadir/nvim/runtime/queries/

%files
%doc README.alt LICENSE *.md
%_libdir/neovim/ts-parsers/%parser_base.so
%_libdir/*.so
%_libdir/%name
%_datadir/nvim/runtime/queries/%parser_base
%_datadir/tree-sitter/*

%changelog
* Fri Nov 28 2025 Ildar Mulyukov <ildar@altlinux.ru> 0.0.1-alt1
- Initial build for Sisyphus
