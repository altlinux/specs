%set_verify_elf_method textrel=relaxed
Name: ocaml-extlib
Version: 1.7.2
Release: alt3%ubt

Summary: extended standard library for OCaml
License: LGPL v2, with exceptions
Group: Development/ML
Url: http://code.google.com/p/ocaml-extlib/
# https://github.com/ygrek/ocaml-extlib
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

Requires: ocaml-runtime
BuildRequires: rpm-build-ocaml ocaml-ocamldoc ocaml-findlib ocaml-cppo ocaml-camlp4-devel
BuildRequires(pre): rpm-build-ubt

%description
ExtLib is a project aiming at providing a complete - yet small - standard
library for the OCaml programming language.

The purpose of this library is to add new functions to OCaml Standard Library
modules, to modify some functions in order to get better performances or more
safety (tail-recursive) but also to provide new modules which should be useful
for the average OCaml programmer.

ExtLib contains modules implementing: enumeration over abstract collection of
elements, efficient bit sets, dynamic arrays, references on lists, Unicode
characters and UTF-8 encoded strings, additional and improved functions for
hashtables, strings, lists and option types.

%define extlibdir %_libdir/ocaml/extlib

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
pushd src
%patch0 -p1
popd

%build
%make
%make doc

%install
mkdir -p mkdir -p %buildroot%_libdir/ocaml
%makeinstall OCAMLFIND_INSTFLAGS="-destdir %buildroot%_libdir/ocaml/"

%files
%doc README.md LICENSE
%_libdir/ocaml/extlib
%exclude %_libdir/ocaml/extlib/*.a
%exclude %_libdir/ocaml/extlib/*.cmxa
%exclude %_libdir/ocaml/extlib/*.cmx
%exclude %_libdir/ocaml/extlib/*.mli

%files devel
%doc CHANGES
%_libdir/ocaml/extlib/*.a
%_libdir/ocaml/extlib/*.cmxa
%_libdir/ocaml/extlib/*.cmx
%_libdir/ocaml/extlib/*.mli

%changelog
* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.7.2-alt3%ubt
- split to devel and runtime packages

* Sat Apr 15 2017 Anton Farygin <rider@altlinux.ru> 1.7.2-alt2%ubt
- do not use site-lib

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 1.7.2-alt1%ubt
- new version

* Thu Dec 22 2011 Alexey Shabalin <shaba@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Wed Jul 02 2008 Alexander Myltsev <avm@altlinux.ru> 1.5.1-alt2
- Fix build error (buildrequire ocamldoc).

* Mon Jan 21 2008 Alex V. Myltsev <avm@altlinux.ru> 1.5.1-alt1
- New version.
- Use rpm-build-ocaml.

* Mon Jul 09 2007 Alex V. Myltsev <avm@altlinux.ru> 1.5-alt1
- Initial build for Sisyphus.

