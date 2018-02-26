%define prever %nil
%define use_prever 0
%define build_static 0
%define build_recode 1
%define build_recode 1
%define build_id3v2 1
%define new_vorbis 0

%define use_rusxmms2 1
%define rusxmms2_ver csa43

Name: xmms
Version: 1.2.11
Release: alt9.6.qa3
Epoch: 20100727

Summary: X Multimedia System - the player for you
License: GPL
Group: Sound

Url: http://xmms.org

%if %use_prever
Source0: %url/files/1.2.x/%name-%version-%prever.tar.bz2
%else
Source0: %url/files/1.2.x/%name-%version.tar.gz
%endif

Source2: gnomexmms.desktop.bz2
Source4: xmms-icons.tar.bz2
Source5: xmms.menu
Source6: wmxmms.menu
Source7: wmxmms.desktop
Source8: xmms-1.2.11-ru.po
Source10: xmms.16.xpm.bz2
Source11: xmms.32.xpm.bz2
Source12: xmms.48.xpm.bz2
Source13: xmms-1.2.10-gentoo-m4-1.1.tar.bz2

# obsolete
%define rusversion 1.2.10
%define rusxmms_ver csa28
Source70: http://heanet.dl.sourceforge.net/sourceforge/rusxmms/xmms-%rusversion-recode-%rusxmms_ver.tar.bz2

Source270: http://heanet.dl.sourceforge.net/sourceforge/rusxmms/RusXMMS2-%{rusxmms2_ver}.tar.bz2
Source71: xmms.rpm-macros
Source72: xmms-cyr-setup.sh
Source73: xmms-cyr-setup.menu
Source74: xmms-wrapper.sh
Source75: xmms.keys
Source76: xmms-cyr-setup.desktop

Source80: xmms-README.ALT
Source81: #xmms-faq.html

Source90: xmms.desktop

Patch0: xmms-1.2.11-alt-ru.po.patch
Patch1: xmms-1.2-audio-patch
Patch4: xmms-fix-smallfiles.patch
Patch5: xmms-1.2.6-fix-title-mp3streaming.patch
Patch6: xmms-fix-textbox.patch
Patch8: xmms-3dse-niqueluisarace.patch

# Local patches
Patch41: xmms-1.2.6-filebrowser_get_files.patch
Patch42: xmms-1.2.7-automake.patch
Patch43: xmms-1.2.7-local-libxmms_n.patch
Patch44: xmms-1.2.9-alt-socketpath.patch
Patch45: xmms-1.2.8-alt-aclocal-mess-cleanup.patch.bz2
Patch46: xmms-1.2.10-alt-gcc34_libctrl.patch
Patch47: xmms-1.2.10-xmmctrl.patch

# imported from 1.2.8-1.9asp
Patch52: xmms-1.2.6-lazy.patch
# ...and additionally fixed
Patch55: xmms-1.2.10-alt-arts.patch

# alsa asound checking
Patch56: xmms-1.2.10-alt-alsa.patch

# rollback winlist changes in 1.2.9
Patch57: xmms-1.2.10-alt-skipwinlist.patch

# id3v2 support - with eugvv@ fix of TYER frame write
Patch60: xmms-1.2.10-yonas-id3v2.patch

# advanced queue mgmt
Patch61: xmms-1.2.10-davinchi-queued.patch

# patch after rusxmms-1.2.10-csa27.4 -- should fix one more segfault
# [included in csa28]
Patch62: xmms-recode.patch
Patch63: xmms-1.2.10-alt-vorbis-headers.patch

# some merge-up -- not applied for 1.2.11
Patch70: xmms-underquoted.patch
Patch71: xmms-alsa-mono-vol-adjust.patch

# TODO: mdv cooker -- not applied yet
Patch72: xmms-1.2.11-3dse.patch
Patch73: xmms-1.2.11-ab.patch
Patch74: xmms-1.2.11-fix-http-title-mpg123.patch
Patch75: xmms-1.2.11-rva.patch

# TODO: dag's -- not applied yet
Patch80: xmms-1.2.6-audio.patch
Patch81: xmms-1.2.8-default-skin.patch
Patch82: xmms-alsa-backport.patch

## gcc4.1 compilation fix http://bugs.xmms.org/show_bug.cgi?id=2225
Patch91: xmms-1.2.10-gcc4-1.patch

# crossfade anti-lockup patch
Patch92: xmms-1.2.10-crossfade-0.3.9.patch

# alsa pause detector
Patch93: xmms-1.2.10-alsa_dmix_pause.patch

# id3v2 segfault
Patch94: xmms-1.2.10-ds-id3v2-crash.patch

# CVE-2007-0653 CVE-2007-0654
#Patch95: xmms-1.2.10-ubuntu-CVE-2007-0653.patch
Patch95: xmms-1.2.11-alt-ubuntu-CVE-2007-0653.patch

# underlinking fix by icesik@
Patch96: xmms-1.2.10-alt-linking.patch

# related to ALT bug #12127
Patch97: xmms-1.2.10-alt-media-cdrom.patch

# suggested by slackwarists
Patch98: xmms.gtk.doublesize.diff.gz

Patch99: xmms-1.2.11-alt-DSO.patch
Patch100: xmms-1.2.11-alt-textrel.patch

Packager: Michael Shigorin <mike@altlinux.org>

Icon: xmms-logo.xpm

Obsoletes: x11amp

# due to added patch from crossfade sources
Conflicts: xmms-out-crossfade < 0.3.10-alt1

