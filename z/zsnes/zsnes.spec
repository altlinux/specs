# for beta
#define snapshot_date 150
#define srcname #name-#version
#Release: alt0.1svn#snapshot_date

Name: zsnes
Version: 1.51
Release: alt6

Packager: Ilya Mashkin <oddity at altlinux.ru>

Summary: Super Nintendo emulator
Summary(ru_RU.KOI8-R): Эмулятор Super Nintendo
URL: http://www.zsnes.com

License: GPL
Group: Emulators


Source0: %{name}151src.tar.bz2
Source1: %name.desktop
Source2: %name-16.xpm
Source3: %name-32.xpm
Source4: %name-48.xpm
Patch1: zsnes-1.51-FORTIFY_SOURCE.patch

#BuildPreReq: gcc3.4-c++ gcc3.4

ExclusiveArch: i586

# Automatically added by buildreq on Sat Oct 22 2005
BuildRequires: gcc4.1 gcc4.1-c++ esound libncurses-devel libSDL-devel libpng-devel libstdc++-devel nasm xorg-x11-mesagl zlib-devel

%description
ZSnes is an emulator for the Super Nintendo video game console, 
written mostly in assembler. Originally a DOS program, it has 
now been ported to Windows and Linux.

%description -l ru_RU.KOI8-R
ZSnes - это эмулятор игровой видеоконсоли Super Nintendo, написанный большей
частью на ассемблере. Первоначально программа была написана под DOS, затем
портирована на Windows и Linux.

%prep
%setup -q -n %{name}_1_51
%patch1 -p1

%build
##export CC="/usr/bin/gcc-3.4" CXX="/usr/bin/g++-3.4"
%set_gcc_version 4.1

cd src
#export LDFLAGS="$LDFLAGS -Wl, --no-as-needed"
#configure --with-x
./autogen.sh


%make_build

%install
cd src
%make_install
install -D -pm 755 zsnes %buildroot%_bindir/%name
install -D -pm 644 linux/zsnes.1 %buildroot%_man1dir/zsnes.1
%__mkdir_p %buildroot%_docdir/%name-%version
#install -D -pm 644 ../docs %buildroot%_docdir/%name-%version/

install -D -pm 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D -pm 644 %SOURCE2 %buildroot%_miconsdir/%name.xpm
install -D -pm 644 %SOURCE3 %buildroot%_niconsdir/%name.xpm
install -D -pm 644 %SOURCE4 %buildroot%_liconsdir/%name.xpm


%files
%doc docs/*
#%_docdir/%name-%version/*
%_bindir/*
%_desktopdir/*
%_man1dir/*
%_niconsdir/*.xpm
%_miconsdir/*.xpm
%_liconsdir/*.xpm

%changelog
* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 1.51-alt6
- Replaced obsolete menu file with desktop file (closes: #25970).

* Sun May 01 2011 Ilya Mashkin <oddity@altlinux.ru> 1.51-alt5
- fix build

* Sun Jan 09 2011 Ilya Mashkin <oddity@altlinux.ru> 1.51-alt4
- fix crash

* Sun Jan 09 2011 Ilya Mashkin <oddity@altlinux.ru> 1.51-alt3
- rebuild

* Wed Mar 03 2010 Ilya Mashkin <oddity@altlinux.ru> 1.51-alt2
- rebuild
- apply repocop patch

* Fri Feb 09 2007 Ilya Mashkin <oddity@altlinux.ru> 1.51-alt1
- Bug fix version 1.51

* Sun Dec 24 2006 Ilya Mashkin <oddity at altlinux dot ru> 1.50-alt1
- Release 1.50 

* Wed Dec 20 2006 Ilya Mashkin <oddity at altlinux dot ru> 1.50-alt0.1svn20061220
- New version 1.50 Beta from svn

* Sun Oct 22 2005 Ilya Mashkin <oddity at altlinux.ru> 1.42-alt5
- add russian description

* Fri Mar 04 2005 Denis Klykvin <nikon@altlinux.ru> 1.42-alt4
- Build new version.
- Fixed typo in description.

* Fri Jul 04 2003 Denis Klykvin <nikon@altlinux.ru> 1.36-alt3
- Fixed icons location.

* Fri Jun 20 2003 Denis Klykvin <nikon@altlinux.ru> 1.36-alt2
- add icons.

* Tue Jun 17 2003 Denis Klykvin <nikon@altlinux.ru> 1.36-alt1
- Initial build.

