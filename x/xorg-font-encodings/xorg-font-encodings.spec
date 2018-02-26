Name: xorg-font-encodings
Version: 1.0.4
Release: alt1
Summary: Encodings for X.Org fonts
License: MIT/X11
Group: System/X11
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: encodings xorg-x11-font-encodings = %version-%release
Obsoletes: xorg-x11-font-encodings

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires: mkfontscale xorg-font-utils xorg-util-macros

%description
This package contains the encodings that map to specific characters

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--build= \
	--host= \
	--with-encodingsdir=%_datadir/X11/fonts/encodings
%make_build

%install
%make DESTDIR=%buildroot install

%files
%dir %_datadir/X11/fonts
%_datadir/X11/fonts/encodings

%changelog
* Sat Oct 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Thu Jun 05 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt2
- renamed xorg-x11-font-encodings to xorg-font-encodings

* Tue Apr 03 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- move encodings to a separate package (close #11328)
- otherwise mkfontscale picks up non-gzipped files (close #11326)
