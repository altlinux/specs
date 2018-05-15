%set_verify_elf_method textrel=relaxed
%define oname   topkg
Name: ocaml-topkg
Version: 0.9.1
Release: alt1%ubt
Summary: The transitory OCaml software packager
License: ISC
Group: Development/ML
Url: http://erratique.ch/software/topkg
Source0: %name-%version.tar
BuildRequires: opam
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-ocamlbuild
BuildRequires(pre):rpm-build-ubt

%description
Topkg is a packager for distributing OCaml software. It provides
an API to describe the files a package installs in a given build
configuration and to specify information about the package's
distribution, creation and publication procedures.

The optional topkg-care package provides the topkg command line
tool which helps with various aspects of a package's life cycle:
creating and linting a distribution, releasing it on the WWW,
publish its documentation, add it to the OCaml opam repository,
etc.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
ocaml pkg/pkg.ml "build"

%install
opam-installer \
	--prefix=%buildroot%prefix \
	--libdir=%buildroot%_libdir/ocaml \
	%oname.install

# remove bogus path of docs
rm -rf %buildroot%prefix/doc/%oname

%files
%doc README.md CHANGES.md LICENSE.md
%dir %_libdir/ocaml/topkg
%_libdir/ocaml/topkg/META
%_libdir/ocaml/topkg/opam
%_libdir/ocaml/topkg/*.cmi
%_libdir/ocaml/topkg/*.cma
%_libdir/ocaml/topkg/*.cmxs

%files devel
%doc doc/ test/
%_libdir/ocaml/topkg/*.a
%_libdir/ocaml/topkg/*.cmx
%_libdir/ocaml/topkg/*.cmxa
%_libdir/ocaml/topkg/*.mli
%_libdir/ocaml/topkg/*.cmti

%changelog
* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1%ubt
- first build for Sisyphus, based on Mageia spec

