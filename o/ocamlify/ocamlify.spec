Name: ocamlify
Version: 0.0.2
Release: alt1
Summary: Include files in OCaml code
License: LGPL with static compilation exception
Group: Development/ML
Url: http://ocamlify.forge.ocamlcore.org/
# https://github.com/gildor478/ocamlify
Source0: %name-%version.tar
Patch0: ocamlify-deprecated_ocaml_functions.patch
Patch1: ocamlify-bytes.patch
Patch2: ocamlify-native.patch
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild, ocaml-ocamlbuild-devel
Requires: ocaml

%description
OCamlify allows to create OCaml source code by including whole files into
OCaml string or string list. The code generated can be compiled as a
standard OCaml file. It allows embedding external resources as OCaml code.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
ocaml -unsafe-string setup.ml -configure --prefix %buildroot/usr
ocaml -unsafe-string setup.ml -build

%install
mkdir -p %buildroot/usr
ocaml -unsafe-string setup.ml -install

%files
%doc AUTHORS.txt COPYING.txt INSTALL.txt README.txt
%_bindir/ocamlify

%changelog
* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 0.0.2-alt1
- first build for ALT with patches from Mageia

