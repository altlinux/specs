%define cvsdate 20060427
Name: lm3g2dmp
Version: 0.00
Release: alt1.cvs.%cvsdate

Summary: Sphinx utility for convert language model to binary dump file
Summary(ru_RU.UTF-8): Утилита sphinx для конвертирования языковой модели в dump файл
License: BSD-style
Group: Sound
Url: http://cmusphinx.sourceforge.net

Packager: Denis Klimov <zver@altlinux.org>
Source: %name-%version.tar

%description
Sphinx utility for convert language model to binary dump file.

%description -l ru_RU.KOI8-R
Утилита sphinx для конвертирования языковой модели в dump файл.

%prep
%setup

%build
%make_build

%install
install -D %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Thu Jan 10 2008 Denis Klimov <zver@altlinux.ru> 0.00-alt1.cvs.20060427
- initial build for ALT Linux

