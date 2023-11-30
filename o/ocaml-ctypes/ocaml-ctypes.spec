%define pkgname ctypes
Name: ocaml-%pkgname
Version: 0.21.1
Release: alt1
Summary: Combinators for binding to C libraries without writing any C

Group: Development/ML
License: MIT
Url: https://github.com/ocamllabs/ocaml-ctypes
Source: %name-%version.tar
BuildRequires:  ocaml-integers-devel ocaml-bigarray-compat-devel
BuildRequires: libffi-devel 
BuildRequires: dune ocaml ocaml-dune-configurator-devel
BuildPreReq: rpm-build-ocaml >= 1.1

%description
ctypes is a library for binding to C libraries using pure OCaml. The primary
aim is to make writing C extensions as straightforward as possible.

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
%dune_build -p %pkgname

%install
%dune_install %pkgname

%files -f ocaml-files.runtime
%doc README.md
%_libdir/ocaml/stublibs/*.so

%files devel -f ocaml-files.devel
%_libdir/ocaml/%pkgname/*.h

%changelog
* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 0.21.1-alt1
- 0.21.1

* Tue Apr 12 2022 Anton Farygin <rider@altlinux.ru> 0.20.1-alt1
- 0.20.1

* Mon Jan 03 2022 Anton Farygin <rider@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Sat Oct 16 2021 Anton Farygin <rider@altlinux.ru> 0.19.1-alt1
- 0.19.1

* Sun Mar 28 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.18.0-alt1
- new version 0.18.0

* Wed Jul 08 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.1-alt1
- Initial build for Sisyphus
