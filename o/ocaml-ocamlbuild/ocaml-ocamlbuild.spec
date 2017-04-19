%define pkgname ocamlbuild
Name: ocaml-%pkgname
Version: 0.11.0
Release: alt1%ubt
Epoch: 1

Summary: The Objective Caml project compilation tool
License: Distributable
Group: Development/ML
Url: https://github.com/ocaml/ocamlbuild

Source: %name-%version.tar

BuildRequires: ocaml >= 4.04
BuildRequires(pre):rpm-build-ubt

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides ocamlbuild, a tool automating the compilation
of OCaml projects.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
This package contains development files for %name.

%prep
%setup

%build
%add_optflags -DUSE_NON_CONST -D_FILE_OFFSET_BITS=64

env OCAML_NATIVE=true make configure
make

%install
make install DESTDIR=%buildroot BINDIR=%_bindir LIBDIR=%_libdir/ocaml

# Remove the META file.  It will be replaced by ocaml-ocamlfind (findlib).
rm %buildroot%_libdir/ocaml/%pkgname/META

%files
%doc Changes Readme.md LICENSE
%_bindir/ocamlbuild
%_bindir/ocamlbuild.byte
%_bindir/ocamlbuild.native
%_mandir/man1/ocamlbuild.1*
%_libdir/ocaml/ocamlbuild
%exclude %_libdir/ocaml/ocamlbuild/*.a
%exclude %_libdir/ocaml/ocamlbuild/*.o
%exclude %_libdir/ocaml/ocamlbuild/*.cmx
%exclude %_libdir/ocaml/ocamlbuild/*.cmxa
%exclude %_libdir/ocaml/ocamlbuild/*.mli

%files devel
%doc LICENSE
%_libdir/ocaml/ocamlbuild/*.a
%_libdir/ocaml/ocamlbuild/*.o
%_libdir/ocaml/ocamlbuild/*.cmx
%_libdir/ocaml/ocamlbuild/*.cmxa
%_libdir/ocaml/ocamlbuild/*.mli

%changelog
* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 1:0.11.0-alt1%ubt
- updated to 0.11.0
- split to runtime and devel packages

* Thu Feb 16 2017 Anton Farygin <rider@altlinux.ru> 1:0.10.1-alt1%ubt
- updated to 0.10.1

* Sun Jun 19 2016 Andrey Bergman <vkni@altlinux.org> 4.03.0_0.9.2-alt1
- Initial release for Sisyphus.
