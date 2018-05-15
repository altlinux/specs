%set_verify_elf_method textrel=relaxed
Name: ocaml-jsonm
Version: 0.9.1
Release: alt1%ubt
Summary: Non-blocking streaming codec to decode and encode JSON
License: BSD3
Group: Development/ML
Url: http://erratique.ch/software/jsonm
Source0: %name-%version.tar
BuildRequires: ocaml-findlib
BuildRequires: ocaml-uutf-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-ocamlbuild
Requires: ocaml-uutf
BuildRequires(pre):rpm-build-ubt

%description
Jsonm is a non-blocking streaming codec to decode and encode the JSON data
format. It can process JSON text without blocking on IO and without a
complete in-memory representation of the data.

The uncut codec also processes whitespace and (non-standard) JSON with
JavaScript comments.

Jsonm is made of a single module and depends on Uutf.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: ocaml-uutf-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
ocaml setup.ml -configure \
    --prefix %prefix \
    --libdir %_libdir \
    --libexecdir %_libexecdir \
    --exec-prefix %_exec_prefix \
    --bindir %_bindir \
    --sbindir %_sbindir \
    --mandir %_mandir \
    --datadir %_datadir \
    --localstatedir %_localstatedir \
    --sharedstatedir %_sharedstatedir \
    --destdir %buildroot

ocaml setup.ml -build

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot/%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR/INSTALL_DIR
ocaml setup.ml -install

%files
%doc README CHANGES
%dir %_libdir/ocaml/jsonm
%_libdir/ocaml/jsonm/META
%_libdir/ocaml/jsonm/*.cma
%_libdir/ocaml/jsonm/*.cmi
%_libdir/ocaml/jsonm/*.cmxs
%_bindir/jsontrip
%_bindir/ocamltweets

%files devel
%doc doc/
%_libdir/ocaml/jsonm/*.a
%_libdir/ocaml/jsonm/*.cmxa
%_libdir/ocaml/jsonm/*.cmx
%_libdir/ocaml/jsonm/*.mli

%changelog
* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1%ubt
- first build for ALT, based on Mageia spec

