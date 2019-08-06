%set_verify_elf_method textrel=relaxed
Name: ocaml-cmdliner
Version: 1.0.4
Release: alt1
Summary: Declarative definition of command line interfaces for OCaml

# In order for this to work as a "global" macro it has to come after the
# definition of Name:, evidently.
%global libname %(echo %name | sed -e 's/^ocaml-//')

License: ISC
Url: https://github.com/dbuenzli/cmdliner/
Source0: %name-%version.tar
Group: Development/ML

BuildRequires: ocaml
BuildRequires: ocaml-findlib-devel
BuildRequires: dune opam
BuildRequires: ocaml-result-devel

%description
Cmdliner allows the declarative definition of command line
interfaces for OCaml.

It provides a simple and compositional mechanism to convert
command line arguments to OCaml values and pass them to your
functions. The module automatically handles syntax errors,
help messages and UNIX man page generation. It supports
programs with single or multiple commands and respects
most of the POSIX and GNU conventions.

Cmdliner has no dependencies and is distributed under
the ISC license.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
sed 's,/lib/,/%_lib/,g' -i Makefile
make build-byte
make build-native
make build-native-dynlink

%install
make install DESTDIR=%buildroot

# Fix some spurious executable perms?
chmod -x %buildroot%_libdir/ocaml/%libname/*.cmx
chmod -x %buildroot%_libdir/ocaml/%libname/*.cmxa
chmod -x %buildroot%_libdir/ocaml/%libname/*.mli
chmod -x %buildroot%_libdir/ocaml/%libname/*.a
chmod -x %buildroot%_libdir/ocaml/%libname/META
chmod -x %buildroot%_libdir/ocaml/%libname/opam

%files
%doc README.md CHANGES.md
%_libdir/ocaml/%libname
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.mli

%files devel
%doc README.md CHANGES.md
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.mli

%changelog
* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt5
- fixed the version repesentation for ocaml findlib

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt4
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt3
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt2
- rebuilt for ocaml 4.06.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- first build for ALT, based on RH spec

