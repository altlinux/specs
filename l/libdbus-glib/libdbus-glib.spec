Name: libdbus-glib
Version: 0.98
Release: alt1
Epoch: 1
Summary: GLib bindings for D-BUS
License: GPL or Academic Free License
Group: System/Libraries
URL: http://www.freedesktop.org/wiki/Software/DBusBindings
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: dbus doxygen gcc-c++ glib2-devel libdbus-devel libexpat-devel libgio-devel xmlto gtk-doc

%description
This package contains D-BUS library wrapper suitable for applications
which make use of GLib event loop.

%package devel
Summary: GLib bindings development files for D-BUS
Group: Development/C
Requires: %name = %version-%release
PreReq: libdbus-devel >= 0.94
Requires: glib2-devel

%description devel
This package contains GLib bindings development files for D-BUS.

%package doc
Summary: GLib bindings documentation for D-BUS
Group: Development/C
Requires: %name = %version-%release
BuildArch: noarch

%description doc
This package contains GLib bindings documentation files for D-BUS.

%prep
%setup -q
%patch -p1

%build
gtkdocize
%autoreconf
%configure \
	--libexecdir=%_prefix/libexec/dbus-1 \
	--enable-gtk-doc \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files 
%doc AUTHORS HACKING NEWS README
%_sysconfdir/bash_completion.d/*.sh
%_libdir/lib*.so.*
%_prefix/libexec/dbus-1/dbus-bash-completion-helper

%files devel
%_includedir/dbus-1.0/dbus/dbus*.h
%_bindir/dbus-binding-tool
%_libdir/lib*.so
%_pkgconfigdir/dbus-glib-1.pc
%_man1dir/dbus-binding-tool.1*

%files doc
%_datadir/gtk-doc/html/dbus-glib

%changelog
* Fri Oct 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.98-alt1
- 0.98

* Sun Jun 12 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.94-alt2
- fixed regression in marshalling objects as object paths

* Thu Jun 02 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.94-alt1
- 0.94

* Tue Feb 08 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:0.92-alt1
- 0.92

* Mon Nov 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.90-alt1
- 0.90

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.88-alt2
- rebuild

* Thu Aug 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.88-alt1
- 0.88

* Sat Apr 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.86-alt1
- 0.86

* Fri Feb 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:0.84-alt1
- 0.84

* Thu Jul 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.82-alt2
- rebuild

* Thu Jul 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.82-alt1
- 0.82

* Tue Feb 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.80-alt2
- fixed http://bugs.freedesktop.org/show_bug.cgi?id=14183

* Tue Feb 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.80-alt1
- 0.80

* Fri Dec 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.78-alt1
- 0.78

* Sun Nov 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.76-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Fri Sep 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.76-alt0.M41.1
- build for branch 4.1

* Thu Jun 19 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.76-alt1
- 0.76

* Tue Dec 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.74-alt2
- rebuild
- spec cleanup
- update URL

* Thu Jul 05 2007 Igor Zubkov <icesik@altlinux.org> 0.74-alt1
- 0.73 -> 0.74

* Tue Apr 10 2007 Igor Zubkov <icesik@altlinux.org> 0.73-alt1
- 0.72 -> 0.73
- clean up buildrequires
- add docs

* Sun Dec 24 2006 Igor Zubkov <icesik@altlinux.org> 0.72-alt2
- merge eostapets@ changes
- add libdbus-devel >= 0.94 to buildprereq

* Sat Dec 16 2006 Eugene Ostapets <eostapets@altlinux.org> 0.72-alt1.1
- buildrequires gtk-doc
- separate package with docs

* Mon Dec 04 2006 Igor Zubkov <icesik@altlinux.org> 0.72-alt1
- 0.71 -> 0.72

* Tue Oct 31 2006 Igor Zubkov <icesik@altlinux.org> 0.71-alt1
- Initial build for Sisyphus

