Name: ocaml-gettext
Version: 0.3.7
Release: alt1%ubt
Summary: OCaml library for i18n
Group: Development/ML

License: LGPLv2+ with exceptions
Url: http://forge.ocamlcore.org/projects/ocaml-gettext

Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar

Patch1: ocaml-gettext-0.3.4-use-ocamlopt-g.patch
# Disable warning 31, so we can compile (with warnings) on OCaml 4.04.
Patch2: ocaml-gettext-0.3.5-disable-warning-31.patch

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-camlp4
BuildRequires: ocaml-fileutils-devel >= 0.4.4
BuildRequires: docbook-style-xsl
BuildRequires: xsltproc
BuildRequires: libxml2
BuildRequires: chrpath
BuildRequires: autoconf
BuildRequires(pre):rpm-build-ubt

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

# BZ 446919.
Requires: ocaml-fileutils-devel >= 0.4.0

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%patch1 -p1
%patch2 -p1

%build
# Parallel builds don't work.
unset MAKEFLAGS
autoreconf -fisv
CFLAGS="$RPM_OPT_FLAGS" \
./configure \
  --libdir=%_libdir \
  --disable-camomile \
  --with-docbook-stylesheet=%_datadir/sgml/docbook/xsl-stylesheets
make all

%install
# make install in the package is screwed up completely.  Install
# by hand instead.
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p %buildroot%_bindir

# Remove *.o files - these shouldn't be distributed.
find _build -name '*.o' -exec rm {} \;

ocamlfind install gettext _build/lib/gettext/*
ocamlfind install gettext-stub _build/lib/gettext-stub/*
install -m 0755 _build/bin/ocaml-gettext %buildroot%_bindir/
install -m 0755 _build/bin/ocaml-xgettext %buildroot%_bindir/

chrpath --delete $OCAMLFIND_DESTDIR/stublibs/dll*.so

%files
%doc COPYING
%_libdir/ocaml/gettext
%_libdir/ocaml/gettext-stub
%exclude %_libdir/ocaml/gettext/*.a
%exclude %_libdir/ocaml/gettext/*.cmxa
%exclude %_libdir/ocaml/gettext/*.cmx
%exclude %_libdir/ocaml/gettext-stub/*.a
%exclude %_libdir/ocaml/gettext-stub/*.cmxa
%exclude %_libdir/ocaml/gettext-stub/*.cmx
%exclude %_libdir/ocaml/gettext/*.ml
%exclude %_libdir/ocaml/gettext/*.mli
%exclude %_libdir/ocaml/gettext-stub/*.ml
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner

%files devel
%doc README CHANGELOG TODO
# %doc build/share/doc/html/*
%_libdir/ocaml/gettext/*.a
%_libdir/ocaml/gettext/*.cmxa
%_libdir/ocaml/gettext/*.cmx
%_libdir/ocaml/gettext-stub/*.a
%_libdir/ocaml/gettext-stub/*.cmxa
%_libdir/ocaml/gettext-stub/*.cmx
%_libdir/ocaml/gettext/*.ml
%_libdir/ocaml/gettext/*.mli
%_libdir/ocaml/gettext-stub/*.ml
%_bindir/ocaml-gettext
%_bindir/ocaml-xgettext

%changelog
* Tue Apr 18 2017 Anton Farygin <rider@altlinux.ru> 0.3.7-alt1%ubt
- rebuild with new rpm-build-ocaml
- moved outsite from site-lib dir

* Sun Apr 09 2017 Anton Farygin <rider@altlinux.ru> 0.3.7-alt1
- new version

* Wed Nov 30 2016 Lenar Shakirov <snejok@altlinux.ru> 0.3.5-alt1
- Initial build for ALT (based on Fedora 0.3.5-9.fc26.src)

