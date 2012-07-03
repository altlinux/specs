# SPEC file for cadaver package

Name:    ocaml-make
Version: 6.35.0
Release: alt1

Summary: a general makefile for the Objective Caml programming language

License: %lgpl21only
Group:   Development/ML
URL:     http://www.ocaml.info/home/ocaml_sources.html#ocaml-make

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Source1: README.examples.idl

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

%description
OCamlMakefile is a general makefile which allows a programmer
to create quickly customized makefiles for a project written
in the Objective Caml programming language. Typically, a
customized makefile consists of the definition of a few
variables, and an inclusion of the general makefile provided
by this package.

%package doc
Summary: documentation and examples files for ocaml-make
Group: Development/Documentation
Requires: %name = %version-%release

%description doc
OCamlMakefile is a general makefile which allows a programmer
to create quickly customized makefiles for a project written
in the Objective Caml programming language.

This package contains documentation and examples files for
developing applications that use OCamlMakefile.

%define ocamlmakefile  %_datadir/ocamlmakefile


%prep
%setup

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/LGPL-2.1 %_docdir/%name/LICENSE) LICENSE

install -m 0644 %SOURCE1 ./README.examples.idl

%build
sed -e "s@/usr/local/lib@%_libdir/ocaml@g" -i OCamlMakefile

# examples/
for d in calc camlp4 gtk idl threads; do
  sed -e "s@../OCamlMakefile@%ocamlmakefile/OCamlMakefile@g" -i ./$d/Makefile;
done
cp ./README.examples.idl ./calc/README
cp ./README.examples.idl ./idl/README

%install
# OCamlMakefile
install -d -m 0755 %buildroot%ocamlmakefile
install -m 0644 OCamlMakefile %buildroot%ocamlmakefile/

%files
%doc README.txt Changelog
%doc --no-dereference LICENSE

%dir %ocamlmakefile
%ocamlmakefile/OCamlMakefile

%files doc
%doc calc camlp4 gtk idl threads

%changelog
* Sun Feb 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 6.35.0-alt1
- Initial build for ALT Linux Sisyphus

* Thu Jun 23 2011 Nikolay A. Fetisov <naf@altlinux.ru> 6.30.0-alt0.1
- Initial build

