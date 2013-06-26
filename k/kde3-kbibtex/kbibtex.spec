%define Name KBibTeX
%define oname kbibtex

Name: kde3-kbibtex
Version: 0.2.3.91
Release: alt1.1
Summary: A BibTeX editor for Qt3 and KDE3 or Trinity
License: %gpl2plus
Group: Publishing
URL: http://www.unix-ag.uni-kl.de/~fischer/%oname
Source: %url/download/%oname-%version.tar
Patch: %oname-%version-%release.patch
Requires: lib%{oname}part3 = %version-%release
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: gcc-c++ imake kdelibs-devel libXt-devel libdnet-devel
BuildRequires: libjpeg-devel libxslt-devel xml-utils xorg-cf-files

Conflicts: kbibtex

%description
%Name is a BibTeX editor for KDE3 or Trinity to edit bibliographies
used with LaTeX. Features include comfortable input masks, starting
web queries (e. g. Google or PubMed) and exporting to PDF, PostScript,
RTF and XML/HTML. As %Name is using KDE's KParts technology.


%package -n lib%{oname}part3
Summary: %Name KParts BibTeX library for Qt3 and KDE3 or Trinity
Group: System/Libraries
Obsoletes: lib%{oname}part < 0.2.3.91
Conflicts: lib%{oname}part4

%description -n lib%{oname}part3
%Name is a BibTeX library for KDE3 or Trinity to edit bibliographies
used with LaTeX. Features include comfortable input masks, starting
web queries (e. g. Google or PubMed) and exporting to PDF, PostScript,
RTF and XML/HTML. This package contains KDE's KParts technology library.


%prep
%setup -n %oname-%version
%patch -p1
touch -mr Makefile.in acinclude.m4 admin/acinclude.m4.in src/Makefile.am

%build
%configure --disable-rpath --without-arts
%make_build
bzip2 --keep --force --best ChangeLog


%install
%make_install DESTDIR=%buildroot install
%find_lang --with-kde %oname


%files -f %oname.lang
%doc AUTHORS BUGS ChangeLog.* NEWS TODO
%_bindir/*
%_man1dir/*
%_desktopdir/kde/*
%_datadir/apps/%oname
%_iconsdir/*/*/apps/*


%files -n lib%{oname}part3
%_libdir/kde3/*.so
%_datadir/services/*
%_datadir/apps/%{oname}part


%changelog
* Wed Jun 26 2013 Evgeny Sinelnikov <sin@altlinux.ru> 0.2.3.91-alt1.1
- adjust buildrequires for sisyphus

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
