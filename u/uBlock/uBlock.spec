%def_enable git
%def_disable firefox

%define cid            uBlock0@raymondhill.net
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

%define cidf_dir       %firefox_noarch_extensionsdir/%cid

Name: uBlock
Version: 1.9.16.0
Release: alt1

Summary: uBlock: an efficient blocker extension for your browser. Fast, potent, and lean
License: GPLv3
Group: Other
Url: https://github.com/chrisaljoudi/uBlock
BuildArch: noarch

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name.tar
Source1: META-INF.tar

# Automatically added by buildreq on Sat Nov 05 2016
# optimized out: python-base python-modules
BuildRequires: python-modules-compiler python-modules-encodings python-modules-json


%package -n palemoon-uBlock
Group: System/Libraries
Summary: Plugin  uBlock for Pale Moon
Requires: palemoon

%if_enabled firefox
%package -n firefox-uBlock
Group: System/Libraries
Summary: Plugin  uBlock for Firefox
Requires: firefox
%endif

BuildRequires(pre):	rpm-build-palemoon

%if_enabled firefox
BuildRequires(pre):	rpm-build-firefox
%endif

%description
An efficient blocker: easy on memory and CPU footprint, and yet can load and enforce
thousands more filters than other popular blockers out there.


%description -l ru_RU.utf8
uBock-origin - эффективный блокировщик: он использует меньше оперативной памяти и меньше нагружает ЦП, 
чем другие популярные блокировщики, при этом используя больше фильтров.

%description -n palemoon-uBlock
Plugin uBlock: an efficient blocker extension for palemoon. Fast, potent, and lean.

%description  -l ru_RU.utf8 -n palemoon-uBlock
Плагин uBlock  эффективный блокировщик: он использует меньше оперативной памяти и меньше нагружает ЦП, 
чем другие популярные блокировщики, при этом используя больше фильтров.

%if_enabled firefox
%description -n firefox-uBlock
Plugin uBlock: an efficient blocker extension for palemoon. Fast, potent, and lean.

%description  -l ru_RU.utf8 -n firefox-uBlock
uBock-origin - эффективный блокировщик: он использует меньше оперативной памяти и меньше нагружает ЦП, 
чем другие популярные блокировщики, при этом используя больше фильтров.
%endif

%prep
%setup -n %name

%if_enabled git
%build
tools/make-firefox.sh
tar -x -f  %SOURCE1
%endif


%install
pushd META-INF/
%if_enabled firefox
install -d -m755  %buildroot/%cidf_dir/META-INF/
install -Dp -m644  ./* %buildroot/%cidf_dir/META-INF/
%endif
install -d -m755  %buildroot/%cid_dir/META-INF/
install -Dp -m644  ./* %buildroot/%cid_dir/META-INF/
popd


%if_enabled git
pushd dist/build/uBlock0.firefox/
%endif

mkdir -p %buildroot/%cid_dir
cp -r * %buildroot/%cid_dir

mkdir -p %buildroot/%cidf_dir
cp -r * %buildroot/%cidf_dir


%files -n palemoon-uBlock
%cid_dir

%if_enabled firefox
%files -n firefox-uBlock
%cidf_dir
%endif

%changelog
* Sat Nov 05 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.9.16.0-alt1
- Version 1.9.16

* Sat Mar 19 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.6.4.0-alt2
- Version from xpi

* Sat Mar 19 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.6.4.0-alt1
- Version 1.6.4

* Sun Nov 22 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.3.5.0-alt1
- new Version

* Fri Jul 31 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.0.1-alt1.2
- Add  Requires

* Tue Jul 28 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.0.0.1-alt1.1
- Fix Builds

* Mon Jul 27 2015 Hihin Ruslan <ruslandh@altlinux.ru> 1.0,0.1-alt1
- initial build for ALT Linux Sisyphus
