%def_with check
%define oname odoc-parser
Name: ocaml-%oname
Version: 0.9.0
Release: alt1
Summary: Parser for ocaml documentation comments
Group: Development/ML
License: ISC
Url: https://github.com/ocaml-odoc/odoc-parser
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml >= 4.13.0
BuildRequires: dune
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-astring-devel
%if_with check
BuildRequires: ocaml-ppx_expect-devel
BuildRequires: ocaml-sexplib0-devel
%endif

%description
Odoc_parser is a library for parsing the contents of OCaml documentation
comments, formatted using 'odoc' syntax, an extension of the language
understood by ocamldoc.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and
signature files for developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Fri Dec 10 2021 Anton Farygin <rider@altlinux.ru> 0.9.0-alt1
- initial build for ALT
