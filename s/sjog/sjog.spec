Name: sjog
Version: cvs20040812
Release: alt4

Summary: A program to use the "Jog Dial" on Sony Vaio Laptops
Summary (ru_RU.UTF-8): Программа, позволяющая использовать ручку прокрутки на портативных компьютерах Sony Vaio
License: GPL
Group: System/Configuration/Other
Url: http://sjog.sourceforge.net/
Source0: %name-%version.tar.gz
Source1: setbrightness.pamd
Source2: setbrightness.apps
Source3: sjog
BuildRequires: imake libgtk+2-devel libXt-devel libXtst-devel xorg-cf-files

%description
The aim of S-Jog is to give Linux a nice graphical application to manage
Jog-Dial wheel on Sony Vaio laptops. It utilizes the Sony Programmable I/O
driver in recent 2.4.x kernels or the legacy SPIC driver provided in S-Jog
distribution (only available from source package).

Currently, S-Jog is able to launch applications defined in the sjogrc file,
adjust the screen brightness level and also the master volume of the sound
card. Also S-Jog makes the Jog-Dial work like a mousewheel and it runs in
background.

%description -l ru_RU.UTF-8
Назначение программы S-Jog - предоставить удобный графический интерфейс 
для функций ручки прокрутки на портативных компьютерах Sony Vaio. Программа
использует драйвер программируемого ввода/вывода в новых версиях ядра 2.4 
или старый драйвер SPIC, который содержится в пакете исходных текстов S-Jog.

В настоящее время S-Jog может запускать перечисленные в файле sjogrc программы,
насраивать яркость экрана и уровень громкости. Кроме того, S-Jog позволяет 
использовать ручку вместо колеса мыши и может работать в фоновом режиме.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall
# consolehelper
%__install -pD -m640 %SOURCE1 $RPM_BUILD_ROOT%_sysconfdir/pam.d/setbrightness
%__install -pD -m640 %SOURCE2 $RPM_BUILD_ROOT%_sysconfdir/security/console.apps/setbrightness
%__mkdir_p $RPM_BUILD_ROOT%_bindir
%__mkdir_p $RPM_BUILD_ROOT%_sbindir
%__mv $RPM_BUILD_ROOT%_bindir/setbrightness $RPM_BUILD_ROOT%_sbindir/setbrightness
%__ln_s %_libdir/helper/consolehelper $RPM_BUILD_ROOT%_bindir/setbrightness
# autorun
%__install -pD -m755 %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/X11/xinit.d/sjog

%find_lang %name

%post
if ! [ -c /dev/sonypi ]; then
   mknod /dev/sonypi c 10 63
fi

%files -f %name.lang
%config(missingok,noreplace) %_sysconfdir/pam.d/setbrightness
%config(missingok,noreplace) %_sysconfdir/security/console.apps/setbrightness
%_sysconfdir/X11/xinit.d/*
%_bindir/*
%_sbindir/setbrightness
%_datadir/sjog
%config(noreplace) %_sysconfdir/sjogrc
%_man1dir/*
%doc README TODO AUTHORS COPYING ChangeLog NEWS

%changelog
* Fri Jan 05 2007 Vyacheslav Dikonov <slava@altlinux.ru> cvs20040812-alt4
- buildfix

* Tue Sep 14 2004 Vyacheslav Dikonov <slava@altlinux.ru> cvs20040812-alt3
- Autorun, create sonypi device if missing

* Fri Aug 27 2004 Vyacheslav Dikonov <slava@altlinux.ru> cvs20040812-alt2
- spec fix

* Tue Aug 04 2004 Vyacheslav Dikonov <slava@altlinux.ru> cvs20040812-alt1
- CVS version with Fn and GTK2, -t option fix, generic rc file

* Tue Aug 04 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.6-alt2
- i18n

* Tue Aug 03 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.6-alt1
- ALTLinux build
