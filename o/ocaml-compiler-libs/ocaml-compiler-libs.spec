%set_verify_elf_method textrel=relaxed
%define libname compiler-libs
Name: ocaml-%libname
Version: 0.11.0
Release: alt1
Summary: OCaml compiler libraries repackaged
License: Apache-2.0
Group: Development/ML
Url: https://github.com/janestreet/ocaml-compiler-libs
Source0: %name-%version.tar
BuildRequires: ocaml-findlib-devel dune opam 

%description
This packages exposes the OCaml compiler libraries repackages under the toplevel
names Ocaml_common, Ocaml_bytecomp, ...

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
make

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc README.org
%dir %_libdir/ocaml/%name
%dir %_libdir/ocaml/%name/bytecomp
%dir %_libdir/ocaml/%name/common
%dir %_libdir/ocaml/%name/toplevel
%dir %_libdir/ocaml/%name/shadow
%_libdir/ocaml/%name/META
%_libdir/ocaml/%name/opam
%_libdir/ocaml/%name/*/*.a
%_libdir/ocaml/%name/*/*.cmi
%_libdir/ocaml/%name/*/*.cma

%files devel
%_libdir/ocaml/%name/*/*.ml
%_libdir/ocaml/%name/*/*.cmx
%_libdir/ocaml/%name/*/*.cmt*
%_libdir/ocaml/%name/*/*.cmxa
%_libdir/ocaml/%name/*/*.cmxs
%_libdir/ocaml/%name/*/*.dune

%changelog
* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT


