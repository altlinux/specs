%set_verify_elf_method textrel=relaxed
%define libname qtest
Name: ocaml-%libname
Version: 2.11
Release: alt1
Summary: Inline (Unit) Tests for OCaml
License: GPLv3
Group: Development/ML
Url: https://github.com/c-cube/ocaml-containers/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: ocaml-findlib-devel dune opam  ocaml-result-devel
BuildRequires: ocaml-qcheck-devel ocaml-ounit-devel ocaml-odoc 

%description
qtest extracts inline unit tests written using a special syntax in comments.
Those tests are then run using the oUnit framework and the qcheck library. The
possibilities range from trivial tests -- extremely simple to use -- to
sophisticated random generation of test cases.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
sed -i 's/oUnit/ounit2/' src/dune
make

%install
dune install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc README.adoc HOWTO.adoc
%dir %_libdir/ocaml/%libname
%_bindir/qtest
%_libdir/ocaml/%libname/*
%exclude %_libdir/ocaml/%libname/*/*.cmx
%exclude %_libdir/ocaml/%libname/*/*.cmt*
%exclude %_libdir/ocaml/%libname/*/*.ml
%exclude %_libdir/ocaml/%libname/*/*.a
%exclude %_libdir/ocaml/%libname/*/*.cmxa
%exclude %_libdir/ocaml/%libname/*/*.cmxs


%files devel
%_libdir/ocaml/%libname/*/*.cmx
%_libdir/ocaml/%libname/*/*.cmt*
%_libdir/ocaml/%libname/*/*.ml
%_libdir/ocaml/%libname/*/*.a
%_libdir/ocaml/%libname/*/*.cmxa
%_libdir/ocaml/%libname/*/*.cmxs

%changelog
* Tue Jun 16 2020 Anton Farygin <rider@altlinux.ru> 2.11-alt1
- 2.11

* Fri Feb 21 2020 Anton Farygin <rider@altlinux.ru> 2.10.1-alt3
- oUnit to ounit2 replace has been moved to specfile

* Mon Feb 17 2020 Anton Farygin <rider@altlinux.ru> 2.10.1-alt2
- update build requires for new ounit2 and qcheck packages

* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 2.9-alt1
- first build for ALT


