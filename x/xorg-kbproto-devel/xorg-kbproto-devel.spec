Name: xorg-kbproto-devel
Version: 1.0.6
Release: alt1

Summary: X.org KBProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: kbproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: xmlto xorg-util-macros xorg-sgml-doctools

%description
X.org KBProto protocol headers.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%install
%make DESTDIR=%buildroot install

%files
%dir %_docdir/kbproto
%_docdir/kbproto/*.html
%_docdir/kbproto/*.svg
%_includedir/X11
%_pkgconfigdir/*.pc

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Wed Aug 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Tue Oct 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.3-alt1
- separate xorg-x11-proto-devel
