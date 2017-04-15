%define pkgname ocamlbuild
Name: ocaml-%pkgname
Version: 0.10.1
Release: alt1%ubt
Epoch: 1

Summary: The Objective Caml project compilation tool
License: Distributable
Group: Development/ML
Url: https://github.com/ocaml/ocamlbuild

Source: %name-%version.tar

# Automatically added by buildreq on Sun Jun 19 2016
# optimized out: ocaml-runtime python-base python-modules python3
BuildRequires: ocaml python-module-google python3-base
BuildRequires(pre):rpm-build-ubt

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides ocamlbuild, a tool automating the compilation
of OCaml projects.

%prep
%setup -q

%build

%add_optflags -DUSE_NON_CONST -D_FILE_OFFSET_BITS=64

env OCAML_NATIVE=true make configure
make 

%install

make install DESTDIR=%buildroot BINDIR=%_bindir LIBDIR=%_libdir/ocaml

# Remove the META file.  It will be replaced by ocaml-ocamlfind (findlib).
rm %buildroot%_libdir/ocaml/ocamlbuild/META

%files
%_bindir/*
%dir %_libdir/ocaml/ocamlbuild
%_libdir/ocaml/ocamlbuild/*
%_man1dir/ocamlbuild*

%changelog
* Thu Feb 16 2017 Anton Farygin <rider@altlinux.ru> 1:0.10.1-alt1%ubt
- updated to 0.10.1

* Sun Jun 19 2016 Andrey Bergman <vkni@altlinux.org> 4.03.0_0.9.2-alt1
- Initial release for Sisyphus.