Requires: libxmms = %epoch:%version-%release

%if %use_rusxmms2
BuildPreReq: librcc-devel librcd-devel librcc-gtk
%endif

%{?!_desktopdir:%define _desktopdir %_datadir/applications}

# Automatically added by buildreq on Sun Nov 25 2007
BuildRequires: esound-devel gcc-c++ glibc-devel-static gtk+-devel imake libalsa-devel libmikmod-devel librcc-devel librcc-gtk libSM-devel libssl-devel libvorbis-devel ORBit-devel xorg-cf-files zlib-devel

BuildPreReq: libGL-devel libGLU-devel chrpath

%set_autoconf_version 2.60
%set_automake_version 1.9
BuildRequires: desktop-file-utils

%description
XMMS is a sound player written from scratch. Since it uses the WinAmp GUI, it
can use WinAmp skins, and play mp3s, mods, s3ms, and other formats. It now has
support for input, output, and general plugins, and has also been GPLd.

%description -l ru_RU.KOI8-R
X MultiMedia System - наиболее популярный медиа-проигрыватель для UNIX-систем.

Поддерживает существенное количество форматов и эффектов благодаря большому
количеству модулей расширения, доступных в отдельных пакетах.

%description -l uk_UA.KOI8-U
X MultiMedia System - найб╕льш популярний мед╕а-програвач для UNIX-систем.

П╕дтриму╓ величезну к╕льк╕сть формат╕в та ефект╕в завдяки велик╕й к╕лькост╕
модул╕в розширення, що доступн╕ в окремих пакетах.

%package -n libxmms
Summary: Library needed for XMMS and its plugins
Summary(ru_RU.KOI8-R): Библиотека для XMMS и модулей к нему
Summary(uk_UA.KOI8-U): Б╕бл╕отека для XMMS та модул╕в до нього
Group: System/Libraries

%description -n libxmms
This library is mandatory for xmms and for all its plugins to run.

%description  -n libxmms -l ru_RU.KOI8-R
Эта библиотека необходима для xmms и всех его модулей.

%description  -n libxmms -l uk_UA.KOI8-U
Ця б╕бл╕отека ╓ необх╕дною для xmms та ус╕х його модулей.

%package -n libxmms-devel
Summary: Development package with headers
Group: Development/C
Icon: xmms-devel-logo.xpm
Requires: libxmms = %epoch:%version-%release
Provides: xmms-devel = %version-%release
Obsoletes: xmms-devel
Requires: rpm-macros-%name = %epoch:%version-%release

%description -n libxmms-devel
Header files required for compiling xmms plugins.

%if %build_static
%package -n libxmms-devel-static
Summary: Development package with static libs
Group: Development/C
Requires: libxmms-devel = %epoch:%version-%release
Obsoletes: xmms-devel-static
Provides: xmms-devel-static = %version-%release

%description -n libxmms-devel-static
Static libraries required for compiling xmms plugins.
%endif

%package in-mikmod
Summary: Mikmod output plugin
Summary(ru_RU.KOI8-R): Модуль поддержки воспроизведения MOD-файлов
Summary(uk_UA.KOI8-U): Модуль п╕дтримки в╕дтворення MOD-файл╕в
Group: Sound
Icon: xmms-mikmod-logo.xpm
BuildPreReq: libmikmod-devel
Requires: %name = %epoch:%version-%release
Requires: libmikmod >= 3.1.6
Obsoletes: x11amp-mikmod xmms-mikmod
Provides: xmms-mikmod = %version-%release

%description in-mikmod
Input plugin for XMMS to play MODs (.mod,.xm,.s3m, etc)

%description in-mikmod -l ru_RU.KOI8-R
Модуль ввода для проигрывания MOD-файлов (.mod, .xm, .s3m, ...)

%description in-mikmod -l uk_UA.KOI8-U
Модуль вводу для програвання MOD-файл╕в (.mod, .xm, .s3m, ...)

%package in-vorbis
Summary: Input plugin that uses the Vorbis library
Summary(ru_RU.KOI8-R): Модуль поддержки воспроизведения Ogg Vorbis
Summary(uk_UA.KOI8-U): Модуль п╕дтримки в╕дтворення Ogg Vorbis
Group: Sound
Requires: %name = %epoch:%version-%release, libvorbis >= 1.0rc2, libogg >= 1.0rc2
BuildPreReq: libvorbis
Obsoletes: xmms-vorbis
Provides: xmms-vorbis = %version-%release

%description in-vorbis
Input plugins that use the Vorbis library

%description in-vorbis -l ru_RU.KOI8-R
Модуль ввода, использующий библиотеку Ogg Vorbis

%description in-vorbis -l uk_UA.KOI8-U
Модуль вводу, що використову╓ б╕бл╕отеку Ogg Vorbis

%package out-alsa
Summary: ALSA output plugin
Summary(ru_RU.KOI8-R): Модуль вывода для ALSA
Summary(uk_UA.KOI8-U): Модуль виводу для ALSA
Group: Sound
BuildPreReq: libalsa-devel
Requires: %name = %epoch:%version-%release
Obsoletes: xmms-alsa < 1.2.8
Provides: xmms-alsa = %version-%release

%description out-alsa
Output plugin for xmms to use with ALSA

%description out-alsa -l ru_RU.KOI8-R
Модуль вывода для использования с ALSA

%description out-alsa -l uk_UA.KOI8-U
Модуль виводу для використання ╕з ALSA

