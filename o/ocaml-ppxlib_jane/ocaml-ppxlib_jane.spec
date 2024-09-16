%define libname ppxlib_jane
Name: ocaml-%libname
Version: 0.17.0
Release: alt1
Summary: Utilities for working with Jane Street AST constructs
License: MIT
Group: Development/ML
Url: https://github.com/janestreet/ppxlib_jane
VCS: https://github.com/janestreet/ppxlib_jane
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-ppxlib-devel >= 0.17.0

%description
A library for use in ppxes for constructing and matching on ASTs corresponding
to the augmented parsetree that is recognized by the Jane Street OCaml compiler.

ASTs constructed using this library are compatible with the standard OCaml
compiler. Any syntax change known to this library is encoded as attributes, and
the standard OCaml compiler's interpretation of the ASTs constructed by these
library (which amounts to ignoring the attributes) is reasonable.

That is, we only expose "unsurprising" things in this library.
For example, if you construct an n-ary function using this library,
the standard OCaml compiler will interpret it as n nested unary functions
in the normal way.


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
%doc README.md LICENSE.md


%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- first build for ALT Linux
