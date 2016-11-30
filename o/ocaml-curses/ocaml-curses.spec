Name: ocaml-curses
Version: 1.0.3
Release: alt1
Summary: OCaml bindings for ncurses

Group: System/Libraries
License: LGPLv2+
Url: http://savannah.nongnu.org/projects/ocaml-tmk/
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: http://download.savannah.gnu.org/releases/ocaml-tmk/%name-%version.tar

BuildRequires: ocaml
BuildRequires: findlib
BuildRequires: libncurses-devel
BuildRequires: gawk

# Doesn't include a configure script, so we have to make one.
BuildRequires: autoconf, automake, libtool

%description
OCaml bindings for ncurses.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

autoreconf

%build
%configure --enable-widec
make all opt

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml/site-lib
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocamlfind install curses META *.cmi *.cmx *.cma *.cmxa *.a *.so *.mli

%files
%doc COPYING
%_libdir/ocaml/site-lib/curses
%exclude %_libdir/ocaml/site-lib/curses/*.a
%exclude %_libdir/ocaml/site-lib/curses/*.cmxa
%exclude %_libdir/ocaml/site-lib/curses/*.cmx
%exclude %_libdir/ocaml/site-lib/curses/*.mli
%_libdir/ocaml/site-lib/stublibs/*.so
%_libdir/ocaml/site-lib/stublibs/*.so.owner

%files devel
%doc COPYING
%_libdir/ocaml/site-lib/curses/*.a
%_libdir/ocaml/site-lib/curses/*.cmxa
%_libdir/ocaml/site-lib/curses/*.cmx
%_libdir/ocaml/site-lib/curses/*.mli

%changelog
* Tue Nov 22 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.3-alt1
- Initial build for ALT (based on 1.0.3-33.fc26.src)

