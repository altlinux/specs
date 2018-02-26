# SPEC file for x2vnc

%define version 1.7.2
%define release alt2

Name: x2vnc
Version: %version
Release: %release

Summary: link two display together, simulating a multiheaded display
Summary(ru_RU.UTF-8): связывает два дисплея для использования одной клавиатуры и мыши

License: GPL v2
Group: System/X11
URL: http://fredrik.hubbe.net/x2vnc.html

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

# Sources could be available from Subversion repository at x2x home page
Source: %name-%version.tar.gz
Source1: README.ALT.utf-8
Patch0: %name-1.7.2-alt-mkdir_fix.patch

BuildRequires: imake libXScrnSaver-devel libXinerama-devel libXrandr-devel libXt-devel libXxf86dga-devel xorg-cf-files

%description
x2vnc  lets you to use two displays on two different computers as
if they were connected to the same  computer and make it possible 
to use single  mouse and  keyboard  for controling  two displays.
While running this program, you can move the mouse pointer beyond
the  edge of your  primary display and the pointer will appear on 
the other computer screen.

It's intended for users who have two computers,  with two monitors, 
but who don't want to switch constantly between two keyboard/mouse 
pairs.

%description -l ru_RU.UTF-8
x2vnc  позволяет использовать  два монитора  на двух  отдельных
компьютерах так, как бы они были подключены к одному компьютеру
и даёт возможность управлять двумя компьютерами с помощью одной
клавиатуры и мыши.  Запустив программу,  вы можете  переместить 
указатель мыши  за границу основного дисплея,  и далее работать 
на экране другого компьютера.

Утилита предназначена для пользователей, имеющих на столе два
компьютера с двумя мониторами и уставших постоянно переходить 
от одной пары клавиатура-мышь к другой.

%prep 
%setup -n %name-%version
%patch0
%__cp %SOURCE1 README.ALT.utf-8

%__mv -f COPYING COPYING.orig
%__ln_s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
%configure
%make

%install
%makeinstall DESTDIR=%buildroot

%files
%doc ChangeLog README README.ALT.utf-8
%doc --no-dereference COPYING
%_x11bindir/%name
%_x11mandir/man1/%{name}*

%changelog
* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.2-alt2
- fix build

* Sun Jul 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.7.2-alt1
- First build for ALT Linux Sisyphus

* Thu Jun 15 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.7.2-alt0
- Initial build

