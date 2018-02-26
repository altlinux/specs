Name: installer-feature-hdd-pm-disable
Version: 0.2
Release: alt1

Summary: Installer hook for disable pm-utils script
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Disable harddrive script from pm-utils.
HDD should be managed by power manager via udisks.

%package stage3
Summary: Installer stage3 hook for disable pm-utils script
License: GPL
Group: System/Configuration/Other

%description stage3
Disable harddrive script from pm-utils.
HDD should be managed by power manager via udisks.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files stage3
%hookdir/*

%changelog
* Fri Nov 25 2011 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Write comments into created file.

* Thu Nov 24 2011 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build.

