Name: python-module-compizconfig
Version: 0.8.4
Release: alt3

Summary: Compiz configuration system bindings
License: GPL
Group: System/X11
Url: http://www.compiz-fusion.org/

Provides: compizconfig-python = %version-%release
Obsoletes: compizconfig-python < %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ glib2-devel libSM-devel libXcomposite-devel libXdamage-devel
BuildRequires: libXinerama-devel libXrandr-devel libcompizconfig-devel
BuildRequires: libstartup-notification-devel libxslt-devel python-module-Pyrex

%description
Compiz configuration system bindings.

%package devel
Summary: Development file for %name
Group: Development/C
Requires: %name = %version-%release
Provides: compizconfig-python-devel = %version-%release
Obsoletes: compizconfig-python-devel < %version-%release

%description devel
Development file for %name

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

rm -f %buildroot%python_sitelibdir/compizconfig.la

%files
%python_sitelibdir/*.so

%files devel
%_pkgconfigdir/*.pc

%changelog
* Sat Apr 14 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.8.4-alt3
- restore compiz in Sisyphus

* Sun Sep 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt2
- fixed build for latest Pyrex

* Wed Oct 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Tue Mar 10 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.8.2-alt1
- 0.8.2

* Sat Feb 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.8-alt2
- rename to python-module-compizconfig

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

