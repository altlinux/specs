Name: ttytest
Version: 1.3
Release: alt4
Summary: ttytest async read-write test and logical stub for terminal lines
License: GPL
Group: System/Libraries
Url: http://ttytest.sourceforge.net/
Packager: Sergey Shilov <hsv@altlinux.org>

Source: %name-%version.tar.bz2

Summary(ru_RU.KOI8-R): асинхронный тест чтения-записи и логическая заглушка для терминальных линий 

%description
ttytest is a small and simple console test-"staircase" of the terminal \
lines (connections between two RS232 devices). The program works in \
modes inverse loop (loopback), shtub and simple terminal. The test consists \
in asynchronous recording in the device the test sequence, and \
reading this sequence from the same device. Readed Data displayed \
in the terminal. To create a reverse loop, can be used a standard \
hardware stub, or nullmodem connection with ttytest in "loopback" mode.

%description -l ru_RU.KOI8-R
ttytest это маленький и простой консольный тест-"лестница" для терминальных \ 
линий (соединений между двумя RS232 устройствами). Программа работает в \
режимах обратной петли, заглушки и простого терминала. Тест состоит \
в асинхронной записи тестовой последовательности в устройство и в \
одновременном чтении этой последовательности из того-же устройства. Прочитанные\
данные выводятся на терминал. Для создания обратной петли можно использовать \
либо стандартную аппаратную заглушку, или нульмодемное соединение с ttytest-ом \
в режиме логической заглушки.

%prep
%setup -q

%build
%make -f Makefile.cvs
%configure
%make

%install
%makeinstall

%files
%_bindir/*
%lang(ru) %_datadir/locale/ru/LC_MESSAGES/*.mo
%_man1dir/*
%lang(ru) %_mandir/ru/man1/* 
%_docdir/*

%changelog
* Sat May 09 2009 Sergey Shilov <hsv@altlinux.org> 1.3-alt4
- run libtoolize before auticonf

* Fri May 08 2009 Sergey Shilov <hsv@altlinux.org> 1.3-alt3
- gear migration

* Wed May 06 2009 Sergey Shilov <hsv@altlinux.org> 1.3-alt2
- added I/0 charset conversion support
- added support of MTK2 codepage
- updated maual pages
- used libtool 2.2 and more
- cleanup spec

* Mon Apr 13 2009 Sergey Shilov <hsv@altlinux.org> 1.3-alt1
- new upstream version.

* Fri Jan 30 2009 Sergey Shilov <hsv@altlinux.org> 1.2-alt1
- added read-only and write-only modes
- added the man page
- added to the mechanism of internationalization
- Russian localization
- POSIX standardization of input-output
- arranged project files
- fixed a lot of small bugs
- ALTLinux port

* Wed Jun 4 2008 Sergey Shilov <hsv@altlinux.org> 1.1-alt1
- Initial release
