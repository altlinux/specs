%define rname kde-file-actions-gost

Name: %rname
Version: 0.8.3
Release: alt2
%K6init

Group: Graphical desktop/KDE
Summary: Simple scripts to encrypt files
Url: https://git.altlinux.org/people/zerg/packages/kde-file-actions-gost
License: GPL-2.0-or-later

Requires: kdialog /usr/bin/openssl
Provides:  kde5-file-actions-gost = %EVR
Obsoletes: kde5-file-actions-gost < %EVR

BuildArch: noarch

Source: %rname-%version.tar

# Automatically added by buildreq on Wed Dec 11 2019 (-bi)
# optimized out: python-modules python2-base python3 python3-base python3-dev python3-module-paste rpm-build-python3 sh4
#BuildRequires: python3-module-mpl_toolkits selinux-policy xdg-utils
BuildRequires(pre): rpm-build-kf6
BuildRequires: xdg-utils

%description
The package adds gost-grasshopper encryption to KDE file manager.

%prep
%setup -n %rname-%version

%build
%install
mkdir -p %buildroot/{%_K6bin,%_K6srv,%_datadir/kio/servicemenus}
install -m 0755 kde-* %buildroot/%_K6bin/
#install -m 0644 *.desktop %buildroot/%_K6srv/
install -m 0644 *.desktop %buildroot/%_datadir/kio/servicemenus/

# translations
find po/* -type d | \
while read d
do
    lang=`basename $d`
    mkdir -p %buildroot/%_K6i18n/$lang/LC_MESSAGES
    msgfmt -o %buildroot/%_K6i18n/$lang/LC_MESSAGES/%rname.mo $d/%rname.po
done
sed -i "s|@LOCALEDATADIR@|%_K6i18n|"  %buildroot/%_K6bin/kde-*crypt-*-gost

%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K6bin/kde-*crypt-*-gost
#%_K6srv/*crypt-*-gost.desktop
%_datadir/kio/servicemenus/*crypt-*-gost.desktop

%changelog
* Fri Dec 27 2024 Sergey V Turchin <zerg at altlinux dot org> 0.8.3-alt2
- fix requires

* Wed Oct 30 2024 Sergey V Turchin <zerg at altlinux dot org> 0.8.3-alt1
- add KDE6 support

* Mon Mar 18 2024 Sergey V Turchin <zerg at altlinux dot org> 0.8.2-alt1
- fix detect openssl

* Mon Mar 18 2024 Sergey V Turchin <zerg at altlinux dot org> 0.8.1-alt1
- fix translations placement

* Tue Nov 07 2023 Sergey V Turchin <zerg at altlinux dot org> 0.8-alt2
- don't hardcode alternate placement

* Mon Sep 04 2023 Sergey V Turchin <zerg at altlinux dot org> 0.8-alt1
- fix cipher name for new openssl (closes: 47294)

* Thu Aug 31 2023 Sergey V Turchin <zerg at altlinux dot org> 0.7-alt1
- fix for new openssl (closes: 47294)

* Fri Jun 26 2020 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- fix encrypt filenames with spaces

* Fri Jun 19 2020 Sergey V Turchin <zerg at altlinux dot org> 0.5-alt1
- make text flexible

* Fri Dec 20 2019 Sergey V Turchin <zerg at altlinux dot org> 0.4-alt1
- checkout password when encrypt

* Fri Dec 20 2019 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt1
- don't show password when encrypt

* Tue Dec 17 2019 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt1
- check for GOST ciphers

* Wed Dec 11 2019 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial build
