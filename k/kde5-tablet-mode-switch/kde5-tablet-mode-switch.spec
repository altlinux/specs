%define rname kde5-tablet-mode-switch
Name: kde5-tablet-mode-switch
Version: 0.2
Release: alt1
%K5init altplace

Group: Graphical desktop/KDE
Summary: Simple utility to help setup tablet mode on desktop
Url: https://git.altlinux.org/people/zerg/packages/kde5-tablet-mode-switch
License: GPL-2.0-or-later

BuildArch: noarch

Requires: kde5-kdialog

Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf5
BuildRequires: xdg-utils

%description
Simple utility to help setup tablet mode on desktop.

%prep
%setup -n %rname-%version

%install
mkdir -p %buildroot/{%_K5bin,%_K5xdgapp}
install -m 0755 %rname %buildroot/%_K5bin/
install -m 0755 %{rname}.desktop %buildroot/%_K5xdgapp/
# translations
#find po/* -type d | \
#while read d
#do
#    lang=`basename $d`
#    mkdir -p %buildroot/%_K5i18n/$lang/LC_MESSAGES
#    msgfmt -o %buildroot/%_K5i18n/$lang/LC_MESSAGES/%rname.mo $d/%rname.po
#done
%find_lang %name --with-kde --all-name

%files -f %name.lang
%_K5bin/kde5-*tablet*mode*
%_K5xdgapp/*tablet*mode*.desktop

%changelog
* Fri Dec 10 2021 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt1
- setup forceFontDPIWayland

* Thu Nov 18 2021 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial build
