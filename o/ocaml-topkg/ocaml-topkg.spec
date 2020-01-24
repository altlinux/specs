%set_verify_elf_method textrel=relaxed
%define oname   topkg
Name: ocaml-topkg
Version: 1.0.1
Release: alt1
Summary: The transitory OCaml software packager
License: ISC
Group: Development/ML
Url: http://erratique.ch/software/topkg
Source0: %name-%version.tar
BuildRequires: opam
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-ocamlbuild

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
sed -i 's,%%%%VERSION_NUM%%%%,%version,g' pkg/META
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
* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.0.0-alt3
- rebuilt with ocaml-4.08

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2
- fixed the version repesentation for ocaml findlib

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.9.1-alt2
- rebuilt for ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1
- first build for Sisyphus, based on Mageia spec

