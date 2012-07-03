Name: freeswitch-sounds-music
Version: 1.0.8
Release: alt1

Summary: Set of music files for use with freeswitch
License: Distributable
Group: System/Servers
Url: http://files.freeswitch.org/

Source0: 8000.tar
Source1: 16000.tar
Source2: 32000.tar

BuildArch: noarch

%description
%summary
Other variants can be obtained from %url.

%package 8000
Summary: %summary
Group: System/Servers

%package 16000
Summary: %summary
Group: System/Servers

%package 32000
Summary: %summary
Group: System/Servers

%description 8000
%summary

%description 16000
%summary

%description 32000
%summary

%install
mkdir -p %buildroot%_datadir/freeswitch/sounds
for src in %SOURCE0 %SOURCE1 %SOURCE2; do
p=${src%%.tar*}; p=${p##*/}
(
tar tvf $src |sed -n '/^d/ s,^.\+[[:blank:]]\([^[:blank:]]\+\)/$,%%dir %_datadir/freeswitch/sounds/\1,p'
tar tvf $src |sed -n '/^-/ s,^.\+[[:blank:]]\([^[:blank:]]\+\)$,%_datadir/freeswitch/sounds/\1,p'
) > FILES.$p
tar xf $src -C %buildroot%_datadir/freeswitch/sounds
done

%files 8000 -f FILES.8000
%files 16000 -f FILES.16000
%files 32000 -f FILES.32000

%changelog
* Sat May  8 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.8-alt1
- Initial build.
