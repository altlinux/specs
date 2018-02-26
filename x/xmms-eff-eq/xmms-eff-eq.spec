Name: xmms-eff-eq
Version: 0.7
Release: alt2

%define _progname eq-xmms

Summary: Xmms equalizer plugin
Summary(ru_RU.KOI8-R): Модуль эквалайзера для xmms.
License: GPL
Group: Sound
Url: http://sourceforge.net/projects/equ
Packager: Dmitriy Khanzhin <jinn@altlinux.ru>

Source: http://switch.dl.sourceforge.net/sourceforge/equ/%_progname-%version.tar.bz2
Source1: README.alt

# Automatically added by buildreq on Sun Nov 01 2009
BuildRequires: libxmms-devel xmms

%description
EQ is a graphic equalizer effect plugin for XMMS that equalizes everything that XMMS sends to the
output, not just MP3s. This means that your OGG, WAV, etc. files are also equalized.

%description -l ru_RU.KOI8-R
EQ -- модуль графического эквалайзера для XMMS, который обрабатывает всё, что в XMMS отправляется
на вывод, а не только MP3. Это значит, что Ваши файлы форматов OGG, WAV и т.п. также будут
обработаны.

%prep
%setup -n %_progname-%version

%build
%autoreconf
%configure
%make_build

%install
%make libdir=%buildroot%xmms_effectdir install
/bin/cp %SOURCE1 .

%files
%xmms_effectdir/*.so
%doc AUTHORS BUGS COPYING README SKINS TODO README.alt

%changelog
* Sun Nov 01 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 0.7-alt2
- internal RPM macros are replaced by real commands

* Sun Jul 02 2006 Dmitriy Khanzhin <jinn@altlinux.ru> 0.7-alt1
- new version
- updated URLs

* Sun Jan 30 2005 Yury Aliaev <mutabor@altlinux.ru> 0.6-alt1.1
- release number increased to avoid a conflict with Master 2.4 updates

* Sun Jan 16 2005 Yury Aliaev <mutabor@altlinux.ru> 0.6-alt1
- Updated to 0.6

* Sat Dec 20 2003 Yury Aliaev <mutabor@altlinux.ru> 0.5-alt1
- First build for Sisyphus.
