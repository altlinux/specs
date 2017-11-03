Name: installer-feature-display-acc-address
Version: 0.0.1
Release: alt1

Summary: Installer hook to display web acc address
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Display web acc URL on console.

%package stage3
Summary: Installer stage 3 hook to display web acc address
License: GPL
Group: System/Configuration/Other

%description stage3
Display web acc URL on console.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files stage3
%hookdir/*

%changelog
* Fri Nov 03 2017 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1
- Initial build.
