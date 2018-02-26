%define sourcename gkrellmss
%define plugin ss

Name: gkrellm-%plugin
Version: 2.6
Release: alt1

Summary: GKrellM Sound Scope Plugin
Summary(ru_RU.CP1251): ѕлагин Sound Scope дл€ GKrellM
License: GPL
Group: Monitoring
Url: http://web.wt.net/~billw/%sourcename/%sourcename.html
Source: http://umn.dl.sourceforge.net/sourceforge/%sourcename/%sourcename-%version.tar.gz
#Patch1: %name-alt-ru-2.4.patch.gz
#Source1: ru.po.bz2

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Mon Mar 15 2004
BuildRequires: esound-devel gkrellm-devel glib2-devel libalsa-devel libatk-devel libaudiofile-devel libfftw-devel libgtk+2-devel libpango-devel pkgconfig

%description
GKrellMSS displays a VU meter showing left and right channel audio
levels and also has a chart that shows combined left and right audio
channels as an oscilloscope trace.

%description -l ru_RU.CP1251
GKrellMSS отображает VU —четчик показывающий левый и правый аудио
каналы и также имеет чарт показывающий комбинированые левый и правый
аудио каналы как след осцилографа.

%package common
Summary: %name with ncurses interface
Group: Monitoring
Provides: %sourcename-common = %version
Obsoletes: %sourcename-common < %version
%description common
GKrellMSS displays a VU meter showing left and right channel audio
levels and also has a chart that shows combined left and right audio
channels as an oscilloscope trace.
Common files for this plugin (doc and translation).

%description -l ru_RU.CP1251 common
GKrellMSS отображает VU —четчик показывающий левый и правый аудио
каналы и также имеет чарт показывающий комбинированые левый и правый
аудио каналы как след осцилографа.
ќбщие файлы дл€ этого плагина (документаци€ и перевод).

%package full
Summary: %name with esd and alsa support
Group: Monitoring
Requires: %name-common = %version-%release
Provides: %sourcename, %sourcename-full = %version
Obsoletes: %sourcename <= 2.3, %sourcename-full < %version
Conflicts: %sourcename-alsa, %sourcename-esound, %name-alsa, %name-esound
%description full
GKrellMSS displays a VU meter showing left and right channel audio
levels and also has a chart that shows combined left and right audio
channels as an oscilloscope trace.
Compiled with alsa and esound support.

%description -l ru_RU.CP1251 full
GKrellMSS отображает VU —четчик показывающий левый и правый аудио
каналы и также имеет чарт показывающий комбинированые левый и правый
аудио каналы как след осцилографа.
—обрано с поддрежкой alsa и esound.

%package esound
Summary: %name with esd support
Group: Monitoring
Requires: %name-common = %version-%release
Provides: %sourcename, %sourcename-esound = %version
Obsoletes: %sourcename <= 2.3, %sourcename-esound < %version
Conflicts: %sourcename-alsa, %sourcename-full, %name-alsa, %name-full
%description esound
GKrellMSS displays a VU meter showing left and right channel audio
levels and also has a chart that shows combined left and right audio
channels as an oscilloscope trace.
Compiled with esound support.

%description -l ru_RU.CP1251 esound
GKrellMSS отображает VU —четчик показывающий левый и правый аудио
каналы и также имеет чарт показывающий комбинированые левый и правый
аудио каналы как след осцилографа.
—обрано с поддрежкой esound.

%package alsa
Summary: %name with alsa support
Group: Monitoring
Requires: %name-common = %version-%release
Provides: %sourcename, %sourcename-alsa = %version
Obsoletes: %sourcename <= 2.3, %sourcename-alsa < %version
Conflicts: %sourcename-full, %sourcename-esound, %name-full, %name-esound
%description alsa
GKrellMSS displays a VU meter showing left and right channel audio
levels and also has a chart that shows combined left and right audio
channels as an oscilloscope trace.
Compiled with alsa support.

%description -l ru_RU.CP1251 alsa
GKrellMSS отображает VU —четчик показывающий левый и правый аудио
каналы и также имеет чарт показывающий комбинированые левый и правый
аудио каналы как след осцилографа.
—обрано с поддрежкой alsa.

%prep
%setup -q -n %sourcename-%version
#patch1 -p1
#__install -pD -m644 %SOURCE1 po/ru.po.bz2
#__rm po/ru.po
#__bzip2 -d po/ru.po.bz2

%build
%make_build without-esd=yes enable_nls=1 LOCALEDIR=%_datadir/locale
%__mv src/%sourcename.so src/%sourcename-alsa.so
%__rm src/*.o
%make_build without-alsa=yes enable_nls=1 LOCALEDIR=%_datadir/locale
%__mv src/%sourcename.so src/%sourcename-esd.so
%__rm src/*.o
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale

%install
%__mkdir -p %buildroot%_libdir/gkrellm2/plugins
%__mkdir -p %buildroot%_man5dir
%make_install install enable_nls=1 INSTALLDIR=%buildroot%_libdir/gkrellm2/plugins LOCALEDIR=%buildroot%_datadir/locale
%__install src/%sourcename-alsa.so %buildroot%_libdir/gkrellm2/plugins/
%__install src/%sourcename-esd.so %buildroot%_libdir/gkrellm2/plugins/
%find_lang %sourcename

%files common -f %sourcename.lang
%doc Changelog README Themes

%files full
%_libdir/gkrellm2/plugins/%sourcename.so

%files esound
%_libdir/gkrellm2/plugins/%sourcename-esd.so

%files alsa
%_libdir/gkrellm2/plugins/%sourcename-alsa.so

%changelog
* Tue May 18 2004 Alex Murygin <murygin@altlinux.ru> 2.6-alt1
- renamed to gkrellm-{NAME}
- new version
- removed internationalisation patches (merged to upstream)
- added russian summary, description

* Mon Mar 15 2004 Alex Murygin <murygin@altlinux.ru> 2.4-alt1
- new version
- splitted to full (alsa & esd), esound, alsa and common (translation and docs)
- updated ru translation
- added %name-alt-ru-2.4.patch (i18n)

* Fri Dec 05 2003 Alex Murygin <murygin@altlinux.ru> 2.3-alt1
- Built for ALTLinux

