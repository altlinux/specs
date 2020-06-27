%set_verify_elf_method textrel=relaxed
%def_with check
Name: ocaml-gettext
Version: 0.4.2
Release: alt1
Summary: OCaml library for i18n
Group: Development/ML

License: LGPLv2+ with exceptions
Url: https://github.com/gildor478/ocaml-gettext
Source: %name-%version.tar

BuildRequires: ocaml
BuildRequires: dune
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-cppo
BuildRequires: ocaml-camomile-devel
BuildRequires: ocaml-fileutils-devel >= 0.4.4
BuildRequires: docbook-style-xsl
BuildRequires: xsltproc
BuildRequires: libxml2
%if_with check
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

%build
dune build

%install
dune install --destdir=%buildroot

%check
find test -type f -name dune -exec sed -i 's,oUnit,ounit2,' {} \;
dune runtest

%files
%doc LICENSE.txt
%_libdir/ocaml/gettext*
%exclude %_libdir/ocaml/gettext*/*.a
%exclude %_libdir/ocaml/gettext*/*.cmxa
%exclude %_libdir/ocaml/gettext*/*.cmx
%exclude %_libdir/ocaml/gettext*/*.ml
%exclude %_libdir/ocaml/gettext*/*.mli
%_libdir/ocaml/stublibs/*.so

%files devel
%doc README.md CHANGES.md TODO.md
%_libdir/ocaml/gettext*/*.a
%_libdir/ocaml/gettext*/*.cmxa
%_libdir/ocaml/gettext*/*.cmx
%_libdir/ocaml/gettext*/*.ml
%_libdir/ocaml/gettext*/*.mli
%_bindir/ocaml-gettext
%_bindir/ocaml-xgettext
%_man1dir/*.1*
%_man5dir/*.5*

%changelog
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

