%set_verify_elf_method textrel=relaxed
Name: ocaml-camlidl
Version: 1.09
Release: alt2
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
mkdir -p %buildroot%_libdir/ocaml/camlidl
mkdir -p %buildroot%_libdir/ocaml/stublibs
mkdir -p %buildroot%_bindir

sed 's/@VERSION@/%version/' < %SOURCE1 > %buildroot%_libdir/ocaml/camlidl/META

make OCAMLLIB=%buildroot%_libdir/ocaml \
     BINDIR=%buildroot%_bindir \
     install

%files
%doc LICENSE
%_libdir/ocaml/*.*
%_libdir/ocaml/stublibs/dllcamlidl.so
%exclude %_libdir/ocaml/*.a
%exclude %_libdir/ocaml/*.cmxa
%_bindir/camlidl

%files devel
%doc LICENSE README Changes tests
%_libdir/ocaml/camlidl
%_libdir/ocaml/*.a
%_libdir/ocaml/*.cmxa
%_libdir/ocaml/caml/*.h

%changelog
* Mon Dec 14 2020 Anton Farygin <rider@altlinux.ru> 1.09-alt2
- enable relaxed mode for textrel check

* Mon Jun 15 2020 Anton Farygin <rider@altlinux.ru> 1.09-alt1
- 1.09

* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 1.07-alt1
- 1.07

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 1.06-alt1
- 1.06

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.05-alt5
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.05-alt4
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 1.05-alt3
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.05-alt2
- rebuild with ocaml 4.04.2

* Mon Feb 13 2017 Anton Farygin <rider@altlinux.ru> 1.05-alt1
- first build for ALT
