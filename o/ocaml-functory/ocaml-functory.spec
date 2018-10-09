%set_verify_elf_method textrel=relaxed
Name: ocaml-functory
Version: 0.6
Release: alt1
Summary: Distributed computing library for OCAML
License: LGPL2.1
Group: Development/ML
Url: http://erratique.ch/software/functory
# https://github.com/backtracking/functory
Source0: %name-%version.tar
BuildRequires: ocaml ocaml-findlib

%description
Functory is a distributed computing library for Objective Caml which facilitates 
distributed execution of parallelizable  computations in a seamless fashion. 
Further, it is polymorphic, incorporates a robust fault-tolerant mechanism and 
is already being deployed in real-world applications.

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
autoreconf -fisv
%configure
%make_build

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make ocamlfind-install

%files
%doc README.md CHANGES 
%dir %_libdir/ocaml/functory
%_libdir/ocaml/functory/META
%_libdir/ocaml/functory/*.cma
%_libdir/ocaml/functory/*.cmi
%_libdir/ocaml/functory/*.cmo

%files devel
%doc TODO
%_libdir/ocaml/functory/*.a
%_libdir/ocaml/functory/*.cmxa
%_libdir/ocaml/functory/*.cmx
%_libdir/ocaml/functory/*.mli

%changelog
* Tue Oct 09 2018 Anton Farygin <rider@altlinux.ru> 0.6-alt1
- first build for ALT


