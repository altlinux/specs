%def_with check
Name: ocaml-yojson
%define libname %(sed -e 's/^ocaml-//' <<< %name)
Version: 2.1.1
Release: alt2
Summary: An optimized parsing and printing library for the JSON format
Group: Development/ML
License: BSD-3-Clause
Url: https://github.com/ocaml-community/yojson
VCS: https://github.com/mjambon/yojson.git
Source0: %name-%version.tar
Source44: %name.watch
BuildRequires: ocaml >= 4.14
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-cppo
BuildRequires: dune >= 2.7

%if_with check
BuildRequires: ocaml-alcotest-devel
%endif

%description
Yojson is an optimized parsing and printing library for the JSON
format. It addresses a few shortcomings of json-wheel including 2x
speedup, polymorphic variants and optional syntax for tuples and
variants.

ydump is a pretty-printing command-line program provided with the
yojson package.

The program atdgen can be used to derive OCaml-JSON serializers and
deserializers from type definitions.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
subst '/libraries seq/d' lib/dune

%build
%dune_build -p %libname

%install
%dune_install %libname

%check
%dune_check -p %libname

%files -f ocaml-files.runtime
%doc CODEOWNERS LICENSE.md
%_bindir/ydump

%files devel -f ocaml-files.devel
%doc README.md CHANGES.md examples

%changelog
* Tue Nov 14 2023 Anton Farygin <rider@altlinux.ru> 2.1.1-alt2
- fixed URL and homepage
- updated BuildRequires

* Sat Nov 11 2023 Ildar Mulyukov <ildar@altlinux.ru> 2.1.1-alt1
- new version

* Fri Sep 18 2020 Anton Farygin <rider@altlinux.ru> 1.7.0-alt4
- migrated to rpm-build-ocaml 1.4

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 1.7.0-alt3
- cmxa have been moved to devel package

* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 1.7.0-alt2
- built with dune-2.x

* Thu Mar 14 2019 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.4.1-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.4.1-alt2
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt2
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- first build for ALT, based on RH spec
