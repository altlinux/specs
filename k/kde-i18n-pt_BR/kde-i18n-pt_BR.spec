%define lng pt_BR
%define lngg Brazil Portuguese

Name: kde-i18n-%lng
Version: 3.5.10
Release: alt2

Group: Graphical desktop/KDE
Summary: %lngg language support for KDE
License: GPL
Url: http://www.kde.org/

BuildArch: noarch
Provides: kde-i18n-lang = %version-%release
Requires: kde-common
Conflicts: kdevelop-i18n < %version-%release 

Source: kde-i18n-%lng-%{version}.tar.bz2
#Source: kde-i18n-%lng-3.3.0.tar.bz2

BuildRequires: kdelibs-devel xml-utils

%description
%lngg language support for KDE.

%prep
#%setup -q -n kde-i18n-%lng-%version
#%setup -q -n kde-i18n-%lng-3.3.0
%setup -q

%build
%K3configure

%make_build

%install
%K3install

%files
%dir %_K3doc/%lng/
%lang(%lng) %_K3doc/%lng/*
#
#%dir %_K3i18n/%lng/
%_K3i18n/%lng/charset
%_K3i18n/%lng/*.desktop
%_K3i18n/%lng/*.png
#
#
#%dir %_K3i18n/%lng/LC_MESSAGES/
%lang(%lng) %_K3i18n/%lng/LC_MESSAGES/*.mo
#
%lang(%lng) %_K3apps/katepart/syntax/logohighlightstyle.%lng.xml
%lang(%lng) %_K3apps/kturtle/data/logokeywords.%lng.xml
%lang(%lng) %_K3apps/kturtle/examples/%lng/
#%lang(%lng) %_K3apps/ktuberling/sounds/%lng
%lang(%lng) %_K3apps/khangman/data/%lng/
%lang(%lng) %_K3apps/khangman/%lng.txt
%lang(%lng) %_K3apps/klettres/%lng/

%changelog
* Mon Mar 14 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt2
- move to alternate place

* Thu Dec 04 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- initial specfile

