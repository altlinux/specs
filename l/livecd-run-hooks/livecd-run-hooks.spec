Name: livecd-run-hooks
Version: 1.2
Release: alt1

Summary: Run additional scripts from livecd boot media
License: GPL
Group: System/Configuration/Other

Source0: %name.tar

BuildArch: noarch
PreReq: service chkconfig

%description
Run additional scripts from livecd boot media.

%prep
%setup -c

%install
mkdir -p %buildroot%_initdir/
install -pD -m0755 %name/%name %buildroot%_initdir/%name

%files 
%_initdir/%name

%changelog
* Wed Feb 16 2011 Mykola Grechukh <gns@altlinux.ru> 1.2-alt1
- do not run tilda files

* Wed Jun 09 2010 Mykola Grechukh <gns@altlinux.ru> 1.1-alt1
- run earlier

* Wed Apr 21 2010 Mykola Grechukh <gns@altlinux.ru> 1.0-alt1
- first version
