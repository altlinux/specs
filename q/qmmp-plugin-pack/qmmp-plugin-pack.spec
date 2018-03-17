%set_verify_elf_method textrel=relaxed

%define		branch 0.12
%define		svn svn7877

Version:	%branch.0
Name:		qmmp-plugin-pack
Release:	alt1.%svn
Summary:	Plugin pack is a set of extra plugins for Qmmp.
Summary(ru_RU.UTF8): Набор дополнительных модулей для Qmmp.
Summary(uk_UA.UTF8): Набір додаткових модулів для Qmmp.
License:	GPLv2
Group:		Sound
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://qmmp.ylsoftware.com/plugins_en.php
Source0:	%name-%branch.tar.bz2

BuildRequires:	libqt4-devel gcc-c++ libqmmp-devel >= %version libtag-devel >= 1.6 libxmp-devel yasm libsamplerate-devel

%description
Plugin pack is a set of extra plugins for Qmmp.

Plugins List
 - FFVideo - FFmpeg-based video plugin
 - FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and embedded cue support)
 - XMP - support for MOD, S3M, IT and others tracker formats
 - SRC - Qmmp Sample Rate Converter Plugin
 - Goom - Qmmp Goom Visual Plugin
 - History - Qmmp Listening History Plugin

%description -l ru_RU.UTF8
Набор дополнительных модулей для Qmmp.

Список модулей
 - FFVideo - плагин видео на базе FFmpeg
 - FFap - улучшенный декодер Monkey's Audio (APE) (поддержка 24-х бит и встроенного cue)
 - XMP - поддержка для MOD, S3M, IT и прочих трекерных форматов
 - SRC - модуль конвертера Sample Rate для Qmmp
 - Goom - Модуль визуализации Goom для Qmmp
 - History - Модуль журнала прослушиваний для Qmmp

%description -l uk_UA.UTF8
Набір додаткових модулів для Qmmp.

Перелік модулів
 - FFVideo - плагін відео на базі FFmpeg
 - FFap - покращений декодер Monkey's Audio (APE) (підтримка 24-х біт та вбудованого cue)
 - XMP - підтримка для MOD, S3M, IT та інших трекерних форматів
 - SRC - модуль конвертера Sample Rate для Qmmp
 - Goom - Модуль візуалізації Goom для Qmmp
 - History - Модуль  журнала прослуховування для Qmmp

%package -n %name-in-ffvideo
Summary: FFVideo - FFmpeg-based video plugin
Summary(ru_RU.UTF8): FFVideo - плагин видео на базе FFmpeg
Summary(uk_UA.UTF8): FFVideo - плагін відео на базі FFmpeg
Group: Video
Requires: qmmp >= %version-%release

%description -n %name-in-ffvideo
FFVideo - FFmpeg-based video plugin

%description -l ru_RU.UTF8 -n %name-in-ffvideo
FFVideo - плагин видео на базе FFmpeg

%description -l uk_UA.UTF8 -n %name-in-ffvideo
FFVideo - плагін відео на базі FFmpeg

%package -n %name-in-ffap
Summary: FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and embedded cue support)
Summary(ru_RU.UTF8): FFap - улучшенный декодер Monkey's Audio (APE) (поддержка 24-х бит и встроенного cue)
Summary(uk_UA.UTF8): FFap - покращений декодер Monkey's Audio (APE) (підтримка 24-х біт та вбудованого cue)
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-in-ffap
FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and embedded cue support) for Qmmp.

%description -l ru_RU.UTF8 -n %name-in-ffap
FFap - улучшенный декодер Monkey's Audio (APE) (поддержка 24-х бит и встроенного cue) для Qmmp.

%description -l uk_UA.UTF8 -n %name-in-ffap
FFap - покращений декодер Monkey's Audio (APE) (підтримка 24-х біт та вбудованого cue) для Qmmp.

%package -n %name-in-xmp
Summary: XMP - support for MOD, S3M, IT and others tracker formats
Summary(ru_RU.UTF8): XMP - поддержка для MOD, S3M, IT и прочих трекерных форматов
Summary(uk_UA.UTF8): XMP - підтримка для MOD, S3M, IT та інших трекерних форматів
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-in-xmp
XMP - support for MOD, S3M, IT and others tracker formats

%description -l ru_RU.UTF8 -n %name-in-xmp
XMP - поддержка для MOD, S3M, IT и прочих трекерных форматов

%description -l uk_UA.UTF8 -n %name-in-xmp
XMP - підтримка для MOD, S3M, IT та інших трекерних форматів

%package -n %name-eff-src
Summary: SRC - Qmmp Sample Rate Converter Plugin
Summary(ru_RU.UTF8): SRC - модуль конвертера Sample Rate для Qmmp
Summary(uk_UA.UTF8): SRC - модуль конвертера Sample Rate для Qmmp
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-eff-src
SRC - Qmmp Sample Rate Converter Plugin

%description -l ru_RU.UTF8 -n %name-eff-src
SRC - модуль конвертера Sample Rate для Qmmp

%description -l uk_UA.UTF8 -n %name-eff-src
SRC - модуль конвертера Sample Rate для Qmmp

%package -n %name-vis-goom
Summary: Qmmp Goom Visual Plugin
Summary(ru_RU.UTF8): Модуль визуализации Goom для Qmmp
Summary(uk_UA.UTF8): Модуль візуалізації Goom для Qmmp
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-vis-goom
Qmmp Goom Visual Plugin

%description -l ru_RU.UTF8 -n %name-vis-goom
Модуль визуализации Goom для Qmmp

