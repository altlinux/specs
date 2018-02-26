Name: installer-feature-rfkill-unblocked
Version: 0.0.1
Release: alt1

Summary: Persistent unblock hardware\software rfkill buttons
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans

BuildArch: noarch
Source: %name-%version.tar

%description
%summary
This feat requires special kernel.
Lookup for existance 'unblocked' parameter for rfkill.ko module.

%prep
%setup

%build

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Aug 29 2011 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build.
