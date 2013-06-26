%define Name KBibTeX
%define oname kbibtex

Name: kbibtex
Version: 0.4.1
Release: alt1
Summary: A BibTeX editor for Qt4 and KDE4
License: %gpl2plus
Group: Publishing
URL: http://home.gna.org/%oname
Source: http://download.gna.org/kbibtex/0.4/%oname-%version.tar
#Patch: %oname-%version-%release.patch
#Requires: lib%{oname}part4 = %version-%release
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ kde4libs-devel libpoppler-qt4-devel 
BuildRequires: libxslt-devel xml-utils xorg-cf-files
BuildRequires: libpoppler-qt4-devel

Conflicts: kde3-kbibtex

%description
%Name is a BibTeX editor for Qt4 and KDE4 to edit bibliographies
used with LaTeX. Features include comfortable input masks, starting
web queries (e. g. Google or PubMed) and exporting to PDF, PostScript,
RTF and XML/HTML. As %Name is using KDE's KParts technology.


%package -n lib%{oname}part4
Summary: %Name KParts BibTeX library for Qt4 and KDE4
Group: System/Libraries
Conflicts: lib%{oname}part3

%description -n lib%{oname}part4
%Name is a BibTeX library for Qt4 and KDE4 to edit bibliographies
used with LaTeX. Features include comfortable input masks, starting
web queries (e. g. Google or PubMed) and exporting to PDF, PostScript,
RTF and XML/HTML. This package contains KDE's KParts technology library.


%prep
%setup -n %oname-%version
#patch -p1


%build
%K4build


%install
%K4cmake
%K4install

%find_lang --with-kde %oname


%files -f %oname.lang
%doc LICENSE README TODO
%_bindir/*
%_man1dir/*
%_K4xdg_apps/*
%_K4xdg_mime/*
%_K4apps/%oname
%_iconsdir/*/*/apps/*


%files -n lib%{oname}part4
%_libdir/*.so
%_K4lib/*.so
%_K4srv/*
%_K4apps/%{oname}part
%_K4conf/*


%changelog
* Wed Jun 26 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.4.1-alt1
- build last stable release for Qt4 and KDE4

* Mon Jun 24 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.2.3.91-alt1
- update to last stable release for Qt3 and KDE3

* Sun Jun 23 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.2.3-alt2
- build with Trinity libraries

* Wed Aug 26 2009 Sergey V Turchin <zerg@altlinux.org> 0.2.3-alt1
- new version

* Wed Mar 11 2009 Led <led@altlinux.ru> 0.2.1.91-alt1
- 0.2.2.91 (0.2.2 Beta 2)

* Sun Feb 01 2009 Led <led@altlinux.ru> 0.2.1.90-alt1
- 0.2.2.90 (0.2.2 Beta 1)

* Sun Dec 28 2008 Led <led@altlinux.ru> 0.2.1.81-alt1
- 0.2.1.81
- cleaned up spec

* Sun Oct 26 2008 Led <led@altlinux.ru> 0.2.1.80-alt2
- fixed build with g++ 4.3

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.2.1.80-alt1
- 0.2.1.80
- updated kbibtex-0.2.1.80-alt-makefile.patch
- added kbibtex-0.2.1.80-alt-format.patch

* Thu Jun 26 2008 Led <led@altlinux.ru> 0.2.1-alt1
- initial build
