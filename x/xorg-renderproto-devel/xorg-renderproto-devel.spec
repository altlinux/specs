Name: xorg-renderproto-devel
Version: 0.11.1
Release: alt3
Summary: X.org RenderProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: renderproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
X.org RenderProto protocol headers

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
%doc renderproto.txt
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.11.1-alt3
- build as noarch

* Fri Apr 22 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.11.1-alt2
- updated build dependencies

* Wed Aug 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Wed Jul 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.11-alt1
- 0.11

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt1
- separate xorg-x11-proto-devel
