%set_verify_elf_method textrel=relaxed
Name: ocaml-camomile
Version: 1.0.1
Release: alt1
Summary: Unicode library for OCaml
License: LGPLv2+
Group: Development/ML
Url: https://github.com/yoriyuki/Camomile
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.08
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-cppo
BuildRequires: dune opam
Requires: %name-data = %EVR

%description
Camomile is a Unicode library for ocaml. Camomile provides Unicode
character type, UTF-8, UTF-16, UTF-32 strings, conversion to/from
about 200 encodings, collation and locale-sensitive case mappings, and
more.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%package data
Group: Development/ML
Summary: Data files for %name

%description data
The %name-data package contains data files for developing
applications that use %name.

%prep
%setup 

%build
# This avoids a stack overflow in the OCaml > 4.05 compiler on POWER only.
%ifarch ppc64le
ulimit -Hs 65536
ulimit -Ss 65536
%endif
dune build --verbose --profile release

%install
dune install \
         --destdir=%buildroot \
         --libdir=%_libdir/ocaml \
         --verbose \
         --profile release

rm -rf %buildroot/usr/doc

# Install the *.mli files by hand.
cp _build/install/default/lib/camomile/library/*.mli %buildroot%_libdir/ocaml/camomile/

%check
dune runtest --profile release

%files
%doc README.md CHANGES.md LICENSE.md
%_libdir/ocaml/camomile
%exclude %_libdir/ocaml/camomile/*.a
%exclude %_libdir/ocaml/camomile/*.cmxa
%exclude %_libdir/ocaml/camomile/*.cmx
%exclude %_libdir/ocaml/camomile/*.mli

%files devel
%_libdir/ocaml/camomile/*.a
%_libdir/ocaml/camomile/*.cmxa
%_libdir/ocaml/camomile/*.cmx
%_libdir/ocaml/camomile/*.mli

%files data
%_datadir/camomile/

%changelog
* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- first build for ALT, based on spec from RH

