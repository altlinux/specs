Name: ocaml-camlidl
Version: 1.05
Release: alt1%ubt
Summary: Stub code generator and COM binding for Objective Caml
License: QPL and LGPLv2 with exceptions
Group: Development/ML
Url: http://caml.inria.fr/pub/old_caml_site/camlidl/
# http://opam.ocaml.org/packages/camlidl/camlidl.1.05/
Source0: %name-%version.tar
# META file from Debian
Source1: META.camlidl.in

# Build the compiler into a native code program using ocamlopt.
Patch1: camlidl-1.05-use-ocamlopt-for-compiler.patch

BuildRequires: ocaml
BuildRequires: ocaml-ocamldoc
BuildRequires(pre): rpm-build-ubt

%description
CamlIDL is a stub code generator and COM binding for Objective Caml.

CamlIDL comprises two parts:

* A stub code generator that generates the C stub code required for
  the Caml/C interface, based on an MIDL specification. (MIDL stands
  for Microsoft's Interface Description Language; it looks like C
  header files with some extra annotations, plus a notion of object
  interfaces that look like C++ classes without inheritance.)

* A (currently small) library of functions and tools to import COM
  components in Caml applications, and export Caml code as COM
  components.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%patch1 -p1

sed -e 's|^OCAMLLIB=.*|OCAMLLIB=%_libdir/ocaml|' \
    -e 's|^BINDIR=.*|BINDIR=%_bindir|' \
    < config/Makefile.unix \
    > config/Makefile

cp %SOURCE1 .

%build
make all

%install
mkdir -p %buildroot%_libdir/ocaml/caml
mkdir -p %buildroot%_libdir/ocaml/site-lib
mkdir -p %buildroot%_libdir/ocaml/stublibs
mkdir -p %buildroot%_bindir

sed 's/@VERSION@/%version/' < %SOURCE1 > %buildroot%_libdir/ocaml/site-lib/META.camlidl

make OCAMLLIB=%buildroot%_libdir/ocaml \
     BINDIR=%buildroot%_bindir \
     install

%files
%doc LICENSE
%_libdir/ocaml/*.*
%_libdir/ocaml/site-lib/META.camlidl
%exclude %_libdir/ocaml/*.a
%exclude %_libdir/ocaml/*.cmxa
%_bindir/camlidl

%files devel
%doc LICENSE README Changes tests
%_libdir/ocaml/*.a
%_libdir/ocaml/*.cmxa
%_libdir/ocaml/caml/*.h

%changelog
* Mon Feb 13 2017 Anton Farygin <rider@altlinux.ru> 1.05-alt1%ubt
- first build for ALT
