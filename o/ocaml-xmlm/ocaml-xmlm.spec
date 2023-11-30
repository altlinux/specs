Name: ocaml-xmlm
%global libname %(sed -e 's/^ocaml-//' <<< %name)
Group: Development/ML
Version: 1.4.0
Release: alt1
Summary: A streaming XML codec
License: BSD
Url: http://erratique.ch/software/xmlm
VCS: https://github.com/dbuenzli/xmlm
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.06
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-topkg
BuildRequires: opam
BuildRequires: rpm-build-ocaml >= 1.6

%description
Xmlm is an OCaml streaming codec to decode and encode the XML data
format. It can process XML documents without a complete in-memory
representation of the data.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
sed -i 's,%%%%VERSION_NUM%%%%,%version,g' pkg/META
ocaml ./pkg/pkg.ml build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%ocaml_find_files

%files -f ocaml-files.runtime
%doc README.md LICENSE.md
%_bindir/xmltrip

%files devel -f ocaml-files.devel
%doc CHANGES.md _build/test/examples.ml _build/test/xhtml.ml doc

%changelog
* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 1.3.0-alt5
- rebuilt with ocaml-4.08

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 1.3.0-alt4
- fixed the version repesentation for ocaml findlib

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.3.0-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.3.0-alt2
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt2
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- first build for ALT, based on RH spec
