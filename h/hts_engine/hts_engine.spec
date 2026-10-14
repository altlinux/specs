%define _unpackaged_files_terminate_build 1
%define sover 0

Name: hts_engine
Version: 1.10
Release: alt1

Summary: HMM-based speech synthesis engine API
Summary(ru_RU.UTF-8): Движок синтеза речи на основе HMM

License: BSD-3-Clause
Group: Sound
Url: https://hts-engine.sourceforge.net/

Source: %name-%version.tar
Patch: %name-%version-alt-shared-library.patch

%description
hts_engine API is software to synthesize speech waveform from HMMs
trained by the HMM-based speech synthesis system (HTS).

This package contains the hts_engine command-line synthesizer.

%description -l ru_RU.UTF-8
hts_engine API — программа для синтеза речевого сигнала по HMM,
обученным системой синтеза речи HTS.

Пакет содержит консольный синтезатор hts_engine.

%package -n libHTSEngine%sover
Summary: Shared library for hts_engine API
Summary(ru_RU.UTF-8): Разделяемая библиотека hts_engine API
Group: System/Libraries

%description -n libHTSEngine%sover
hts_engine API is software to synthesize speech waveform from HMMs
trained by the HMM-based speech synthesis system (HTS).

This package contains the shared library.

%description -n libHTSEngine%sover -l ru_RU.UTF-8
hts_engine API — программа для синтеза речевого сигнала по HMM,
обученным системой синтеза речи HTS.

Пакет содержит разделяемую библиотеку.

%package -n libHTSEngine-devel
Summary: Development files for hts_engine API
Summary(ru_RU.UTF-8): Файлы для разработки с hts_engine API
Group: Development/C

%description -n libHTSEngine-devel
hts_engine API is software to synthesize speech waveform from HMMs
trained by the HMM-based speech synthesis system (HTS).

This package contains the header file and the library symlink needed
to build applications that use hts_engine API (e.g. Open JTalk).

%description -n libHTSEngine-devel -l ru_RU.UTF-8
hts_engine API — программа для синтеза речевого сигнала по HMM,
обученным системой синтеза речи HTS.

Пакет содержит заголовочный файл и символическую ссылку на библиотеку,
необходимые для сборки программ, использующих hts_engine API
(например, Open JTalk).

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/libHTSEngine.la

%check
bin/hts_engine 2>&1 | grep -q 'hts_engine API'

%files
%doc AUTHORS COPYING NEWS README
%_bindir/hts_engine

%files -n libHTSEngine%sover
%_libdir/libHTSEngine.so.%sover
%_libdir/libHTSEngine.so.%sover.*

%files -n libHTSEngine-devel
%_includedir/HTS_engine.h
%_libdir/libHTSEngine.so

%changelog
* Tue Oct 13 2026 Dina Tagantseva <dinchik@altlinux.org> 1.10-alt1
- Initial build for Sisyphus.
