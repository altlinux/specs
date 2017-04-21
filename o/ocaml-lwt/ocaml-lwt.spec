# on i586: verify-elf: ERROR: ./usr/lib/ocaml/site-lib/lwt/lwt.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed
Name: ocaml-lwt
Version: 2.5.2
Release: alt2%ubt
Summary: OCaml lightweight thread library

Group: Development/ML
License: LGPLv2+ with exceptions
Url: http://ocsigen.org/lwt/
# https://github.com/ocsigen/lwt
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-ocamldoc termutils ocaml-ssl ocaml-camlp4-devel ocaml-react glib2-devel libev-devel chrpath
BuildRequires(pre): rpm-build-ubt
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
Lwt is a lightweight thread library for Objective Caml.  This library
is part of the Ocsigen project.

%prep
%setup

%build
./configure \
    --enable-ssl \
    --enable-glib \
    --enable-react \
    --enable-camlp4 \
    --prefix=%_prefix

make
pushd _build
# hack for passing the ALT elf checker
/usr/bin/ocamlfind ocamlopt  -linkpkg -package threads -thread -shared src/preemptive/lwt-preemptive.cmxa src/preemptive/lwt_preemptive.cmx -o src/preemptive/lwt-preemptive.cmxs
/usr/bin/ocamlfind ocamlopt -linkpkg -shared -package compiler-libs.optcomp,dynlink src/simple_top/lwt-simple-top.cmxa src/simple_top/lwt_simple_top.cmx -o src/simple_top/lwt-simple-top.cmxs
popd

%install
export OCAMLFIND_LDCONF=ignore
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p %buildroot%_libdir/ocaml/lwt
make install
chrpath -d %buildroot%_libdir/ocaml/lwt/dlllwt-unix_stubs.so

%files
%doc CHANGES README.md
%_libdir/ocaml/lwt

%changelog
* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt2%ubt
- rebuild in new environment

* Mon Apr 10 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt1%ubt
- new version from upstream git

* Wed Dec 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt3
- rebuild with new ocaml

* Mon Sep 08 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.1.0-alt2
- darcs update

* Mon Sep 08 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux

* Mon Sep  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-1
- Initial RPM release.
