%set_verify_elf_method textrel=relaxed
Name: ocaml-num
Version: 1.1
Release: alt1%ubt
Summary: Legacy Num library for arbitrary-precision integer and rational arithmetic
Group: Development/ML
License: LGPLv2+ with exceptions

Url: https://github.com/ocaml/num
Source0: %name-%version.tar

# Downstream patch to make DESTDIR installs work.
Patch1: 0001-install-Use-DESTDIR.patch
BuildRequires: ocaml
BuildRequires: ocaml-findlib-devel
BuildRequires(pre): rpm-build-ubt

%description
This library implements arbitrary-precision arithmetic on big integers
and on rationals.

This is a legacy library. It used to be part of the core OCaml
distribution (in otherlibs/num) but is now distributed separately. New
applications that need arbitrary-precision arithmetic should use the
Zarith library (https://github.com/ocaml/Zarith) instead of the Num
library, and older applications that already use Num are encouraged to
switch to Zarith. Zarith delivers much better performance than Num and
has a nicer API.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch1 -p1

%build
%make_build all

%check
make -j1 test

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install

find $OCAMLFIND_DESTDIR -name '*.cmti' -delete

%files
%doc Changelog README.md
%doc LICENSE
%_libdir/ocaml/*.cmi
%_libdir/ocaml/*.cma
%_libdir/ocaml/*.cmxs
%_libdir/ocaml/num
%_libdir/ocaml/num-top
%_libdir/ocaml/stublibs/dll*.so
%exclude %_libdir/ocaml/*.a
%exclude %_libdir/ocaml/*.cmxa
%exclude %_libdir/ocaml/*.cmx
%exclude %_libdir/ocaml/*.mli

%files devel
%doc LICENSE
%_libdir/ocaml/*.a
%_libdir/ocaml/*.cmxa
%_libdir/ocaml/*.cmx
%_libdir/ocaml/*.mli

%changelog
* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 1.1-alt1%ubt
- first build for ALT, based on Mageia spec

