%set_verify_elf_method textrel=relaxed
Name: dune
Version: 1.6.2
Release: alt1
Summary: A composable build system for OCaml
Group: Development/ML
License: ASL 2.0
Url: https://github.com/ocaml/dune
Source0: %name-%version-%release.tar
Provides: jbuilder = %version-%release
Obsoletes: jbuilder

BuildRequires: ocaml >= 4.06.1
BuildRequires: ocaml-findlib-devel
BuildRequires: opam

# Required by tests.
BuildRequires: ocaml-menhir

%description
Dune is a build system designed for OCaml/Reason projects only. It focuses
on providing the user with a consistent experience and takes care of most of
the low-level details of OCaml compilation. All you have to do is provide a
description of your project and Dune will do the rest.

The scheme it implements is inspired from the one used inside Jane Street and
adapted to the open source world. It has matured over a long time and is used
daily by hundred of developers, which means that it is highly tested and
productive.

%prep
%setup -n %name-%version-%release

%build
./configure --libdir=%_libdir/ocaml
%make_build release VERSION=%version-%release

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml --mandir=%buildroot/%_mandir dune.install

%files
%doc README.md CHANGES.md
%_libdir/ocaml/dune
%_bindir/dune
%_bindir/jbuilder
%_man1dir/dune.1*
%_man1dir/dune-help.1*
%_man1dir/dune-printenv.1*
%_man1dir/dune-promote.1*
%_man1dir/dune-build.1*
%_man1dir/dune-clean.1*
%_man1dir/dune-exec.1*
%_man1dir/dune-external-lib-deps.1*
%_man1dir/dune-install.1*
%_man1dir/dune-installed-libraries.1*
%_man1dir/dune-rules.1*
%_man1dir/dune-runtest.1*
%_man1dir/dune-subst.1*
%_man1dir/dune-uninstall.1*
%_man1dir/dune-utop.1*
%_man5dir/dune-config.5*

%changelog
* Fri Dec 28 2018 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Fri Oct 26 2018 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.1.1-alt2
- rebuilt for ocaml-4.07.1

* Sat Aug 11 2018 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 1.0-alt2.beta20
- update to beta20

* Tue Dec 19 2017 Anton Farygin <rider@altlinux.ru> 1.0-alt1.git4570020
- first build for ALT, based on RH spec


