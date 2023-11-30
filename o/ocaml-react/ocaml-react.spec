%global pkgname react
%define ocamlsitelib %_libdir/ocaml
%define pkgsitelib %ocamlsitelib/%pkgname
%define ocamlstublib %_libdir/ocaml/stublibs/

Name: ocaml-%pkgname
Version: 1.2.2
Release: alt2
Summary: OCaml module for Functional Reactive Programming (FRP)
License: BSD
Group: Development/ML
Url: https://erratique.ch/software/react
VCS: https://github.com/dbuenzli/react
Source: %name-%version.tar
BuildPreReq: rpm-build-ocaml >= 1.6
BuildRequires: ocaml ocaml-ocamlbuild ocaml-findlib opam ocaml-topkg

%description
React is an OCaml module for functional reactive programming (FRP).
It provides support to program with time varying values : applicative
events and signals. React doesn't define any primitive event or signal,
this lets the client chooses the concrete timeline.

React is made of a single, independent, module and distributed under
the new BSD license.

Given an absolute notion of time Rtime helps you to manage a timeline
and provides time stamp events, delayed events and delayed signals.

%package devel
Summary: OCaml module for Functional Reactive Programming (FRP)
Group: Development/ML
Requires: %name = %EVR
%description devel
React is an OCaml module for functional reactive programming (FRP).
It provides support to program with time varying values : applicative
events and signals. React doesn't define any primitive event or signal,
this lets the client chooses the concrete timeline.

React is made of a single, independent, module and distributed under
the new BSD license.

Given an absolute notion of time Rtime helps you to manage a timeline
and provides time stamp events, delayed events and delayed signals.

%prep
%setup 

%build
sed -i 's,%%%%VERSION_NUM%%%%,%version,g' pkg/META
ocaml pkg/pkg.ml build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%ocaml_find_files

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Thu Nov 16 2023 Anton Farygin <rider@altlinux.ru> 1.2.2-alt2
- added support for bytecode-only version of the ocaml package

* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.2.1-alt4
- rebuilt with ocaml-4.08

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 1.2.1-alt3
- fixed the version repesentation for ocaml findlib
- installation method changed to opam-installer

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.2.1-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.2.0-alt4
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt2
- rebuild with ocaml 4.04.1

* Tue Apr 11 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- new version

* Tue Dec 27 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux Sisyphus
