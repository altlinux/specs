%define lng ru
%define lngg Russian

Name: koffice16-i18n-%lng
Version: 1.6.3
Release: alt2

Group: Graphical desktop/KDE
Summary: %lngg language support for koffice16
License: GPL
Url: http://www.koffice.org/

Requires: koffice16-common

Source: koffice-l10n-%lng-%version.tar.bz2
Source1: admin.tar.bz2

BuildArch: noarch
BuildRequires: kdelibs xml-utils kde-common-devel

%description
%lngg language support for koffice.

%prep
%setup -q -n koffice-l10n-%lng-%version -a1


%build
%K3configure
%make_build

%install
%K3install
for f in kdgantt.mo
do
    rm -f %buildroot/%_K3i18n/*/LC_MESSAGES/$f
done

%files
%lang(%lng) %_K3i18n/%lng/LC_MESSAGES/kivio.mo
%_K3doc/%lng/kivio

%changelog
* Thu Mar 10 2011 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt2
- move to alternate place

* Wed Sep 16 2009 Sergey V Turchin <zerg@altlinux.org> 1.6.3-alt1
- initial specfile
