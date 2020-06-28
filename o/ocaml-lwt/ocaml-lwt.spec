# on i586: verify-elf: ERROR: ./usr/lib/ocaml/site-lib/lwt/lwt.cmxs: TEXTREL entry found: 0x00000000
%set_verify_elf_method textrel=relaxed
Name: ocaml-lwt
Version: 5.3.0
Release: alt1
Summary: OCaml lightweight thread library

Group: Development/ML
License: MIT
Url: http://ocsigen.org/lwt/
# https://github.com/ocsigen/lwt
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: ocaml-findlib ocaml-ocamldoc termutils ocaml-ssl ocaml-react glib2-devel libev-devel chrpath
BuildRequires: dune ocaml-cppo ocaml-bisect_ppx-devel ocaml-ocplib-endian-devel
BuildRequires: ocaml-migrate-parsetree-devel ocaml-ppx_tools_versioned-devel ocaml-result-devel
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
%patch0 -p1

%build
dune build

%install
dune install --destdir=%buildroot

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
%_libdir/ocaml/stublibs/*.so

%files devel
%_libdir/ocaml/lwt*/dune-package
%_libdir/ocaml/lwt*/opam
%_libdir/ocaml/lwt*/*.a
%_libdir/ocaml/lwt*/*.cmt*
%_libdir/ocaml/lwt*/*.cmxa
%_libdir/ocaml/lwt*/*.cmx
%_libdir/ocaml/lwt*/*.mli
%_libdir/ocaml/lwt*/*.ml
%_libdir/ocaml/lwt*/*.exe
%_libdir/ocaml/lwt/unix/*.a
%_libdir/ocaml/lwt/unix/*.cmt*
%_libdir/ocaml/lwt/unix/*.cmxa
%_libdir/ocaml/lwt/unix/*.cmx
%_libdir/ocaml/lwt/unix/*.mli
%_libdir/ocaml/lwt/unix/*.ml
%_libdir/ocaml/lwt/unix/*.h

%changelog
* Sun Jun 28 2020 Anton Farygin <rider@altlinux.ru> 5.3.0-alt1
- 5.3.0

* Wed Feb 12 2020 Anton Farygin <rider@altlinux.ru> 5.1.1-alt1
- 5.1.1
- fixed License tag

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 4.2.1-alt1
- 4.2.1

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 4.1.0-alt4
- rebuilt with dune-1.8

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 4.1.0-alt3
- rebuilt with ocaml-migrate-parsetree 1.2.0-alt1

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 4.1.0-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 4.1.0-alt1
- 4.1.0

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 4.0.1-alt1
- 4.0.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt3
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt2
- rebuild in new environment

* Mon Apr 10 2017 Anton Farygin <rider@altlinux.ru> 2.5.2-alt1
- new version from upstream git

* Wed Dec 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt3
- rebuild with new ocaml

* Mon Sep 08 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.1.0-alt2
- darcs update

* Mon Sep 08 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux

* Mon Sep  1 2008 Richard W.M. Jones <rjones@redhat.com> - 1.1.0-1
- Initial RPM release.
