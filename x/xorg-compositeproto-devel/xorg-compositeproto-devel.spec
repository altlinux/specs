Name: xorg-compositeproto-devel
Version: 0.4.2
Release: alt1

Summary: Composite extension protocol specification and header files
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: compositeproto = %version-%release
Conflicts: xorg-x11-proto-devel <= 7.4.0-alt1

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
Composite extension protocol specification and header files

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
%_docdir/compositeproto
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Fri May 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.4-alt1
- separate xorg-x11-proto-devel
