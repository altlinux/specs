%set_verify_elf_method textrel=relaxed
%define module sqlite3
Name: ocaml-%module
Version: 5.0.2
Release: alt1

Summary: OCaml library for accessing SQLite3 databases
License: MIT
Group: Development/ML
Url: https://mmottl.github.io/sqlite3-ocaml/
# https://github.com/mmottl/sqlite3-ocaml
Source: %name-%version.tar

BuildRequires: libsqlite3-devel ocaml-ocamldoc ocaml-dune-devel opam ocaml-base ocaml-stdio ocaml-configurator
Provides: ocaml4-%module
Obsoletes: ocaml4-%module
Obsoletes: ocaml-%module-runtime < %EVR
BuildPreReq: rpm-build-ocaml >= 1.1.1-alt2

%description
SQLite 3 database library wrapper for OCaml.

%package devel
Summary: Development files for %name 
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -q 
%define docdir %_docdir/%name-%version

%build
make

%install
dune install --destdir=%buildroot

%files
%doc LICENSE.md CHANGES.md README.md TODO.md
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/%module
%exclude %_libdir/ocaml/%module/*.cmx
%exclude %_libdir/ocaml/%module/*.cmt*
%exclude %_libdir/ocaml/%module/*.ml
%exclude %_libdir/ocaml/%module/*.mli
%exclude %_libdir/ocaml/%module/*.cmxa
%exclude %_libdir/ocaml/%module/*.a

%files devel
%_libdir/ocaml/%module/*.cmx
%_libdir/ocaml/%module/*.cmt*
%_libdir/ocaml/%module/*.ml
%_libdir/ocaml/%module/*.mli
%_libdir/ocaml/%module/*.cmxa
%_libdir/ocaml/%module/*.a

%changelog
* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 5.0.2-alt1
- 5.0.2
- added devel package
- runtime package merged to %name

* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 5.0.1-alt1
- 5.0.1

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
