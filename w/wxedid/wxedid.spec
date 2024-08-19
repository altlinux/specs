%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name:     wxedid
Version:  0.0.31
Release:  alt1

Summary:  wxEDID - A tool for modifying EDID data on Linux
License:  GPL-3.0-only
Group:    System/Configuration/Hardware
Url:      https://sourceforge.net/projects/wxedid/

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:   %name-%version.tar
Source1:  %name.desktop
Source2:  wxEdid.svg  

BuildRequires(pre): gcc-c++ 

# Automatically added by buildreq on Sat Jun 04 2022
# optimized out: at-spi2-atk bash4 fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libat-spi2-core libcairo-gobject libgdk-pixbuf libgpg-error libstdc++-devel libwayland-client libwayland-cursor libwayland-egl libwxBase3.1-devel perl python3 python3-base sh4
BuildRequires: gcc-c++ libwxGTK3.2-devel

BuildRequires: /proc 

%description
wxEDID is a wxWidgets - based EDID (Extended Display Identification Data)
editor.  This is an early stage of development, allowing to modify the base
EDID v1.3+ structures.  Support for EDID extensions is planned, but not yet
implemented.  Besides normal editor functionality, it currently allows to
export to and import EDID data from text files (hex format) and also to save
the structures in a human-readable text format.

%description -l ru_RU.utf8
wxEDID — это основанный на wxWidgets редактор EDID (Extended Display
Identification Data).  Это ранняя стадия разработки, позволяющая модифицировать
базовые структуры EDID v1.3+.  Поддержка расширений EDID запланирована, но еще
не реализована.  Помимо обычных функций редактора, в настоящее время он
позволяет экспортировать и импортировать данные EDID.  из текстовых файлов
(шестнадцатеричный формат), а также сохранять структуры в удобочитаемом
текстовом формате.


%prep
%setup

%build
%autoreconf
%configure --enable-build-mode=none
%make_build

%install
%makeinstall_std
install -d %buildroot/%_man1dir/  
install -m 644 man/*  %buildroot/%_man1dir/
install -d  %buildroot/%_desktopdir
install -m 644 %SOURCE1 %buildroot/%_desktopdir/
install -d  %buildroot/%_liconsdir/
install -m 644 %SOURCE2 %buildroot/%_liconsdir/

%find_lang %name

%files
%_bindir/*
%doc AUTHORS ChangeLog
%_man1dir/*
%_desktopdir/*
%_liconsdir/*

%changelog
* Mon Aug 19 2024 L.A. Kostis <lakostis@altlinux.ru> 0.0.31-alt1
- NMU:
  + update to 0.0.31.
  + do not strip during install.

* Fri Jul 08 2022 Anton Midyukov <antohami@altlinux.org> 0.0.27-alt2
- rebuilt with stable wxGTK3.2

* Sun Jun 05 2022 Hihin Ruslan <ruslandh@altlinux.ru> 0.0.27-alt1.1
- Added desktop and icon files 

* Sat Jun 04 2022 Hihin Ruslan <ruslandh@altlinux.ru> 0.0.27-alt1
- Initial Build to Sisyphus
