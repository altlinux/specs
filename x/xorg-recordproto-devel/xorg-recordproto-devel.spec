Name: xorg-recordproto-devel
Version: 1.14.2
Release: alt1
Epoch: 1
Summary: X.org RecordProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: recordproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xmlto xorg-sgml-doctools xorg-util-macros

%description
X.org RecordProto protocol headers

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
%dir %_docdir/recordproto
%_docdir/recordproto/*.html
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:1.14.2-alt1
- 1.14.2

* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.14.1-alt1
- 1.14.1

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.14-alt2
- 1.14

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.13.2-alt2
- 1.13.2

* Sat Oct 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.14-alt1
- 1.14

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.13.2-alt1
- separate xorg-x11-proto-devel
