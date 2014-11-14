
%define oname iceB
%define oversion 15_0

Name:    iceb
Version: 15.1
Release: alt1

Summary: Free financial accounting system (console)

Packager: Andrey Cherepanov <cas@altlinux.org>

Group:   Office
License: GPL
Url:     http://iceb.net.ua

Source:  %url/download/%name-%oversion.tar.bz2
Source1: %name
Source3: %name.16.xpm
Source4: %name.32.xpm
Source5: %name.48.xpm
Source6: %name.watch

#Patch:   iceb-fix-overflow-buffer.patch
Patch1:	 %name-12.11-remove-missing-automake-target.patch

BuildRequires: gcc-c++ glib2-devel libMySQL-devel libncursesw-devel

%description
Free financial accounting system.

%prep
%setup -q -c
#%%patch -p2
%patch1 -p2

%build
%autoreconf
%configure \
	--disable-static \
	--with-lang-path=%_datadir/locale \
	--with-lock-dir=/var/lock/serial \
	--with-config-path=%_datadir/%name \
	--with-maxfkeys=10 \
	--with-gnu-ld

%make_build

%install
[ -z "$TMPDIR" ] && TMPDIR=/tmp
FAKEDIR=$TMPDIR/%{name}_tmp_install
mkdir -p $FAKEDIR

%makeinstall \
    CONFDIR=$FAKEDIR \
    ICEB_LANG_PATH=%buildroot/%_datadir/locale/uk \
    bindir=%buildroot/%_libdir/%name/bin \
    libdir=%buildroot/%_libdir/%name

rm -rf $FAKEDIR

%makeinstall CONFDIR=%buildroot/%_datadir/%name/iceb -C buhg/bx
%makeinstall CONFDIR=%buildroot/%_datadir/%name/doc -C buhg/doc

mkdir -p %buildroot%_bindir
install -m 755 %SOURCE1 %buildroot/%_bindir
subst "s|/usr/lib|%_libdir|g" %buildroot/%_bindir/%name
rm -rf %buildroot%_libdir/%name/*.{a,la}

%files
%doc CHANGES TODO
%_bindir/%name
%_libdir/%name/bin
%_datadir/%name

%changelog
* Fri Nov 14 2014 Andrey Cherepanov <cas@altlinux.org> 15.1-alt1
- new version 15.1

* Mon Sep 01 2014 Andrey Cherepanov <cas@altlinux.org> 15.0-alt1
- Nee version

* Mon Jun 02 2014 Andrey Cherepanov <cas@altlinux.org> 14.15-alt1
- New version

* Thu Feb 27 2014 Andrey Cherepanov <cas@altlinux.org> 14.11-alt1
- New version
- Fix project URL

* Sun Apr 07 2013 Andrey Cherepanov <cas@altlinux.org> 12.0-alt3
- Rebuild with new libmysqlclient

* Wed Sep 19 2012 Andrey Cherepanov <cas@altlinux.org> 12.0-alt2
- Fix build

* Thu Sep 01 2011 Andrey Cherepanov <cas@altlinux.org> 12.0-alt1
- New version 12.0

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 9.0-alt1
- build new version, update spec
- disable build html doc

* Fri Jun 18 2004 Sergey V Turchin <zerg at altlinux dot org> 5.60-alt2
- fix menu section

* Tue Feb 03 2004 Sergey V Turchin <zerg at altlinux dot org> 5.60-alt1
- new version

* Tue Sep 30 2003 Sergey V Turchin <zerg at altlinux dot org> 5.35-alt2
- fix build requires

* Fri Sep 13 2002 Sergey V Turchin <zerg@altlinux.ru> 5.35-alt1
- new version
- byuld with gcc3.2

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 5.24-alt2
- add -doc-html package

* Fri Apr 05 2002 Sergey V Turchin <zerg@altlinux.ru> 5.24-alt1
- initial spec
