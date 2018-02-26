Name: xorg-randrproto-devel
Version: 1.3.2
Release: alt1
Serial: 1
Summary: X Resize and Rotate protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: randrproto = %version-%release
Conflicts: xorg-x11-proto-devel <= 7.4.0-alt1

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
X Resize and Rotate protocol headers

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
%_docdir/randrproto
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.2-alt1
- 1.3.2

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.1-alt2
- 1.3.1

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.3.0-alt2
- 1.3.0

* Tue Oct 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Fri Mar 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Tue Jan 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.99.3-alt1
- 1.3 RC3

* Thu Jul 03 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.1-alt1
- separate xorg-x11-proto-devel
