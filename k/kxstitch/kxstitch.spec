Name: kxstitch
Version: 0.8.4.1
Release: alt2.1

Summary: Cross stitch patterns editor
License: GPL
Group: Toys

Url: http://kxstitch.sourceforge.net
Source: http://dl.sf.net/kxstitch/%name-%version.tar.gz
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

# Automatically added by buildreq on Sat Jun 23 2007
BuildRequires: gcc-c++ imake kdelibs-devel libdnet-devel libImageMagick-devel libjpeg-devel libXext-devel libXt-devel qt3-designer xml-utils xorg-cf-files

Requires: ImageMagick

%description
KXStitch allows the creation and editing of cross stitch patterns.

%prep
%setup
subst "s|%_datadir/man|\\\$(mandir)|g;" kxstitch/Makefile*

%build
%add_optflags -I%_includedir/tqtinterface
unset QTDIR ||: ; . /etc/profile.d/qt3dir.sh
%K3configure  --with-extra-includes=%_includedir/ImageMagick
%make_build

%install
unset QTDIR ||: ; . /etc/profile.d/qt3dir.sh
%K3install
%K3find_lang %name
for d in %buildroot%_K3datadir/doc/HTML/*; do
    l=$(basename "$d")
    c=${l:0:2}
    echo "%%lang($c) %_K3datadir/doc/HTML/$l" >> %name.lang
done

%files -f %name.lang
%doc AUTHORS ChangeLog README TODO
%doc %_man1dir/kxstitch*
%_K3bindir/kxstitch
%_K3datadir/apps/kxstitch/
%_K3datadir/applnk/Graphics/kxstitch.desktop
%_K3datadir/mimelnk/application/kxstitch.desktop
%_K3datadir/icons/*/*/apps/kxstitch.png
%_K3datadir/config.kcfg/kxstitch.kcfg

%changelog
* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.8.4.1-alt2.1
- Rebuild with new libImageMagick

* Fri Mar 04 2011 Timur Aitov <timonbl4@altlinux.org> 0.8.4.1-alt2
- move to alternate place

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 0.8.4.1-alt1.1
- rebuild with new ImageMagick

* Fri Aug 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4.1-alt1
- 0.8.4.1

* Wed Jul 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt2
- rebuild with new ImageMagick

* Mon Apr 12 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.4-alt1
- 0.8.4

* Tue Jun 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.3.1-alt2
- rebuild with new imagemagick

* Tue Mar 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.3.1-alt1
- 0.8.3.1

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 0.8.1-alt1
- 0.8.1 (thx at@)

* Wed Jun 27 2007 Michael Shigorin <mike@altlinux.org> 0.8-alt2
- added Requires: ImageMagick (for image import),
  thanks Alexey Morozov (morozov@) for a hint

* Sat Jun 23 2007 Michael Shigorin <mike@altlinux.org> 0.8-alt1
- built for ALT Linux
- relatively minor spec cleanup

* Fri Jan 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Thu Mar 30 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-2
- Simplify buildequirements: kdelibs-devel already requires xorg-x11-devel/XFree86-devel

* Fri Jun 11 2004 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Initial package.
