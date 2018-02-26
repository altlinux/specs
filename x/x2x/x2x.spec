# SPEC file for x2x

%define baseversion 1.30
%define subversion svn24
%define version %baseversion
%define release alt3.%subversion

Name: x2x
Version: %version
Release: %release

Summary: links two X displays for using single keyboard and mouse
Summary(ru_RU.UTF-8): связывает два X-дисплея для использования одной клавиатуры и мыши

License: BSD
Group: System/X11
URL: http://x2x.dottedmag.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

# Sources could be available from Subversion repository at x2x home page
Source: %name-%subversion.tar.bz2
Source1: README.ALT.utf-8

BuildRequires: imake libXtst-devel xorg-cf-files

%description
x2x links two X displays together so you can use single  mouse and
keyboard to control two displays. Your keyboard and mouse works as
usual on the display they attached to,  until you switch mode, and
then all your input goes to the second display. In other words x2x
acts as software KM  (not KVM)  switch,  although X selection data 
also (should) propagates as expected. 

It's intended for users who have two computers,  with two monitors, 
but who don't want to switch constantly between two keyboard/mouse 
pairs.

%description -l ru_RU.UTF-8
x2x  объединяет два X-терминала вместе и позволяет использовать
одну клавиатуру и мышь для управления Х-сессиями на двух разных
компьютерах.  Клавиатура и мышь  работают как  обычно  с первым 
терминалом (к которому они подключены),  потом  Вы переключаете 
режим - и сигналы от них  перенаправляются на второй  терминал.
Другими словами, x2x работает  как программый KM-переключатель.
Данные из  буфера обмена  X также  (должны)  переноситься между 
терминалами.

Утилита предназначена для пользователей, имеющих на столе два
компьютера с двумя мониторами и уставших постоянно переходить 
от одной пары клавиатура-мышь к другой.

%prep 
%setup -n %name-%subversion
%__cp %SOURCE1 .

%build
xmkmf
%make

%install
%makeinstall DESTDIR=%buildroot
%make install.man DESTDIR=%buildroot

%files
%doc Changes README.ALT.utf-8
%_x11bindir/x2x
%_x11mandir/man1/x2x*

%changelog
* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.30-alt3.svn24
- fix build

* Tue Mar 27 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.30-alt2.svn24
-  SVN release 24:
  - Added -singlesticky option to take in account difference of handling
    sticky keys by different HW, such as Irix one.
  - Fixed one-by-off error resulted in the single pixel at right/down
    border was inaccessible by mouse pointer.
  - Fixed error messages when -dpmsmousue is not used due to
    DPMSForceLevel misuse.

* Sun Jul 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.30-alt1.svn20060511
- Initial build for ALT Linux
- Adding README.ALT.utf-8

* Thu May 11 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.30.svn20060511-alt0
- Updating to current version (rev.23) from SVN repository

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.30-alt0.svn20060423
- Updating to current version from SVN repository

* Sun Jan 29 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.30-alt0.svn20060129
- Version from SVN repository

* Thu Sep 29 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.30-alt0.beta
- Initial build