%package out-diskwriter
Summary: DiskWriter output plugin
Summary(ru_RU.KOI8-R): Модуль вывода в файл
Summary(uk_UA.KOI8-U): Модуль виводу в файл
Group: Sound
Requires: %name = %epoch:%version-%release
Obsoletes: xmms-diskwriter < 1.2.8-alt2
Provides: xmms-diskwriter = %version-%release

%description out-diskwriter
Output plugin for xmms in order to output *.wav files instead of playing
sound on the soundcard.

%description out-diskwriter -l ru_RU.KOI8-R
Модуль вывода для записи wav-файлов вместо воспроизведения

%description out-diskwriter -l uk_UA.KOI8-U
Модуль виводу для запису wav-файл╕в зам╕сть в╕дтворення

%package out-esd
Summary: ESound output plugin
Summary(ru_RU.KOI8-R): Модуль вывода через ESound
Summary(uk_UA.KOI8-U): Модуль виводу через ESound
Group: Sound
Icon: xmms-esd-logo.xpm
BuildPreReq: esound-devel
Requires: %name = %epoch:%version-%release
Requires: esound >= 0.2.14
Obsoletes: x11amp-esd xmms-esd < 1.2.8-alt2
Provides: xmms-esd = %version-%release

%description out-esd
Output plugin for xmms to use with the ESD

%description out-esd -l ru_RU.KOI8-R
Модуль вывода, применяемый при необходимости использования ESound

%description out-esd -l uk_UA.KOI8-U
Модуль виводу, що застосову╓ться при необх╕дност╕ використання ESound

%package vis-mesa
Summary: Visualization plugins that use the Mesa3D library
Summary(ru_RU.KOI8-R): Модули визуализации с использованием Mesa3D
Summary(uk_UA.KOI8-U): Модул╕ в╕зуал╕зац╕╖ з використанням Mesa3D
Group: Sound
Icon: xmms-mesa-logo.xpm
Requires: %name = %epoch:%version-%release
Obsoletes: xmms-mesa < 1.2.8-alt2
Provides: xmms-mesa = %version-%release

%description vis-mesa
3D Visualization plugins for XMMS that use the Mesa3d library

%description vis-mesa -l ru_RU.KOI8-R
Модуль визуализации с использованием 3D-эффектов

%description vis-mesa -l uk_UA.KOI8-U
Модуль в╕зуал╕зац╕╖ з використанням 3D-ефект╕в

%package -n wmxmms
Summary: XMMS applet for WindowMaker
Group: Graphical desktop/Window Maker
Requires: %name = %epoch:%version-%release

%description -n wmxmms
XMMS applet for WindowMaker.  

You might also want to take a look at wmusic.

%description -n wmxmms -l ru_RU.KOI8-R
Аплет XMMS для WindowMaker.

В отличие от wmusic, не поддерживает кириллицу.

%description -n wmxmms -l uk_UA.KOI8-U
Аплет XMMS для WindowMaker.

На в╕дм╕ну в╕д wmusic, не п╕дтриму╓ кирилицю.

%package cyr-setup
Summary: Script to auto-tune XMMS for cyrillic tags
Summary(ru_RU.KOI8-R): Скрипт для автонастройки XMMS под кириллицу
Summary(uk_UA.KOI8-U): Скрипт для автоналаштування XMMS п╕д кирилицю
Summary(be_BY.CP1251): яЖЩМЮП Ю╒РЮЛЮРШВМЮЕ МЮКЮДЙЁ ОПЮЖШ XMMS Г ЙЁПШКЁВМШЛЁ ЬПШТРЮЛЁ
Requires: fonts-bitmap-cyr_rfx-koi8-u fonts-bitmap-cyr_rfx-cp1251
Requires: fonts-bitmap-cyrillic fonts-bitmap-75dpi
Requires: xmms
Group: Sound
BuildArch: noarch

%description cyr-setup
This package is of use to Cyrillic users only.

%description cyr-setup -l ru_RU.KOI8-R
Этот пакет поможет пользователям XMMS настроить его для использования
кириллицы "одним щелчком"

%description cyr-setup -l uk_UA.KOI8-U
Цей пакунок допоможе користувачам XMMS налаштувати його для використання
кирилиц╕ "одним кл╕ком"

%description cyr-setup -l be_BY.CP1251
цЩРШ ОЮЙЕР ДЮОЮЛНФЮ ЙЮПШЯРЮКЭМЁЙЮЛ XMMS МЮКЮДГЁЖЭ ЪЦН ДКЪ БШЙЮПШЯРЮМЭМЪ
ЙЁПШКЁЖШ "ЮДМШЛ ЬВЮ╒ВЙНЛ"


%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
Conflicts: libxmms-devel <= 1.2.11-alt6
BuildArch: noarch

%description -n rpm-macros-%name
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep
%if %use_prever
%setup -n xmms-%version-%prever -q -a 70 -a 13
%else
%if %use_rusxmms2
%setup -n xmms-%version -q -a 270 -a 13
%else
%setup -n xmms-%version -q -a 70 -a 13
%endif
%endif

%patch1 -p1
%patch4 -p1
%if %use_rusxmms2
## with this patch, rusxmms2 apply failed. check it later
%else
%patch5 -p1
%endif
%patch6 -p1

%patch8 -p1

%patch41 -p1
%patch44 -p1
#patch46 -p1
#patch47 -p1

#patch70 -p1
#patch71 -p1

