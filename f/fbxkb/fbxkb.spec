Name: fbxkb
Version: 0.8
Release: alt1

Summary: Systray indicator of current keyboard layout
Summary(ru_RU.UTF-8): Индикатор текущей раскладки клавиатуры для системного лотка
License: GPLv2
Group: System/Internationalization
Url: http://sourceforge.net/projects/fbxkb/
Vcs: https://gitflic.ru/project/jinn-alt/fbxkb.git
Packager: Dmitriy Khanzhin <jinn@altlinux.org>

Source: %name-%version.tar

BuildRequires: libgtk+3-devel libgdk-pixbuf-devel libxkbfile-devel

%description
X11 keyboard indicator and switcher.
It shows a flag of current keyboard in a systray area.
It is NETWM compliant and depends on gtk+ only (no GNOME is needed).

%prep
%setup

%build
./configure --with-gtk3
%make

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/%name
%_desktopdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%doc AUTHORS CHANGELOG CREDITS

%changelog
* Thu Apr 10 2025 Dmitriy Khanzhin <jinn@altlinux.org> 0.8-alt1
- version 0.8 is built with gtk3

* Wed Dec 11 2024 Dmitriy Khanzhin <jinn@altlinux.org> 0.7-alt1
- 0.7

* Mon Aug 04 2008 Nick S. Grechukh <gns@altlinux.org> 0.6-alt1
- initial build

