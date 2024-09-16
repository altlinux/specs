%define libname ppx_ignore_instrumentation
Name: ocaml-%libname
Version: 0.17.0
Release: alt1
Summary: Ignore Jane Street specific instrumentation extensions
License: MIT
Group: Development/ML
Url: https://github.com/janestreet/ppx_ignore_instrumentation
VCS: https://github.com/janestreet/ppx_ignore_instrumentation
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-ppxlib-devel

%description
Ignore Jane Street specific instrumentation extensions from
internal PPXs or compiler features not yet upstreamed

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