# RH/ASP patches
# Use RTLD_LAZY, not RTLD_NOW
%patch52 -p1 -b .lazy

%patch56 -p1 -b .alsa

#patch57 -p1 -b .winlist

# id3v2
%if %use_rusxmms2
## with this patch, rusxmms2 apply failed. check it later
%else
%if %build_id3v2
%patch60 -p1 -b .id3v2
%endif
%endif

# ID3 recoding patch (rusxmms)
%if %build_recode
%if %use_rusxmms2
# new shining rusxmms 2
pushd RusXMMS2
# NB: in csa40 version, there's single apply.sh
#if %build_id3v2
#./apply-id3v2.sh
#else
./apply.sh
#endif
popd
%else
# ancient rusxmms
%if %build_id3v2
%patch -p1 -s < xmms_id3v2-ds-recode.patch
%else
%patch -p1 -s < xmms-ds-recode.patch
%endif
#patch62 -p1
%endif
%endif

%if %new_vorbis
%patch63 -p1 -b .new_vorbis
%endif

%if %use_rusxmms2
%else
# another 1.2.9 fix from ds
%patch -p1 -s < recode.addons/xmms-ds-ctrl3.patch
%endif

#patch91 -p1
%patch92 -p1
#patch93 -p1
#patch94 -p1

%patch95 -p1
%patch96 -p1

%patch97 -p1
%patch98 -p0

# subqueue management -- 1..9 keys set queue number,
# Ctrl-1..9 exchange it with an existing one;
# contact Boldin Pavel <ldavinchi inbox ru> for details
#patch61 -p1

%patch99 -p2
#patch100 -p2

msgfmt -c -o po/ru.gmo %SOURCE8

%define _optlevel 3
%add_optflags %optflags_notraceback -funroll-all-loops
%add_optflags -fexpensive-optimizations -fomit-frame-pointer -fPIC -DPIC
%set_verify_elf_method textrel=relaxed

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' \
	ltmain.sh config.rpath *.m4 */*.m4

%build
#libtoolize --copy --force
#aclocal -I m4
#autoconf
#automake -a
#%%autoreconf
#pushd libxmms
#aclocal -I ../m4
#autoconf
#%%autoreconf
#popd

FLAGS="`glib-config --cflags` -I%_x11includedir/GL"
FLAGS="$FLAGS $(orbit-config --cflags client server)"
%add_optflags $FLAGS

export STRIP=echo
aclocal && automake && autoconf
%configure \
%ifarch %ix86
	--enable-3dnow \
	--enable-simd \
%endif
	--enable-recode \
	--enable-texthack 
sed -i 's|^STRIP\=.*|STRIP=echo|' libtool libxmms/libtool
sed -i 's|^\(old_striplib\).*|\1=echo|' libtool libxmms/libtool
sed -i 's|^\(striplib\).*|\1=echo|' libtool libxmms/libtool
sed -i 's|\(stripme\=\).*|\1|' libtool libxmms/libtool
sed -i 's|^STRIP\=.*|STRIP=echo|' libtool libxmms/libtool
sed -i 's|\(INSTALL_STRIP_FLAG\=\)\-s|\1-c|g' \
	$(find ./ -name 'Makefile*')
sed -i 's|^\(INSTALL_STRIP_PROGRAM.*\)\ \-s|\1|' Makefile \
	libxmms/Makefile
%make

%install
mkdir -p %buildroot{%_desktopdir,%_menudir,%_liconsdir,%_miconsdir,%_niconsdir}
sed -i 's|^STRIP\=.*|STRIP=echo|' libtool libxmms/libtool
sed -i 's|^\(old_striplib\).*|\1=echo|' libtool libxmms/libtool
sed -i 's|^\(striplib\).*|\1=echo|' libtool libxmms/libtool
sed -i 's|\(stripme\=\).*|\1|' libtool libxmms/libtool
sed -i 's|^\(Makefile\:.*\)|_\1|' Makefile libxmms/Makefile
sed -i 's|\(INSTALL_STRIP_FLAG\=\)\-s|\1-c|g' \
	$(find ./ -name 'Makefile*')
sed -i 's|^\(INSTALL_STRIP_PROGRAM.*\)\ \-s|\1|' Makefile \
	libxmms/Makefile
%make DESTDIR=%buildroot install

install -pD -m644 %SOURCE75 %buildroot%_datadir/mime-info/xmms.keys 

# icons
install -m644 $RPM_SOURCE_DIR/xmms-logo.xpm %buildroot%_datadir/xmms/xmms.xpm
install -m755 -d %buildroot%_datadir/pixmaps/
ln -s ../xmms/xmms.xpm %buildroot%_datadir/pixmaps/

bzcat %SOURCE10 > %buildroot%_miconsdir/%name.xpm
bzcat %SOURCE11 > %buildroot%_niconsdir/%name.xpm
bzcat %SOURCE12 > %buildroot%_liconsdir/%name.xpm

install -m644 %SOURCE5 %buildroot%_menudir/%name
install -m644 %SOURCE6 %buildroot%_menudir/wmxmms
install -m644 %SOURCE7 %buildroot%_desktopdir/wmxmms.desktop

install -pD -m644 %SOURCE71 %buildroot%_rpmmacrosdir/%name

# cyr setup
install -pD -m755 %SOURCE72 %buildroot%_bindir/xmms-cyr-setup.sh
install -pD -m644 %SOURCE73 %buildroot%_menudir/xmms-cyr-setup
install -pD -m644 %SOURCE76 %buildroot%_desktopdir/xmms-cyr-setup.desktop

