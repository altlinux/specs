%define  modulename cohttp
%def_with check
Name:    ocaml-%modulename
Version: 5.0.0
Release: alt1
Summary: An OCaml library for HTTP clients and servers
License: ISC
Group:   Development/ML
URL:     https://github.com/mirage/ocaml-cohttp
BuildRequires: dune
BuildRequires: ocaml-uri-devel  ocaml-fieldslib-devel
BuildRequires: ocaml-re-devel ocaml-ppx_sexp_conv-devel
BuildRequires: ocaml-sexplib0-devel ocaml-ppx_fields_conv-devel
BuildRequires: ocaml-jsonm-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-base64-devel
BuildRequires: ocaml-lwt-devel
BuildRequires: ocaml-logs-devel
BuildRequires: ocaml-conduit-devel
BuildRequires: ocaml-magic-mime-devel
%if_with check
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-ounit-devel
%endif
BuildRequires: libev-devel
BuildPreReq: rpm-build-ocaml >= 1.4
Source:  %name-%version.tar
Patch0: %name-%version-%release.patch

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
sed -si 's,oUnit,ounit2,' cohttp-lwt-unix/test/dune \
			  cohttp_lwt_unix_test/src/dune \
			  cohttp_test/src/dune
%dune_build -p %{modulename},%{modulename}-lwt,%{modulename}-lwt-unix

%install
%dune_install %{modulename} %{modulename}-lwt %{modulename}-lwt-unix 

%check
# remove fuzzing test
rm -rf cohttp/fuzz
%dune_check %{modulename} %{modulename}-lwt %{modulename}-lwt-unix  

%files -f ocaml-files.runtime
%doc README.md
%_bindir/cohttp-*

%files devel -f ocaml-files.devel

%changelog
* Mon Jan 03 2022 Anton Farygin <rider@altlinux.ru> 5.0.0-alt1
- 5.0.0

* Wed Sep 08 2021 Anton Farygin <rider@altlinux.ru> 4.0.0-alt1
- 4.0.0

* Thu Mar 18 2021 Anton Farygin <rider@altlinux.org> 2.5.5-alt1
- 2.5.5

* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 2.5.4-alt1
- first build for ALT

