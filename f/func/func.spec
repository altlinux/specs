Summary: Remote management framework
Name: func
Version: 0.30
Release: alt1
Url: https://fedorahosted.org/func/
Source0: %name-%version.tar
License: GPLv2+
Group: System/Configuration/Other

BuildRequires: python-module-setuptools perl-podlators

BuildArch: noarch

%description
func is a remote api for mangement, configuration, and monitoring of systems.

%prep
%setup -q

echo "%version" > etc/version

%build
%make manpage
%__python setup.py build

%install
%__python setup.py install --prefix=/usr --root=$RPM_BUILD_ROOT
touch $RPM_BUILD_ROOT/var/log/func/func.log
touch $RPM_BUILD_ROOT/var/log/func/audit.log

install -pD -m 755 init-scripts/funcd.alt  %buildroot%_initrddir/funcd

%post
%post_service funcd

%preun
%preun_service funcd

%files
%_bindir/*

%_initrddir/*
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/minion-acl.d/
%dir %_sysconfdir/%name/modules/

%config(noreplace) /etc/func/minion.conf
%config(noreplace) /etc/func/async_methods.conf
%config(noreplace) /etc/func/overlord.conf
%config(noreplace) /etc/logrotate.d/func_rotate
%config(noreplace) /etc/func/modules/Test.conf
%config(noreplace) /etc/func/modules/Bridge.conf
%config(noreplace) /etc/func/modules/Vlan.conf
%config /etc/func/version

%python_sitelibdir/*

%dir /var/log/func
%attr(0600,root,root) %config(noreplace) %verify(not md5 size mtime) /var/log/func/func.log
%attr(0600,root,root) %config(noreplace) %verify(not md5 size mtime) /var/log/func/audit.log

%dir /var/lib/func

#%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) /var/log/prelink/prelink.log

%doc AUTHORS README LICENSE CHANGES
%_mandir/man1/func*


%changelog
* Mon Nov 12 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.30-alt1
- New version

* Sat Feb 19 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.27-alt1
- Build for ALT
