Name: compiz-bcop
Version: 0.8.8
Release: alt2
Summary: Compiz option code generator
License: GPL
Group: System/X11
Url: http://www.compiz-fusion.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
BuildRequires: libxslt-devel

%description
Bcop is a tool to autogenerate code for working with options in
compiz plugins.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure

%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/bcop
%_datadir/bcop
%_datadir/pkgconfig/*.pc

%changelog
* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.8-alt2
- restore compiz in Sisyphus

* Thu Apr 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Wed Oct 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Tue Mar 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Tue Sep 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt1
- 0.7.8

* Wed Sep 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.7-alt1
- 0.7.7

* Sun Jun 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.6-alt1
- 0.7.6

* Fri Apr 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Fri Mar 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Wed Jan 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.6.99-alt1
- 0.6.99

* Sun Oct 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Wed Aug 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.2-alt1
- initial release

