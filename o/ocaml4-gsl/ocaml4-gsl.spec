%define srcName ocaml4-gsl
%set_verify_elf_method textrel=relaxed

Name:           ocaml4-gsl
Version:        1.19.1
Release:        alt2
Summary:        Interface to GSL (GNU scientific library) for OCaml
Summary(ru_RU.UTF-8): Интерфейс библиотеки GSL для OCaml
License:        GPLv2
Group:          Development/ML
Url:            https://bitbucket.org/mmottl/gsl-ocaml
Packager:	%packager

Provides:	ocaml-gsl
Obsoletes:	ocaml-gsl

Source:         ocaml4-gsl-%{version}.tar.bz2
Patch:          ocaml4-gsl-1.18.4-alt-compilation_fix.patch

# Automatically added by buildreq on Wed Jun 24 2015
BuildRequires: libgsl-devel ocaml4-camlp4 ocaml4-findlib ocaml4-ocamlbuild ocaml4-ocamldoc

%package devel
Summary: Development files for programs which will use the OcamlGSL library
Summary(ru_RU.UTF-8): Заголовочные файлы для программ, использующих библиотеку OcamlGSL
Group: Development/ML
Requires: %name = %version-%release
Provides:	ocaml-gsl-devel
Obsoletes:	ocaml-gsl-devel
Conflicts:	ocaml-gsl-devel

%description
This is an interface to GSL (GNU scientific library), for the
Objective Caml language.

%description devel
This package includes development files necessary for developing 
programs which use interface to GSL (GNU scientific library)

%prep
%setup -q -n %srcName-%version

%patch -p1

# Поскольку в дистрибутиве ALT есть только ocamlfind-mini, используем его.
sed -i s/ocamlfind/ocamlfind-mini/g Makefile

%build
%make

strip _build/lib/dllgsl_stubs.so

%install
%define ocamlsitelib %_libdir/ocaml/site-lib
%define ocamlstublib %_libdir/ocaml/stublibs/
%define docdir %_docdir/%name-%version
export OCAMLFIND_DESTDIR=%buildroot%ocamlsitelib/
export DESTDIR=%buildroot
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs

%makeinstall

rm -f %buildroot%ocamlsitelib/gsl/*.annot
rm -f %buildroot%ocamlsitelib/gsl/*.cmx
rm -f %buildroot%ocamlsitelib/gsl/*.cmt
rm -f %buildroot%ocamlsitelib/gsl/*.cmti
rm -f %buildroot%ocamlsitelib/gsl/*.ml
rm -f %buildroot%ocamlsitelib/gsl/*.mli

mkdir -p %buildroot%ocamlstublib/
mv $OCAMLFIND_DESTDIR/stublibs/* %buildroot%ocamlstublib/

mkdir -p %buildroot/%docdir

%files
%doc COPYING.txt
%ocamlstublib/*.so
%ocamlstublib/*.so.owner
%dir %ocamlsitelib/gsl/
%ocamlsitelib/gsl/gsl.cma
%ocamlsitelib/gsl/gsl.cmxs
%ocamlsitelib/gsl/libgsl_stubs.a

%files devel
%ocamlsitelib/gsl/gsl.a
%ocamlsitelib/gsl/*.cmxa
%ocamlsitelib/gsl/*.cmi
%ocamlsitelib/gsl/META

%changelog
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

* Tue Oct 15 2013 Andrey Bergman <vkni@altlinux.org> 1.13.0-alt1
- Version update.

* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- rebuild with new ocaml

* Fri Dec 17 2010 Andrey Bergman <vkni@altlinux.org> 0.6.0-alt0.1
- Initial release for Sisyphus.

