%define cid            pm-localeswitch@palemoon.org
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

%define pname pm_locale_switch

Name:    palemoon-locale_switcher
Version: 3.2.0
Release: alt1

Summary: The Palemoon locale switcher


License: GPL-3
Group: Networking/WWW
Url: http://www.gooeysoftware.com/mozaddons/zinglocale/

# BuildArch: noarch
ExclusiveArch: x86_64 aarch64


Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %pname-%version.xpi
Patch1: %name-bootstrap-3.1.0.patch

BuildRequires(pre):	rpm-build-palemoon

# Automatically added by buildreq on Thu Jul 16 2015
BuildRequires: libdb4-devel unzip
Requires: palemoon

%description
This is an extension that allows quick and easy changing
of the current language/locale being used by the application.
It works with Pale Moon,
and is distributed under the GNU General Public License, V3.

%description -l ru_RU.utf8
Это расширение, которое позволяет быстро и легко менять язык и локаль
используемая в приложениии.
Оно работает с Pale Moon,

%prep
%setup -c -n %pname-%version/%cid
%patch1 -p1


%install
mkdir -p %buildroot/%cid_dir
cp -r pm_locale_switch/. %buildroot/%cid_dir

install -d %buildroot%palemoon_datadir/defaults/pref/

cat << EOF >> %buildroot%palemoon_datadir/defaults/pref/local_switcher_pref.js
pref("intl.locale.matchOS", false);
EOF

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%cid_dir" ] || rm -rf "%cid_dir"
fi

%files
%cid_dir
%palemoon_datadir/defaults/pref/local_switcher_pref.js

%changelog
* Thu Jul 18 2024 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.0-alt1
- Version 3.2.0-alt1

* Thu Dec 21 2023 Hihin Ruslan <ruslandh@altlinux.ru> 3.1.0-alt3
- Add palemoon-locale_switcher-bootstrap-3.1.0.patch

* Sat Dec 09 2023 Hihin Ruslan <ruslandh@altlinux.ru> 3.1.0-alt2.3
- Add local_switcher_pref.js (ALT bug #48746)

* Thu Nov 23 2023 Hihin Ruslan <ruslandh@altlinux.ru> 3.1.0-alt2.2
- Change to ExclusiveArch x86_64 aarch64

* Sun Sep 17 2023 Hihin Ruslan <ruslandh@altlinux.ru> 3.1.0-alt2.1
- Add ExcluderArch ppc64le

* Fri Dec 23 2022 Hihin Ruslan <ruslandh@altlinux.ru> 3.1.0-alt2
- Fix pm_locale_switch
- Remove patch

* Wed Jul 20 2022 Hihin Ruslan <ruslandh@altlinux.ru> 3.1.0-alt1
- New Version

* Thu Feb 01 2018 Hihin Ruslan <ruslandh@altlinux.ru> 3.0.0-alt3
- Fix pm_locale_switch-3.0.0-locale.patch

* Wed Jan 31 2018 Hihin Ruslan <ruslandh@altlinux.ru> 3.0.0-alt2
- Change package name

* Thu Sep 28 2017 Hihin Ruslan <ruslandh@altlinux.ru> 3.0.0-alt1
- Version 3.0

* Fri Jul 31 2015 Hihin Ruslan <ruslandh@altlinux.ru> 2.1.3-alt1.1
- Add  Requires to palemoon

* Thu Jul 16 2015 Hihin Ruslan <ruslandh@altlinux.ru> 2.1.3-alt1
- initial build for ALT Linux Sisyphus

palemoon-locale_swicher-bootstrap-3.1.0.patch
