%set_verify_elf_method textrel=relaxed
Name: ocaml-gapi
Version: 0.3.3
Release: alt2%ubt
Summary: A simple OCaml client for Google Services
License: MIT
Group: Development/ML
Url: https://github.com/astrada/gapi-ocaml
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-ocamldoc ocaml-ocamlbuild
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
BuildRequires(pre): rpm-build-ubt

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
ocaml setup.ml -configure --enable-examples
ocaml setup.ml -build

%install
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
ocaml setup.ml -install

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
* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.3.3-alt2%ubt
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 0.3.3-alt1%ubt
- first build for ALT
