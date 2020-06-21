%set_verify_elf_method textrel=relaxed
Name: ocaml-lwt_log
Version: 1.1.1
Release: alt1
Summary: Lwt-friendly logger

Group: Development/ML
License: LGPL-2.1
Url: https://github.com/ocsigen/lwt_log
Source: %name-%version.tar

# Remove self dependence
%filter_from_requires /ocaml-cmi(Lwt_log_core)/d

BuildRequires: dune ocaml-lwt
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
%summary.

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
dune build

%install
dune install --destdir=%buildroot

%files
%doc CHANGES README.md
%dir %_libdir/ocaml/lwt_log
%dir %_libdir/ocaml/lwt_log/core
%_libdir/ocaml/lwt_log*/META
%_libdir/ocaml/lwt_log*/*.cma
%_libdir/ocaml/lwt_log*/*.cmi
%_libdir/ocaml/lwt_log*/*.cmxs
%_libdir/ocaml/lwt_log/core/*.cma
%_libdir/ocaml/lwt_log/core/*.cmi
%_libdir/ocaml/lwt_log/core/*.cmxs

%files devel
%_libdir/ocaml/lwt_log*/dune-package
%_libdir/ocaml/lwt_log*/opam
%_libdir/ocaml/lwt_log*/*.a
%_libdir/ocaml/lwt_log*/*.cmt*
%_libdir/ocaml/lwt_log*/*.cmxa
%_libdir/ocaml/lwt_log*/*.cmx
%_libdir/ocaml/lwt_log*/*.mli
%_libdir/ocaml/lwt_log*/*.ml
%_libdir/ocaml/lwt_log/core/*.a
%_libdir/ocaml/lwt_log/core/*.cmt*
%_libdir/ocaml/lwt_log/core/*.cmxa
%_libdir/ocaml/lwt_log/core/*.cmx
%_libdir/ocaml/lwt_log/core/*.mli
%_libdir/ocaml/lwt_log/core/*.ml

%changelog
* Sun Jun 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
