%set_verify_elf_method textrel=relaxed
Name: ocaml-gapi
Version: 0.3.9
Release: alt1
Summary: A simple OCaml client for Google Services
License: MIT
Group: Development/ML
Url: https://github.com/astrada/gapi-ocaml
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.06
BuildRequires: ocaml-ocamldoc dune opam ocaml-base ocaml-stdio ocaml-configurator
BuildRequires: ocaml-biniou
BuildRequires: ocaml-findlib-devel >= 1.7.1
BuildRequires: ocaml-ocamlnet-nethttpd-devel >= 4.1.2
BuildRequires: ocaml-cryptokit-devel >= 1.11
BuildRequires: ocaml-extlib-devel >= 1.7.2
BuildRequires: ocaml-yojson >= 1.3.3
BuildRequires: ocaml-xmlm-devel >= 1.2.0
BuildRequires: ocaml-ounit-devel >= 2.0.0
BuildRequires: ocaml-curl-devel
BuildRequires: zlib-devel

%description
**gapi-ocaml** is a simple, unofficial, OCaml client for Google Services. The
library supports ClientLogin, OAuth 1.0a, and OAuth 2.0 authentication.
Supported RESTful APIs:

* Calendar APIs v3
* Google+ API v1
* Tasks API v1
* APIs Discovery Service v1
* URL Shortener API v1
* OAuth2 API v2
* Custom Search API v1
* Google Analytics API v3
* Page Speed Online API v1
* Blogger API v2
* Site Verification API v1
* AdSense Management API v1.1
* BigQuery API v2
* Drive API v2
* Gmail API v1

Google Data Protocol APIs (GData):

* Google Documents List API v3 (supports Google Drive)

### Features

* Monadic interface
* [Functional lenses](http://astrada.github.com/gapi-ocaml/GapiLens.html) to
  access data structures
* Service generator (experimental): a tool for generating client libraries for
  APIs based on the Google API Discovery format

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name%{?_isa} = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml gapi-ocaml.install

%files
%doc README.md LICENSE
%_libdir/ocaml/gapi-ocaml
%exclude %_libdir/ocaml/gapi-ocaml/*.a
%exclude %_libdir/ocaml/gapi-ocaml/*.cmx
%exclude %_libdir/ocaml/gapi-ocaml/*.cmxa
%exclude %_libdir/ocaml/gapi-ocaml/*.mli

%files devel
%_libdir/ocaml/gapi-ocaml/*.a
%_libdir/ocaml/gapi-ocaml/*.cmx
%_libdir/ocaml/gapi-ocaml/*.cmxa
%_libdir/ocaml/gapi-ocaml/*.mli

%changelog
* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 0.3.9-alt1
- 0.3.9

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.3.7-alt2
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 0.3.7-alt1
- 0.3.7

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.3.4-alt1
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.3.3-alt2
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 0.3.3-alt1
- first build for ALT
