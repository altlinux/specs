Name: xorg-scrnsaverproto-devel
Version: 1.2.2
Release: alt1

Summary: X.org ScrnSaverProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: scrnsaverproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xmlto xorg-sgml-doctools xorg-util-macros

%description
X.org ScrnSaverProto protocol headers

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--build= \
	--host=

%install
%make DESTDIR=%buildroot install

%files
%dir %_docdir/scrnsaverproto
%_docdir/scrnsaverproto/*.html
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Tue Aug 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- separate xorg-x11-proto-devel
