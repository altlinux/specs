%def_with check
%define ocamlmodule gettext
Name: ocaml-%ocamlmodule
Version: 0.4.2
Release: alt5
Summary: OCaml library for i18n
Group: Development/ML
License: LGPLv2+ with OCaml-LGPL-linking-exception
Url: https://github.com/gildor478/ocaml-gettext
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: ocaml-dune-configurator-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-cppo
BuildRequires: ocaml-camlp-streams-devel
BuildRequires: ocaml-camomile-devel
BuildRequires: ocaml-fileutils-devel >= 0.4.4
BuildRequires: docbook-style-xsl
BuildRequires: xsltproc
BuildRequires: libxml2
%if_with check
BuildRequires: ocaml-dune-site-devel
BuildRequires: ocaml-ounit-devel
%endif

%description
Ocaml-gettext provides support for internationalization of Ocaml
programs.

Constraints :

* provides a pure Ocaml implementation,
* the API should be as close as possible to GNU gettext,
* provides a way to automatically extract translatable
  strings from Ocaml source code.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release
Requires: ocaml-fileutils-devel >= 0.4.0

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build --release @install

%install
%dune_install

%check
find test -type f -name dune -exec sed -i 's,oUnit,ounit2,' {} \;
%dune_check

%files -f ocaml-files.runtime
%doc LICENSE.txt

%files devel -f ocaml-files.devel
%doc README.md CHANGES.md TODO.md
%_bindir/ocaml-gettext
%_bindir/ocaml-xgettext
%_man1dir/*.1*
%_man5dir/*.5*

%changelog
* Tue Sep 10 2024 Anton Farygin <rider@altlinux.ru> 0.4.2-alt5
- added a fix to pass tests with ocaml 5.2.x

* Sun Nov 12 2023 Anton Farygin <rider@altlinux.ru> 0.4.2-alt4
- ported to camomile 2
- replaced ounit to ounit2
- added commits from upstream PR 28 and 24 against ocaml 5

* Tue Mar 16 2021 Anton Farygin <rider@altlinux.org> 0.4.2-alt3
- spec BR: ocaml-dune-devel changed to ocaml-dune-configurator-devel
- spec: use SPDX for ocaml linking exception in license tag

* Thu Dec 10 2020 Anton Farygin <rider@altlinux.ru> 0.4.2-alt2
- added ocaml-dune-devel to BuildRequires
- build process moved to macros from rpm-build-ocaml 1.4

* Sat Jun 27 2020 Anton Farygin <rider@altlinux.ru> 0.4.2-alt1
- 0.4.2
- enabled tests

* Tue Oct 08 2019 Anton Farygin <rider@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 0.3.8-alt4.gd9509df
- build from upstream git with fixes for ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.3.8-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 0.3.8-alt2
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 0.3.8-alt1
- 0.3.8

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.3.7-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.3.7-alt3
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 0.3.7-alt2
- fixed build in new environment

* Tue Apr 18 2017 Anton Farygin <rider@altlinux.ru> 0.3.7-alt1
- rebuild with new rpm-build-ocaml
- moved outsite from site-lib dir

* Sun Apr 09 2017 Anton Farygin <rider@altlinux.ru> 0.3.7-alt1
- new version

* Wed Nov 30 2016 Lenar Shakirov <snejok@altlinux.ru> 0.3.5-alt1
- Initial build for ALT (based on Fedora 0.3.5-9.fc26.src)

