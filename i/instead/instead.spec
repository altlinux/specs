
Name: instead
Version: 1.7.0
Release: alt2
Group: Games/Adventure
License: GPLv2
Summary: STEAD text adventures/visual novels engine
Summary(ru_RU.UTF-8): Интерпретатор текстовых приключение и визуальных новелл STEAD
Url: http://instead.googlecode.com
Source: %{name}_%version.tar.gz
Patch: %name-1.7.0-Rules.make.system.patch

# Automatically added by buildreq on Wed Sep 08 2010
BuildRequires: ImageMagick-tools libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel liblua5-devel libncurses-devel libreadline-devel zlib-devel

%description
INSTEAD was designed to interpret the games that are the mix of visual novels,
text quests and classical 90'ss quests.

%description -l ru_RU.UTF-8
Интерпретатор STEAD (Simple Text Adventure) позволяет проигрывать игры, которые
по жанру являются смесью визуальной новеллы, текстового квеста и классических
квестов 90-х. Особенности STEAD игры:

    * очень простой исходный текст историй. (В качестве основы используется LUA);
    * возможность использования графического или текстового (readline) интерфейса для игры;
    * в графическом интерфейсе поддерживается музыка и графика;
    * поддержка тем для графического интерпретатора -- конкретная игра может менять вид интерфейса;
    * переносимость (изначально написана для Linux, зависит от SDL и lua).

%package sdl
Group: Games/Adventure
License: GPLv2
Summary: STEAD text adventures/visual novels GUI engine
Summary(ru_RU.UTF-8): Графический интерпретатор текстовых приключение и визуальных новелл STEAD
Requires: %name = %version-%release
Obsoletes: %name < %version-%release

%description sdl
This is GUI version of %name, text adventures/visual novels engine

%description sdl -l ru_RU.UTF-8
GUI-версия интерпретатора текстовых приключение и визуальных новелл STEAD

%prep
%setup
%patch -p2
cat > subst <<@@@
sed -i --follow-symlinks -e '\${x;s/./&/;x;t;q 1};'"\$1"';T;x;s/.*/./;x' "\$2"
@@@
chmod +x subst

./subst s/[.]png$// desktop/instead.desktop.in 
ln -sf Rules.make.system Rules.make
for N in 16 32 48 64 128; do convert -resize ${N}x${N} icon/sdl_%name.png ${N}x${N}.png; done
./subst 's@char \*games_sw = NULL@char *games_sw = "%_localstatedir/%name/games"@' src/sdl-instead/main.c
./subst 's@src/sdl-instead@src/instead src/sdl-instead@' Makefile
sed -i '/LN/{h;d};${x;s/./&/;x;t;q 1}' src/sdl-instead/Makefile
echo "2
/usr" | ./configure.sh

%build
%make_build EXTRA_LDFLAGS=-lm

%install
%makeinstall DESTDIR=%buildroot
for N in 16 32 48 64 128; do install -pD ${N}x${N}.png %buildroot/%_iconsdir/hicolor/${N}x${N}/apps/sdl_%name.png; done
mkdir -p %buildroot%_localstatedir/%name/games

%files
%doc %_defaultdocdir/%name
%dir %_datadir/%name
%dir %attr(1775,root,games) %_localstatedir/%name/games
%_datadir/%name/*
%_man6dir/*
%_bindir/%name

%files sdl
%_bindir/sdl-%name
%_iconsdir/hicolor/*/apps/sdl_%name.png
%_pixmapsdir/*
%_desktopdir/%name.desktop

%changelog
* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 1.7.0-alt2
- DSO list completion

* Thu May 03 2012 Fr. Br. George <george@altlinux.ru> 1.7.0-alt1
- Autobuild version bump to 1.7.0

* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 1.6.2-alt1
- Autobuild version bump to 1.6.2

* Sun Jan 22 2012 Fr. Br. George <george@altlinux.ru> 1.6.1-alt1
- Autobuild version bump to 1.6.1

* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 1.6.0-alt1
- Autobuild version bump to 1.6.0

* Wed Sep 07 2011 Fr. Br. George <george@altlinux.ru> 1.5.1-alt1
- Autobuild version bump to 1.5.1

* Tue Aug 30 2011 Fr. Br. George <george@altlinux.ru> 1.5.0-alt1
- Autobuild version bump to 1.5.0

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 1.4.5-alt1
- Autobuild version bump to 1.4.5

* Tue Jul 05 2011 Fr. Br. George <george@altlinux.ru> 1.4.4-alt1
- Autobuild version bump to 1.4.4

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 1.4.0-alt1
- Autobuild version bump to 1.4.0

* Thu Mar 31 2011 Fr. Br. George <george@altlinux.ru> 1.3.4-alt1
- Autobuild version bump to 1.3.4

* Thu Mar 10 2011 Fr. Br. George <george@altlinux.ru> 1.3.3-alt1
- Autobuild version bump to 1.3.3

* Wed Dec 08 2010 Fr. Br. George <george@altlinux.ru> 1.3.1-alt1
- Autobuild version bump to 1.3.1

* Sun Nov 14 2010 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Autobuild version bump to 1.3.0

* Wed Oct 06 2010 Fr. Br. George <george@altlinux.ru> 1.2.3-alt1
- Autobuild version bump to 1.2.3

* Thu Sep 30 2010 Fr. Br. George <george@altlinux.ru> 1.2.2-alt1
- Autobuild version bump to 1.2.2

* Mon Sep 20 2010 Fr. Br. George <george@altlinux.ru> 1.2.1-alt2
- Use native configure.sh for build (iconv now works)

* Thu Sep 09 2010 Fr. Br. George <george@altlinux.ru> 1.2.1-alt1
- Version up

* Tue Mar 23 2010 Fr. Br. George <george@altlinux.ru> 1.1.5-alt2
- Ncurses version added
- SDL version is moved to another package

* Sun Mar 21 2010 Fr. Br. George <george@altlinux.ru> 1.1.5-alt1
- Version up
- Default user-loaded games directory added
- Russian description added

* Sat Mar 13 2010 Fr. Br. George <george@altlinux.ru> 1.1.4-alt1
- Version up

* Sun Jan 10 2010 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Version up

* Mon Jan 04 2010 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Version up

* Fri Dec 25 2009 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Version up

* Sat Nov 28 2009 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Version up

* Sat Nov 21 2009 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Version up

* Wed Nov 11 2009 Fr. Br. George <george@altlinux.ru> 0.9.3-alt1
- Initial build from scratch

