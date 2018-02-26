Name: instead-launcher
Version: 0.6.1
Release: alt1
Group: Games/Adventure
Summary: Game update/launch program for INSTEAD, simple text adventures interpreter
Summary(ru_RU.UTF-8): Загрузчик игр, написанных для интерпретатора простых текстовых приключений INSTEAD
License: Distributable
Source: %{name}_%version.tar.gz
Url: http://instead-launcher.googlecode.com

Requires: instead-sdl
# Automatically added by buildreq on Sun Mar 21 2010
BuildRequires: gcc-c++ libqt4-devel

%description
Game update/launch program for INSTEAD, simple text adventures interpreter.

%description -l ru_RU.UTF-8
Загрузчик игр, написанных для интерпретатора простых текстовых приключений INSTEAD.

%prep
%setup
sed -i 's@return QDir::home().absolutePath() + "/.instead/games/";@return "%_localstatedir/instead/games";@
s@"/usr/local/bin/sdl-instead"@"%_bindir/sdl-instead"@' platform.cpp
sed -i '/Exec=/s@.*@Exec=%_bindir/%name@' %name.desktop.in

cat > %name.sh <<@@@
#!/bin/sh
GAMESDIR="\$HOME/.instead/games"
test -r "\$GAMESDIR" || {
rm -rf "\$GAMESDIR"
mkdir -p "\$HOME/.instead"
ln -s "%_localstatedir/instead/games" "\$GAMESDIR"; }
exec "\$0.bin"
@@@

%build
qmake-qt4 PREFIX="%prefix"
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
mv %buildroot%_bindir/%name %buildroot%_bindir/%name.bin
install -m755 %name.sh %buildroot%_bindir/%name

%files
%doc readme.txt
%attr(2711, root, games) %_bindir/%name.bin
%_bindir/%name
%_desktopdir/%name.desktop

%changelog
* Wed Sep 07 2011 Fr. Br. George <george@altlinux.ru> 0.6.1-alt1
- Autobuild version bump to 0.6.1
- Fix dependency

* Tue Jul 19 2011 Fr. Br. George <george@altlinux.ru> 0.6-alt1
- Autobuild version bump to 0.6

* Tue Feb 15 2011 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Autobuild version bump to 0.5

* Mon Sep 20 2010 Fr. Br. George <george@altlinux.ru> 0.4-alt3
- Fix gamesdir

* Wed Sep 01 2010 Fr. Br. George <george@altlinux.ru> 0.4-alt2
- Add project URL

* Wed Aug 18 2010 Fr. Br. George <george@altlinux.ru> 0.4-alt1
- Version up

* Sun Apr 11 2010 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Version up

* Mon Mar 22 2010 Fr. Br. George <george@altlinux.ru> 0.2.1-alt1
- Version up

* Sun Mar 21 2010 Fr. Br. George <george@altlinux.ru> 0.2-alt1
- Initial build from scratch

