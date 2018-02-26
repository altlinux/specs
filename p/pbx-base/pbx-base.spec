Name: pbx-base
Summary: Base packages for Asterisk and CallWeaver PBX
Version: 0.0.2
Release: alt1
License: GPL
Group: System/Servers
BuildArch: noarch
Url: http://sisyphus.ru/ru/srpm/Sisyphus/pbx-base

%package user
Summary: pbxadmin group
Group: System/Servers
Requires(pre): shadow-utils

%description user
pbxadmin group

%package -n pbx-music-base
Summary: Direcotry for MusicOnHold files
Group: System/Servers
Requires(pre): pbx-base-user

%description -n pbx-music-base
Direcotry for MusicOnHold files


%description
Base packages for Asterisk and CallWeaver PBX


%install
mkdir -p %buildroot/var/lib/pbx/music

%pre user
%_sbindir/groupadd -r -f pbxadmin

%files user

%files -n pbx-music-base
%dir %attr(0755,root,pbxadmin) /var/lib/pbx
%dir %attr(2775,root,pbxadmin) /var/lib/pbx/music

%changelog
* Wed Oct 14 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.2-alt1
- add /var/lib/pbx dir

* Tue Oct 06 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt2
- add Url tag

* Mon Sep 21 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus

