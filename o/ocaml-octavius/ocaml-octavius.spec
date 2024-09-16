%set_verify_elf_method textrel=relaxed
%define  modulename octavius

Name:    ocaml-%modulename
Version: 1.2.2
Release: alt4
Summary: ocamldoc comment syntax parser
License: ISC
Group:   Development/ML
URL:     https://github.com/ocaml-doc/octavius
BuildRequires: dune ocaml ocaml-compiler-libs >= 5.2.0
BuildPreReq: rpm-build-ocaml >= 1.6.3

Source:  %modulename-%version.tar

%description
Octavius is a library to parse the ocamldoc comment syntax.

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
%doc README.md
%dir %_libdir/ocaml/%modulename
%_bindir/%modulename

%files devel -f ocaml-files.devel

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 1.2.2-alt4
- add ocaml-compiler-libs to BuildRequires to fix build with ocaml-5.2.0

* Thu Oct 15 2020 Anton Farygin <rider@altlinux.ru> 1.2.2-alt3
- added ocaml to BuildRequires

* Thu Sep 17 2020 Anton Farygin <rider@altlinux.ru> 1.2.2-alt2
- removed rpm-build-ocaml dependency for runtime package
- migrated to rpm-build-ocaml 1.4

* Wed Jul 29 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus
