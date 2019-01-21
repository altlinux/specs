%set_verify_elf_method textrel=relaxed
%define libname ptime
Name: ocaml-%libname
Version: 0.8.4
Release: alt2
Summary: POSIX time for OCaml
License: ISC
Group: Development/ML
Url: http://erratique.ch/software/ptime
# https://github.com/dbuenzli/ptime
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam
BuildRequires: ocaml-cmdliner-devel ocaml-result-devel ocaml-js_of_ocaml-devel

%package devel
Summary: Development files for programs which will use the BOS library
Group: Development/ML
Requires: %name = %EVR

%description
Ptime has platform independent POSIX time support in pure OCaml. It provides
a type to represent a well-defined range of POSIX timestamps with picosecond
precision, conversion with date-time values, conversion with RFC 3339 timestamps
and pretty printing to a human-readable, locale-independent representation.

The additional Ptime_clock library provides access to a system POSIX clock and
to the system's current time zone offset.

%description devel
This package includes development files necessary for developing
programs which use %name

%prep
%setup

%build
ocaml pkg/pkg.ml build

%install
sed -i 's,%%%%VERSION_NUM%%%%,%version,g' pkg/META
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc LICENSE.md CHANGES.md README.md
%_libdir/ocaml/%libname
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.mli
%_libdir/ocaml/stublibs/*.so

%files devel
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.mli

%changelog
* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 0.8.4-alt2
- rebuilt with js_of_ocaml 3.3.0

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.8.4-alt1
- first build for ALT

