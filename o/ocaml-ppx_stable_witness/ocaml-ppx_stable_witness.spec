%define libname ppx_stable_witness
Name: ocaml-%libname
Version: 0.17.0
Release: alt1
Summary: OCAML ppx extension for deriving a witness that a type is intended to be stable
License: MIT
Group: Development/ML
Url: https://github.com/janestreet/ppx_stable_witness
VCS: https://github.com/janestreet/ppx_stable_witness
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-ppxlib-devel >= %version
BuildRequires: ocaml-base-devel >= %version

%description
%summary

In this context, stable means that the serialization format will never change.
This allows programs running at different versions of the code
to safely communicate.


%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %libname

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- first build for ALT Linux
