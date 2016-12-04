%set_verify_elf_method textrel=relaxed

Name: ocaml-calendar
Version: 2.04
Release: alt1
Summary: Objective Caml library for managing dates and times
License: LGPLv2
Group: Development/ML

Url: http://calendar.forge.ocamlcore.org/
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar

Patch1: calendar-2.03.2-enable-debug.patch

BuildRequires: ocaml
BuildRequires: findlib
BuildRequires: ocamldoc

%description
Objective Caml library for managing dates and times.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch1 -p1

%build
./configure --libdir=%_libdir
make
make doc

mv TODO TODO.old
iconv -f iso-8859-1 -t utf-8 < TODO.old > TODO

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml/site-lib
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc CHANGES README TODO LGPL COPYING
%_libdir/ocaml/site-lib/calendar
%exclude %_libdir/ocaml/site-lib/calendar/*.cmx
%exclude %_libdir/ocaml/site-lib/calendar/*.mli

%files devel
%doc CHANGES README TODO LGPL COPYING calendarFAQ-2.6.txt doc/*
%_libdir/ocaml/site-lib/calendar/*.cmx
%_libdir/ocaml/site-lib/calendar/*.mli

%changelog
* Wed Nov 30 2016 Lenar Shakirov <snejok@altlinux.ru> 2.04-alt1
- Initial build for ALT (based on 2.04-6.fc26.src)

