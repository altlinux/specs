%set_verify_elf_method textrel=relaxed

Name: ocaml-csv
Version: 1.3.1
Release: alt1
Summary: OCaml library for reading and writing CSV files
License: LGPLv2+
Group: Development/ML

Url: https://forge.ocamlcore.org/projects/csv/
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar

BuildRequires: ocaml
BuildRequires: ocamlbuild
BuildRequires: ocamldoc
BuildRequires: findlib
BuildRequires: ocaml-extlib

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
ocaml setup.ml -configure --prefix %prefix --destdir %buildroot
make

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml/site-lib
mkdir -p $OCAMLFIND_DESTDIR

%make_install install

mkdir -p $DESTDIR%_bindir
install -m 0755 csvtool.native $DESTDIR%_bindir/csvtool

%check
make test

%files
%doc LICENSE.txt
%_libdir/ocaml/site-lib/csv
%exclude %_libdir/ocaml/site-lib/csv/*.a
%exclude %_libdir/ocaml/site-lib/csv/*.cmxa
%exclude %_libdir/ocaml/site-lib/csv/*.cmx
%exclude %_libdir/ocaml/site-lib/csv/*.mli
%_bindir/csvtool

%files devel
%doc AUTHORS.txt LICENSE.txt README.txt
%_libdir/ocaml/site-lib/csv/*.a
%_libdir/ocaml/site-lib/csv/*.cmxa
%_libdir/ocaml/site-lib/csv/*.cmx
%_libdir/ocaml/site-lib/csv/*.mli

%changelog
* Wed Nov 30 2016 Lenar Shakirov <snejok@altlinux.ru> 1.3.1-alt1
- Initial build for ALT (2.3-0.19.svn234.fc26.src)

