Name: xorg-xf86bigfontproto-devel
Version: 1.2.0
Release: alt1

Summary: X.org XF86BigFontProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xf86bigfontproto = %version-%release
Conflicts: xorg-x11-proto-devel <= 7.4.0-alt1

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xorg-util-macros

%description
X.org XF86BigFontProto protocol headers.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%install
%make DESTDIR=%buildroot install

%files
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Thu Aug 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- separate xorg-x11-proto-devel
