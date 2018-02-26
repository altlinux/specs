Name: avarice
Version: 2.12
Release: alt1

Summary: Interface for GDB to Atmel AVR JTAG ICE in circuit emulator
Summary(ru_RU.UTF8): Программа, управляющая устройством AVR JTAG ICE
License: GPL
Group: Development/Other
Url: http://avarice.sourceforge.net/
Packager: Malo Skryleve <malo@altlinux.org>

Source: %name-%version.tar

Requires: binutils
BuildPreReq: glibc-kernheaders kernel-headers-common
BuildRequires: glibc-kernheaders kernel-headers-common binutils-devel, gcc-c++

%description
AVaRICE is a program which interfaces the GNU Debugger with the AVR JTAG
ICE available from Atmel.

AVaRICE runs on a POSIX machine and connects to gdb via a TCP socket and
communicates via gdb's "serial debug protocol". This protocol allows gdb
to send commands like "set/remove breakpoint" and "read/write memory".
AVaRICE translates these commands into the Atmel protocol used to
control the AVR JTAG ICE. Connection to the AVR JTAG ICE is via a serial
port on the POSIX machine. Because the GDB <---> AVaRICE connection is
via a TCP socket, the two programs do not need to run on the same
machine. In an office environment, this allows a developer to debug
a target in the lab from the comfort of their cube (or even better,
their home!)

%description -l ru_RU.UTF8
Аварис есть программа, способная управлять видом устройств AVR JTAG ICE
от компании Атмель с помощью отладчика GNU.

Аварис работает на позикс-компьютерах. Он соединяется с GNU-отладчиком
по TCP протоколу и общается с нем, используя его последовательный
отладочный протокол, позволяющий задавать или удалять точки останова,
а также читать из или писать данные в память. Ктому Аварис переводит сии
команды в Атмель-протокол, который и используется для управления
устройствами AVR JTAG ICE. Устройство же должно быть подключено к
последовательному порту компьютера. Поскольку сообщение отладчика
с Аварисом происходит через TCP-соединение, то запускать отладчик
на томже компьютере не обязательно. Сиречь, вполне допустимо и даже
желательно, чтобы разработчик находился не в лаборатории, а в ином месте
или даже дома.

%prep
%setup

%build
%configure
%make

%install
%make DESTDIR=%buildroot install

%files
%doc ChangeLog AUTHORS INSTALL COPYING
%_bindir/*
%_datadir/%name/gdb-avarice-script
%_mandir/man?/*

%changelog
* Fri May 25 2012 Malo Skryleve <malo@altlinux.org> 2.12-alt1
- updated to version 2.12

* Tue Apr 05 2011 Malo Skryleve <malo@altlinux.org> 2.10-alt5
- Fixed spec 2.10-alt5

* Tue Apr 05 2011 Malo Skryleve <malo@altlinux.org> 2.10-alt4
- Fixed spec. Version 2.10-alt4

* Thu Mar 31 2011 Malo Skryleve <malo@altlinux.org> 2.10-alt3
- Fixed Requires field

* Thu Mar 31 2011 Malo Skryleve <malo@altlinux.org> 2.10-alt2
- Added gear rules

* Fri Feb 11 2011 Malo Skryleve <malo@altlinux.org> 2.10-alt1
- initial build for ALT Linux Sisyphus

