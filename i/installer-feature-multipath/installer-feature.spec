Name: installer-feature-multipath
Version: 0.3
Release: alt2

Summary: Start multipathd in early install stage
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
BuildArch: noarch

%define hookdir %_datadir/install2/initinstall.d
%define hookdirp %_datadir/install2/preinstall.d

%description
Start multipathd in early install stage

%prep
%setup

%install
mkdir -p %buildroot%hookdir
install -pm755 01-multipath.sh %buildroot%hookdir/
mkdir -p %buildroot%hookdirp
install -pm755 48-cpympathids.sh %buildroot%hookdirp/

%files
%hookdir/*
%hookdirp/*

%changelog
* Thu Feb 27 2025 Dmitry Terekhin <jqt4@altlinux.org> 0.3-alt2
- copy bindings and wwids for make-initrd in 50-instkernel.sh

* Thu Jun 01 2017 Michael Shigorin <mike@altlinux.org> 0.2-alt3
- fixed exit code
- added message about 'mpath' kernel cmdline parameter

* Thu Apr 13 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.2-alt2
- release up

* Thu Apr 13 2017 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.2-alt1
- run only when mpath parameter passed to cmdline

* Thu Nov 10 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.1-alt1
- initial build


