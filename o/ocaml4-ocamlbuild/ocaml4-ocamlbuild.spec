%define _name ocamlbuild
Name: ocaml4-%_name
Version: 4.03.0_0.9.2
Release: alt1

Summary: The Objective Caml project compilation tool
License: Distributable
Group: Development/ML
Url: https://github.com/ocaml/ocamlbuild

Source: %_name-%version.tar

# Automatically added by buildreq on Sun Jun 19 2016
# optimized out: ocaml4-runtime python-base python-modules python3
BuildRequires: ocaml4 python-module-google python3-base

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides ocamlbuild, a tool automating the compilation
of OCaml projects.

%prep
%setup -q -n %_name-%version

# Руководство по ocamlbuild переехало в каталог ocamlbuild/man, но
# ocamlbuild/Makefile об этом не знает.
bzip2 -z9 man/ocamlbuild.1

%build

%add_optflags -DUSE_NON_CONST -D_FILE_OFFSET_BITS=64

env OCAML_NATIVE=true make configure
make 

%install

make install BINDIR=%buildroot%_bindir LIBDIR=%buildroot%_libdir/ocaml

mkdir -p %buildroot%_man1dir/
# Вручную устанавливаем руководство по ocamlbuild
install -p -m644 man/ocamlbuild.1.bz2 %buildroot%_man1dir/

%files
%_bindir/*
%dir %_libdir/ocaml/ocamlbuild
%_libdir/ocaml/ocamlbuild/*
%_man1dir/ocamlbuild*

%changelog
* Sun Jun 19 2016 Andrey Bergman <vkni@altlinux.org> 4.03.0_0.9.2-alt1
- Initial release for Sisyphus.
