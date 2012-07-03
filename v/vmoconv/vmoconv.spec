Name: vmoconv
Version: 1.0
Release: alt2
License: GPL
Group: Communications
URL: http://triq.net/obex/downloads.html
Packager: Yury Aliaev <mutabor@altlinux.org>

Source0: http://triq.net/obex/%{name}-%{version}.tar.gz
Patch1: %name-%version-configure_in-alt.patch
Patch2: %name-%version-fixincludes-alt.patch

BuildRequires: libgsm-devel

Summary: VMOconv converts Siemens phones VMO and VMI audio files to gsm and wav
Summary(ru_RU.KOI8-R): VMOconv -- конвертер файлов из форматов Siemens VMO и VMI в gsm и wav

%description
This package includes two simple convertes to get from VMO to GSM and vice
versa. Additionally there is a patched GSM audio library contained that
converts to WAV. It's well tested with Siemens (S/ME45, SL45 and M55) and should
work on all Siemens VMO audio files.

%description -l ru_RU.KOI8-R
В состав пакета входят две простых программы для преобразования файлов из
формата VMO в формат GSM и наоборот. Также он позволяет конвертировать файлы в
формат WAV. Работа программ из пактета проверялась на телефонах марки Siemens
S/ME45, SL55 и M55. Они должны работать со всеми файлами формата Siemens VMO.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
autoreconf -fisv
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%doc AUTHORS README THANKS

%changelog
* Mon Dec 29 2006 Yury Aliaev <mutabor@altlinux.org> 1.0-alt2
- fixed build with new toolchain (some includes were missed)

* Sat Dec 09 2006 Yury Aliaev <mutabor@altlinux.org> 1.0-alt1
- First build for ALT Linux Sisyphus
