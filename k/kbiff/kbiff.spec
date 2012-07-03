%define qtdir %_qt3dir
%define _optlevel s

Name: kbiff
Version: 3.9
Release: alt4

Group: Graphical desktop/KDE
Summary: Kbiff is a new mail notification utility
Url: http://kbiff.granroth.org
License: GPL

Requires: %{get_dep kdelibs}

Source0: %name-%version.tar.bz2
Source1: kbiff-ru.po
Source2: admin.tar.gz

Patch1: kbiff-3.7-alt_default_settings.patch
Patch2: kbiff-3.7-alt_autostart.patch
Patch3: kbiff-3.9-alt-makefile.patch

# Automatically added by buildreq on Tue Feb 07 2006
#BuildRequires: fontconfig freetype2 gcc-c++ gcc-java imake kde-settings kdelibs-devel libICE-devel libSM-devel libX11-devel libXext-devel libXt-devel libarts-devel libjpeg-devel libpng-devel libqt3-devel libqt3-settings libstdc++-devel linux-libc-headers qt3-designer xml-utils xorg-cf-files xorg-x11-proto-devel zlib-devel
BuildRequires: gcc-c++ kdelibs-devel
BuildRequires: libjpeg-devel libpng-devel libqt3-devel libstdc++-devel xml-utils zlib-devel

%description
KBiff is a "biff", or new mail notification utility. It is highly configurable
but very easy to use and set up. It tries to combine the best of the features of
most of the "other" biff programs out there. KBiff supports all major mailbox
formats: mbox (Berkely style), maildir, mh, POP3, IMAP4 and NNTP.

%prep
%setup -q -a2
%patch1 -p1
%patch2 -p1
%patch3 -p1

rm -f po/*.gmo
pushd po
install -m 0644 %SOURCE1 ru.po
#for f in *.po
#do
#    cp $f "$f".tmp
#    CCHARSET=`grep charset "$f".tmp| sed "s/^.*charset=//"| sed "s/\\\\\\.*//"`
#    iconv -f$CCHARSET -tUTF-8 "$f".tmp -o $f ||:
#    rm -f "$f".tmp
#    subst "s/charset\=$CCHARSET/charset=UTF-8/" $f
#done
popd

#subst "s/\(Wl,--no-undefined\)/ -Wl,--allow-shlib-undefined \1/g" admin/acinclude.m4.in
#subst "s/\-lkdeui/-lkdeui -lpthread/g" admin/acinclude.m4.in
#subst "s/\.la/.so/g" admin/acinclude.m4.in
make -f admin/Makefile.common cvs ||:


%build
export QTDIR=%qtdir
%add_optflags -I%_includedir/tqtinterface
%K3configure \
	--enable-ssl \
	--enable-final

%make_build

%install
mkdir -p %buildroot/%_K3datadir/config/
%K3install

install -d %buildroot/%_K3datadir/autostart/
install -m644 %buildroot/%_K3datadir/applnk/Internet/%name.desktop %buildroot/%_K3datadir/autostart/%name.desktop

# fix .po names
#for f in %buildroot/%_datadir/locale/*/*/*.mo; do
#    mv $f `dirname $f`/%name.mo
#done

%K3find_lang --with-kde %name


%files -f %name.lang
%doc AUTHORS ChangeLog README
%doc %_man1dir/%{name}*
#
%_K3bindir/*
%_K3libdir/libkdeinit_*.so
%_K3lib/kbiff.so
#
%_K3datadir/apps/%name
%_K3datadir/icons/*/*/*/*
#
%_K3datadir/autostart/%name.desktop
%_K3datadir/applnk/Internet/*.desktop

%changelog
* Tue Apr 26 2011 Sergey V Turchin <zerg@altlinux.org> 3.9-alt4
- move to alternate place

* Tue Feb 01 2011 Sergey V Turchin <zerg@altlinux.org> 3.9-alt3
- fix to build with kde-3.5.12

* Mon Mar 01 2010 Sergey V Turchin <zerg@altlinux.org> 3.9-alt2
- fix to build with new autotools

* Mon Jul 06 2009 Sergey V Turchin <zerg@altlinux.org> 3.9-alt1
- new version

* Tue Dec 25 2007 Sergey V Turchin <zerg at altlinux dot org> 3.8-alt2
- fixed build with new autotools

* Tue Feb 07 2006 Sergey V Turchin <zerg at altlinux dot org> 3.8-alt1
- new version

* Mon Jan 24 2005 Sergey V Turchin <zerg at altlinux dot org> 3.7.1-alt4
- rebuild with gcc3.4

* Thu Jul 15 2004 Sergey V Turchin <zerg at altlinux dot org> 3.7.1-alt2
- fix menufile

* Tue Jul 13 2004 Sergey V Turchin <zerg at altlinux dot org> 3.7.1-alt1
- new version

* Fri Mar 26 2004 Sergey V Turchin <zerg at altlinux dot org> 3.7-alt3
- rebuild with new KDE

* Wed Oct 29 2003 Sergey V Turchin <zerg at altlinux dot org> 3.7-alt2
- turn off autostart by default
- fix non-UTF8 translations files

* Mon Oct 27 2003 Sergey V Turchin <zerg at altlinux dot org> 3.7-alt1
- new version
- add autostart by default

* Fri Mar 28 2003 Sergey V Turchin <zerg@altlinux.ru> 3.6.3-alt1
- new version

* Tue Nov 05 2002 Sergey V Turchin <zerg@altlinux.ru> 3.6.2-alt1
- new version

* Thu Sep 12 2002 Sergey V Turchin <zerg@altlinux.ru> 3.6.1-alt2
- rebuild with gcc3.2 && objprelink

* Fri Apr 26 2002 Sergey V Turchin <zerg@altlinux.ru> 3.6.1-alt1
- new version
- build with KDE3

* Fri Jan 18 2002 Sergey V Turchin <zerg@altlinux.ru> 3.5.4-alt2
- rebuild without fam

* Wed Nov 14 2001 Sergey V Turchin <zerg@altlinux.ru> 3.5.4-alt1
- new version

* Tue Oct 30 2001 Sergey V Turchin <zerg@altlinux.ru> 3.5.2-alt1
- new version

* Thu Oct 11 2001 Sergey V Turchin <zerg@altlinux.ru> 3.4.2-alt2
- rebuild with new libpng

* Wed Jun 27 2001 Sergey V Turchin <zerg@altlinux.ru> 3.4.2-alt1
- build for ALT

* Tue May 22 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4.2-2mdk
- Update code (3.4.2)

* Tue Apr 10 2001 David BAUDENS <baudens@mandrakesoft.com> 3.4-4mdk
- Move KDE menu entry in %%_datadir/applnk
- Use more macro
- Don't delete usefull links for documentation
- Rebuild against latest GCC

* Sat Mar 31 2001 David BAUDENS <baudens@mandrakesoft.com> 3.4-3mdk
- Fix BuildRequires for non %%ix86 architectures

* Wed Mar 28 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4-2mdk
- Add build requires

* Tue Mar 27 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.4-1mdk
- Update code

* Fri Mar 16 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.2-1mdk
- Update code

* Wed Mar 14 2001 David BAUDENS <baudens@mandrakesoft.com> 3.3.1-2mdk
- Rebuild agains Qt 2.3.0

* Thu Jan 23 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.3.1-1mdk
- Update code

* Thu Dec 07 2000 Laurent Montel <lmontel@mandrakesoft.com> 3.3-2mdk
- Fix package

* Mon Nov 22 2000 Laurent Montel <lmontel@mandrakesoft.com> 3.3-1mdk
- Initial package fix compile with gcc-2.96
