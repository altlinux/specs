
%define svn 7046
%define rname smplayer
Name: kde4-%rname
Version: 14.9.0.%svn
Release: alt3

Summary: A great MPlayer/MPV front-end
Summary(ru_RU.UTF8): Мощный интерфейс для MPlayer/MPV
Summary(uk_UA.UTF8): Потужний інтерфейс для MPlayer/MPV
Group: Video
#Url: http://smplayer.sourceforge.net
#Url: http://www.smplayer.es/
Url: http://www.smplayer.info/
License: GPLv2

Requires: mplayer

Source: %name-%version.tar
Patch1: alt-defines.patch
Patch2: alt-defaults.patch
Patch3: alt-ui-defaults.patch
Patch4: alt-config-dir.patch

# Automatically added by buildreq on Thu Jul 23 2015 (-bi)
# optimized out: elfutils fontconfig glibc-devel-static libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-script libqt4-xml libstdc++-devel phonon-devel python-base python3 python3-base zlib-devel
#BuildRequires: gcc-c++ libqt4-webkit-devel rpm-build-python3 ruby ruby-stdlibs zlib-devel-static
BuildRequires: gcc-c++ libqt4-devel libqt4-webkit-devel

%description
smplayer intends to be a complete front-end for MPlayer/MPV, from basic features
like playing videos, DVDs, and VCDs to more advanced features like support
for MPlayer/MPV filters and more. One of the main features is the ability to
remember the state of a played file, so when you play it later it will resume
at the same point and with the same settings. smplayer is developed with
the Qt toolkit, so it's multi-platform.
Compiled with Qt4

%description -l ru_RU.UTF8
SMPlayer стремится быть как можно более полным интерфейсом для MPlayer/MPV,
от базовых функций проигрывания видео, DVD, VCDs до самого продвинутого
функционала MPlayer/MPV по поддержке фильтров и т.п. Одна из главных
особенностей - способность запоминать положение проигрываемого файла для
того, чтобы при следующем его открытии Вы могли смотреть его дальше с
того же места и с теми же параметрами настроек. SMPlayer разработан на
инструментарии Qt и является мультиплатформенным.
Скомпилировано с Qt4

%description -l uk_UA.UTF8
SMPlayer направлений на те, щоб стати як можна більш повним інтерфейсом
для MPlayer/MPV, від базових функцій відтворення відео, DVD, VCD до самого
продвинутого функціонала MPlayer/MPV по підтримці фільтрів і т.і. Одна з
головних особливостей - здатність запам'ятовувати положення файлу, що
відтворюється, для того, щоб при наступному його відкритті Ви мали змогу
переглядати його далі з того ж місця і з тими ж параметрами налаштувань.
SMPlayer розробено на інструментарії Qt і є мультиплатформним.
Зібрано з Qt4

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

export PATH=%_qt4dir/bin:$PATH

sed -i 's|^PREFIX=.*|PREFIX=%_prefix|' Makefile
sed -i 's|^DATA_PATH=.*|DATA_PATH=%_datadir/%name|' Makefile
sed -i 's|^TRANSLATION_PATH=.*|TRANSLATION_PATH=%_datadir/%name/translations|' Makefile
sed -i 's|^DOC_PATH=.*|DOC_PATH=%_docdir/%name-%version|' Makefile
sed -i 's|^THEMES_PATH=.*|THEMES_PATH=%_datadir/%name/themes|' Makefile
sed -i 's|^SHORTCUTS_PATH=.*|SHORTCUTS_PATH=%_datadir/%name/shortcuts|' Makefile

pushd src
echo '#define SVN_REVISION "%svn"' > svn_revision.h
%qmake_qt4 smplayer.pro
popd


%build
export PATH=%_qt4dir/bin:$PATH
%make_build src/smplayer


%install
%make DESTDIR=%buildroot install

# renames
mv %buildroot/%_bindir/smplayer %buildroot/%_bindir/%name
mkdir -p %buildroot/%_desktopdir/kde4/
mv %buildroot/%_desktopdir/*.desktop %buildroot/%_desktopdir/kde4/
find %buildroot/%_desktopdir/ -type f -name \*.desktop | \
while read f; do
    sed -i 's|^Exec=\(.*\)|Exec=kde4-\1|' $f
    sed -i 's|^Icon=\(.*\)|Icon=kde4-\1|' $f
    sed -i 's|SMPlayer|SMPlayer KDE4|g' $f
done
find %buildroot/%_iconsdir/ -type f | \
while read f; do
    oldname=`basename $f`
    newname="kde4-$oldname"
    filedir=`dirname $f`
    mv $f $filedir/$newname
done


%files
%_bindir/%name
%_desktopdir/kde4/*.desktop
%_docdir/%name-%version
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.*

%changelog
* Thu Jul 23 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.7046-alt3
- separate configs with smplayer

* Thu Jul 23 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.7046-alt2
- update UI defaults

* Thu Jul 23 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.7046-alt1
- update to r7046

* Mon Jul 20 2015 Sergey V Turchin <zerg@altlinux.org> 14.9.0.6748-alt1
- initial build
