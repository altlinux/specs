%set_verify_elf_method textrel=relaxed

Name: ocaml-csv
Version: 2.2
Release: alt1
Summary: OCaml library for reading and writing CSV files
License: LGPLv2+
Group: Development/ML

Url: https://opam.ocaml.org/packages/csv/

Source: %name-%version.tar

BuildRequires: ocaml
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-extlib-devel
BuildRequires: ocaml-lwt-devel
BuildRequires: ocaml-findlib
BuildRequires: opam dune

%description
This OCaml library can read and write CSV files, including all
extensions used by Excel - eg. quotes, newlines, 8 bit characters in
fields, quote-0 etc.

The library comes with a handy command line tool called csvtool for
handling CSV files from shell scripts.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make

%install

mkdir -p %buildroot%prefix %buildroot%_libdir/ocaml
dune install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml


%files
%doc LICENSE.md
%_libdir/ocaml/csv
%_libdir/ocaml/csv-lwt
%exclude %_libdir/ocaml/csv/*.a
%exclude %_libdir/ocaml/csv/*.cmxa
%exclude %_libdir/ocaml/csv/*.cmx
%exclude %_libdir/ocaml/csv/*.mli
%exclude %_libdir/ocaml/csv-lwt/*.a
%exclude %_libdir/ocaml/csv-lwt/*.cmxa
%exclude %_libdir/ocaml/csv-lwt/*.cmx
%exclude %_libdir/ocaml/csv-lwt/*.mli
%_bindir/csvtool

%files devel
%doc README.md LICENSE.md
%_libdir/ocaml/csv/*.a
%_libdir/ocaml/csv/*.cmxa
%_libdir/ocaml/csv/*.cmx
%_libdir/ocaml/csv/*.mli
%_libdir/ocaml/csv-lwt/*.a
%_libdir/ocaml/csv-lwt/*.cmxa
%_libdir/ocaml/csv-lwt/*.cmx
%_libdir/ocaml/csv-lwt/*.mli

%changelog
* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- 2.2

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.1-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 2.1-alt1
- 2.1

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 2.0-alt1
- 2.0

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt2
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- rebuild with ocaml-extlib-devel
- added ubt

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 1.3.3-alt1
- new version

* Wed Nov 30 2016 Lenar Shakirov <snejok@altlinux.ru> 1.3.1-alt1
- Initial build for ALT (2.3-0.19.svn234.fc26.src)

