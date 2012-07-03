Name: microdc2
Version: 0.15.6
Release: alt7

Summary: A command-line based Direct Connect client
License: GPL
Group: Networking/File transfer
Url: http://corsair626.no-ip.org/microdc/
Packager: Boris Savelev <boris@altlinux.org>

Source: %url%name-%version.tar.gz
Source1: microdc2.desktop
Source2: microdc2.png
Patch: microdc2-ru.patch
Patch1: microdc2-slave-mode.patch
Patch2: %name-%version-libxml2-configure.patch
Patch3: debian-link-system-bz2.patch
BuildPreReq: libreadline-devel libncurses-devel libxml2-devel bzlib-devel

Summary(ru_RU.KOI8-R): Консольный клиент файлообменной системы DirectConnect

%description
microdc is a command-line based Direct Connect client that uses the GNU
Readline library for user interaction. It was developed from ground up and
does not depend on any other program. Despite the command-line user
interface, microdc was designed to be user friendly and simple to use.

microdc is currently in beta state - there may be many bugs not yet
discovered. It also lacks some features that other clients support, such as
file hashing, multiple hub connections, and hub list support.

%description -l ru_RU.KOI8-R
microdc2 - это консольный текстовый клиент для DirectConnect (DC),
популярной пиринговой (P2P, peer-to-peer) файлообменной системы.

microdc2 не поддерживает следующие возможности:
 - списки хабов,
 - одновременное подключение к нескольким хабам,
 - скачивание файлов из нескольких источников по TTH (tiger hash).

Для управления microdc2 использует командную строку:
 - поддерживается история команд через readline,
 - работает автодополнение команд и имён клавишей TAB,
 - имеется встроенная справка.

%prep
%setup -q
rm -rf src/bzip2
%patch0 -p0 -b .ru
%patch1 -p0 -b .slave-mode
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure --enable-nls --enable-largefile
%make_build

%install
%makeinstall_std

install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D %SOURCE2 %buildroot%_pixmapsdir/%name.png
mv %buildroot%_man1dir/microdc.1 %buildroot%_man1dir/microdc2.1
rm -f %buildroot%_man1dir/microdc.pl.1

%find_lang %name

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Sat Feb 13 2010 Boris Savelev <boris@altlinux.org> 0.15.6-alt7
- build with system bzlib
- clean spec

* Mon Feb 09 2009 Boris Savelev <boris@altlinux.org> 0.15.6-alt6
- pickup from orphaned
- fix build (add terrible patch from gentoo)
- remove pre, post
- spec cleanup with rpmcs

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.15.6-alt5.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for microdc2

* Mon Jul 23 2007 Ilya Evseev <evseev@altlinux.ru> 0.15.6-alt5
- bugfix: added buildprereq on libreadline-devel

* Mon Jul 23 2007 Ilya Evseev <evseev@altlinux.ru> 0.15.6-alt4
- apply works of Andrew Zabolotny (ru.po, slave-mode, .desktop and specfixes):
  http://lists.gnu.org/archive/html/microdc-devel/2007-04/msg00000.html

* Mon Jul 23 2007 Ilya Evseev <evseev@altlinux.ru> 0.15.6-alt3
- bugfix: added buildprereq on libxml2-devel

* Mon Jul 23 2007 Ilya Evseev <evseev@altlinux.ru> 0.15.6-alt2
- specfile: added russian description, fixed URL

* Mon Jul 23 2007 Ilya Evseev <evseev@altlinux.ru> 0.15.6-alt1
- initial build for ALTLinux
