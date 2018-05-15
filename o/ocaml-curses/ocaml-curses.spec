%set_verify_elf_method textrel=relaxed
Name: ocaml-curses
Version: 1.0.3
Release: alt5%ubt
Summary: OCaml bindings for ncurses

Group: System/Libraries
License: LGPLv2+
Url: http://savannah.nongnu.org/projects/ocaml-tmk/
Source: http://download.savannah.gnu.org/releases/ocaml-tmk/%name-%version.tar
Patch0:ocaml-curses-1.0.3-fix-term-h-detection.patch

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: libncurses-devel libtinfo-devel
BuildRequires: gawk
BuildRequires(pre): rpm-build-ubt

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
%patch0 -p1

autoreconf

%build
%configure --enable-widec
make all opt

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocamlfind install curses META *.cmi *.cmx *.cma *.cmxa *.a *.so *.mli

%files
%doc COPYING
%_libdir/ocaml/curses
%exclude %_libdir/ocaml/curses/*.a
%exclude %_libdir/ocaml/curses/*.cmxa
%exclude %_libdir/ocaml/curses/*.cmx
%exclude %_libdir/ocaml/curses/*.mli
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner

%files devel
%doc COPYING
%_libdir/ocaml/curses/*.a
%_libdir/ocaml/curses/*.cmxa
%_libdir/ocaml/curses/*.cmx
%_libdir/ocaml/curses/*.mli

%changelog
* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.3-alt5%ubt
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt4%ubt
- rebuild with ocaml 4.04.2

* Thu May 04 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt3%ubt
- moved out from site-lib dir
- added ubt tag

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt3
- rebuild with ocaml 4.04.1

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt2
- rebuild with new ocaml

* Tue Nov 22 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.3-alt1
- Initial build for ALT (based on 1.0.3-33.fc26.src)

