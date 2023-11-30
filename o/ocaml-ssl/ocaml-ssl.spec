%def_with check
Name: ocaml-ssl
Version: 0.7.0
Release: alt1
Summary: OCaml bindings for the OpenSSL library
License: LGPLv2.1 with OCaml-LGPL-linking-exception
Group: Development/ML
Url: https://github.com/savonet/ocaml-ssl
Source: %name-%version.tar
BuildRequires: libssl-devel
BuildRequires: ocaml ocaml-dune-configurator-devel
%if_with check
BuildRequires: ocaml-alcotest-devel
%endif

%description
This package contains OCaml bindings for libssl.

Install it if you intend to develop
SSL-enabled applications in OCaml.

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Requires: libssl-devel
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%build
%dune_build -p ssl

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime

%files devel -f ocaml-files.devel

%changelog
* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 0.7.0-alt1
- 0.7.0
- enabled tests

* Fri Mar 26 2021 Anton Farygin <rider@altlinux.org> 0.5.10-alt1
- 0.5.10

* Tue Mar 16 2021 Anton Farygin <rider@altlinux.org> 0.5.9-alt4
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel
- spec: use SPDX for ocaml linking exception in license tag
- simplified specfile with macros from rpm-build-ocaml 1.4

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 0.5.9-alt3
- cmx moved to the devel package

* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 0.5.9-alt2
- fix for build with dune-2.x

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 0.5.9-alt1
- 0.5.9

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 0.5.7-alt1
- 0.5.7

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.5.6-alt1
- 0.5.6

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.5.5-alt2
- rebuilt with ocaml 4.07

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 0.5.5-alt1
- 0.5.5

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.5.3-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.5.3-alt3
- rebuild with ocaml 4.04.1

* Tue Apr 18 2017 Anton Farygin <rider@altlinux.ru> 0.5.3-alt2
- move module outside site-lib dir
- split to runtime and devel packages

* Mon Apr 10 2017 Anton Farygin <rider@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Fri Dec 23 2011 Alexey Shabalin <shaba@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.2-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sun Jan 06 2008 Alex V. Myltsev <avm@altlinux.ru> 0.4.2-alt1
- Initial build for Sisyphus
