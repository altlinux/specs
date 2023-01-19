Name: fbgrab
Version: 1.5
Release: alt1

Summary: fbgrab - takes screenshots using the framebuffer device
Summary(ru_RU.UTF-8): gbgrab - программа для создания скриншотов с помощью устройста фреймбуфера (/dev/fb*)

License: GPL-2
Group: Graphics
URL: https://github.com/GunnarMonell/fbgrab

Source: %name-%version.tar

Source1: Readme_ru


# Automatically added by buildreq on Thu Jan 19 2023
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error sh4 zlib-devel
BuildRequires: libpng-devel


%description
fbgrab  reads  the  framebuffer device (/dev/fb*) or a dump thereof and
saves a PNG image file. You can use it for  making  screenshots  of  of
virtually  any  application, from traditional test applications to your
X-windows desktop, as well as framebuffer applications.

%description  -l ru_RU.UTF-8
fbgrub считывает содержимое устройства фреймбуфера (/dev/fb*) или его дампа
и преобразует его в файл изображения типа png.
Вы можете использовать его для создания скриншотов практически любого приложения от консольных команд до
создания скриншотов рабочего стола и X-окон приложений, а также приложений, использующих фреймбуфер.


%prep
%setup

%build
%make_build

%install
%makeinstall_std
install -d %buildroot%_docdir/%name
install -D -m644 %SOURCE1  %buildroot%_docdir/%name
install -D -m644 readme.md  %buildroot%_docdir/%name/README
install -D -m644 screenshots/*.png  %buildroot%_docdir/%name

%files
%_bindir/*
%_man1dir/f*
%dir %_docdir/%name
%_docdir/%name/*

%changelog
* Thu Jan 19 2023 Hihin Ruslan <ruslandh@altlinux.ru> 1.5-alt1
- Version 1.5

* Sat Sep 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt4.1
- Rebuilt with libpng15

* Fri Sep 21 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt4
- Remove Russian summary and description.

* Sun Oct 23 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt3
- Rebuild for x86_64.

* Sat Feb 19 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt2
- Rebuild with gcc 3.4.

* Sun May 09 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt1
- Rebuild with %optflags.

* Sat Mar 06 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt0.01
- First ALT Linux release.
