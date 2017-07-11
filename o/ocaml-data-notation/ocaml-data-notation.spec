%set_verify_elf_method textrel=relaxed
Name: ocaml-data-notation
Version: 0.0.11
Release: alt2%ubt
Summary: Store data using OCaml notation
License: LGPL-2.1 with OCaml linking exception
Group: Development/ML
Url: http://forge.ocamlcore.org/projects/odn
# https://github.com/gildor478/ocaml-data-notation
Source0: %name-%version.tar
BuildRequires: ocaml-ocamlbuild ocaml-findlib ocaml-type-conv  ocaml-ounit ocaml-fileutils ocaml-camlp4-devel
BuildRequires(pre): rpm-build-ubt

%description
This project uses type-conv to dump OCaml data structure using OCaml data
notation. This kind of data dumping helps to write OCaml code generator,
like OASIS.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

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
  # --enable-tests

make

%check
#make test

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot/%ocamldir
mkdir -p $OCAMLFIND_DESTDIR/odn
make install

%files
%doc README.txt COPYING.txt AUTHORS.txt CHANGES.txt INSTALL.txt
%dir %ocamldir/odn
%ocamldir/odn/META
%ocamldir/odn/*.cma
%ocamldir/odn/*.cmi
%ocamldir/odn/*.cmxs
%ocamldir/odn/*.ml

%files devel
%ocamldir/odn/*.a
%ocamldir/odn/*.cmxa
%ocamldir/odn/*.cmx

%changelog
* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.0.11-alt2%ubt
- rebuild with ocaml 4.04.2

* Wed May 17 2017 Anton Farygin <rider@altlinux.ru> 0.0.11-alt1%ubt
- first build for ALT
