%def_with check
%define pkgname zed
Name: ocaml-%pkgname
Version: 3.2.3
Release: alt1
Summary: Abstract engine for text edition in OCaml
Group: Development/ML
License: BSD-3-Clause
Url: https://github.com/ocaml-community/zed
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: dune 
BuildRequires: ocaml-camomile
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-react-devel
BuildRequires: ocaml-uuseg-devel
BuildRequires: ocaml-uutf-devel
BuildRequires: ocaml-uucp-devel
%if_with check
BuildRequires: ocaml-alcotest-devel
%endif
BuildPreReq: rpm-build-ocaml >= 1.4

%description
  Zed is an abstract engine for text edition. It can be used to write text
editors, edition widgets, readlines, ... Zed uses Camomile to fully support the
Unicode specification, and implements an UTF-8 encoded string type with
validation, and a rope datastructure to achieve efficient operations on large
Unicode buffers. Zed also features a regular expression search on ropes. To
support efficient text edition capabilities, Zed provides macro recording and
cursor management facilities.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p %pkgname

%install
%dune_install %pkgname

%check
%dune_check -p %pkgname

%files -f ocaml-files.runtime
%doc CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Sun Jun 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus
