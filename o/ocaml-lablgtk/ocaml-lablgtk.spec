%set_verify_elf_method textrel=relaxed

Name: ocaml-lablgtk
Version: 2.18.5
Release: alt1%ubt

Summary: Objective Caml interface to gtk+

License: LGPLv2 with exceptions
Group: Development/ML

Url: http://lablgtk.forge.ocamlcore.org/
# https://forge.ocamlcore.org/anonscm/git/lablgtk/lablgtk.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: libncurses-devel
BuildRequires: libgtk+2-devel
#BuildRequires:  gtkglarea2-devel
BuildRequires: libgtkspell-devel
BuildRequires: libXmu-devel
BuildRequires: libglade-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: libgnomeui-devel
BuildRequires: librsvg-devel
BuildRequires: ocaml
BuildRequires: ocaml-camlp4
BuildRequires: ocaml-findlib
BuildRequires: ocaml-lablgl
BuildRequires: ocaml-ocamldoc
BuildRequires: zlib-devel
BuildRequires: libgtksourceview-devel

%description
LablGTK is is an Objective Caml interface to gtk+.

It uses the rich type system of Objective Caml 3 to provide a strongly
typed, yet very comfortable, object-oriented interface to gtk+. This
is not that easy if you know the dynamic typing approach taken by
gtk+.

%package doc
Group: Development/ML
Summary: Documentation for LablGTK
Requires: %name = %version-%release

%description doc
Documentation for %name.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release
Requires: gtk2-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
# Parallel builds don't work.
unset MAKEFLAGS
%configure --without-gl --enable-debug
perl -pi -e "s|-O|$RPM_OPT_FLAGS|" src/Makefile
make world CAMLOPT="ocamlopt.opt -g"
make opt CAMLOPT="ocamlopt.opt -g"
make doc CAMLP4O="camlp4o -I %_libdir/ocaml/camlp4/Camlp4Parsers"

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_libdir/ocaml/lablgtk2
mkdir -p %buildroot%_libdir/ocaml/stublibs
make install \
     RANLIB=true \
     BINDIR=%buildroot%_bindir \
     LIBDIR=%buildroot%_libdir \
     INSTALLDIR=%buildroot%_libdir/ocaml/lablgtk2 \
     DLLDIR=%buildroot%_libdir/ocaml/stublibs
cp META %buildroot%_libdir/ocaml/lablgtk2
#  needed for Provides ocaml(gtkSourceView2_types)
cp src/gtkSourceView2_types.cmi %buildroot%_libdir/ocaml/lablgtk2/


# Remove ld.conf (part of main OCaml dist).
rm %buildroot%_libdir/ocaml/ld.conf

# Remove unnecessary *.ml files (ones which have a *.mli).
pushd %buildroot%_libdir/ocaml/lablgtk2
for f in *.ml; do \
  b=`basename $f .ml`; \
  if [ -f "$b.mli" ]; then \
    rm $f; \
  fi; \
done
popd

# Remove .cvsignore files from examples directory.
find examples -name .cvsignore -exec rm {} \;

%files
%doc README COPYING CHANGES
%dir %_libdir/ocaml/lablgtk2
%_libdir/ocaml/lablgtk2/*.cmi
%_libdir/ocaml/lablgtk2/*.cma
%_libdir/ocaml/lablgtk2/*.cmxs
%_libdir/ocaml/stublibs/*.so*
%_bindir/gdk_pixbuf_mlsource
%_bindir/lablgladecc2
%_bindir/lablgtk2

%files devel
%doc README COPYING CHANGES
%dir %_libdir/ocaml/lablgtk2
%_libdir/ocaml/lablgtk2/META
%_libdir/ocaml/lablgtk2/*.a
%_libdir/ocaml/lablgtk2/*.cmxa
%_libdir/ocaml/lablgtk2/*.cmx
%_libdir/ocaml/lablgtk2/*.mli
%_libdir/ocaml/lablgtk2/*.ml
%_libdir/ocaml/lablgtk2/*.h
%_libdir/ocaml/lablgtk2/gtkInit.cmo
%_libdir/ocaml/lablgtk2/gtkInit.o
%_libdir/ocaml/lablgtk2/gtkThInit.cmo
%_libdir/ocaml/lablgtk2/gtkThread.cmo
%_libdir/ocaml/lablgtk2/gtkThread.o
%_libdir/ocaml/lablgtk2/propcc
%_libdir/ocaml/lablgtk2/varcc

%files doc
%doc examples doc/html

%changelog
* Sun Apr 16 2017 Anton Farygin <rider@altlinux.ru> 2.18.5-alt1%ubt
- first build for ALT, based on RH spec