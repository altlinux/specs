%define libname ptime
Name: ocaml-%libname
Version: 1.1.0
Release: alt1
Summary: POSIX time for OCaml
License: ISC
Group: Development/ML
Url: http://erratique.ch/software/ptime
VCS:https://github.com/dbuenzli/ptime
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild-devel ocaml-topkg-devel ocaml >= 4.07.1 opam
BuildRequires: ocaml-compiler-libs

%package devel
Summary: Development files for programs which will use the BOS library
Group: Development/ML
Requires: %name = %EVR

%description
Ptime has platform independent POSIX time support in pure OCaml. It provides
a type to represent a well-defined range of POSIX timestamps with picosecond
precision, conversion with date-time values, conversion with RFC 3339 timestamps
and pretty printing to a human-readable, locale-independent representation.

The additional Ptime_clock library provides access to a system POSIX clock and
to the system's current time zone offset.

%description devel
This package includes development files necessary for developing
programs which use %name

%prep
%setup

%build
ocaml pkg/pkg.ml build --dev-pkg false --tests true

%install
sed -i 's,%%%%VERSION_NUM%%%%,%version,g' pkg/META
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%ocaml_find_files

%check
ocaml pkg/pkg.ml test

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.8.5-alt2
- move devel parts to the ocaml-ptime-devel package

* Sat May 11 2019 Anton Farygin <rider@altlinux.ru> 0.8.5-alt1
- 0.8.5

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 0.8.4-alt3
- rebuilt with js_of_ocaml

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 0.8.4-alt2
- rebuilt with js_of_ocaml 3.3.0

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.8.4-alt1
- first build for ALT

