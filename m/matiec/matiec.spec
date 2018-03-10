Name: matiec
Version: 20180301
Release: alt1

Summary: IEC 61131-3 compiler
Summary(ru_RU.UTF-8): МЭК 61131-3 компилятор

License: GPLv3+
Group: Engineering
Url: https://bitbucket.org/mjsousa/matiec

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildPreReq: gcc-c++ flex

%description
This project has the goal of producing an open source compiler for
the programming languages defined in the IEC 61131-3 standard.
These programming languages are mostly used in the industrial
automation domain, to program PLCs (Programmable Logic Controllers).

This standard defines 5 programming languages:
  - IL : Instructtion List
         A textual programming language, somewhat similar to assembly.
  - ST : Structured Text
         A textual programming language, somewhat similar to Pascal.
  - FBD: Function Block Diagram
         A graphical programming language, somewhat similar to an
         electrical circuit diagram based on small scale integration
         ICs (Integrated Circuits) (counters, AND/OR/XOR/... logic
         gates, timers, ...).
  - LD : Ladder Diagram
         A graphical programming language, somewhat similar to an
         electrical circuit diagram based on relays (used for basic
         cabled logic controllers).
  - SFC: Sequential Function Chart
         A graphical programming language, that defines a state
         machine, based largely on Grafcet. (may also be expressed
         in textual format).

%description -l ru_RU.UTF-8
Этот проект имеет целью создание компилятора с открытым исходным
кодом для языков программирования, определённых стандартом МЭК 
61131-3. Эти языки программирования в основном используются для
программирования ПЛК (программируемых логических контроллеров).

Этот стандарт определяет 5 языков программирования:
  - IL:  Instructtion List (список инструкций)
         Язык текстового программирования, похож на ассемблер.
  - ST:  Structured Text (cтруктурированный текст)
         Язык текстового программирования, похож на Паскаль.
  - FBD: Function Block Diagram (диаграммы функциональных блоков)
         Графический язык программирования, похож на электрическую
         схему, основанную на малых интегральных схемах (счетчики,
         логические вентили AND / OR / XOR / ..., таймеры, ...).
  - LD:  Ladder Diagram (релейно-контактные схемы)
         Графический язык программирования, напоминающий
         электрическую схему, основанную на реле.
  - SFC: Sequential Function Chart (последовательнаые функциональные схемы)
         Графический язык программирования, который определяет
         машину состояний, основанную в основном на Grafcet.
         (Может также выражаться в текстовом формате).

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%_libexecdir/%name
cp -r lib/* %buildroot/%_libexecdir/%name

%files
%doc COPYING readme
%_bindir/*
%_libexecdir/%name
%exclude %_libdir/*.a

%changelog
* Wed Mar 07 2018 Anton Midyukov <antohami@altlinux.org> 20180301-alt1
- New snapshot.

* Thu Sep 28 2017 Anton Midyukov <antohami@altlinux.org> 20170920-alt1
- New snapshot.

* Mon Sep 04 2017 Anton Midyukov <antohami@altlinux.org> 20170830-alt1
- New snapshot.

* Sun Jul 09 2017 Anton Midyukov <antohami@altlinux.org> 20170703-alt1
- New snapshot.

* Sat May 27 2017 Anton Midyukov <antohami@altlinux.org> 20170510-alt1
- New snapshot.

* Fri Apr 28 2017 Anton Midyukov <antohami@altlinux.org> 20170416-alt1
- Initial build for ALT Linux Sisyphus.
