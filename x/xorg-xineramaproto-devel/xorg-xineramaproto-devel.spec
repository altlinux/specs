Name: xorg-xineramaproto-devel
Version: 1.2.1
Release: alt1
Epoch: 1
Summary: X.org XineramaProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xineramaproto = %version-%release
Conflicts: xorg-x11-proto-devel <= 7.4.0-alt1

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
X.org XineramaProto protocol headers

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--host= \
	--build=

%install
%make DESTDIR=%buildroot install

%files
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Thu Jan 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2.1-alt1
- 1.2.1

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.2-alt2
- 1.2

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1.2-alt2
- 1.1.2

* Sat Oct 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2-alt1
- 1.2

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- separate xorg-x11-proto-devel
