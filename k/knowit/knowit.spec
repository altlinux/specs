%define qtdir %_qt3dir
%define kdedir %_K3prefix

Name: knowit
Version:0.10
Release:alt10

Summary: Knowledge management program for KDE
License: GPL
Group: Editors

Url: http://knowit.sourceforge.net
Source0: %name-%version.tar.bz2
Source1: %name.desktop

Patch0: tde-3.5.13-build-defdir-autotool.patch

BuildRequires(pre): kdelibs-devel
BuildRequires: gcc-c++ imake libXt-devel libjpeg-devel libqt3-devel xml-utils xorg-cf-files

%description
KnowIt is a simple tool for managing notes. It is similar
to TuxCards, but KDE-based. Notes are organized in tree-like
hierarchy, texts are in RichText format, so bold, italic and
lists are supported, with more to come.

KnowIt should handle any characters properly, as files are saved
in UTF8 and KDE takes care of proper display for current
language/charset.

%prep
%setup
%patch0
# sed -i "s/\.la\"/\.so\"/g" configure

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%kdedir

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

#add_optflags -I%_includedir/tqtinterface
%K3configure --disable-rpath
%make

%install
%K3install
install -pD %SOURCE1 %buildroot/%_desktopdir/%name.desktop
%K3find_lang --with-kde %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog README NEWS TODO
%_K3bindir/%name
%_desktopdir/%name.desktop
%_kde3_iconsdir/*/*/*/%name.png
%_K3apps/%name

%changelog
* Thu Feb 23 2012 Roman Savochenko <rom_as@altlinux.ru> 0.10-alt10
- Build for TDE 3.5.13 release

* Tue Apr 26 2011 Andrey Cherepanov <cas@altlinux.org> 0.10-alt9.1
- Fix building

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 0.10-alt9
- applied repocop patch
- minor spec cleanup

* Thu Sep 25 2008 Michael Shigorin <mike@altlinux.org> 0.10-alt8
- buildreq
- spec cleanup

* Wed Apr 02 2008 Nick S. Grechukh <gns@altlinux.org> 0.10-alt7
- desktopdb post/postun, as suggested by repocop

* Mon Dec 31 2007 Nick S. Grechukh <gns@altlinux.ru> 0.10-alt5
- fixed path to icon; fixed menu category

* Mon Mar 27 2006 Nick S. Grechukh <gns@altlinux.org> 0.10-alt4.1
- removed kdedesktop2mdkmenu.pl. .desktop file moved to %_desktopdir

* Mon Oct 24 2005 Nick S. Grechukh <gns@altlinux.org> 0.10-alt4.0
- fixed %_datadir/locale (now using find_lang)

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.10-alt3.1
- Rebuilt with libstdc++.so.6.

* Wed Jun 02 2004 Nick S. Grechukh <gns@altlinux.ru> 0.10-alt3
- menu group changed to Accessibility. Added buildreq.

* Wed Jun 02 2004 Nick S. Grechukh <gns@altlinux.ru> 0.10-alt2
- added menu entry

* Wed Jun 02 2004 Nick S. Grechukh <gns@altlinux.ru> 0.10-alt1
- first Sisyphus build

