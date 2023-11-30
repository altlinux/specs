Name: ocaml-jsonm
Version: 1.0.2
Release: alt1
Summary: Non-blocking streaming codec to decode and encode JSON
License: BSD3
Group: Development/ML
Url: http://erratique.ch/software/jsonm
Source0: %name-%version.tar
BuildRequires: ocaml-findlib
BuildRequires: ocaml-uutf-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-ocamlbuild opam ocaml-topkg
BuildRequires: ocaml-uutf 
Requires: ocaml-uutf
BuildRequires(pre): rpm-build-ocaml >= 1.6


%description
Jsonm is a non-blocking streaming codec to decode and encode the JSON data
format. It can process JSON text without blocking on IO and without a
complete in-memory representation of the data.

The uncut codec also processes whitespace and (non-standard) JSON with
JavaScript comments.

Jsonm is made of a single module and depends on Uutf.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: ocaml-uutf-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
ocaml pkg/pkg.ml build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml
%ocaml_find_files

%files -f ocaml-files.runtime
%doc README.md CHANGES.md
%_bindir/jsontrip

%files devel -f ocaml-files.devel
%doc doc/

%changelog
* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 1.0.1-alt4
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.1-alt3
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.0.1-alt2
- rebuilt with ocaml-4.07

* Mon May 21 2018 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1
- first build for ALT, based on Mageia spec

