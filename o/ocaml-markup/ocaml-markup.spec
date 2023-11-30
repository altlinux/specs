%define libnamelwt %libname-lwt
%define pkglist markup,markup-lwt
%def_with check
%define libname markup
%ifarch %ocaml_native_arch
%def_with native
%else
%def_without native
%endif
Name: ocaml-%libname
Version: 1.0.3
Release: alt2
Summary: Error-recovering streaming HTML5 and XML parsers.
License: MIT
Group: Development/ML
Url: https://github.com/aantron/markup.ml
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ocaml >= 1.6
BuildRequires: ocaml >= 4.07.1 dune >= 2.9
BuildRequires: ocaml-uutf-devel ocaml-bisect_ppx-devel ocaml-migrate-parsetree-devel ocaml-result-devel

%if_with check
BuildRequires: ocaml-ounit-devel libev-devel
%endif

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %EVR

%description
Markup.ml provides an HTML parser and an XML parser. The parsers are wrapped in
a simple interface: they are functions that transform byte streams to parsing signal
streams. Streams can be manipulated in various ways, such as processing by fold,
filter, and map, assembly into DOM tree structures, or serialization back to HTML or XML.

%description devel
This package includes development files necessary for developing
programs which use %name

%package lwt
Summary: Adapter between Markup.ml and Lwt
Group: Development/ML
Requires: %name = %EVR
BuildRequires: ocaml-lwt-devel

%package lwt-devel
Summary: Development files for programs which will use the %name-lwt
Group: Development/ML
Requires: %name-lwt = %EVR
Requires: ocaml-bisect_ppx-devel

%description lwt
Adapter between Markup.ml and Lwt

%description lwt-devel
This package includes development files necessary for developing
programs which use %name-lwt

%prep
%setup
%patch0 -p1

%build
%dune_build -p %pkglist

%install
%dune_install %libname
%dune_install %libnamelwt

%check
%dune_check -p %pkglist

%files
%doc LICENSE.md README.md
%_libdir/ocaml/%libname
%if_with native
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmx
%endif
%exclude %_libdir/ocaml/%libname/*.mli

%files devel
%if_with native
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmx
%endif
%_libdir/ocaml/%libname/*.mli

%files lwt
%_libdir/ocaml/%libnamelwt
%if_with native
%exclude %_libdir/ocaml/%libnamelwt/*.a
%exclude %_libdir/ocaml/%libnamelwt/*.cmxa
%exclude %_libdir/ocaml/%libnamelwt/*.cmx
%endif
%exclude %_libdir/ocaml/%libnamelwt/*.mli

%files lwt-devel
%if_with native
%_libdir/ocaml/%libnamelwt/*.a
%_libdir/ocaml/%libnamelwt/*.cmxa
%_libdir/ocaml/%libnamelwt/*.cmx
%endif
%_libdir/ocaml/%libnamelwt/*.mli

%changelog
* Sat Nov 18 2023 Anton Farygin <rider@altlinux.ru> 1.0.3-alt2
- support for bytecode-only ocaml

* Tue Mar 29 2022 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Wed Nov 03 2021 Anton Farygin <rider@altlinux.ru> 1.0.2-alt2
- run tests with --release flag

* Wed Jul 28 2021 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Jan 11 2021 Anton Farygin <rider@altlinux.ru> 1.0.0-alt1
- 1.0.0
- testing enabled

* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 0.8.0-alt1
- first build for ALT

