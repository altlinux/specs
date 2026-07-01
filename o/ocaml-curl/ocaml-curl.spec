%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%global pkgname curl
%define ocamlsitelib %_libdir/ocaml
%define pkgsitelib %ocamlsitelib/%pkgname
%define ocamlstublib %_libdir/ocaml/stublibs/

Name: ocaml-%pkgname
Version: 0.10.0
Release: alt2
Summary: OCaml Curl library (ocurl)
License: MIT
Group: Development/ML
Url: https://ygrek.org/p/ocurl/
VCS: https://github.com/ygrek/ocurl
Source0: %name-%version.tar

BuildRequires: ocaml libcurl-devel
BuildRequires: rpm-build-ocaml dune
BuildRequires: ocaml-dune-configurator-devel
BuildRequires: ocaml-lwt-devel

%description
The Ocaml Curl Library (Ocurl) is an interface library for the
programming language Ocaml to the networking library libcurl.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build --release @install

%install
%dune_install --release

%files -f ocaml-files.runtime
%doc COPYING

%files devel -f ocaml-files.devel
%doc examples/*

%changelog
* Wed Jul 01 2026 Anton Farygin <rider@altlinux.org> 0.10.0-alt2
- built with lwt support

* Tue Jan 13 2026 Anton Farygin <rider@altlinux.org> 0.10.0-alt1
- 0.9.2 -> 0.10.0

* Thu Nov 16 2023 Anton Farygin <rider@altlinux.ru> 0.9.2-alt2
- added support for bytecode-only version of the ocaml package
- fixed URL and VCS tags

* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Sat Sep 18 2021 Anton Farygin <rider@altlinux.ru> 0.9.1-alt2
- fixed build with enabled LTO

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 0.8.2-alt3
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.8.2-alt2
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Thu May 17 2018 Anton Farygin <rider@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 0.7.9-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.7.9-alt2
- rebuild with ocaml 4.04.1

* Sun Apr 16 2017 Anton Farygin <rider@altlinux.ru> 0.7.9-alt1
- first build for ALT
