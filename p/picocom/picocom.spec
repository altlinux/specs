Name: picocom
Version: 1.6
Release: alt4

Summary: Picocom is a minimal dumb-terminal emulation program
Summary(ru_RU.UTF-8): Пикоком есть крошечная терминалка
License: GPL
Group: Communications
Url: http://picocom.googlecode.com/files/
Packager: Malo Skryleve <malo@altlinux.org>

Source: %name-%version.tar.bz2
Patch: %name-%version.patch

%description
Picocom is a minimal dumb-terminal emulation program.
It is, in principle, very much like minicom, only it's pico
instead of mini! It was designed to serve as a simple, manual,
modem configuration, testing, and debugging tool. It has also
served (quite well) as a low-tech "terminal-window" to allow
operator intervention in PPP connection scripts (something
like the ms-windows "open terminal window before / after dialing"
feature). It could also prove useful in many other similar tasks.
It is ideal for embedded systems since its memory footprint is
minimal (less than 20K, when stripped). Apart from being a handy
little tool, picocom source distribution includes a simple, easy
to use, and thoroughly documented terminal-management library,
which could serve other projects as well. This library hides
the termios(3) calls, and provides a less complex and safer
(though certainly less feature-rich) interface. "picocom"
runs on Linux, and with minor modifications it could run on
any Unix system with the termios(3) library.

%description -l ru_RU.UTF-8
Пикоком есть терминальная программа, подобная миникому, разве лишь
обладающая приставкою пико вместо мини. Был разработан он
в качестве простой программы, позволяющей проводить ручную
настройку модема, его отладку и проверку. Наряду с сим он может
использоваться как терминал низкоуровневого доступа оператором к
соединению точка-точка в скриптах подобно, например, свойству терминала
"открыть окно терминала пред и по дозвону" в МС-Окнах, а также
использоваться во множестве подобных задач. Программа же сия великолепно
подходит для использования во встраиваемых системах, понеже занимаемое
ею пространство памяти достаточно мало, около 20Кб. Кроме того, в
пикоком входит неплохо освещённая крошечная объектная библиотека,
используя код которой программисты могут разрабатывать свои собственные
приложения. Библиотека сия таит вызовы к термиос(3), и его интерфейс
в оной подменяется более простым, удобным и надёжным. Программа
разработана для запуска её на линуксовых системах, а с небольшими
изменениями в коде и на иных юниксоподобных системах с библиотекою
термиос(3).

%prep
%setup
%patch -p1

%build
%make

%install
mkdir -p %buildroot/usr/bin
mkdir -p %buildroot%_man8dir
cp %name %buildroot/usr/bin
cp %name.8 %buildroot%_man8dir

%files
%doc CHANGES CONTRIBUTORS LICENSE.txt NEWS README TODO %name.8.html
%_bindir/*
%_mandir/man?/*

%changelog
* Tue Apr 05 2011 Malo Skryleve <malo@altlinux.org> 1.6-alt4
- Fixed spec. Version 1.6-alt4

* Tue Apr 05 2011 Malo Skryleve <malo@altlinux.org> 1.6-alt3
- Fixed spec file. Version 1.6-alt3

* Thu Mar 31 2011 Malo Skryleve <malo@altlinux.org> 1.6-alt2
- Added gear rules

* Fri Feb 11 2011 Malo Skryleve <malo@altlinux.org> 1.6-alt1
- Initial build for ALT Linux
