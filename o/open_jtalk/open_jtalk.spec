%define _unpackaged_files_terminate_build 1
%define dicdir %_datadir/%name/dic

Name: open_jtalk
Version: 1.11
Release: alt1

Summary: Japanese text-to-speech system
Summary(ru_RU.UTF-8): Система синтеза японской речи

License: BSD-3-Clause
Group: Sound
Url: https://open-jtalk.sourceforge.net/

BuildRequires: gcc-c++
BuildRequires: libHTSEngine-devel

Requires: %name-dic = %EVR

Source: %name-%version.tar
Patch: %name-%version-alt-shared-hts_engine.patch

%description
Open JTalk is a Japanese text-to-speech system based on the HTS engine.
It uses Mecab and a dictionary optimized for Open JTalk to analyse text
and to obtain its pronunciation.

Voice data (*.htsvoice) is not shipped with this package and has to be
passed to open_jtalk with the -m option.

%description -l ru_RU.UTF-8
Open JTalk — система синтеза японской речи на основе движка HTS.
Для анализа текста и получения произношения используется Mecab
и словарь, оптимизированный для Open JTalk.

Голосовые данные (*.htsvoice) в пакет не входят и передаются
open_jtalk через опцию -m.

%package dic
Summary: NAIST Japanese dictionary for Open JTalk
Summary(ru_RU.UTF-8): Японский словарь NAIST для Open JTalk
Group: Sound
BuildArch: noarch

%description dic
NAIST Japanese dictionary (mecab-naist-jdic) compiled in UTF-8 encoding
for use with Open JTalk.

%description dic -l ru_RU.UTF-8
Японский словарь NAIST (mecab-naist-jdic), собранный в кодировке
UTF-8, для использования с Open JTalk.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
    --with-charset=UTF-8 \
    --with-hts-engine-header-path=%_includedir \
    --with-hts-engine-library-path=%_libdir
%make

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/%name
mv %buildroot%_prefix/dic %buildroot%dicdir

%check
bin/open_jtalk 2>&1 | grep -q 'Open JTalk'

%files
%doc COPYING README
%_bindir/open_jtalk

%files dic
%doc mecab-naist-jdic/COPYING
%dir %_datadir/%name
%dicdir

%changelog
* Tue Oct 13 2026 Dina Tagantseva <dinchik@altlinux.org> 1.11-alt1
- Initial build for Sisyphus.
