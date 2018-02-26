Name: installer-feature-services
Version: 0.2
Release: alt1

Summary: Setup services for start/not start on boot
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Setup services for start/not start on boot
Put list of services to start to altinst:%_datadir/install2/
and not to start to altinst:%_datadir/install2/

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue May 24 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- put errors to log, but not to console

* Wed Apr 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- run_chroot fixed

* Wed Apr 07 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- path fixed

* Tue Apr 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build


