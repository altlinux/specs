Name: tray_mixer_plus
Version: 0.0.4
Release: alt1.1

Summary: Small tray sound volume
License: GPL
Group: System/Base

Url: forum.altlinux.org
Source0: %name-%version.tar.gz
Source1: tray_mixer_plus.desktop

BuildRequires: libgtk+2-devel  libalsa-devel

Summary(ru_RU.UTF-8): Маленькая программа регулирующая громкость

%description
Small tray sound volume control based on "tray" tray_mixer project
by Claudio Matsuoka and other authors.

Run this programm with -h option to see help message.

%description -l ru_RU.UTF-8
Небольшая программа регулировки громкости звука для трея.

Базируется на программе tray_mixer проекта tray.
Авторы: Claudio Matsuoka и д.р.

Чтобы помощь, запустите с ключом -h.

%prep
%setup -n %name-%version

%build
make
make locale

%install
mkdir -p %buildroot{%_bindir,%_datadir/applications}
%makeinstall_std
install -pDm644 %SOURCE1 %buildroot%_datadir/applications/
%find_lang %name

%files 
%_bindir/tray_mixer_plus
%_iconsdir/tray_mixer_plus/*
%_datadir/locale/*/LC_MESSAGES/*.mo
%_datadir/applications/*

%changelog
* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.4-alt1.1
- NMU: fixed .desktop category: not a Player, but Mixer.

* Thu Mar 21 2013 Michael Shigorin <mike@altlinux.org> 0.0.4-alt1
- new version with docking bugfixes and a new -s option:
  http://forum.altlinux.org/index.php/topic,28619.msg201123.html#msg201123

* Wed Mar 20 2013 Michael Shigorin <mike@altlinux.org> 0.0.3-alt1
- built for Sisyphus (thx YYY at the forum)

