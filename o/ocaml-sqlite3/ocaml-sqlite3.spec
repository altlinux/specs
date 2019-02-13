%set_verify_elf_method textrel=relaxed
%define module sqlite3
Name: ocaml-%module
Version: 4.4.1
Release: alt1

Summary: OCaml library for accessing SQLite3 databases
License: GPL
Group: Development/ML
Url: http://www.ocaml.info/home/ocaml_sources.html
Source: http://www.ocaml.info/ocaml_sources/%name-%version.tar

BuildRequires: ocaml-findlib libsqlite3-devel ocaml-ocamldoc dune opam ocaml-base ocaml-stdio ocaml-configurator
Provides:	ocaml4-%module
Obsoletes:	ocaml4-%module


BuildPreReq: rpm-build-ocaml >= 1.1.1-alt2
%description
SQLite 3 database library wrapper for OCaml.

%package runtime
Summary: OCaml library for accessing SQLite3 databases
Group: Development/ML

%description runtime
Runtime part of OCaml library for accessing SQLite3 databases

%prep
%setup -q 
%define docdir %_docdir/%name-%version

%build
make

%install
mkdir -p %buildroot%_libdir/ocaml
dune install --destdir=%buildroot --libdir=%_libdir/ocaml

%files
%doc LICENSE.md CHANGES.md README.md TODO.md
%_libdir/ocaml/%module

%files runtime
%_libdir/ocaml/stublibs/*.so

%changelog
* Wed Feb 13 2019 Anton Farygin <rider@altlinux.ru> 4.4.1-alt1
- 4.4.1

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 4.4.0-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 4.4.0-alt2
- rebuilt with ocaml-4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 4.1.3-alt1
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 4.1.2-alt3
- rebuild with ocaml 4.04.1

* Wed Mar 29 2017 Anton Farygin <rider@altlinux.ru> 4.1.2-alt2
- updated to new version

* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Sep 17 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.2.0-alt1
- updated to new version

* Thu Mar 06 2008 Veaceslav Grecea <slavutich@altlinux.org> 0.23.0-alt1
- Adapted for ALTLinux

* Fri Feb 29 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-2
- Added BR ocaml-camlp4-devel.

* Sun Feb 24 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-1
- Initial RPM release.
