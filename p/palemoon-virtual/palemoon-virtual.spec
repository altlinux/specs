Name: palemoon-virtual
Version: 25.6.0
Release: alt3

%define smr palemoon/newmoon (dependencies package)

Summary: %smr
License: GPL
Group: Networking/WWW
Url: https://github.com/MoonchildProductions/Pale-Moon

BuildArch: noarch

%description
Virtual packets to Pale Moon

%description -l ru_RU.UTF8
Виртуальные пакеты для Pale Moon


%package -n palemoon-html5
Summary: %smr
License: GPL
Group: Networking/WWW
Requires: gst-plugins-bad1.0 
Requires: gst-plugins-gl
Requires: gst-plugins-good1.0 
Requires: gst-plugins-nice1.0 
Requires: gst-plugins-ugly1.0 
Requires: gst-plugins1.0-tools
#Requires: gstreamer-java 
Requires: gstreamer1.0-utils 


%package -n palemoon-suggested
Summary: %smr
License: GPL
Group: Networking/WWW
Requires:  palemoon >= %version
Requires: palemoon-ru
#Requires: palemoon-uk
#Requires: palemoon-kk
Requires: palemoon-uBlock
Requires: palemoon-html5


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
Requires: palemoon-html5


%description -n palemoon-suggested
Recommended setplugins to  newmoon

%description -n palemoon-suggested -l ru_RU.UTF8
Рекомендуемый набор раширений newmoon

%description -n palemoon-html5
Recommended set for newmoon with html5

%description -n palemoon-html5 -l ru_RU.UTF8
Рекомендуемый набор для работы newmoon c HTML5 

%description -n palemoon-full
Full set natives plugins to  newmoon

%description -n palemoon-full -l ru_RU.UTF8
Полный  набор нативных раширений newmoon



%files -n palemoon-suggested
%files -n palemoon-full
%files -n palemoon-html5

%changelog
* Sat Aug 13 2016 Hihin Ruslan <ruslandh@altlinux.ru> 25.6.0-alt3
- Fix palemoon-html5

* Sun Aug 07 2016 Hihin Ruslan <ruslandh@altlinux.ru> 25.6.0-alt2
- Add palemoon-html5

* Fri Jul 31 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.6.0-alt1
- initial build for ALT Linux Sisyphus

