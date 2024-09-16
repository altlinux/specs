Name: ocaml-ocamlfuse
Version: 2.7.1
Release: alt13.cvs11
Summary: Ocaml FUSE binding
Group: Development/ML
License: GPL-2.0
Url: https://opam.ocaml.org/packages/ocamlfuse/
# https://github.com/astrada/ocamlfuse
Source: %name-%version.tar
BuildRequires: libfuse-devel
BuildRequires: ocaml ocaml-camlidl-devel ocaml-ocamldoc ocaml-findlib
BuildRequires: ocaml-dune-configurator-devel ocaml-dune-private-libs-devel
Provides: ocaml-fuse = %EVR
Obsoletes: ocaml-fuse < %EVR

%description
This is a binding to fuse for the ocaml programming language, enabling
you to write multithreaded filesystems in the ocaml language. It has
been designed with simplicity as a goal, as you can see by looking at
example/fusexmp.ml. Efficiency has also been a separate goal. The
Bigarray library is used for read and writes, allowing the library to
do zero-copy in ocaml land.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Obsoletes: ocaml-fuse-devel < %EVR
Provides: ocaml-fuse-devel = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p ocamlfuse

%install
%dune_install ocamlfuse

%files -f ocaml-files.runtime
%doc LICENSE README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 10 2024 Anton Farygin <rider@altlinux.ru> 2.7.1-alt13.cvs11
- updated to v2.7.1_cvs11

* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 2.7.1-alt12
- updated to v2.7.1_cvs8

* Wed Mar 17 2021 Anton Farygin <rider@altlinux.org> 2.7.1-alt11
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel
- simplified specfile with macros from rpm-build-ocaml 1.4

* Mon Jun 15 2020 Anton Farygin <rider@altlinux.ru> 2.7.1-alt10
- added fix to building using dune-2.6

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 2.7.1-alt9
- build with dune-2

* Sat Apr 06 2019 Anton Farygin <rider@altlinux.ru> 2.7.1-alt8
- renamed to ocaml-ocamlfuse
- build from upstream git with dune

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.7.1-alt7
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 2.7.1-alt6
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 2.7.1-alt5
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt3
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt2
- split to devel and runtime

* Mon Feb 13 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1
- first build for ALT, version 2.7.1.cvs4
