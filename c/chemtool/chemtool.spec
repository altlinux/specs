Name: chemtool
Version: 1.6.13
Release: alt1

%define pre %nil

Summary: A program for 2D drawing organic molecules
License: GPL
Group: Sciences/Chemistry

Url: http://ruby.chemie.uni-freiburg.de/~martin/chemtool
Source0: %url/%name-%version%pre.tar.gz
Source1: %name.desktop
Source2: %name.menu
Patch: chemtool-cht.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): Программа для рисования двумерных органических структур
Summary(uk_UA.KOI8-U): Програма для малювання двовим╕рних орган╕чних структур
Summary(pl): Program do rysowania 2-wymiarowych cz╠steczek organicznych.

# should be generalized?
%define _applnkdir %_datadir/applnk
%define desktop_cat Edutainment/Science

# Automatically added by buildreq on Sun Dec 13 2009
BuildRequires: imake libEMF-devel libXt-devel libgtk+2-devel xorg-cf-files

# actually soft requires but better get them here than not...
Requires: openbabel transfig

%description
A program for drawing organic molecules easily and store
them as a X bitmap, Xfig or EPS file. It runs under the
X Window System using the GTK widget set.

%description -l ru_RU.KOI8-R
Программа для удобного рисования органических молекул и
сохранения их в различных форматах, использующая gtk+.

%description -l uk_UA.KOI8-U
Програма для зручного малювання орган╕чних молекул та
збереження ╖х у р╕зних форматах, що використову╓ gtk+.

%description -l pl
Programem do rysowania cz╠steczek organicznych i zapisu
ich jako pliki X-bitmap, Xfig lub EPS. Pracuje pod X Window
u©ywaj╠c bibliotek GTK.

%prep
%setup
%patch -p1

%build
%configure --enable-undo --enable-emf
%make_build

%install
%makeinstall_std
install -d %buildroot%_datadir/mime-info/
install -pm644 gnome/mime-types/* %buildroot%_datadir/mime-info/
install -pDm644 kde/mimelnk/application/x-chemtool.desktop \
	%buildroot%_datadir/mimelnk/application/x-chemtool.desktop
install -pDm644 kde/icons/hicolor/32x32/mimetypes/chemtool.png \
	%buildroot%_iconsdir/hicolor/32x32/mimetypes/chemtool.png
install -pDm644 gnome/gnome-application-chemtool.png \
	%buildroot%_liconsdir/gnome-application-chemtool.png
install -pDm644 %name.xpm %buildroot%_niconsdir/%name.xpm
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
%find_lang %name

%files -f %name.lang
%doc ChangeLog README TODO examples/
%_bindir/*
%_man1dir/*
%_datadir/mimelnk/application/*
%_datadir/icons/hicolor/32x32/mimetypes/*.png
%_datadir/mime-info/*
%_liconsdir/*.png
%_niconsdir/*.xpm
%_desktopdir/*.desktop

%changelog
* Sat Dec 24 2011 Michael Shigorin <mike@altlinux.org> 1.6.13-alt1
- 1.6.13

* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 1.6.12-alt1
- 1.6.12
- built with libEMF
- description cleanup
- repocop cleanup

* Sat Aug 01 2009 Michael Shigorin <mike@altlinux.org> 1.6.11-alt7
- *applied* repocop patch
- fixed desktop file once again

* Thu Jul 30 2009 Michael Shigorin <mike@altlinux.org> 1.6.11-alt6
- applied repocop patch
- desktop file moved to proper location and fixed (thx PLD)
- spec cleanup

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 1.6.11-alt5
- added Packager:
- minor spec cleanup

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.6.11-alt4
- applied repocop patch

* Sat May 31 2008 Michael Shigorin <mike@altlinux.org> 1.6.11-alt3
- added patch by Pasha Solntsev <solntsev/univ.kiev.ua>
  to supply .cht file extension if missing (#15636)

* Wed Oct 17 2007 Michael Shigorin <mike@altlinux.org> 1.6.11-alt2
- moved from Scientific/Chemistry to Edutainment/Science
  (fixes #13145)
- removed Debian menu file

* Tue Aug 28 2007 Michael Shigorin <mike@altlinux.org> 1.6.11-alt1
- 1.6.11 (major bugfixes)

* Tue Apr 24 2007 Michael Shigorin <mike@altlinux.org> 1.6.10-alt1
- 1.6.10

* Tue Oct 24 2006 Michael Shigorin <mike@altlinux.org> 1.6.10-alt0.1
- 1.6.10pre
- build problems with gcc-4.1/glibc-2.5 fixed upstream
- macro abuse cleanup

* Sat Aug 05 2006 Michael Shigorin <mike@altlinux.org> 1.6.9-alt1
- new version 1.6.9 (with rpmrb script)

* Wed Feb 08 2006 Michael Shigorin <mike@altlinux.org> 1.6.8-alt1
- 1.6.8
- should work with OpenBabel 2.0

* Mon Feb 06 2006 Michael Shigorin <mike@altlinux.org> 1.6.7-alt2
- s/xorg-x11-devel-static/xorg-x11-devel/

* Thu Aug 04 2005 Michael Shigorin <mike@altlinux.org> 1.6.7-alt1
- 1.6.7
  + 1.6.5a fixed last-minute crash bug in MDL loader... missed that :(
  + gtk2 bugfixes
  + some backports from 1.7.x, including SVD adjustments
    and SXD export with fig2sxd
- updated buildrequires
- built against gtk2

* Tue Feb 08 2005 Michael Shigorin <mike@altlinux.ru> 1.6.5-alt1
- 1.6.5

* Mon Feb 07 2005 Michael Shigorin <mike@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Mon Jul 07 2003 Michael Shigorin <mike@altlinux.ru> 1.6-alt1
- 1.6
- images relocated (thanks to Denis G. Samsonenko <earthsea@ngs.ru>
- spec cleanup

* Fri Jun 27 2003 Michael Shigorin <mike@altlinux.ru> 1.6-alt0.1
- 1.6rc
- destdir patch unneeded, but ru.po got updated

* Fri Apr 25 2003 Michael Shigorin <mike@altlinux.ru> 1.5-alt0.1
- built for ALT Linux
- spec adapted from PLD <feedback@pld.org.pl> (1.5-2)
  All persons listed below can be reached at <cvs_login>@pld.org.pl
  blues, kloczek
- spec cleanup
- may need some MIME/applnk check, didn't bother :(
