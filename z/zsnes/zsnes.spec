# for beta
#define snapshot_date 150
#define srcname #name-#version
#Release: alt0.1svn#snapshot_date

Name: zsnes
Version: 1.51
Release: alt7

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
#Patch1: zsnes-1.51-FORTIFY_SOURCE.patch

# Source Mage
Patch1: zsnes-1.51-Makefile.in.FIX.BROKENESS.patch
# Hans de Goede
Patch2: zsnes-1.51-FORTIFY_SOURCE.patch
# Paul Bender (minimyth)
Patch3: zsnes-1.51-gcc43.patch
# Upstream CVS
Patch4: zsnes-1.51-pulseaudio.patch
# Ralf Corsepius
Patch5: zsnes-1.51-psr.patch
# Fix gamepad diagonals problem
# http://board.zsnes.com/phpBB3/viewtopic.php?t=12544
Patch6: zsnes-1.51-hat_events.patch
# Fix FTBFS with libpng 1.5
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=649801
Patch7: zsnes-1.51-libpng15.patch
# Fix FTBFS with gcc 4.7
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=667429
Patch8: zsnes-1.51-gcc47.patch
# Fix crash due to passing a non initialized ao_sample_format struct to libao
Patch9: zsnes-1.51-libao-crash.patch


#BuildPreReq: gcc3.4-c++ gcc3.4

ExclusiveArch: i586

# Automatically added by buildreq on Sat Oct 22 2005
BuildRequires: gcc4.7 gcc4.7-c++ esound libncurses-devel libSDL-devel libpng-devel libstdc++-devel nasm zlib-devel libao-devel

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
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

cd src

# Remove hardcoded CFLAGS and LDFLAGS
sed -i \
  -e 's:^\s*CFLAGS=.* -D__RELEASE__.*$:CFLAGS="$CFLAGS -D__RELEASE__":' \
  -e 's:^\s*CFLAGS=.* -I\/usr\/local\/include .*$:CFLAGS="${CFLAGS} -I.":' \
  -e '/^\s*LDFLAGS=.* -L\/usr\/local\/lib /d' \
  configure.in

# Fix line encodings in docs/readme.txt/*
sed -i 's/\r//' ../docs/readme.txt/*.txt

# Fix char encondigs
iconv --from=ISO-8859-1 --to=UTF-8 ../docs/readme.txt/games.txt > ../docs/readme.txt/games.txt.utf8
mv ../docs/readme.txt/games.txt.utf8 ../docs/readme.txt/games.txt
iconv --from=ISO-8859-1 --to=UTF-8 ../docs/readme.txt/support.txt > ../docs/readme.txt/support.txt.utf8
mv ../docs/readme.txt/support.txt.utf8 ../docs/readme.txt/support.txt


%build
%set_gcc_version 4.7


cd src
aclocal
autoconf
%configure \
  --enable-libao \
  --enable-release \
  --disable-cpucheck force_arch=i586
make %{?_smp_mflags}



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
* Sat Mar 01 2014 Ilya Mashkin <oddity@altlinux.ru> 1.51-alt7
- fix build

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

