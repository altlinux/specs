%define srcName ocamlgsl

Name:           ocaml-gsl
Version:        0.6.0
Release:        alt1
Summary:        Interface to GSL (GNU scientific library) for OCaml
Summary(ru_RU.UTF-8): Интерфейс библиотеки GSL для OCaml
License:        GPLv2
Group:          Development/ML
Url:            http://oandrieu.nerim.net/ocaml/gsl/
Packager:	%packager

Source:         ocamlgsl-%{version}.tar.bz2

# Automatically added by buildreq on Sat Dec 18 2010
BuildRequires: libgsl-devel ocaml

%description
This is an interface to GSL (GNU scientific library), for the
Objective Caml language.

%prep
%setup -q -n %srcName-%version

# Поскольку в дистрибутиве ALT есть только ocamlfind-mini, используем его.
sed -i s/ocamlfind/ocamlfind-mini/g Makefile
sed -i s/"DESTDIR ="/"DESTDIR = \$(OCAMLDIR)\/site-lib\/gsl"/g Makefile

%build
%make
strip dllmlgsl.so

%install
%define ocamlsitelib %_libdir/ocaml/site-lib
%define docdir %_docdir/%name-%version
mkdir -p %buildroot/%ocamlsitelib/gsl
mkdir -p %buildroot/%docdir

install -pm644 gsl.*  %buildroot/%ocamlsitelib/gsl
install -pm644 *.a  %buildroot/%ocamlsitelib/gsl
install -pm644 *.cmxa  %buildroot/%ocamlsitelib/gsl
install -pm644 *.cmi  %buildroot/%ocamlsitelib/gsl
install -pm644 *.cmo  %buildroot/%ocamlsitelib/gsl
install -pm644 dllmlgsl.so %buildroot/%ocamlsitelib/gsl

%files
%doc COPYING
%dir %ocamlsitelib/gsl/
%ocamlsitelib/gsl/*.so
%ocamlsitelib/gsl/*.a
%ocamlsitelib/gsl/*.cmxa
%ocamlsitelib/gsl/*.cmi
%ocamlsitelib/gsl/*.cmo
%ocamlsitelib/gsl/*.cma
#%%ocamlsitelib/gsl/*.mli
#%%ocamlsitelib/gsl/*.ml

%changelog
* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.0-alt1
- rebuild with new ocaml

* Fri Dec 17 2010 Andrey Bergman <vkni@altlinux.org> 0.6.0-alt0.1
- Initial release for Sisyphus.

