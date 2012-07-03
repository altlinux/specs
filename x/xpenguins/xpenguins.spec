# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: xpenguins
Version: 2.2
Release: alt6.qa3

Summary: XPenguins -- little penguins on your desktop
Summary(ru_RU.KOI8-R): XPenguins -- маленькие пингвины на вашем рабочем столе

License: GPLv2
Group: Toys
Url: http://xpenguins.seul.org/
Packager: Slava Semushin <php-coder@altlinux.ru>

Source0: %name-%version.tar.bz2
Source2: %name-icons.tar.bz2

Patch: %name-2.2-alt-warnings-Wall_fix.patch

BuildRequires: libXpm-devel libXext-devel libXt-devel

%description
XPenguins is an desktop amusement. It creates little penguins that
walk across your screen, fly like helicopters, by explode. It's great
fun. (WARNING: It cannot be used during you're working, use it while
IRC'ing).

%description -l ru_RU.KOI8-R
XPenguins это представление на рабочем столе. Эта программа создает на
экране маленьких пингвинов, устраивающих настоящее цирковое
представление. (Внимание: не запускайте эту программу во время работы -
она будет вас отвлекать. Используйте ее во время отдыха или общения)

%prep
%setup -a2
%patch

%build
%configure
%make_build --silent --no-print-directory

%install
%make_install --silent --no-print-directory DESTDIR=%buildroot install

install -pD -m 644 %name-48x48.xpm %buildroot%_liconsdir/%name.xpm
install -pD -m 644 %name-32x32.xpm %buildroot%_niconsdir/%name.xpm
install -pD -m 644 %name-16x16.xpm %buildroot%_miconsdir/%name.xpm

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Xpenguins
Comment=Display penguins running on your desktop
Icon=%{name}
#Exec=%_gamesbindir/%name
Exec=%name
Terminal=false
Categories=Game;Amusement;
EOF


%files
%doc README AUTHORS ChangeLog
%_bindir/%name
%_man1dir/%name.1.*
%_datadir/%name/
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm
%_miconsdir/%name.xpm
%_liconsdir/%name.xpm

%changelog
* Fri Apr 08 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt6.qa3
NMU: polished desktop file

* Thu Apr 07 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt6.qa2
- NMU: converted debian menu to freedesktop

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.2-alt6.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for xpenguins
  * postclean-05-filetriggers for spec file

* Sat Dec 13 2008 Slava Semushin <php-coder@altlinux.ru> 2.2-alt6
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)
- More proper License tag

* Sun Nov 26 2006 Slava Semushin <php-coder@altlinux.ru> 2.2-alt5
- Updated BuildRequires for Xorg7
- Added patch Wall_fix for fixes one warning
- Spec cleanup:
  + Change my name in Packager tag
  + Formatted %%description
  + More strict names in %%files section
  + s/%%setup -q/%%setup/
  + Fixed orthographical errors in %%changelog (thnx to mike@)
- Enable _unpackaged_files_terminate_build

* Wed Dec 28 2005 php-coder <php-coder@altlinux.ru> 2.2-alt4
- New maintainer
- Now /usr/share/xpenguins belongs to package (#8709)
- Updated BuildRequires
- Removed COPYING and lay-out-frames.scm files from package
- Running make with --no-print-directory and --silent options to make
  terminal output clean
- Cleanup spec
- Separate menu to file, not generate from spec
- Combine icons to one tarball

* Tue Sep 30 2003 Rider <rider@altlinux.ru> 2.2-alt3
- buildrequires fix

* Fri Oct 11 2002 Rider <rider@altlinux.ru> 2.2-alt2
- gcc 3.2 rebuild

* Sun Feb 24 2002 Rider <rider@altlinux.ru> 2.2-alt1
- more icons from MDK
- 2.2
- specfile cleunup
- russian summary and description

* Fri May 11 2001 Rider <rider@altlinux.ru> 2.0-alt1
- 2.0

* Tue May 8 2001 Peter 'Nidd' Novodvorsky <nidd@altlinux.ru> 1.2-ipl2
- Fixed GROUP Tag.

* Fri Dec 8 2000 Peter 'Nidd' Novodvorsky <petya@logic.ru>
- Initial release.
