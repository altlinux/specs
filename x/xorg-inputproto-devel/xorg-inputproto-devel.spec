Name: xorg-inputproto-devel
Version: 2.2
Release: alt1
Epoch: 1
Summary: X.org InputProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: inputproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: asciidoc xorg-util-macros

%description
X.org InputProto protocol headers

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
%_docdir/inputproto
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Mon Mar 05 2012 Valery Inozemtsev <shrek@altlinux.ru> 1:2.2-alt1
- 2.2

* Fri Dec 16 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.1-alt1
- 2.1

* Fri Jun 10 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.2-alt1
- 2.0.2

* Thu Nov 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0.1-alt1
- 2.0.1

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:2.0-alt2
- 2.0

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 1:1.5.1-alt2
- 1.5.1

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.0-alt1
- 2.0

* Thu Jun 18 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Fri Nov 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Sun Aug 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.4-alt1
- 1.4.4

* Wed Jul 09 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.3-alt3
- returned lost define sz_xGetExtensionVersionReq, sz_xGetExtensionVersionReply

* Mon Jun 30 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.3-alt2
- define XEventClass in terms of unsigned int, not CARD32

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.3-alt1
- separate xorg-x11-proto-devel
