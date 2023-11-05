%def_enable check
%define libname tyxml
Name:           ocaml-%libname
Version:        4.6.0
Release:        alt1
Summary:        TyXML is a library for building statically correct HTML5 and SVG documents
License:        LGPLv2.1 with OCaml-LGPL-linking-exception
Group:          Development/ML
Url:            https://ocsigen.org/tyxml/
# https://github.com/ocsigen/tyxml
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml >= 4.07.1 dune 
BuildRequires: ocaml-ocamldoc ocaml-uutf-devel ocaml-markup-devel
BuildRequires: ocaml-re-devel 
%if_enabled check
BuildRequires: ocaml-alcotest-devel
%endif
BuildRequires(pre):rpm-build-ocaml

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %EVR

%description
TyXML allows you to build HTML5 and SVG trees whose validity is ensured by the typechecker.
It provides a printer for said XML trees, along with a ppx syntax extension. Finally 
it also provides a functorial interface to choose your XML datastructure. 
It's part of the ocsigen project and is used in js_of_ocaml and eliom.

%description devel
This package includes development files necessary for developing 
programs which use %name

%prep
%setup
%patch0 -p1

%build
%dune_build -p %libname

%check
%dune_check -p %libname

%install
mkdir -p %buildroot%_libdir/ocaml/
%dune_install %libname


%files -f ocaml-files.runtime
%doc LICENSE CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Sat Nov 04 2023 Anton Farygin <rider@altlinux.ru> 4.6.0-alt1
- 4.6.0

* Thu May 13 2021 Anton Farygin <rider@altlinux.ru> 4.5.0-alt1
- 4.5.0

* Sat Mar 20 2021 Anton Farygin <rider@altlinux.org> 4.4.0-alt4
- cleanup BR
- built clean library without addittonal modules
- enabled test

* Thu Dec 10 2020 Anton Farygin <rider@altlinux.ru> 4.4.0-alt3
- BR: devel package for ocaml-ppx_tools_versioned
- building process moved to rpm-build-ocaml 1.4

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 4.4.0-alt2
- devel parts moved to the ocaml-tyxml-devel package

* Tue Jun 30 2020 Anton Farygin <rider@altlinux.ru> 4.4.0-alt1
- 4.4.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 4.3.0-alt3
- fix for build by dune-2

* Thu Aug 08 2019 Anton Farygin <rider@altlinux.ru> 4.3.0-alt2
- rebuilt with ocaml-re 1.9.0

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 4.3.0-alt1
- 4.3.0

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 4.2.0-alt1
- first build for ALT

