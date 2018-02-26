%def_disable shared
%def_enable static
%def_disable rpath
%def_disable debug

%define Name Kile
%define oname kile
%define prerel b4
Name: kde4-kile
Version: 2.1%prerel
Release: alt1
Summary: LaTeX source editor - TeX shell
Group: Publishing
License: %gpl2plus
URL: http://%name.sourceforge.net
Source: %oname-%version.tar
Patch: %oname-%version-%release.patch
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Requires: kde4graphics-okular
Requires: %_bindir/asy %_bindir/convert %_bindir/dblatex
Requires: %_bindir/bibtex %_bindir/dvipdfm %_bindir/dvipng
Requires: %_bindir/dvips %_bindir/latex %_bindir/latex2html
Requires: %_bindir/lilypond %_bindir/makeindex %_bindir/mpost
Requires: %_bindir/pdflatex %_bindir/pdftex %_bindir/ps2pdf
Requires: %_bindir/tex

BuildRequires(pre): rpm-build-licenses
BuildRequires: doxygen gcc-c++ cmake kde4libs-devel
BuildRequires: libXt-devel libjpeg-devel xml-utils xorg-cf-files

%description
%Name is a program for KDE 4, that integrates many tools needed to
develop documents with LaTeX, in just one application.


%prep
%setup -n %oname-%version
%patch -p1


%build
%K4cmake -DKMIMELNK_INSTALL_DIR=%_K4mimelnk -DKILE_VERSION=%version
%K4make


%install
%K4install

%find_lang --with-kde %oname


%files -f %oname.lang
#%doc AUTHORS ChangeLog README README.cwl %oname-remote-control.txt
%_docdir/%oname-%version
%_bindir/*
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/scalable/apps/*
%_K4xdg_apps/*
%_K4apps/%oname
%_K4conf_update/*
%_K4cfg/*
%_K4mimelnk/text/x-%{oname}*
%_K4dbus_interfaces/*
%_K4doc/*/%oname
%_K4i18n/*/LC_MESSAGES/*.mo

%changelog
* Tue Apr 27 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.1b4-alt1
- build new version

* Sun Mar 14 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.1b3-alt2
- add translations from l10n-kde4 SVN (revision 1055480 from Nov 28)
- fixed force termination when the main window is closed (Fedora#557436, kde#220343)

* Sun Mar 14 2010 Evgeny Sinelnikov <sin@altlinux.ru> 2.1b3-alt1
- build new version for KDE4

* Sun Dec 14 2008 Led <led@altlinux.ru> 2.0.3-alt1
- 2.0.3
- cleaned up spec
- fixed BuildRequires

* Sun Sep 14 2008 Led <led@altlinux.ru> 2.0.2-alt1
- 2.0.2
- updated BuildRequires

* Sat Aug 09 2008 Led <led@altlinux.ru> 2.0.1-alt3
- fixed %name.desktop
- fixed post scripts

* Thu Jun 26 2008 Led <led@altlinux.ru> 2.0.1-alt2
- added Requires (#9379)
- added %name-2.0.1-alt-tools_prio.patch

* Wed Jun 18 2008 Led <led@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Mon Mar 31 2008 Led <led@altlinux.ru> 2.0.1-alt0.1
- 2.0.1rc1
- fixed License

* Fri Feb 15 2008 Led <led@altlinux.ru> 2.0-alt0.1
- 2.0

* Fri Feb 15 2008 Led <led@altlinux.ru> 1.9.3-alt0.1
- 1.9.3
- cleaned up spec

* Mon Sep 25 2006 Mikerin Sergey <mikcor@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Tue Jul 04 2006 Mikerin Sergey <mikcor@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Wed Mar 22 2006 Mikerin Sergey <mikcor@altlinux.ru> 1.9-alt1
- 1.9
- new buildrequires

* Tue May 03 2005 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.8-alt0.1.b2
- 1.8b2

* Thu Jan 20 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.7.1-alt1.1.1
- Rebuilt with libstdc++.so.6.

* Wed Nov 17 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.7.1-alt1.1
- remove conflict files

* Fri Oct 22 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Wed Jun 02 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Sun Jan 25 2004 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6-alt3
- fix builrequires

* Sun Dec 14 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6-alt2
- rebuilding without *.la

* Thu Nov 13 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.6-alt1
- 1.6
- new buildrequires and rebuilding in hasher

* Fri Aug 22 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Wed May 21 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.5-alt1
- 1.5

* Wed Mar 12 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.4-alt1
- 1.4

* Mon Jan 20 2003 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.32-alt1
- 1.32
- new buildrequires

* Sun Dec 22 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.31-alt1
- 1.31

* Mon Oct 14 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.3beta-alt1
- 1.3beta

* Tue Sep 17 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2-alt1
- new version
- built with gcc3.2

* Mon Jun 17 2002 Yehuda Ben-Yosef <ilar@altlinux.ru> 1.0-alt1
- 1.0

- specfile cleanup

