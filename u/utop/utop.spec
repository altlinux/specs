Name: utop
Version: 2.17.0
Release: alt2
Summary: Universal toplevel for OCaml
Group: Development/ML
License: MIT
Url: https://github.com/ocaml-community/utop
Source: %name-%version.tar
Provides: ocaml-%name = %EVR
BuildRequires: dune ocaml-cppo 
BuildRequires: ocaml-xdg-devel
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-lambda-term-devel
BuildRequires: ocaml-lwt-devel
BuildRequires: ocaml-zed-devel
BuildRequires: ocaml-logs-devel
BuildRequires: libev-devel
BuildPreReq: rpm-build-ocaml >= 1.4
Obsoletes: utop-devel <= 2.17.0-alt1

%description
utop is an improved toplevel (i.e., Read-Eval-Print Loop) for OCaml.

%prep
%setup
sed -i 's/%%%%VERSION%%%%/%version/' src/lib/uTop.ml

%build
%dune_build -p %name

%install
%dune_install %name

%check
%dune_check

%files -f ocaml-files.runtime -f ocaml-files.devel
%doc CHANGES.md README.md
%doc %_datadir/utop
%_man1dir/utop*
%_man5dir/utop*
%_bindir/utop
%_bindir/utop-full
%_emacslispdir/utop.el

%changelog
* Thu Apr 09 2026 Anton Farygin <rider@altlinux.org> 2.17.0-alt2
- merged devel subpackage into main package since utop is a bytecode-only
  end-user tool that requires META at runtime (closes: #58599)

* Fri Mar 27 2026 Anton Farygin <rider@altlinux.org> 2.17.0-alt1
- 2.16.0 -> 2.17.0

* Mon Dec 08 2025 Anton Farygin <rider@altlinux.org> 2.16.0-alt1
- 2.15.0 -> 2.16.0

* Fri Jan 17 2025 Anton Farygin <rider@altlinux.ru> 2.15.0-alt1
- 2.15.0

* Fri Sep 13 2024 Anton Farygin <rider@altlinux.ru> 2.14.0-alt1
- 2.14.0

* Sun Nov 05 2023 Anton Farygin <rider@altlinux.ru> 2.13.1-alt1
- 2.13.1

* Tue Mar 29 2022 Anton Farygin <rider@altlinux.ru> 2.9.1-alt1
- 2.9.1

* Fri Dec 10 2021 Anton Farygin <rider@altlinux.ru> 2.9.0-alt1
- 2.9.0

* Tue Nov 02 2021 Anton Farygin <rider@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Sun Mar 28 2021 Mikhail Gordeev <obirvalger@altlinux.org> 2.7.0-alt1
- new version 2.7.0

* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus
