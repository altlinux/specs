Name: sirius
Version: 0.8.0
Release: alt2.2

Summary: Othello game
Summary (ru_RU.UTF-8): Игра реверси
License: GPL
Group: Games/Boards
Url: http://sirius.bitvis.nu
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %name-%version.tar.gz
Patch0: fix.patch
Patch1: %name.desktop.in.patch
Patch2: %name-0.8.0-alt-DSO.patch
BuildRequires: ORBit2-devel xorg-libs esound-devel fontconfig freetype2 glib2-devel glibc-devel-static gnome-vfs2-devel libGConf2-devel libalsa-devel libart_lgpl-devel libatk-devel libaudiofile-devel libbonobo2-devel libbonoboui-devel libexpat libgnome-devel libgnomecanvas-devel libgnomeui-devel libgtk+2-devel libjpeg-devel libpango-devel libpopt-devel libssl-devel libxml2-devel pkgconfig rootfiles zlib-devel

BuildPreReq: libX11-devel libSM-devel libICE-devel

%description
Sirius is a program for playing the game of othello. The program includes 
an AI (Artificial Intelligence) opponent which plays at a very challenging 
level and is actually quite hard to beat. The AI opponent's strength can 
therefore be adjusted in several ways to give you a suitable opponent.

%description -l ru_RU.UTF-8
Программа "Сириус" предназначена для игры в реверси. Она даёт возможность 
сразиться с компьютерным противником, способным играть на очень высоком уровне.
Победить компьютер нелегко. Поэтому, чтобы уравновесить силы, уровень игры 
компьютера можно настраивать несколькими способами.

%prep
%setup
%patch0
%patch1
%patch2 -p2

%build
%configure
%make

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name
%_datadir/pixmaps/%name
%_datadir/pixmaps/%name.png
%_datadir/applications/%name.desktop
%doc README ChangeLog

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.2
- Fixed build

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2.1
- Fixed build

* Sun Dec 27 2009 Ilya Mashkin <oddity@altlinux.ru> 0.8.0-alt2
- fix requires
- remove menu file
- fix desktop file (Closes: #22521)

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.0-alt1.2.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for sirius
  * postclean-05-filetriggers for spec file

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 0.8.0-alt1.2
- rebuild
- update requires

* Wed May 12 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.0-alt1.1
- Rebuilt with openssl-0.9.7d.

* Sat Oct 18 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Tue Jul 01 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.7.0-alt1
- ALTLinux build, i18n hacks
