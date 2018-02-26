%define srcName lacaml

Name:           ocaml-lacaml
Version:        5.5.2
Release:        alt1
Summary:        BLAS/LAPACK-interface for OCaml
Summary(ru_RU.UTF-8): Интерфейс библиотек BLAS/LAPACK для OCaml
License:        LGPLv2 with exceptions
Group:          Development/ML
Url:            http://ocaml.info/home/ocaml_sources.html#lacaml
Packager:	Andrey Bergman <vkni@altlinux.org>

Source:         lacaml-%{version}.tar.bz2
Patch: ocaml-lacaml-alt-gotoblas2.patch

BuildRequires: liblapack-devel ocaml ocamlfind-mini

%description
This OCaml-library interfaces the BLAS-library (Basic Linear Algebra
Subroutines) and LAPACK-library (Linear Algebra routines), which are
written in FORTRAN.

This allows people to write high-performance numerical code for
applications that need linear algebra.

%description -l ru_RU.UTF-8
Это библиотека-интерфейс к библиотекам BLAS (Basic Linear Algebra
Subroutines) и LAPACK (Linear Algebra routines), написанным
на Фортране.

%prep
%setup -q -n %srcName-%version
%patch0 -p2

# Поскольку в дистрибутиве ALT есть только ocamlfind-mini, используем его.
sed -i s/ocamlfind/ocamlfind-mini/g OCamlMakefile

%build
make
make examples

strip lib/dlllacaml_stubs.so

%install
%define ocamlsitelib %_libdir/ocaml/site-lib
%define docdir %_docdir/%name-%version
mkdir -p %buildroot/%ocamlsitelib
mkdir -p %buildroot/%docdir
%make_install OCAMLFIND_INSTFLAGS="-destdir %buildroot/%ocamlsitelib" install

install -pm644 LICENSE %buildroot%docdir/
install -pm644 COPYRIGHT %buildroot%docdir/
install -pm644 README.txt %buildroot%docdir/
install -pm644 Changelog %buildroot%docdir/
install -pm644 TODO %buildroot%docdir/

%files
%dir %docdir
%dir %ocamlsitelib/lacaml
%docdir/*

%ocamlsitelib/lacaml/
%ocamlsitelib/lacaml/*.a
%ocamlsitelib/lacaml/*.cmxa
%ocamlsitelib/lacaml/*.mli
%ocamlsitelib/lacaml/*.ml

%changelog
* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 5.5.2-alt1
- 5.5.2

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.8-alt0.4
- Built with GotoBLAS2 instead of ATLAS

* Fri Dec 24 2010 Andrey Bergman <vkni@altlinux.org> 5.4.8-alt0.3
- Devel package merged into main package.

* Mon Dec 13 2010 Andrey Bergman <vkni@altlinux.org> 5.4.8-alt0.2
- Corrected Group.

* Mon Dec 13 2010 Andrey Bergman <vkni@altlinux.org> 5.4.8-alt0.1
- Initial build for Sisyphus.

