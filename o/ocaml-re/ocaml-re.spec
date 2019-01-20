%set_verify_elf_method textrel=relaxed
Name: ocaml-re
Version: 1.8.0
Release: alt5
Summary: A regular expression library for OCaml

License: LGPLv2 with exceptions
Url: https://github.com/ocaml/ocaml-re
Source0: ocaml-re-%version.tar
Patch0: %name-%version-alt.patch
Group: Development/ML
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: dune

%description
A pure OCaml regular expression library. Supports Perl-style regular
expressions, Posix extended regular expressions, Emacs-style regular
expressions, and shell-style file globbing.  It is also possible to
build regular expressions by combining simpler regular expressions.
There is also a subset of the PCRE interface available in the Re.pcre
library.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
make 

%install
dune install --destdir %buildroot --libdir=%_libdir/ocaml

%files
%doc CHANGES.md README.md
%_libdir/ocaml/re
%exclude %_libdir/ocaml/re/*.a
%exclude %_libdir/ocaml/re/*.cmxa
%exclude %_libdir/ocaml/re/*.cmx
%exclude %_libdir/ocaml/re/*.mli
%exclude %_libdir/ocaml/re/*/*.a
%exclude %_libdir/ocaml/re/*/*.cmxa
%exclude %_libdir/ocaml/re/*/*.cmx

%files devel
%_libdir/ocaml/re/*.a
%_libdir/ocaml/re/*.cmx
%_libdir/ocaml/re/*.cmxa
%_libdir/ocaml/re/*.mli
%_libdir/ocaml/re/*/*.a
%_libdir/ocaml/re/*/*.cmx
%_libdir/ocaml/re/*/*.cmxa

%changelog
* Sun Jan 20 2019 Anton Farygin <rider@altlinux.ru> 1.8.0-alt5
- fixed built with dune-1.6.4

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt4
- fixed install section with dune-1.4.0

* Fri Oct 26 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt3
- all development stuff were moved to the devel package

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt2
- rebuilt with ocaml-4.07.1

* Sat Aug 11 2018 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 1.7.1-alt2
- rebuilt for ocaml 4.06.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.7.1-alt1
- first build for ALT, based on RH spec

