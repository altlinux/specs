Name: keyfuzz
Version: 0.2
Release: alt1

Epoch: 1

Summary: A Utility for manipulating the scancode/keycode translation tables of keyboard drivers
Summary(ru_RU.utf8): Утилита для работы с таблицами перевода скан-кодов/кодов клавиш драйверовспециальныз клавиатур.

License: GPL-2.0
Group: System/Configuration/Hardware

Url: https://github.com/a-sync/keyfuzz

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar

BuildRequires: libsigsegv-devel

# Automatically added by buildreq on Wed Nov 16 2022
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error perl perl-XML-Parser sh4
BuildRequires: gengetopt gperf lynx xmltoman

%description
 Manipulate the scancode/keycode translation tables of keyboard drivers
 You may use keyfuzz to manipulate the scancode/keycode translation
 tables of keyboard drivers supporting the Linux input layer API (as
 included in Linux 2.6). This is useful for fixing the translation
 tables of multimedia keyboards or laptop keyboards with special
 keys. keyfuzz is not a daemon like Gnome acme which reacts on special
 hotkeys but a tool to make non-standard keyboards compatible with
 such daemons. keyfuzz should be run once at boot time, the
 modifications it makes stay active after the tool quits until
 reboot. keyfuzz does not interact directly with XFree86. However,
 newer releases of the latter (4.1 and above) rely on the Linux input
 API, so they take advantage of the fixed translation tables.

%description -l ru_RU.utf8
"Манипулятор" таблицами перевода скан-кодов/кодов клавиш драйверов клавиатуры.
Вы можете использовать keyfuzz для манипулирования таблицами перевода скан-кодов/кодов клавиш драйверов клавиатуры,
поддерживающих API уровня ввода Linux (входит в состав Linux 2.6).
Это полезно для исправления таблиц перевода мультимедийных клавиатур или клавиатур ноутбуков со специальными клавишами.
keyfuzz — это не демон, подобный Gnome acme, который реагирует на специальные горячие клавиши, а инструмент для обеспечения
совместимости нестандартных клавиатур с  такиими демонами.
keyfuzz следует запускать один раз во время загрузки,  изменения, которые он делает, остаются активными после закрытия инструмента до тех пор,
пока не произоёдёт перезагрузка.
keyfuzz не взаимодействует напрямую с XFree86.
Однако более новые версии Xorg (4.1 и выше) полагаются на входной Linux api, поэтому keyfuzz  и там исправляет коды  нажатия клавиш.
Применим к нестандартными медиа клавиатурам.

%prep
%setup
%__subst 's/vebose/verbose/' man/keyfuzz.8.xml.in

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -d  %buildroot%_initdir/
install -D  %buildroot%_sysconfdir/init.d/%name  %buildroot%_initdir/
rm -rf %buildroot%_sysconfdir/init.d

%check
%make_build check

%files
%_sbindir/*
%_man8dir/*
%doc README

%_sysconfdir/%name
%_initdir/*

%changelog
* Tue Dec 13 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1:0.2-alt1
- Fix Alt Bugs (ALT #44610, #44611, #44612)

* Wed Nov 16 2022 Hihin Ruslan <ruslandh@altlinux.ru> 4.4-alt1
- Initial build for Sisyphus

