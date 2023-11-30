%def_without check
%define  modulename pp
Name:    ocaml-%modulename
Version: 1.2.0
Release: alt1
Summary: An OCaml pretty-printing library
License: MIT
Group:   Development/ML
URL:     https://github.com/ocaml-dune/pp
BuildRequires: dune ocaml
BuildRequires: rpm-build-ocaml >= 1.4
%if_with check
BuildRequires: ocaml-ppx_expect-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-ppx_compare-devel
BuildRequires: ocaml-ppx_enumerate-devel
BuildRequires: ocaml-ppx_hash-devel
%endif
Source:  %name-%version.tar

%description
 This library provides a lean alternative to the Format 1 module of the OCaml
standard library. It aims to make it easy for users to do the right thing.
If you have tried Format before but find its API complicated and difficult to
use, then Pp might be a good choice for you.

Pp uses the same concepts of boxes and break hints, and the final rendering is
done to formatter from the Format module. However it defines its own algebra
which some might find easier to work with and reason about. No previous
knowledge is required to start using this library, however the various guides
for the Format module such as this one 2 should be applicable to Pp as well.

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
%dune_build -p %{modulename}

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- first build for ALT