%description -l uk_UA.UTF8 -n %name-vis-goom
Модуль візуалізації Goom для Qmmp

%package -n %name-history
Summary: Qmmp Listening History Plugin
Summary(ru_RU.UTF8): Модуль журнала прослушиваний для Qmmp
Summary(uk_UA.UTF8): Модуль  журнала прослуховування для Qmmp
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-history
Qmmp Listening History Plugin

%description -l ru_RU.UTF8 -n %name-history
Модуль журнала прослушиваний для Qmmp

%description -l uk_UA.UTF8 -n %name-history
Модуль  журнала прослуховування для Qmmp

%prep
%setup -q -n %name-svn

%build
export PATH=$PATH:%_qt4dir/bin
# #qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" LIB_DIR=/%_lib INCLUDEPATH+="%_libdir/ffmpeg-static/include" %name.pro
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" LIB_DIR=/%_lib DISABLED_PLUGINS+=FFVIDEO_PLUGIN %name.pro
%make_build VERBOSE=1

%install
%make INSTALL_ROOT=%buildroot%prefix install

# #%files -n %name-in-ffvideo
# #%_libdir/qmmp/Engines/libffvideo.so

%files -n %name-in-ffap
%_libdir/qmmp/Input/libffap.so

%files -n %name-in-xmp
%_libdir/qmmp/Input/libxmp.so

%files -n %name-eff-src
%_libdir/qmmp/Effect/libsrconverter.so

%files -n %name-vis-goom
%_libdir/qmmp/Visual/libgoom.so

%files -n %name-history
%_libdir/qmmp/General/libhistory.so

%changelog
* Sat Mar 17 2018 Motsyo Gennadi <drool@altlinux.ru> 0.12.0-alt1.svn7877
- build svn7877

* Sat Mar 10 2018 Motsyo Gennadi <drool@altlinux.ru> 0.11.0-alt1.svn7871
- build svn7871

* Fri Aug 25 2017 Motsyo Gennadi <drool@altlinux.ru> 0.11.0-alt1.svn7388
- build svn7388

* Mon Apr 17 2017 Motsyo Gennadi <drool@altlinux.ru> 0.11.0-alt1.svn7121
- build svn7121

* Sun Jan 08 2017 Motsyo Gennadi <drool@altlinux.ru> 0.11.0-alt1.svn6953
- build svn6953

* Fri Aug 12 2016 Motsyo Gennadi <drool@altlinux.ru> 0.11.0-alt1.svn6670
- build svn6670

* Sun Jun 26 2016 Motsyo Gennadi <drool@altlinux.ru> 0.11.0-alt1.svn6521
- build svn6521

* Sun Mar 27 2016 Motsyo Gennadi <drool@altlinux.ru> 0.10.0-alt1.svn6199
- build svn6199

* Tue Nov 03 2015 Motsyo Gennadi <drool@altlinux.ru> 0.10.0-alt1.svn5734
- build svn5734
- bump version

* Sun Sep 06 2015 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1.svn5545
- build svn5545

* Sun Jul 26 2015 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1.svn5273
- build svn5273

* Tue Jun 16 2015 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1.svn5161
- build svn5161

* Sun Jun 14 2015 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1.svn5138
- build svn5138

* Thu Dec 25 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1.svn4636
- build svn4636

* Mon Oct 20 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1.svn4587
- rebuild with new qmmp svn snapshot

* Fri Oct 17 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1.svn4582
- build svn4582

* Thu Oct 16 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1.svn4581
- build svn4581

* Thu Aug 07 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1.svn4425
- build svn4425

* Sun Jul 06 2014 Motsyo Gennadi <drool@altlinux.ru> 0.9.0-alt1.svn4344
- build svn4344

* Wed Apr 23 2014 Motsyo Gennadi <drool@altlinux.ru> 0.8.0.1-alt1.svn4266
- build svn4266

* Fri Mar 21 2014 Motsyo Gennadi <drool@altlinux.ru> 0.8.0.1-alt1.svn4183
- build svn4183

* Sat Jan 18 2014 Motsyo Gennadi <drool@altlinux.ru> 0.8.0.1-alt1.svn4101.2
- set_verify_elf_method textrel to relaxed for asm optimization

* Fri Jan 17 2014 Motsyo Gennadi <drool@altlinux.ru> 0.8.0.1-alt1.svn4101.1
- fix git-rules

* Fri Jan 17 2014 Motsyo Gennadi <drool@altlinux.ru> 0.8.0.1-alt1.svn4101
- build svn4101

* Wed Dec 25 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0.1-alt1.svn3984
- build svn3984

* Sat Nov 23 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0.1-alt1.svn3924
- build svn3924

* Thu Nov 14 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3910
- build svn3910

* Thu Nov 07 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3880
- build svn3880

* Fri Oct 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3815
- build svn3815

* Mon Aug 26 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3669
- build svn3669

* Thu Aug 22 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3647
- build svn3647

* Tue Aug 20 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3630
- build svn3630

* Thu Jul 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3555
- build svn3555

* Tue May 21 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3479
- build svn3479

* Wed Jan 16 2013 Motsyo Gennadi <drool@altlinux.ru> 0.7.0-alt1.svn3169
- build svn3169

* Tue Dec 18 2012 Motsyo Gennadi <drool@altlinux.ru> 0.7.0-alt1.svn3077
- build svn3077

* Mon Jul 16 2012 Motsyo Gennadi <drool@altlinux.ru> 0.6.0-alt1.svn2810
- initial build for ALT Linux
