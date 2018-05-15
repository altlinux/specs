# on i586: verify-elf: ERROR: ./usr/lib/ocaml/site-lib/lwt/lwt.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed
Name: ocaml-lwt
Version: 4.0.1
Release: alt1%ubt
Summary: OCaml lightweight thread library

Group: Development/ML
License: LGPLv2+ with exceptions
Url: http://ocsigen.org/lwt/
# https://github.com/ocsigen/lwt
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamldoc termutils ocaml-ssl ocaml-camlp4-devel ocaml-react glib2-devel libev-devel chrpath
BuildRequires: jbuilder opam ocaml-cppo
BuildRequires: ocaml-migrate-parsetree ocaml-ppx_tools_versioned-devel ocaml-result-devel
BuildRequires(pre): rpm-build-ubt
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
Lwt is a lightweight thread library for Objective Caml.  This library
is part of the Ocsigen project.

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
make default-config
make

%install
mkdir -p %buildroot%_libdir/ocaml/
jbuilder install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc CHANGES README.md
%dir %_libdir/ocaml/lwt
%dir %_libdir/ocaml/lwt/unix
%dir %_libdir/ocaml/lwt_ppx
%dir %_libdir/ocaml/lwt_react
%_libdir/ocaml/lwt*/META
%_libdir/ocaml/lwt*/*.cma
%_libdir/ocaml/lwt*/*.cmi
%_libdir/ocaml/lwt*/*.cmxs
%_libdir/ocaml/lwt/unix/*.cma
%_libdir/ocaml/lwt/unix/*.cmi
%_libdir/ocaml/lwt/unix/*.cmxs
%_libdir/ocaml/stublibs/*.so*

%files devel
%_libdir/ocaml/lwt*/*.a
%_libdir/ocaml/lwt*/*.cmt*
%_libdir/ocaml/lwt*/*.cmxa
%_libdir/ocaml/lwt*/*.cmx
%_libdir/ocaml/lwt*/*.mli
%_libdir/ocaml/lwt/unix/*.a
%_libdir/ocaml/lwt/unix/*.cmt*
%_libdir/ocaml/lwt/unix/*.cmxa
%_libdir/ocaml/lwt/unix/*.cmx
%_libdir/ocaml/lwt/unix/*.mli

%changelog
* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 4.0.1-alt1%ubt
- 4.0.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt4%ubt
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt3%ubt
- rebuild with ocaml 4.04.1

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
