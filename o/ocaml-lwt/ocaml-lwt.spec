%define lwt_modules lwt,lwt_ppx,lwt_react
Name: ocaml-lwt
Version: 5.7.0
Release: alt3
Summary: OCaml lightweight thread library

Group: Development/ML
License: MIT
Url: http://ocsigen.org/lwt/
# https://github.com/ocsigen/lwt
Source: %name-%version.tar

BuildRequires:  ocaml-ocamldoc termutils ocaml-ssl ocaml-react-devel glib2-devel libev-devel chrpath
BuildRequires: dune ocaml-cppo ocaml-bisect_ppx-devel ocaml-ppxlib-devel ocaml-ocplib-endian-devel
BuildRequires: ocaml-migrate-parsetree-devel ocaml-result-devel
BuildRequires: ocaml-dune-configurator-devel ocaml-luv-devel
BuildRequires(pre): rpm-build-ocaml >= 1.6

%description
Lwt is a lightweight thread library for Objective Caml.  This library
is part of the Ocsigen project.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: ocaml-ocplib-endian-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %lwt_modules

%install
%dune_install `echo "%lwt_modules"|tr ',' ' '`

%check
%dune_check -p %lwt_modules

%files -f ocaml-files.runtime
%doc CHANGES README.md

%files devel -f ocaml-files.devel
%_libdir/ocaml/lwt/unix/*.h

%changelog
* Fri Nov 17 2023 Anton Farygin <rider@altlinux.ru> 5.7.0-alt3
- fixed build with bytecode-only ocaml

* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 5.7.0-alt2
- fixed BuildRequires
- removed unused ALT patch

* Fri Nov 03 2023 Anton Farygin <rider@altlinux.ru> 5.7.0-alt1
- 5.5.0 -> 5.7.0

* Mon Jan 03 2022 Anton Farygin <rider@altlinux.ru> 5.5.0-alt1
- 5.4.2 -> 5.5.0

* Mon Aug 16 2021 Anton Farygin <rider@altlinux.ru> 5.4.2-alt1
- 5.4.2

* Mon Aug 02 2021 Anton Farygin <rider@altlinux.ru> 5.4.1-alt1
- 5.4.1

* Sat Mar 20 2021 Anton Farygin <rider@altlinux.org> 5.4.0-alt2
- spec BR: removed ocaml-ppx_tools_versioned-devel

* Thu Mar 11 2021 Anton Farygin <rider@altlinux.org> 5.4.0-alt1
- 5.4.0 

* Thu Dec 10 2020 Anton Farygin <rider@altlinux.ru> 5.3.0-alt3
- build process mirgrated to rpm-build-ocaml 1.4

* Wed Jul 01 2020 Anton Farygin <rider@altlinux.ru> 5.3.0-alt2
- added ocaml-ocplib-endian-devel requires to devel package

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
