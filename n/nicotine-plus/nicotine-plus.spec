%define py_geoip_pkg python3-module-GeoIP
%define oname nicotine+

Name: nicotine-plus
Version: 3.3.4
Release: alt1

Summary: The client program for the SoulSeek filesharing system
Summary(ru_RU.UTF-8): Клиент для файлообменной сети SoulSeek

Group: Networking/File transfer
License: GPLv2
Url: https://github.com/Nicotine-Plus/nicotine-plus

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Nicotine-Plus/nicotine-plus/archive/%version.tar.gz
Source: %oname-%version.tar

Patch: %name-alt-desktop-entry.patch

BuildArch: noarch

AutoProv:yes,nopython3

Provides: nicotine
Obsoletes: nicotine

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-intro

%py3_use pygobject3 >= 3.18
BuildRequires: python3-devel

BuildRequires: desktop-file-utils

Requires: libgtk+3-gir
#add_python_req_skip pywintypes win32con win32gui
#Requires: python-module-sexy python-module-pygtk-libglade

# Mozilla does not embedding anymore
#add_python_req_skip gtkmozembed

%description
Nicotine is a feature-complete client for the SoulSeek filesharing network that
is used primarily to share music.

Nicotine supports everything a SoulSeek client is supposed to do, such as
downloading, uploading, searching, chatting, keeping a "buddy" list and has
lots of other features like finding similar users and getting listening
recommendations based on user's preferences.

Nicotine also supports a country code blocker using the GeoIP library.
To enable this functionality install the %py_geoip_pkg package.

Nicotine is a successor to the PySoulSeek project by Alexander Kanavin.

Nicotine supports psyco, an inline optimizer for python code,
you can install it from python-module-psyco package.

%description -l ru_RU.UTF-8
Nicotine -- это полнофункциональный клиент для файлообменной сети SoulSeek,
ориентированной, прежде всего, на обмен музыкой.

Nicotine поддерживает все стандартные для клиента сети SoulSeek функции, такие
как загрузка и пересылка файлов, поиск, чат, ведение списка "друзей", а также
множество других, как, например, поиск похожих пользователей и получение
рекомендаций по музыке на основе пользовательских предпочтений.

Помимо этого, Nicotine умеет блокировать пользователей из определённых стран,
посредством библиотеки GeoIP. Для включения данной функциональности необходимо
дополнительно установить пакет %py_geoip_pkg.

Nicotine является преемником проекта PySoulSeek, который создал Александр Канавин.

Nicotine поддерживает оптимизатор кода psyco, вы можете установить
его из пакета python-module-psyco.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install

%find_lang nicotine

%files -f nicotine.lang
%_bindir/nicotine
#doc %_docdir/nicotine/
%python3_sitelibdir/pynicotine/
%python3_sitelibdir/nicotine*egg-info
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*.svg
%_man1dir/*
%_datadir/metainfo/

%changelog
* Sun Sep 01 2024 Vitaly Lipatov <lav@altlinux.ru> 3.3.4-alt1
- new version 3.3.4 (with rpmrb script)

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 3.0.6-alt1
- new version 3.0.6 (with rpmrb script)
- switch to python3, cleanup spec

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.4.1-alt2
- fix build requires.

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version (1.4.1) with rpmgs script
- cleanup spec, change sources to github

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.16-alt2.1
- Rebuild with Python-2.7

* Wed Oct 12 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2.16-alt2
- build without gtkmozembed (ALT bug #26129)

* Tue Sep 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2.16-alt1
- build new version
- cleanup spec

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.12-alt1.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for nicotine-plus

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.12-alt1.1
- Rebuilt with python 2.6

* Wed Aug 19 2009 Vitaly Lipatov <lav@altlinux.ru> 1.2.12-alt1
- new version 1.2.12 (with rpmrb script)

* Mon Oct 29 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt2
- remove psyco requires (fix bug #13236)
- cleanup spec

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt1
- new version 1.2.9 (with rpmrb script)

* Fri Jul 06 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt2
- add provides, obsoletes: nicotine
- add some useful requires
- disable old russian translation (it brokes dialogs)

* Fri Jun 08 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.8-alt1
- new version 1.2.8 (with rpmrb script)

* Sat May 26 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.7.1-alt1
- nicotine-plus forks from nicotine

* Fri Mar 25 2005 Dmitry Vukolov <dav@altlinux.ru> 1.0.8-alt2
- rebuilt with python 2.4

* Wed Mar 02 2005 Dmitry Vukolov <dav@altlinux.ru> 1.0.8-alt1
- new version

* Mon Jul 19 2004 Dmitry Vukolov <dav@altlinux.ru> 1.0.7-alt3
- repackaged according to the new python policy
- altered description

* Mon May 10 2004 Dmitry Vukolov <dav@altlinux.ru> 1.0.7-alt2
- added Russian translation
- use %%find_lang to mark language files

* Sat May 01 2004 Dmitry Vukolov <dav@altlinux.ru> 1.0.7-alt1
- initial release for ALT Linux Sisyphus
- patched to use the standard GTK+ directory selection dialog (Debian)

