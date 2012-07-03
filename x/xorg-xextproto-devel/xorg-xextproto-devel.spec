Name: xorg-xextproto-devel
Version: 7.2.1
Release: alt1
Epoch: 2
Summary: X.org XExtProto protocol headers
License: MIT/X11
Group: Development/C
Url: http://xorg.freedesktop.org
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: xextproto = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: xmlto xorg-sgml-doctools xorg-util-macros

%description
X.org XExtProto protocol headers

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
%doc %_docdir/xextproto
%_docdir/xextproto/*.html
%_includedir/X11
%_datadir/pkgconfig/*.pc

%changelog
* Fri Mar 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 2:7.2.1-alt1
- 7.2.1

* Sun Feb 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 2:7.2.0-alt1
- 7.2.0

* Wed Aug 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:7.1.2-alt1
- 7.1.2

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:7.1.1-alt2
- 7.1.1

* Sat Feb 20 2010 Valery Inozemtsev <shrek@altlinux.ru> 2:7.0.5-alt3
- 7.0.5

* Mon Oct 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:7.1.1-alt1
- 7.1.1

* Tue Feb 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:7.0.5-alt2
- 7.0.5

* Mon Feb 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:7.0.4-alt2
- rollback to 7.0.4

* Thu Jan 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 7.0.5-alt1
- 7.0.5

* Thu Dec 18 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.0.4-alt1
- 7.0.4

* Sat May 31 2008 Valery Inozemtsev <shrek@altlinux.ru> 7.0.3-alt1
- separate xorg-x11-proto-devel
