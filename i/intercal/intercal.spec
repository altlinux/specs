Name: intercal
Version: 0.24
Release: alt1

Summary: The language that kills the weak and drives mad the strong
License: GPL, except for ick-wrap.c
Group: Development/Other
Url: http://www.catb.org/~esr/intercal/

Source: %url/%name-%version.tar.gz
Patch0: %name-0.24-debian-fixes.patch

BuildPreReq: flex groff-base groff-ps

Requires: gcc

%description
An implementation of the language INTERCAL, legendary for
its perversity and horribleness (this version adds COME FROM
for extra flavor).  Comes with language manual and examples
including possibly the entire extant body of INTERCAL code.
Now supports i18n and l14n (to Ancient Roman locale only)
Now with fix patch by Donald Knuth.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build
pushd doc
%make_build all
%__rm -f Makefile intercal.refs.tmp
popd

%install
%__mkdir_p %buildroot{%_bindir,%_libdir,%_man1dir,{%_includedir,%_datadir}/%name}
%__install ick %buildroot%_bindir/
%__install -m644 libick.a %buildroot%_libdir/
%__install -m644 {abcess,fiddle,lose}.h %buildroot%_includedir/%name/
%__cp -a ick-wrap.c pit/lib/ %buildroot%_datadir/%name/
%__cp -a pit examples
%__rm -fr examples/{lib,Makefile}
%__install -m644 ick.1 %buildroot%_man1dir

%files
%_bindir/*
%_libdir/*.a
%_includedir/%name
%_datadir/%name
%_mandir/man?/*
%doc BUGS NEWS README doc/ examples/ %name.el

%changelog
* Mon Sep 26 2005 Andrey Rahmatullin <wrar@altlinux.ru> 0.24-alt1
- initial build
