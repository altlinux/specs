Name: installer-feature-pam_selinux
Version: 0.1
Release: alt1

Summary: Installer hook for pam_selinux.so
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
This package contains installer hook for adding
pam_selinux.so to the PAM stack.

%package stage3
Summary: Installer stage3 hook for pam_selinux.so
License: GPL
Group: System/Configuration/Other

%description stage3
This package contains installer stage3 hook for adding
pam_selinux.so to the PAM stack.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files stage3
%hookdir/*

%changelog
* Fri Feb 10 2012 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build.

