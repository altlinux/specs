Name: palemoon-virtual
Version: 25.6.0
Release: alt1

%define smr palemoon (dependencies package)

Summary: %smr
License: GPL
Group: Networking/WWW
Url: https://github.com/MoonchildProductions/Pale-Moon

BuildArch: noarch

%description
Virtual packets to Pale Moon

%description -l ru_RU.UTF8
Виртуальные пакеты для Pale Moon

%package -n palemoon-suggested
Summary: %smr
License: GPL
Group: Networking/WWW
Requires:  palemoon >= %version
Requires: palemoon-ru
#Requires: palemoon-uk
#Requires: palemoon-kk
Requires: palemoon-uBlock

%package -n palemoon-full
Summary: %smr
License: GPL
Group: Networking/WWW
Requires: palemoon >= %version
Requires: palemoon-ru
#Requires: palemoon-uk
#Requires: palemoon-kk
Requires: palemoon-tabgroups
Requires: palemoon-uBlock
Requires: palemoon-zing_locale_switcher

%description -n palemoon-suggested
Recommended setplugins to  palemoon

%description -n palemoon-suggested -l ru_RU.UTF8
Рекомендуемый набор раширений palemoon

%description -n palemoon-full
Full set natives plugins to  palemoon

%description -n palemoon-suggested -l ru_RU.UTF8
Полный  набор нативных раширений palemoon

%files -n palemoon-suggested
%files -n palemoon-full

%changelog
* Fri Jul 31 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.6.0-alt1
- initial build for ALT Linux Sisyphus

