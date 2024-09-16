%define libname ppx_disable_unused_warnings
Name: ocaml-%libname
Version: 0.17.0
Release: alt1
Summary: Jane Street extension to @disable_unused_warnings annotation
License: MIT
Group: Development/ML
Url: https://github.com/janestreet/ppx_disable_unused_warnings
VCS: https://github.com/janestreet/ppx_disable_unused_warnings
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-ppxlib-devel >= 0.17.0
BuildRequires: ocaml-base-devel >= 0.17.0

%description
The @disable_unused_warnings annotation disables the many OCaml compiler
warnings having to do with something being used (variable, constructor,
declaration, open, rec keyword, etc.).

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
