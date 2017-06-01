Name: installer-feature-multipath
Version: 0.2
Release: alt3

Summary: Start multipathd in early install stage
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
BuildArch: noarch

%define hookdir %_datadir/install2/initinstall.d

%description
Start multipathd in early install stage

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Thu Jun 01 2017 Michael Shigorin <mike@altlinux.org> 0.2-alt3
- fixed exit code
- added message about 'mpath' kernel cmdline parameter

* Thu Apr 13 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.2-alt2
- release up

* Thu Apr 13 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.2-alt1
- run only when mpath parameter passed to cmdline

* Thu Nov 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.1-alt1
- initial build


