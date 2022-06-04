Name:     wxedid
Version:  0.0.27
Release:  alt1

Summary:  wxEDID - A tool for modifying EDID data on Linux
License:  GPL-3.0-only
Group:    System/Configuration/Hardware
Url:      https://sourceforge.net/projects/wxedid/


Packager: Hihin Ruslan <ruslandh@altlinux.ru>

#set_gcc_version 11

Source:   %name-%version.tar

BuildRequires(pre): gcc-c++ 

# Automatically added by buildreq on Sat Jun 04 2022
# optimized out: at-spi2-atk bash4 fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libat-spi2-core libcairo-gobject libgdk-pixbuf libgpg-error libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwxBase3.1-devel perl python3 python3-base sh4
BuildRequires: gcc-c++ libwxGTK3.1-devel

BuildRequires: /proc 

%description
wxEDID is a wxWidgets - based EDID (Extended Display Identification Data) editor.
This is an early stage of development, allowing to modify the base EDID v1.3+ structures.
Support for EDID extensions is planned, but not yet implemented.
Besides normal editor functionality, it currently allows to export to and import EDID data
from text files (hex format) and also to save the structures in a human-readable text format.

%description -l ru_RU.utf8
wxEDID — это основанный на wxWidgets редактор EDID (Extended Display Identification Data).
Это ранняя стадия разработки, позволяющая модифицировать базовые структуры EDID v1.3+.
Поддержка расширений EDID запланирована, но еще не реализована.
Помимо обычных функций редактора, в настоящее время он позволяет экспортировать и импортировать данные EDID.
из текстовых файлов (шестнадцатеричный формат), а также сохранять структуры в удобочитаемом текстовом формате.


%prep
%setup

%build
%autoreconf
%configure
%make_build


%install
%makeinstall_std
install -d %buildroot/%_man1dir/  
install -m 644 man/*  %buildroot/%_man1dir/


%find_lang %name

%files
%_bindir/*
%doc AUTHORS ChangeLog
%_man1dir/*

%changelog
* Sat Jun 04 2022 Hihin Ruslan <ruslandh@altlinux.ru> 0.0.27-alt1
- Initial Build to Sisyphus

