%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: ocaml-curses
Version: 1.0.8
Release: alt1
Summary: OCaml bindings for ncurses

Group: System/Libraries
License: LGPLv2+
Url: http://savannah.nongnu.org/projects/ocaml-tmk/
Source: http://download.savannah.gnu.org/releases/ocaml-tmk/%name-%version.tar

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: libncurses-devel libtinfo-devel
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


%build
%autoreconf
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
* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Sun Jun 28 2020 Anton Farygin <rider@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.0.3-alt8
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.3-alt7
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.0.3-alt6
- rebuilt with ocaml 4.07

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.0.3-alt5
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt4
- rebuild with ocaml 4.04.2

* Thu May 04 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt3
- moved out from site-lib dir
- added ubt tag

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt3
- rebuild with ocaml 4.04.1

* Sat Apr 08 2017 Anton Farygin <rider@altlinux.ru> 1.0.3-alt2
- rebuild with new ocaml

* Tue Nov 22 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.3-alt1
- Initial build for ALT (based on 1.0.3-33.fc26.src)