# wrapper
mv %buildroot%_bindir/xmms %buildroot%_bindir/xmms-bin
install -pD -m755 %SOURCE74 %buildroot%_bindir/xmms
subst 's,@@LIBDIR@@,%_libdir,g' %buildroot%_bindir/xmms
%if %build_recode
subst 's,@@RECODE@@,yes,' %buildroot%_bindir/xmms
%else
subst 's,@@RECODE@@,no,' %buildroot%_bindir/xmms
%endif

# packaging policy
install -p -m644 %SOURCE80 $RPM_BUILD_DIR/%name-%version/README.ALT-koi8r

# FAQ
install -p -m644 %SOURCE81 $RPM_BUILD_DIR/%name-%version/\#xmms-faq.html

# desktop entry
install -pD -m644 %SOURCE90 %buildroot%_datadir/applications/%name.desktop

gzip -9nf ChangeLog ||:

%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Player \
	%buildroot%_desktopdir/wmxmms.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Player \
	%buildroot%_desktopdir/xmms-cyr-setup.desktop

#for i in %buildroot%_bindir/* %buildroot%_libdir/%name/*/*
#do
#	chrpath -d $i ||:
#done

%files -f %name.lang 
%doc AUTHORS ChangeLog.gz NEWS* README* TODO 
%if %use_rusxmms2
%else
%doc recode.docs/README*.rus
%endif
%dir %_datadir/%name
%dir %_libdir/%name/
%dir %_libdir/%name/*
%_bindir/%name
%_bindir/%name-bin
%_libdir/%name/Input/libcdaudio*
%_libdir/%name/Input/libmpg123*
%_libdir/%name/Input/libtonegen*
%_libdir/%name/Input/libwav*
%_libdir/%name/Output/libOSS*
%_libdir/%name/General/*
%_libdir/%name/Effect/*
%_libdir/%name/Visualization/libbscope*
%_libdir/%name/Visualization/libsanalyzer*
%_datadir/%name/xmms.xpm
%_datadir/mime-info/xmms.keys
%_datadir/pixmaps/*
%_niconsdir/%name.xpm
%_miconsdir/%name.xpm
%_liconsdir/%name.xpm
%_desktopdir/%name.desktop
%_man1dir/xmms.1.*

%files -n libxmms
%_libdir/libxmms.so.*

%files -n libxmms-devel
%_libdir/lib*.so
%_includedir/*
%_datadir/aclocal/xmms.m4
%_bindir/xmms-config

%if %build_static
%files -n libxmms-devel-static
%_libdir/lib*.a
%endif

%files in-mikmod
%_libdir/xmms/Input/libmikmod*

%files in-vorbis
%_libdir/xmms/Input/libvorbis*

%files out-alsa
%_libdir/xmms/Output/libALSA*

%files out-esd
%_libdir/xmms/Output/libesdout*

%files out-diskwriter
%_libdir/xmms/Output/libdisk_writer*

%files vis-mesa
%_libdir/xmms/Visualization/libogl_spectrum*

%files -n wmxmms
%_bindir/wmxmms
%_man1dir/wmxmms.1.*
%_datadir/xmms/wmxmms.*
%_desktopdir/wmxmms.desktop

%files cyr-setup
%_bindir/xmms-cyr-setup.sh
%_desktopdir/xmms-cyr-setup.desktop

# TODO:
# - re-check patch71 and especially patch93 (dmix pause)

%files -n rpm-macros-%name
%_rpmmacrosdir/*

%changelog
* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100727:1.2.11-alt9.6.qa3
- Fixed build

* Wed Feb 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100727:1.2.11-alt9.6.qa2
- Removed bad RPATH

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 20100727:1.2.11-alt9.6.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for wmxmms
  * freedesktop-desktop-file-proposed-patch for xmms-cyr-setup

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100727:1.2.11-alt9.6
- BuildRequires: replaced libmesa-devel by libGL-devel and libGLU-devel

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100727:1.2.11-alt9.5
- Removed self-requirement of libxmms
- Added Epoch into requirements

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100727:1.2.11-alt9.4
- Really rebuilt for debuginfo

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100727:1.2.11-alt9.3
- Rebuilt for debuginfo

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 20100727:1.2.11-alt9.2
- rebuilt against openssl-1.0.0a

* Sun Jun 27 2010 Michael Shigorin <mike@altlinux.org> 20100727:1.2.11-alt9.1
- rpm-macros-xmms, xmms-cyr-setup are now noarch (thx GB)
- officially bug-free(tm)

* Sun Jun 27 2010 Michael Shigorin <mike@altlinux.org> 20100605:1.2.11-alt9
- fixed FTBFS by dropping all of autorecrap on the same floor

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 20090513:1.2.11-alt8
- fixed FTBFS by dropping extra autocrap on the floor

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 20081204:1.2.11-alt7
- xmms-cyr-setup: replaced fonts-bitmap-misc with fonts-bitmap-75dpi for UTF-8
- xmms: tweaked wrapper script to behave better
  + choose better Unicode fonts by default
  + if ALSA output plugin is present on first run, use that
  + if crossfade plugin is similarly found, use that too
  + dropped remnants of soundwrapper support
- updated rusxmms2 patch to csa43
- updated ru.po with many spelling and other fixes (finally)
- applied repocop patch
  + introduced rpm-macros-%name subpackage
- fixed desktop files as well
- spec cleanup

* Sat Oct 11 2008 Michael Shigorin <mike@altlinux.org> 20081011:1.2.11-alt6
- added one-line patch to work around problems with double-size
  when compositing is enabled (taken from Slackware upon a hint)

* Sun Aug 10 2008 Michael Shigorin <mike@altlinux.org> 20080810:1.2.11-alt5
- updated rusxmms2 to csa42

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 20080515:1.2.11-alt4.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Thu May 15 2008 Michael Shigorin <mike@altlinux.org> 20080515:1.2.11-alt4
- upgraded cyrsetup subpackage font dependencies

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 20071121:1.2.11-alt3.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for xmms

* Fri Dec 07 2007 Michael Shigorin <mike@altlinux.org> 20071121:1.2.11-alt3
- fixed xmms wrapper so that UTF8 locales get treated properly,
  plus some sanitizations and SisyphusProof(TM) additions
- fixed silly typo in xmms-cyr-setup which would overlook gxmessage

* Wed Dec 05 2007 Michael Shigorin <mike@altlinux.org> 20071121:1.2.11-alt2
- fixed x86_64 build
- rehashed non-applied patches and TODO for these

* Sun Nov 25 2007 Michael Shigorin <mike@altlinux.org> 20071121:1.2.11-alt1
- 1.2.11
- [20071121] disabled patches:
  + 46, 47, 70, 91 (already applied)
  + 71, 93, 95(!)  (failed to apply)
  + rusxmms (update asked for)
- [20071125] re-enabled rusxmms (csa41), thanks Suren!
- disabled patch94, seems obsolete (might be not)
- updated patch95 (xmms bug #2478)
- buildreq

* Fri Aug 31 2007 Michael Shigorin <mike@altlinux.org> 20070831:1.2.10-alt15
- minor tweak to fd.o menu (as discussed in #12653 and devel@)
- added patch to partially fix #12127 (/media/cdrom)

* Thu Aug 30 2007 Michael Shigorin <mike@altlinux.org> 20070830:1.2.10-alt14
- dropped Debian menu file on Ge^H^Hthe floor (#12653)
- merged xmms.desktop with PLD version
  (udarim perevodami po okamenelosti gtk+!)
- added {wmxmms,xmms-cyr-setup}.desktop (minimalistic on translations,
  I don't know enough Kana or Bulgar)

* Wed Mar 28 2007 Michael Shigorin <mike@altlinux.org> 20070328:1.2.10-alt13
- security fix for CVE-2007-0653, CVE-2007-0654:
  integer overflow/underflow in bmp.c (skin loader);
  patch extracted from Ubuntu advisory package by Igor Zubkov (icesik@),
  see also #11172
- minor linking patch by icesik@ (#11177)

* Sun Dec 17 2006 Michael Shigorin <mike@altlinux.org> 20061217:1.2.10-alt12
- applied id3v2 segfault fix by Suren Chilingaryan (#10258)
- borrowed xmms.desktop from Gentoo, added be/ru/uk stubs (also #3777)
- removed old hack for "new" (actually broken) libvorbis build
  introduced in 1.2.10-alt7

* Mon Jun 05 2006 Michael Shigorin <mike@altlinux.org> 20060605:1.2.10-alt11
- applied patch provided and recommended by xmms-crossfade author
  (hopefully should avoid lockups)
  NB: works with rebuilt crossfade plugin, or segfaults on song change
  with older one!
- applied patch by Artem Delendik (u2u nm ru) to fix pause with various
  ALSA configurations (#7857, XMMS #1842)
- minor spec cleanup
- 1.2.10-alt10.gns2 changelog pretty-printed
- added xorg-x11-cyrillic-fonts to xmms-cyr-setup requires (#8002)

* Mon May 15 2006 Nick S. Grechukh <gns@altlinux.org> 20060515:1.2.10-alt10.gns2
- merged with mike@.
- both unmerged specs added as sources 201,202.
- xmms.keys moved to separate source instead of in-spec.
- removed creation of pkgdocdir.
- Removed BR on ORBit-devel.
- Fixed build with gcc 4.1. 

* Mon May 08 2006 Nick S. Grechukh <gns@altlinux.org> 20060508:1.2.10-alt10.gns1
- merged with latest mike@ stuff 

* Mon May 08 2006 Michael Shigorin <mike@altlinux.org> 20060508:1.2.10-alt10
- compressed changelog (thanks wrar@ for alerting)

* Mon Dec 26 2005 Michael Shigorin <mike@altlinux.org> 20051226:1.2.10-alt8.M30.1
- enhance wrapper/cyrsetup to support UTF-8 (yay!)
  NB: Unicode support updated gtk+ >= 1.2.10-alt13.M30.1
  or manual gtkrc.utf8 fixup

* Sun Nov 27 2005 Nick S. Grechukh <gns@altlinux.org> 20051127:1.2.10-alt9.gns4
- RusXMMS2

* Mon Oct 10 2005 Michael Shigorin <mike@altlinux.org> 20051010:1.2.10-alt9
- an attempt to workaround X.org/Composite/GTK1 bugs within wrapper
  (http://bugs.xmms.org/show_bug.cgi?id=1907)

* Sun Aug 07 2005 Eugene Vlasov <eugvv@altlinux.ru> 20050808:1.2.10-alt8
- NMU: Fixed saving TYER (year) frame in id3v2 (#7555)

* Sat Aug 06 2005 Boldin Pavel <bp@altlinux.ru> 20050806:1.2.10-alt7.1
- NMU: ALSA autodetect added, removed output_plugin from xmms-wrapper.sh

* Thu Jul 21 2005 Michael Shigorin <mike@altlinux.org> 20050721:1.2.10-alt7
- removed soundwrapper support (see also #7303)
- q&dh for the latest vorbis headers changes (1.1.1-alt1)

* Tue Jun 14 2005 Michael Shigorin <mike@altlinux.org> 20050603:1.2.10-alt6
- added post-1.2.10 fix for #7065 (XMMS bug #1583), should eliminate
  random crashes with any non-official plugins

* Fri Jun 03 2005 Michael Shigorin <mike@altlinux.ru> 20050603:1.2.10-alt5
- rusxmms patch to csa28, thanks Suren Chilingaryan
  (should fix segfault on start in some situations)

* Tue May 03 2005 Michael Shigorin <mike@altlinux.ru> 20050503:1.2.10-alt4
- (really Sat Apr 30 2005, incoming lags :)
- removed patch55 (ARTS autodetection -- done with soundwrapper anyways)
  (partially #3874; #5451, #5730, #6718. *ouch*)
- small shuffle: /usr/bin/xmms is now wrapper with binary in xmms-bin
  (should fix "first run from console results in krakozabras" trouble)
  (could cause keyboard shortcuts reset) [test please]
- added small check to wrapper (should fix "segfault on start", #3874);
  one more to cope with non-recode-enabled build (can use cp1251), #6752
- fixed #6008; thanks Ilya Mashkin (oddity@) for report/patch
- merged alsa-mono-vol-adjust patch from PLD
- merged some Dag's patches (autoconf 1.8 "underquoted" + some for TODO)
- added m4 pack from gentoo to cope with recent autotools demands
- added #xmms-faq.html to docs
- spec cleanup: BuildPreReq unneeded
- patch46 fixed by Alex Gorbachenko (algor@)... really trivial problem
  but the one breaking C++ builds with libxmms (#6195)
- added subqueue patch (#61) by Boldin Pavel <ldavinchi inbox.ru>;
  not applied by default, please apply/build/test/report
- rusxmms up to csa27.4; disabled for now :( -- still causes segfaults
  [reminder: #6752]

* Tue May 25 2004 Michael Shigorin <mike@altlinux.ru> 20040525:1.2.10-alt3
- removed patch56 (NetWM problem was in WindowMaker patches)
- fixed wrapper (honored only explicit LC_CTYPE, all my fault)
- freshened csa patch to 1.2.10-csa27.3 (no changes)

* Tue Mar 02 2004 Michael Shigorin <mike@altlinux.ru> 20040302:1.2.10-alt2
- fixed arts autodetect patch (regarding library permissions)
- finally fixed #3777 (multi-file DnD support in menufile);
  great thanks for reporting/fixing to Dmitry Vukolov (dav@)!
- fixed "more" NetWM support to behave as in 1.2.8 and before;
  thanks for patience and advice to Sergey Pinaev (dfo@)!

* Tue Feb 24 2004 Michael Shigorin <mike@altlinux.ru> 20040224:1.2.10-alt1
- 1.2.10
- csa27.3

* Sat Jan 31 2004 Michael Shigorin <mike@altlinux.ru> 20040131:1.2.9-alt1
- 1.2.9
- csa27 (plus one more fix)
- using id3v2-aware branch of rusxmms (csa) patch
- patch60 (id3v2): 1.2.9 flavour
- patch45 disabled for now (4/5, 1/2 failed)
- patch44 updated against 1.2.9
- patch0 merged to upstream (alsa+crossfade)
- drop gnomexmms ("I'll follow upstream", almost The Beatles :)

* Fri Jan 23 2004 Michael Shigorin <mike@altlinux.ru> 20040123:1.2.8-alt7
- *fixed* xmms-wrapper.sh (forgot to refresh the source from test script)

* Mon Jan 19 2004 Michael Shigorin <mike@altlinux.ru> 20040119:1.2.8-alt6
- fixed xmms-wrapper.sh (was broken regarding parameters) (#3513)
  thanks Dmitry Vukolov (dav@) for pointing out this silly thinko!
- added Belarussian subpackage descriptions,
  thanks to Vital Khil'ko <vk@>
- rusxmms to 1.2.8-csa23.2:
  - upstream fixed "Jump to" window recoding;
  - partially (.rus) included docs
- aclocal-mess-cleanup patch (see alt5) now applied
- moved xmms.keys from gnome subpackage to main one
- moved wmxmms to subpackage, added menufile
- built against libalsa-1.0.1 (shouldn't matter)
- spec cleanup

* Wed Jan 07 2004 Michael Shigorin <mike@altlinux.ru> 20040107:1.2.8-alt5
- added id3v2 patch by Yonas <yonas_ yahoo com> (#3392, xmms #335);
  adapted for use with rusxmms-patched 1.2.8 by Alexey Morozov <morozov@>
- added aclocal-mess-cleanup patch by Alexey Morozov <morozov@>
  (not applied for now, waiting 'till libtool gets fixed)
- added cyr-setup subpackage to enable single-click ready-to-use XMMS
  for Belarussian, Russian and Ukrainian users
- added wrapper to do the cyr init for first run with cyrillic locales
- added README.ALT containing packaging policy
- added Ukrainian subpackage descriptions
- fixed annoying "xmms-logo.xpm: file listed twice" :-)

* Sun Jan 04 2004 Michael Shigorin <mike@altlinux.ru> 20040104:1.2.8-alt4
- one-liner fix for crossfade + alsa-out segfault on exit (#3427);
  thanks to Peter Eisenlohr <p.eisenlohr gmx net> for that
- cleaned up "without-gnome" build deps
- spec cleanup (one more stale #patch removed)

* Fri Dec 05 2003 Michael Shigorin <mike@altlinux.ru> 20031205:1.2.8-alt3
- rusxmms to csa22.2
- TEXTREL workaround (won't fix asm for Input/libmpg123.so)
- package ALSA output plugin (got included in 1.2.8)
- disabled building static libraries by default
- removed *.la from devel subpackage

* Tue Oct 28 2003 Michael Shigorin <mike@altlinux.ru> 20031028:1.2.8-alt2.22.1
- csa22.1

* Mon Oct 27 2003 Michael Shigorin <mike@altlinux.ru> 20031027:1.2.8-alt2.22
- updated rusxmms to csa22

* Sat Oct 25 2003 Michael Shigorin <mike@altlinux.ru> 20031025:1.2.8-alt2
- moving to PLD-like plugin package naming scheme
- introduced %_sysconfdir/rpm/macros.d/%name in lib%name-devel
- rusxmms updated to 1.2.8-csa21.1 (dynamic enca support, minor fixes)
- fixed some source file permissions

* Fri Oct 24 2003 Michael Shigorin <mike@altlinux.ru> 1.2.8-alt1.20
- rusxmms updated to 1.2.8-csa20 (full enca support, streaming fixes)

* Fri Oct 24 2003 Michael Shigorin <mike@altlinux.ru> 1.2.8-alt1
- 1.2.8
- removed idcin (excluded in upstream)
- changed recode patch to rusxmms.sf.net's version (1.2.8-csa19)
  as it's up to date and active
- removed perversive (gc) build of xmms-shell and sox effects:
  xmms-shell is built separately and sox is outdated (source removed from
  author's site) and widely outperformed by xmms-ladspa) 
- fixed patch55 (arts plugin autodetect)
- removed old-forgotten libxmms.so.0 symlink
- spec cleanup

* Thu Oct 31 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.7-alt7
- Added patches from Alexey Morozov <morozov@novosoft.ru>
  - Re-applied GTK+ File Browsing fix patch
  - Re-applied autoconf-2.5 / automake-1.6 compatibility patches
  - automake-1.6 fixes for build process
- Fixed xmms-locallib patch

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.7-alt6
- Rebuilt in new environment
- Updated xmms-shell to 0.99.3
- Now we don't build xmms-gnome package

* Wed Aug 27 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.7-alt5
- Fixed recoding - now xmms don't recode characters that absent in
  result codeset. Thnx to Vitaly Lipatov
- Added gcc3 patches from MDK

* Wed Jul 31 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.7-alt4
- Rebuilt with new OGG
- Changed make_build to make - bugs with man pages

* Mon Apr 29 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.7-alt3
- Package xmms splitted to xmms & libxmms

* Thu Apr 11 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.7-alt2
- Updated xmms-shell & 3dse plugins to latest versions

* Tue Mar 05 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.7-alt1
- 1.2.7
- Fixed Russian description for xmms package

* Thu Jan 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.6-alt1
- 1.2.6-release
- Updated rus & intl patches - fixed some bugs (Apply in preferences
  & Vorbis recoding)
- Updated russian translation file

* Mon Dec 10 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.2.6-alt0.2.pre1
- Fixed requires for xmms-vorbis (>= 1.0rc2). Thanx to Mikhail Yakshin.
- Fixed Requires (%version-%release).

* Fri Dec 07 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.2.6-alt0.1.pre1
- 1.2.6-pre1
- Fixed filelist
- Some spec cleanup

* Mon Nov 19 2001 Mikhail Zabaluev <mhz@altlinux.ru> 1.2.5-alt3
- Fixed ORBit cflags

* Thu Jun 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.2.5-alt2
- Fixed plugin.h

* Wed Jun 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.2.5-alt1
- Update to new version - 1.2.5
- Fix some patches
- Added manpages to xmms
- Remove all entries in changelog before 2001
- Some spec cleanup

* Wed Apr 25 2001 Kostya Timoshenko <kt@altlinux.ru> 1.2.4-ipl7mdk
- Moved static libraries to devel-static subpackage.

* Fri Mar 16 2001 Konstantin Volckov <goldhead@linux.ru.net>  1.2.4-ipl6mdk
- Final rebuild for RE

* Mon Mar 12 2001 Kostya Timoshenko <kt@petr.kz> 1.2.4-ipl5mdk
- added a patch to fix wchar_t to GdkWChar conversion problem in
  playlist_list.c, thanks to Chun-Chung Chen <cjj@u.washington.edu>
- Geoffrey Lee <snailtalk@mandrakesoft.com>
  - Ugly hack to make it build with the latest glib/gtk.

* Fri Feb  9  2001 Kostya Timoshenko <kt@petr.kz> 1.2.4-ipl4mdk
- change tag Group

* Tue Jan 16 2001 Kostya Timoshenko <kt@petr.kz>
- fix lib policy

* Tue Jan  2 2001 Kostya Timoshenko <kt@petr.kz>
- Use patches by Konstantin Volckov <goldhead@linux.ru.net>
- Build for RE
