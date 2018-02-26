Name: xorg-bigreqsproto-devel
Version: 1.1.2
Release: alt1
Epoch: 1
Summary: X.org BigReqsProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: bigreqsproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xmlto xorg-util-macros xorg-sgml-doctools

%description
X.org BigReqsProto protocol headers

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
%dir %_docdir/bigreqsproto
%_docdir/bigreqsproto/*.html
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.2-alt1
- 1.1.2

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.1-alt1
- 1.1.1

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.0-alt2
- 1.1.0

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0.2-alt2
- 1.0.2

* Thu Aug 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Fri May 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- separate xorg-x11-proto-devel
