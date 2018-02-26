Name: installer-feature-bell-off
Version: 0.1
Release: alt1

Summary: Installer bell off hook
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
This package contains installer hook for disable bell.

%package stage3
Summary: Installer stage3 bell off hook
License: GPL
Group: System/Configuration/Other

%description stage3
This package contains installer stage3 hook for disable bell.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files stage3
%hookdir/*

%changelog
* Thu Sep 08 2011 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build
