Name: xorg-dmxproto-devel
Version: 2.3.1
Release: alt1
Serial: 1
Summary: X.org DMXProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: dmxproto = %version-%release
Conflicts: xorg-x11-proto-devel <= 7.4.0-alt1

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
X.org DMXProto protocol headers

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
* Thu Jan 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3.1-alt1
- 2.3.1

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.3-alt2
- 2.3

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.2.2-alt2
- 2.2.2

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.3-alt1
- 2.3

* Fri May 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 2.2.2-alt1
- separate xorg-x11-proto-devel
