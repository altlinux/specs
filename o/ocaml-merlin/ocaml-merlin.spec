%define pkgname merlin
Name: ocaml-%pkgname
Version: 5.6.1.504
Release: alt1
Summary: Editor helper, provides completion, typing and source browsing in Vim and Emacs
License: MIT
Group: Development/ML
Url: https://github.com/ocaml/merlin
VCS: https://github.com/ocaml/merlin
Source0: %name-%version.tar
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-yojson-devel
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-odoc-devel
BuildRequires: ocaml-menhir
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-csexp-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: jq

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

%build
%dune_build --release @install

%install
%dune_install --release

%check
%ifnarch %ix86
sed -si 's;lib/ocaml;%_libdir/ocaml;' tests/test-dirs/locate/context-detection/cd-mod_constr.t/run.t \
	tests/test-dirs/occurrences/issue1404.t \
	tests/test-dirs/locate/ill-typed/issue1580.t
%endif
%dune_check --release

%files -f ocaml-files.runtime
%_bindir/*
%_datadir/merlin
%_datadir/emacs

%files devel -f ocaml-files.devel

%changelog
* Sat Mar 07 2026 Anton Farygin <rider@altlinux.org> 5.6.1.504-alt1
- 5.4.503 -> 5.6.1.504

* Fri Jan 17 2025 Anton Farygin <rider@altlinux.ru> 5.4.503-alt1
- 5.1.502 -> 5.4.503

* Mon Sep 16 2024 Anton Farygin <rider@altlinux.ru> 5.1.502-alt1
- first build for ALT Linux
