Name: hunspell-mhr
Version: 230312
Release: alt2

Summary(ru_RU.UTF-8): Словарь hunspell для лугового диалекта марийского языка
Summary: Hunspell dictionary for meadow dialect of the Mari language
License: GPLv3
Group: Text tools

Url: https://github.com/kod-odin/hunspell-mhr
BuildArch: noarch
Source: %name-%version.tar

Requires: libhunspell

%description -l ru_RU.UTF-8
Словарь Hunspell для лугового диалекта марийского языка

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/myspell/
install -m 644 mhr.dic %buildroot%_datadir/myspell/mhr_RU.dic
install -m 644 mhr.aff %buildroot%_datadir/myspell/mhr_RU.aff

%files
%doc LICENSE
%_datadir/myspell/*

%changelog
* Mon Jun 26 2023 Kirill Izmestev <felixz@altlinux.org> 230312-alt2
- Rename .aff and .dic files to be found out by LibreOffice (closes: 45862)

* Mon Mar 13 2023 Kirill Izmestev <felixz@altlinux.org> 230312-alt1
- Initial build for Sisyphus
