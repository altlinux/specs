Name: bygfoot
Version: 2.3.2
Release: alt1

Summary: The game - a manager of football team
Summary(ru_RU.KOI8-R): Игра - менеджер футбольной команды

License: GPL
Group: Games/Strategy
Url: http://bygfoot.sourceforge.net
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %name-%version.tar.bz2
Patch0:         bygfoot-dso-linking.patch

# Automatically added by buildreq on Tue Nov 22 2005
BuildRequires: fontconfig-devel freetype2-devel glib2-devel libatk-devel libcairo-devel libglitz-devel libgtk+2-devel libpango-devel libpng-devel pkg-config

%description
The game - a manager of football team


%prep
%setup -q -n %name-%version
%patch0 -p0

%build

%configure
%make_build 

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_bindir/bygfoot
%_datadir/bygfoot/

%changelog
* Tue May 06 2014 Ilya Mashkin <oddity@altlinux.ru> 2.3.2-alt1
- 2.3.2

* Sun May 01 2011 Ilya Mashkin <oddity@altlinux.ru> 2.2.1-alt2
- fix build

* Mon Dec 07 2009 Ilya Mashkin <oddity@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Sat Dec 10 2005 Alexander  Plikus <plik@altlinux.ru> 1.9.2-alt1
- new version

* Tue Nov 22 2005 Alexander  Plikus <pav@etersoft.ru> 4.4-alt1
- initial build for ALT Linux Sisyphus

