Name: gnubik
Version: 2.4.3
Release: alt1

Summary: An interactive, graphic Magic cube program
License: GPL
Group: Games/Puzzles
Url: http://www.gnu.org/software/gnubik/

Source0: %name-%version.tar
Source1: %name.desktop

BuildRequires: pkgconfig(gl) pkgconfig(glu) pkgconfig(gtk+-2.0) pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gdkglext-1.0) pkgconfig(glut)
BuildRequires: guile-devel >= 2.0 texinfo

%description
gnubik - an interactive, graphic Magic cube program.

%prep
%setup
sed -i s,guile-2\.0,guile-2.2, configure.ac

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -pm644 -D %SOURCE1 %buildroot%_desktopdir/gnubik.desktop
install -pm644 -D doc/%name.6 %buildroot%_man6dir/%name.6

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO THANKS
%_bindir/gnubik
%_desktopdir/gnubik.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/gnubik
%_infodir/gnubik.*
%_man6dir/gnubik.*

%changelog
* Wed Nov 21 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.3-alt1
- 2.4.3 released

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1.1
- NMU: added BR: texinfo

* Sat Jun 15 2013 Fr. Br. George <george@altlinux.ru> 2.4.1-alt1
- Autobuild version bump to 2.4.1
- Package icons

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.3-alt1.qa3
- NMU: rebuilt for debuginfo.

* Mon Dec 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.3-alt1.qa2
- NMU (by repocop): the following fixes applied:
  * secondary menu category for gnubik

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for gnubik
  * postclean-05-filetriggers for spec file

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 2.3-alt1
- 2.3

* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 2.2-alt4
- apply patch from repocop

* Fri Jun 08 2007 Igor Zubkov <icesik@altlinux.org> 2.2-alt3
- sync with debian gnubik_2.2-7.diff (add desktop file)

* Wed May 03 2006 Igor Zubkov <icesik@altlinux.ru> 2.2-alt2
- fix rebuild with new ld (by -Wl,--no-as-needed)
- buildreq

* Thu Jan 26 2006 Igor Zubkov <icesik@altlinux.ru> 2.2-alt1
- Initial build for Sisyphus
