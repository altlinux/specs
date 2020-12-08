%set_verify_elf_method textrel=relaxed

Name:           ocaml-gsl
Version:        1.24.1
Release:        alt2
Summary:        Interface to GSL (GNU scientific library) for OCaml
Summary(ru_RU.UTF-8): Интерфейс библиотеки GSL для OCaml
License:        GPLv2
Group:          Development/ML
Url:            http://mmottl.github.io/gsl-ocaml/
ExcludeArch: armh

Provides:	ocaml4-gsl
Obsoletes:	ocaml4-gsl

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libgsl-devel ocaml-findlib ocaml-ocamlbuild ocaml-ocamldoc ocaml-dune-devel opam
BuildRequires: ocaml-base-devel ocaml-stdio-devel

%package devel
Summary: Development files for programs which will use the OcamlGSL library
Summary(ru_RU.UTF-8): Заголовочные файлы для программ, использующих библиотеку OcamlGSL
Group: Development/ML
Requires: %name = %EVR

%description
This is an interface to GSL (GNU scientific library), for the
Objective Caml language.

%description devel
This package includes development files necessary for developing 
programs which use interface to GSL (GNU scientific library)

%prep
%setup -q
%patch0 -p1

%build
%make

%install
dune install \
         --destdir=%buildroot \
         --verbose \
         --profile release

%files
%doc LICENSE.md README.md
%dir %_libdir/ocaml/gsl/
%_libdir/ocaml/gsl/*
%exclude %_libdir/ocaml/gsl/*.a
%exclude %_libdir/ocaml/gsl/*.cmxs
%exclude %_libdir/ocaml/gsl/*.cmxa
%exclude %_libdir/ocaml/gsl/*.ml*
%_libdir/ocaml/gsl/libgsl_stubs.a
%_libdir//ocaml/stublibs/*.so*

%files devel
%exclude %_libdir/ocaml/gsl/*.a
%exclude %_libdir/ocaml/gsl/*.cmxs
%exclude %_libdir/ocaml/gsl/*.cmxa
%exclude %_libdir/ocaml/gsl/*.ml*

%changelog
* Thu Dec 24 2020 Anton Farygin <rider@altlinux.ru> 1.24.1-alt2
- exclude the armh architecture

* Tue Feb 04 2020 Anton Farygin <rider@altlinux.ru> 1.24.1-alt1
- 1.24.1

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 1.24.0-alt1
- 1.24.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.19.3-alt6
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.19.3-alt5
- rebuilt with ocaml-4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 1.19.3-alt4
- rebuilt for ocaml-4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.19.3-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.19.3-alt2
- rebuild with ocaml 4.04.1

* Tue Mar 28 2017 Anton Farygin <rider@altlinux.ru> 1.19.3-alt1
- renamed back to ocaml-gsl

* Mon Jun 20 2016 Andrey Bergman <vkni@altlinux.org> 1.19.1-alt2
- Rebuild with ocaml4 4.03.0.

* Fri Nov 27 2015 Andrey Bergman <vkni@altlinux.org> 1.19.1-alt1
- Version update.

* Thu Aug 27 2015 Andrey Bergman <vkni@altlinux.org> 1.18.5-alt1
- Version update. Corrected packaging of *.a files.

* Wed Jun 24 2015 Andrey Bergman <vkni@altlinux.org> 1.18.4-alt1
- Version update. Built with ocaml4.

* Tue Jul 15 2014 Andrey Bergman <vkni@altlinux.org> 1.15.4-alt2
- Added patch for new GSL library support.

* Mon Jul 14 2014 Andrey Bergman <vkni@altlinux.org> 1.15.4-alt1
- Version update.

* Mon Jul 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.1
- Rebuilt with gsl90 instead of gsl

* Tue Oct 15 2013 Andrey Bergman <vkni@altlinux.org> 1.13.0-alt1
- Version update.

* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- rebuild with new ocaml

* Fri Dec 17 2010 Andrey Bergman <vkni@altlinux.org> 0.6.0-alt0.1
- Initial release for Sisyphus.
