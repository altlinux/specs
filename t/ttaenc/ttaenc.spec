Name: ttaenc
Version: 3.4.1
Release: alt3
Summary: The True Audio (TTA) codec lossless audio compressor
Summary(uk_UA.CP1251): Безвтратний аудіокомпресор кодека TTA (The True Audio)
Summary(ru_RU.CP1251): Аудиокомпрессор без потерь кодека TTA (The True Audio)
License: %gpl2only
Group: Sound
URL: http://tta.sourceforge.net/
Source: %name-%version-src.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses

%description
The True Audio (TTA) codec is a free, simple, realtime lossless audio
compressor. Based on adaptive prognostic filters, TTA has compared
favorably to a majority of its popular open-source peers. The codec was
built to offer adequate compression levels while maintaining high
operation speeds.

TTA performs lossless compression on multichannel 8,16 and 24 bits data
of the Wav audio files. Being "lossless" means that no data-quality is
lost in the compression - when uncompressed, the data will be identical
to the original. The compression ratios of TTA depend on the type of
music file being compressed, but the compression size will generally
range between 30%% - 70%% of the original. TTA format supports both of
ID3v1/v2 and APEv2 tags.

%description -l uk_UA.CP1251
The True Audio (TTA) кодек - вільний, простий, безвтратний аудіо-
компресор реального часу. Оснований на адаптивних прогностичних
фільтрах, TTA добре виглядає серед більшості його популярних аналогів з
відкритим кодом. Кодек було розроблено, щоб запропонувати адекватні
рівні стиснення, підьримуючи високі швидкостіоперації.

TTA виконує стиснення без втрат багатоканальних 8, 16 та 24-бітовых
даних аудіо-файлів WAV. "Без втрат" означає, що не втрачаються
властивості даних при стисненні даних - розпаковані дані будуть
ідентичі оригіналу. Коефіцієнт стиснення TTA залежить від типу музики і
звичайно становить 30%% - 70%% від оригиналу. TTA-формат підтримує
ID3v1/v2 та APEv2 теги.

%description -l ru_RU.CP1251
The True Audio (TTA) кодек - свободный, простой аудио-компрессор без
потерь реального времени. Основанный на адаптивных предвещающих
фильтрах, TTA хорошо смотрится в ряду с большинством его популярных
аналогов с открытым кодом. Кодек был разработан, чтобы предложить
адекватные уровни сжатия, сохраняя высокие скорости операции.

TTA выполняет сжатие без потерь многоканальных 8, 16 и 24-битовых
данных аудио-файлов WAV. "Без потерь" означает, что не теряются
свойства данных при сжатии - распакованные данные будут идентичны
оригиналам. Степень сжатия TTA зависит от типа музыки и обычно
составляет 30%% - 70%% от оригинала. TTA-формат поддерживает ID3v1/v2 и
APEv2 тэги.


%prep
%setup -n %name-%version-src
%patch -p1


%build
%define _optlevel 3
%make_build


%install
install -D -m 0755 %name %buildroot%_bindir/%name


%files
%doc README ChangeLog*
%_bindir/*


%changelog
* Sun Feb 15 2009 Led <led@altlinux.ru> 3.4.1-alt3
- cleaned up CFLAGS

* Sun Oct 12 2008 Led <led@altlinux.ru> 3.4.1-alt2
- fixed License

* Sat Sep 01 2007 Led <led@altlinux.ru> 3.4.1-alt1
- 3.4.1:
  + added support for standard input/output interface
  + fixed x86_64 build
- updated %%description

* Mon Nov 06 2006 Led <led@altlinux.ru> 3.3-alt3
- fixed x86_64 build
- fixed description formatting

* Tue Feb 14 2006 Led <led@altlinux.ru> 3.3-alt2
- uk and ru descriptions
- fix spec

* Wed Feb 01 2006 Led <led@altlinux.ru> 3.3-alt1
- initial build
