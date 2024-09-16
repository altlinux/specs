%define libname ppx_tydi
Name: ocaml-%libname
Version: 0.17.0
Release: alt1
Summary: Type-directed disambiguation of records in let-bindings for Ocaml
License: MIT
Group: Development/ML
Url: https://github.com/janestreet/ppx_tydi
VCS: https://github.com/janestreet/ppx_tydi
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-ppxlib-devel >= %version
BuildRequires: ocaml-base-devel >= %version

%description
Provides a ppx for [let] bindings. In [let%%tydi a = b in ...], [a]'s type
is inferred from [b] rather than the other way around.
This is convenient for record patterns whose fields are not in scope.


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
%doc README.mdx LICENSE.md


%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.17.0-alt1
- first build for ALT Linux
