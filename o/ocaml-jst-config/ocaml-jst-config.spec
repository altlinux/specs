%set_verify_elf_method textrel=relaxed
%define  modulename jst-config

Name:    ocaml-%modulename
Version: 0.14.0
Release: alt2

Summary: Compile-time configuration for Jane Street libraries
License: MIT
Group:   Development/ML
URL:     https://github.com/janestreet/jst-config

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires: dune ocaml-ppx_assert-devel ocaml-result-devel
BuildRequires: ocaml-ppxlib-devel ocaml-migrate-parsetree-devel
BuildRequires: ocaml-ppx_compare-devel ocaml-ppx_here-devel
BuildRequires: ocaml-ppx_sexp_conv-devel ocaml-compiler-libs-devel
BuildRequires: ocaml-stdio-devel
BuildPreReq: rpm-build-ocaml >= 1.4

Source:  %modulename-%version.tar

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -n %modulename-%version

%build
%dune_build -p %modulename

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel
%_libdir/ocaml/%{modulename}*/*.h
%_libdir/ocaml/%{modulename}*/rt-flags

%changelog
* Wed Sep 16 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- migrated to rpm-build-ocaml-1.4
- added ocaml-stdio-devel to BuildRequires

* Thu Jul 30 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
