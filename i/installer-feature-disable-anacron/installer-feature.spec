Name: installer-feature-disable-anacron
Version: 0.1
Release: alt1

Summary: Disable anacron service
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Andrey Cherepanov <cas@altlinux.org>
Source: %name-%version.tar

%description
Disable anacron service

Requires: chrooted

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Jan 17 2011 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus

