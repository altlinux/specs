%set_verify_elf_method textrel=relaxed
%define  modulename ipaddr

Name:    ocaml-%modulename
Version: 5.0.0
Release: alt1
Summary: An OCaml library for manipulation of IP (and MAC) address representations 
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-ipaddr
Source:  %name-%version.tar
Patch0:   %name-%version-%release.patch
BuildRequires: dune
BuildRequires: ocaml-domain-name-devel
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-cstruct-devel
BuildPreReq: rpm-build-ocaml >= 1.4

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
%setup
%patch0 -p1

%build
sed -si 's,oUnit,ounit2,' lib_test/dune
%dune_build --release @install

%install
%dune_install

%check
# test fail on i586 https://github.com/mirage/ocaml-ipaddr/issues/101
%ifnarch %ix86
%dune_check
%endif

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 5.0.0-alt1
- first build for ALT
