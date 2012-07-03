Name: livecd-evms
Version: 0.2
Release: alt1

Summary: tune evms config to run from LiveCD
License: GPLv2
Group: System/Configuration/Other

Source0: %name


BuildArch: noarch
PreReq: service chkconfig
Requires: libevms

Requires(post): chkconfig
Requires(preun): chkconfig

%description
%summary

%install
install -pD -m0755 %SOURCE0 %buildroot%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%_initdir/%name


%changelog
* Thu May 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- exclude zram*

* Mon May 25 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- start service by default

* Thu May 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
