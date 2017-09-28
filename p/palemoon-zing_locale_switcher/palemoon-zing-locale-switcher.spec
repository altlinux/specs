%define cid            mozext_zinglocale@gooeysoftware.com
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

#%define sids_dir       %sm_prefixr/%cid
#%define cidf_dir       %firefox_noarch_extensionsdir/%cid

%define pname zing_locale_switcher

Name:    palemoon-zing_locale_switcher
Version: 3.0.0
Release: alt1
Summary: The Palemoon locale switcher

License: GPL3
Group: Networking/WWW
Url: http://www.gooeysoftware.com/mozaddons/zinglocale/
BuildArch: noarch

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %pname-%version-pm.xpi

BuildRequires(pre):	rpm-build-palemoon
#BuildRequires(pre):	rpm-build-firefox
#BuildRequires(pre):	rpm-build-seamonkey

# Automatically added by buildreq on Thu Jul 16 2015
BuildRequires: libdb4-devel unzip
Requires: palemoon

%description
This is an extension that allows quick and easy changing
of the current language/locale being used by the application.
It works with SeaMonkey, Firefox, and Pale Moon,
and is distributed under the GNU General Public License, V3.

%description -l ru_RU.utf8
Это расширение, которое позволяет быстро и легко менять язык и локаль
используемая в приложениии.
Оно работает с SeaMonkey, Firefox и Pale Moon,

%prep
%setup -c -n %pname-%version/%cid

%install
mkdir -p %buildroot/%cid_dir
cp -r * %buildroot/%cid_dir

mkdir -p %buildroot/%cidf_dir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%cid_dir" ] || rm -rf "%cid_dir"
fi

%files
%cid_dir

%changelog
* Thu Sep 28 2017 Hihin Ruslan <ruslandh@altlinux.ru> 3.0.0-alt1
- Version 3.0

* Fri Jul 31 2015 Hihin Ruslan <ruslandh@altlinux.ru> 2.1.3-alt1.1
- Add  Requires to palemoon

* Thu Jul 16 2015 Hihin Ruslan <ruslandh@altlinux.ru> 2.1.3-alt1
- initial build for ALT Linux Sisyphus
