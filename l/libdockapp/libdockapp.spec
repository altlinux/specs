# vim: set ft=spec: -*- rpm-spec -*-

Name: libdockapp
Version: 0.6.2
Release: alt1

Summary: DockApp Making Standard Library
Group: System/Libraries
License: MIT/X11
Url: http://solfertje.student.utwente.nl/~dalroi/libdockapp/

Packager: Sir Raorn <raorn@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Thu Jun 19 2008
BuildRequires: libXext-devel libXpm-devel libXt-devel

%description
This is a simple (trivial) library for writing Window Maker dock
applications, or dockapps (those that only show up in the dock), easily.

It is very limited and can be only used for dockapps that open a single
appicon for process in only be single display, but this seems to be
enough for most, if not all, dockapps.

%package devel
Summary: DockApp Making Standard Library
Group: Development/C
Requires: %name = %version-%release
Requires: libX11-devel libXpm-devel

%description devel
This is a simple (trivial) library for writing Window Maker dock
applications, or dockapps (those that only show up in the dock), easily.

It is very limited and can be only used for dockapps that open a single
appicon for process in only be single display, but this seems to be
enough for most, if not all, dockapps.

This package contains header files needed for development.

%prep 
%setup
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--without-font \
	--without-examples
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/lib*.so.*

%files devel
%doc examples fonts
%_libdir/lib*.so
%_includedir/*.h

%changelog
* Thu Jun 19 2008 Sir Raorn <raorn@altlinux.ru> 0.6.2-alt1
- [0.6.2]
- Updated [build]deps for "modular X" (closes: #9922)
- License is really MIT/X11

* Wed Aug 03 2005 Sir Raorn <raorn@altlinux.ru> 0.6.1-alt1
- [0.6.1]

* Sat Jun 04 2005 Sir Raorn <raorn@altlinux.ru> 0.6.0-alt1
- [0.6.0]
- Patches merged upstream

* Mon Apr 11 2005 Sir Raorn <raorn@altlinux.ru> 0.5.0-alt1
- [0.5.0]
- Updated buildrequires

* Fri Sep 27 2002 Rider <rider@altlinux.ru> 0.4.0-alt6
- Rebuild

* Tue May  8 2001 Alexey Voinov <voins@voins.program.ru>
- XFree86-static-libs removed from automatic BuildReqs

* Sat May  5 2001 Alexey Voinov <voins@voins.program.ru>
- translated Summary & description

* Mon Apr 30 2001 Alexey Voinov <voins@voins.program.ru>
- little spec cleanup
- conditional NoSource. build nosrc.rpm with --define 'nosource 1'
- BuildReq added

* Wed Apr 18 2001 Alexey Voinov <voins@voins.program.ru>
- Spring2001 build
- devel subpackage added

* Tue Feb 13 2001 Alexey Voinov <voins@voins.program.ru>
- initial release







