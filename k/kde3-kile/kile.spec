%def_disable shared
%def_enable static
%def_disable rpath
%def_disable debug
%def_without arts

%define Name Kile
%define oname kile
Name: kde3-kile
Version: 2.0.3
%define prerel %nil
Release: alt3
Summary: LaTeX source editor - TeX shell
Group: Publishing
License: %gpl2plus
URL: http://%name.sourceforge.net
Source: %oname-%version%prerel.tar
Patch: %oname-%version-%release.patch
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Requires: libkbibtexpart3
Requires: kdegraphics-kghostview kdegraphics-kpdf kdegraphics-kview kdegraphics-kdvi
Requires: %_bindir/asy %_bindir/convert %_bindir/dblatex
Requires: %_bindir/bibtex %_bindir/dvipdfm %_bindir/dvipng
Requires: %_bindir/dvips %_bindir/latex %_bindir/latex2html
Requires: %_bindir/lilypond %_bindir/makeindex %_bindir/mpost
Requires: %_bindir/pdflatex %_bindir/pdftex %_bindir/ps2pdf
Requires: %_bindir/tex

BuildRequires(pre): rpm-build-licenses
BuildRequires: doxygen gcc-c++ imake kdelibs-devel libdnet-devel
BuildRequires: libXt-devel libjpeg-devel xml-utils xorg-cf-files

Conflicts: kile >= 2.1
Conflicts: kde4-kile

%description
%Name is a program for KDE 3, that integrates many tools needed to
develop documents with LaTeX, in just one application.


%prep
%setup -n %oname-%version%prerel
%patch -p1


%build
sh admin/cvs.sh dist
%configure \
    %{subst_enable rpath} \
    %{subst_enable shared} \
    %{subst_enable static} \
    %{subst_with   arts} \
%if_enabled debug
    --enable_debug=full
%else
    --disable-debug
%endif

%make_build

bzip2 --best --keep --force ChangeLog

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_docdir/%oname-%version
install AUTHORS ChangeLog.* README README.cwl TODO %oname-remote-control.txt \
    %buildroot%_docdir/%oname-%version/

%find_lang --with-kde %oname


%files -f %oname.lang
#doc AUTHORS ChangeLog.* README README.cwl TODO %oname-remote-control.txt
%_docdir/%oname-%version
%_bindir/*
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/scalable/apps/*
%_datadir/applications/kde/*
%_datadir/apps/%oname
%_datadir/apps/kconf_update/*
%_datadir/config.kcfg/*
%_datadir/mimelnk/text/x-%{oname}*


%changelog
* Tue Nov 05 2013 Evgeny Sinelnikov <sin@altlinux.ru> 2.0.3-alt3
- Update automake higher check version for admin/cvs.sh to 1.14

* Sun Jun 23 2013 Evgeny Sinelnikov <sin@altlinux.ru> 2.0.3-alt2
- Build with Trinity libraries
- Using with kdvi and libkbibtex for Qt3 and KDE3 build with Trinity

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

