Name: ocaml-num
Version: 1.4
Release: alt2
Summary: Legacy Num library for arbitrary-precision integer and rational arithmetic
Group: Development/ML
License: LGPLv2+ with exceptions
Url: https://github.com/ocaml/num
Source0: %name-%version.tar
BuildRequires: ocaml
BuildRequires: dune

%description
This library implements arbitrary-precision arithmetic on big integers
and on rationals.

This is a legacy library. It used to be part of the core OCaml
distribution (in otherlibs/num) but is now distributed separately. New
applications that need arbitrary-precision arithmetic should use the
Zarith library (https://github.com/ocaml/Zarith) instead of the Num
library, and older applications that already use Num are encouraged to
switch to Zarith. Zarith delivers much better performance than Num and
has a nicer API.

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
%dune_build --release @install

%check
%dune_check

%install
%dune_install

%files -f ocaml-files.runtime
%doc Changelog README.md
%doc LICENSE

%files devel -f ocaml-files.devel
%doc LICENSE

%changelog
* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 1.4-alt2
- removed findlib from BuildRequires

* Wed Jan 13 2021 Anton Farygin <rider@altlinux.ru> 1.4-alt1
- 1.4

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- 1.3

* Tue Jul 30 2019 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- 1.2

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.1-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.1-alt2
- rebuilt with ocaml 4.07

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 1.1-alt1
- first build for ALT, based on Mageia spec

