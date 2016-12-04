Name: ocaml-gettext
Version: 0.3.5
Release: alt1
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
BuildRequires: findlib
BuildRequires: ocamldoc
BuildRequires: camlp4
BuildRequires: ocaml-fileutils-devel >= 0.4.4
BuildRequires: docbook-style-xsl
BuildRequires: xsltproc
BuildRequires: libxml2
BuildRequires: chrpath
BuildRequires: autoconf

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
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml/site-lib
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
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
%_libdir/ocaml/site-lib/gettext
%_libdir/ocaml/site-lib/gettext-stub
%exclude %_libdir/ocaml/site-lib/gettext/*.a
%exclude %_libdir/ocaml/site-lib/gettext/*.cmxa
%exclude %_libdir/ocaml/site-lib/gettext/*.cmx
%exclude %_libdir/ocaml/site-lib/gettext-stub/*.a
%exclude %_libdir/ocaml/site-lib/gettext-stub/*.cmxa
%exclude %_libdir/ocaml/site-lib/gettext-stub/*.cmx
%exclude %_libdir/ocaml/site-lib/gettext/*.ml
%exclude %_libdir/ocaml/site-lib/gettext/*.mli
%exclude %_libdir/ocaml/site-lib/gettext-stub/*.ml
%_libdir/ocaml/site-lib/stublibs/*.so
%_libdir/ocaml/site-lib/stublibs/*.so.owner

%files devel
%doc README CHANGELOG TODO
# %doc build/share/doc/html/*
%_libdir/ocaml/site-lib/gettext/*.a
%_libdir/ocaml/site-lib/gettext/*.cmxa
%_libdir/ocaml/site-lib/gettext/*.cmx
%_libdir/ocaml/site-lib/gettext-stub/*.a
%_libdir/ocaml/site-lib/gettext-stub/*.cmxa
%_libdir/ocaml/site-lib/gettext-stub/*.cmx
%_libdir/ocaml/site-lib/gettext/*.ml
%_libdir/ocaml/site-lib/gettext/*.mli
%_libdir/ocaml/site-lib/gettext-stub/*.ml
%_bindir/ocaml-gettext
%_bindir/ocaml-xgettext

%changelog
* Wed Nov 30 2016 Lenar Shakirov <snejok@altlinux.ru> 0.3.5-alt1
- Initial build for ALT (based on Fedora 0.3.5-9.fc26.src)

