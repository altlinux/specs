Name: live-hooks-tftp
Version: 20110406
Release: alt1

Summary: Run additional scripts from tftp
License: GPL
Group: System/Configuration/Other

Source0: %name.tar

BuildArch: noarch
PreReq: service chkconfig

%description
Run additional scripts from tftp.

%prep
%setup -c

%install
mkdir -p %buildroot%_initdir/
install -pD -m0755 %name/%name %buildroot%_initdir/%name

%files
%_initdir/%name

%changelog
* Wed Apr 06 2011 Eugene Prokopiev <enp@altlinux.ru> 20110406-alt1
- fork from livecd-run-hooks

* Wed Feb 16 2011 Mykola Grechukh <gns@altlinux.ru> 1.2-alt1
- do not run tilda files

* Wed Jun 09 2010 Mykola Grechukh <gns@altlinux.ru> 1.1-alt1
- run earlier

* Wed Apr 21 2010 Mykola Grechukh <gns@altlinux.ru> 1.0-alt1
- first version
