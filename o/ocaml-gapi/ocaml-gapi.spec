%def_with check
Name: ocaml-gapi
Version: 0.4.5
Release: alt1
Summary: A simple OCaml client for Google Services
License: MIT
Group: Development/ML
Url: https://github.com/astrada/gapi-ocaml
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.08
BuildRequires: dune 
BuildRequires: ocaml-cryptokit-devel >= 1.11
BuildRequires: ocaml-yojson-devel >= 1.3.3
BuildRequires: ocaml-cppo
BuildRequires: ocaml-camlp-streams-devel
%if_with check
BuildRequires: ocaml-ounit-devel >= 2.0.0
BuildRequires: libcurl-devel
%endif
BuildRequires: ocaml-curl-devel
BuildRequires: zlib-devel

%description
**gapi-ocaml** is a simple, unofficial, OCaml client for Google Services. The
library supports ClientLogin, OAuth 1.0a, and OAuth 2.0 authentication.
Supported RESTful APIs:

    Calendar APIs v3
    Google+ API v1
    Tasks API v1
    APIs Discovery Service v1
    URL Shortener API v1
    OAuth2 API v2
    Custom Search API v1
    Google Analytics API v3
    Page Speed Online API v1
    Blogger API v2
    Site Verification API v1
    AdSense Management API v1.1
    BigQuery API v2
    Drive API v2
    Drive API v3
    Gmail API v1

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
sed -i 's,oUnit,ounit2,' src/test/dune
%dune_build -p gapi-ocaml

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md LICENSE

%files devel -f ocaml-files.devel

%changelog
* Tue Nov 14 2023 Anton Farygin <rider@altlinux.ru> 0.4.5-alt1
- 0.4.5

* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Fri Mar 19 2021 Anton Farygin <rider@altlinux.org> 0.4.1-alt2
- enabled tests
- cleanup BR
- simplified specfile with macros from rpm-build-ocaml 1.4

* Wed Jul 01 2020 Anton Farygin <rider@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Wed Feb 26 2020 Anton Farygin <rider@altlinux.ru> 0.3.17-alt1
- 0.3.17

* Tue Jan 28 2020 Anton Farygin <rider@altlinux.ru> 0.3.16-alt1
- 0.3.16

* Tue Sep 03 2019 Anton Farygin <rider@altlinux.ru> 0.3.14-alt1
- 0.3.14

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 0.3.13-alt1
- 0.3.13

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 0.3.10-alt2
- 0.3.10

* Thu Mar 14 2019 Anton Farygin <rider@altlinux.ru> 0.3.9-alt2
- rebuilt with ocaml-yojson-1.7.0

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
