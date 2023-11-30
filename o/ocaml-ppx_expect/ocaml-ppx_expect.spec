%define ocamlmod ppx_expect
Name: ocaml-%ocamlmod
Version: 0.16.0
Release: alt1
Summary: a cram like framework for OCaml
Group: Development/ML
License: MIT
Url: http://ounit.forge.ocamlcore.org/
# https://github.com/gildor478/ounit
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: ocaml >= 4.10
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-stdio-devel
BuildRequires: ocaml-ppx_inline_test-devel
BuildRequires: ocaml-ppx_here-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-base-devel
BuildRequires: dune

%description
Expect-test is a framework for writing tests in OCaml, similar to Cram.
Expect-tests mimic the existing inline tests framework with the let%%expect_test
construct. The body of an expect-test can contain output-generating code,
interleaved with %%expect extension expressions to denote the expected output.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p %ocamlmod

%install
%dune_install %ocamlmod

# tests is broken in upstream
#check
#dune_check -p %ocamlmod

%files -f ocaml-files.runtime
%doc LICENSE.md

%files devel -f ocaml-files.devel
%doc README.org CHANGES.md

%changelog
* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 0.15.0-alt1
- 0.15.0

* Wed Mar 24 2021 Anton Farygin <rider@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sun Mar 21 2021 Anton Farygin <rider@altlinux.org> 0.14.0-alt3
- specfile BR: cleanup
- simplified specfile with macros from rpm-build-ocaml 1.4

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt2
- devel parts have been moved from the main package

* Fri Sep 04 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- first build for ALT
