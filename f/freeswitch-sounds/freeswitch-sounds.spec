Name: freeswitch-sounds
Version: 1.0.13
Release: alt1

Summary: Set of sound files for use with freeswitch
License: Distributable
Group: System/Servers
Url: http://files.freeswitch.org/

Source0: en-us-callie-8000.tar
Source1: en-us-callie-16000.tar
Source2: en-us-callie-32000.tar
Source3: ru-ru-elena-8000.tar
Source4: ru-ru-elena-16000.tar
Source5: ru-ru-elena-32000.tar

BuildArch: noarch

%description
%summary
Other variants can be obtained from %url.

%package en-us-callie-8000
Provides: freeswitch-sounds-default = %version
Summary: Set of sound files for use with freeswitch
Group: System/Servers

%package en-us-callie-16000
Summary: %summary
Group: System/Servers

%package en-us-callie-32000
Summary: %summary
Group: System/Servers

%package ru-ru-elena-8000
Summary: %summary
Group: System/Servers

%package ru-ru-elena-16000
Summary: %summary
Group: System/Servers

%package ru-ru-elena-32000
Summary: %summary
Group: System/Servers

%description en-us-callie-8000
%summary

%description en-us-callie-16000
%summary

%description en-us-callie-32000
%summary

%description ru-ru-elena-8000
%summary

%description ru-ru-elena-16000
%summary

%description ru-ru-elena-32000
%summary

%install
mkdir -p %buildroot%_datadir/freeswitch/sounds
for src in %SOURCE0 %SOURCE1 %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5; do
p=${src%%.tar*}; p=${p##*/}
(
tar tvf $src |sed -n '/^d/ s,^.\+[[:blank:]]\([^[:blank:]]\+\)/$,%%dir %_datadir/freeswitch/sounds/\1,p'
tar tvf $src |sed -n '/^-/ s,^.\+[[:blank:]]\([^[:blank:]]\+\)$,%_datadir/freeswitch/sounds/\1,p'
) > FILES.$p
tar xf $src -C %buildroot%_datadir/freeswitch/sounds
done

%files en-us-callie-8000 -f FILES.en-us-callie-8000
%files en-us-callie-16000 -f FILES.en-us-callie-16000
%files en-us-callie-32000 -f FILES.en-us-callie-32000
%files ru-ru-elena-8000 -f FILES.ru-ru-elena-8000
%files ru-ru-elena-16000 -f FILES.ru-ru-elena-16000
%files ru-ru-elena-32000 -f FILES.ru-ru-elena-32000

%changelog
* Sat May  8 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.13-alt1
- russian voice added

* Sat Sep 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.12-alt1
- Initial build.
