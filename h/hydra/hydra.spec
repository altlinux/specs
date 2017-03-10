Name: hydra
Version: 8.4
Release: alt1

Summary: A very fast network logon cracker which support many different services
Summary(ru_RU.KOI8-R): Очень быстрый сетевой взломщик с поддержкой множства сервисов
Group: Networking/Other
License: AGPLv3
Url: http://thc.org/thc-hydra/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %name-%version.tar.gz
Source1: x%name.desktop
Source2: xhydra.png
Patch0: hydra-5.4-open-fix.patch
Patch1:         hydra-use-system-libpq-fe.patch
Patch2:         hydra-fix-dpl4hydra-dir.patch

Provides: hydra = %version-%release
Requires: hydra-common hydra-gtk hydra-pwinspector 

# Automatically added by buildreq on Wed Jun 08 2005
BuildRequires: fontconfig freetype2 glib2-devel libatk-devel libgtk+2-devel libpango-devel libpq-devel libssl-devel pkgconfig gcc-c++ libssh-devel desktop-file-utils

%description
A very fast network logon cracker which support many different services

%description -l ru_RU.KOI8-R
Очень быстрый сетевой взломщик с поддержкой множства сервисов 

%package common
Summary: Main hydra executable
Summary(ru_RU.KOI8-R): Основной исполняемый файл hydra
Group: Networking/Other
Provides: hydra-common = %version-%release

%description common
Main hydra executable

%description common -l ru_RU.KOI8-R
Основной исполняемый файл hydra

%package gtk
Summary: Graphical frontend for hydra
Summary(ru_RU.KOI8-R): Графический интерфейс для hydra
Group: Networking/Other
Requires: %name-common = %version-%release
Provides: hydra-gtk = %version-%release

%description gtk
Graphical frontend for hydra

%description gtk -l ru_RU.KOI8-R
Графический интерфейс для hydra

%package pwinspector
Summary: PW-Inspector reads passwords in and prints those which meet the requirements
Summary(ru_RU.KOI8-R): PW-Inspector считывает пароли и отображает соответствующие требованиям
Group: Networking/Other
Provides: hydra-pwinspector = %version-%release

%description pwinspector
PW-Inspector reads passwords in and prints those which meet the requirements.
The return code is the number of valid passwords found, 0 if none was found.
Use for security: check passwords, if 0 is returned, reject password choice.
Use for hacking: trim your dictionary file to the pw requirements of the target.
Usage only allowed for legal purposes.

%description pwinspector -l ru_RU.KOI8-R
PW-Inspector считывает пароли и отображает соответствующие требованиям

%prep

%setup -qn thc-hydra-%{version}

#patch0 -p1

%patch1 -p0
%patch2 -p0

#fix permissions - already fixed upstream in 8.3-dev
chmod -x *.csv hydra-gtk/src/*.c hydra-gtk/src/*.h



%build
#set_automake_version 1.10
#set_autoconf_version 2.5

#export CC=gcc-4.3 CXX=g++-4.3
%configure
%make

%install

#make install PREFIX="%{buildroot}"
# PREFIX="%{buildroot}/usr" MANDIR="%{buildroot}/usr/share/man"

mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
install -m 644 -p %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/

desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1};


%__install -pm755 -d %buildroot%_bindir
%__install -pm755 -d %buildroot%_man1dir
%__install -pm755 %name %buildroot%_bindir/%name
%__install -pm755 x%name %buildroot%_bindir/x%name
%__install -pm755 pw-inspector %buildroot%_bindir/pw-inspector
%__install -pm755 hydra-wizard.sh %buildroot%_bindir/hydra-wizard.sh
%__install -pm755 dpl4hydra.sh %buildroot%_bindir/dpl4hydra.sh



bzip2 %name.1
bzip2 xhydra.1
bzip2 pw-inspector.1
install -pD -m644 %name.1.bz2 %buildroot%_man1dir/%name.1.bz2
install -pD -m644 x%name.1.bz2 %buildroot%_man1dir/x%name.1.bz2
install -pD -m644 pw-inspector.1.bz2 %buildroot%_man1dir/pw-inspector.1.bz2


%find_lang %name

%files  -f %name.lang
%doc CHANGES README LICENSE

%files common
%_bindir/%name
%_bindir/hydra-wizard.sh
%_bindir/dpl4hydra.sh
%_man1dir/hydra*

%files gtk
%doc hydra-gtk/AUTHORS hydra-gtk/COPYING hydra-gtk/INSTALL hydra-gtk/NEWS hydra-gtk/README
%_bindir/x%name
%_man1dir/xhydra*
%_datadir/pixmaps/*
%_datadir/applications/*


%files pwinspector
%_bindir/pw-inspector
%_man1dir/pw-inspector*

%changelog
* Fri Mar 10 2017 Ilya Mashkin <oddity@altlinux.ru> 8.4-alt1
- 8.4

* Fri Jun 17 2016 Ilya Mashkin <oddity@altlinux.ru> 8.2-alt1
- 8.2

* Tue Jul 28 2015 Ilya Mashkin <oddity@altlinux.ru> 8.1-alt2
- build with libssh (Closes: #31173)
- add man pages

* Tue Dec 09 2014 Ilya Mashkin <oddity@altlinux.ru> 8.1-alt1
- 8.1

* Mon May 12 2014 Ilya Mashkin <oddity@altlinux.ru> 8.0-alt1
- 8.0

* Mon Dec 30 2013 Ilya Mashkin <oddity@altlinux.ru> 7.6-alt1
- 7.6

* Sun Aug 11 2013 Ilya Mashkin <oddity@altlinux.ru> 7.5-alt1
- 7.5
- Moved the license from GPLv3 to AGPLv3 (see LICENSE file)

* Sun Jan 20 2013 Ilya Mashkin <oddity@altlinux.ru> 7.4.2-alt1
- 7.4.2

* Thu May 24 2012 Ilya Mashkin <oddity@altlinux.ru> 7.3-alt1
- 7.3

* Sun Feb 12 2012 Ilya Mashkin <oddity@altlinux.ru> 7.2-alt1
- 7.2

* Mon Oct 03 2011 Ilya Mashkin <oddity@altlinux.ru> 7.1-alt1
- 7.1

* Tue Jun 28 2011 Ilya Mashkin <oddity@altlinux.ru> 6.4-alt1
- 6.4

* Mon Jun 13 2011 Ilya Mashkin <oddity@altlinux.ru> 6.3-alt1
- 6.3

* Sun Mar 06 2011 Ilya Mashkin <oddity@altlinux.ru> 5.9.1-alt1
- 5.9.1: fixes for SSH, VNC and LDAP

* Mon Jan 24 2011 Ilya Mashkin <oddity@altlinux.ru> 5.9-alt1
- 5.9
- Change License to GPLv3

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 5.4-alt1.1
- fix build

* Mon Dec 15 2008 Ilya Mashkin <oddity@altlinux.ru> 5.4-alt1
- New version 5.4

* Sun Mar 25 2007 Ilya Mashkin <oddity@altlinux.ru> 5.3-alt2
- fix menu

* Thu Dec 28 2006 Ilya Mashkin <oddity@altlinux.ru> 5.3-alt1
- New version 5.3

* Wed Jun 08 2005 Vitaly Smirnov <device@altlinux.org> 4.7-alt1
- Inital release

