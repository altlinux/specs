%define lng tt_RU
%define lngg Tatarish (Russia)

Name: kde-i18n-%lng
Version: 3.5.9
Release: alt3

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE
License: GPL
Url: http://www.kde.org/

Packager: Andrey Cherepanov <cas@altlinux.ru>

Provides: kde-i18n-lang = %version-%release
Requires: kde-common
BuildArch: noarch
Conflicts: kdevelop-i18n < %version-%release 

Source: %name-%{version}.tar.bz2

BuildRequires: kdelibs-devel xml-utils

%description
%lngg language support for KDE.

%prep
%setup -q
find -type f -name *.gmo | while read f; do rm -f $f; done
find -type f -name index.cache.bz2 | while read f; do rm -f $f; done

%build
%set_automake_version 1.7
%set_autoconf_version 2.5
%__autoreconf
perl admin/am_edit
%K3configure
%make_build

%install
%K3install

%files
%_K3i18n/%lng/charset
%_K3i18n/%lng/*.desktop
%_K3i18n/%lng/*.png
%lang(%lng) %_K3i18n/%lng/LC_MESSAGES/*.mo

%changelog
* Thu Mar 24 2011 Andrey Cherepanov <cas@altlinux.org> 3.5.9-alt3
- Fix build without libarts

* Tue Mar 01 2011 Andrey Cherepanov <cas@altlinux.org> 3.5.9-alt2
- Migrate to new KDE3 placement

* Thu Jun 19 2008 Andrey Cherepanov <cas@altlinux.ru> 3.5.9-alt1
- initial build for Sisyphus
