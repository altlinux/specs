Name: xorg-fontsproto-devel
Version: 2.1.2
Release: alt1

Summary: X.org FontsProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: fontsroto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xmlto xorg-sgml-doctools xorg-util-macros

%description
X.org FontsProto protocol headers

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
%dir %_docdir/fontsproto
%_docdir/fontsproto/*.html
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Thu Aug 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.0.2-alt1
- separate xorg-x11-proto-devel
