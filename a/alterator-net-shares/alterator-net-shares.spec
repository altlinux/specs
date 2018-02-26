Name: alterator-net-shares
Version: 0.1
Release: alt4

Summary: Enable/disable mounting samba shares from "domain" server
License: GPL
Group: System/Configuration/Other

Source: %name-%version.tar
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
BuildArch: noarch

Requires: gettext
Requires: bind-utils
Requires: alterator >= 2.9
BuildPreReq: alterator >= 3.1

%description
%summary

%prep
%setup -q

%build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
#%_datadir/alterator/help/ru_RU/*
/usr/lib/alterator/backend3/*

%changelog
* Thu Jun 09 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt4
- dependence on bind-utils added

* Thu Apr 07 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- domain server address calculation fixed

* Wed Apr 06 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- debug output removed

* Fri Apr 01 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build


