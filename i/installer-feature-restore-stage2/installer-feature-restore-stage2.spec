Name: installer-feature-restore-stage2
Version: 0.1
Release: alt1

%define install2dir %_datadir/install2/

Summary: "system restore" wizard's branch
Group: System/Configuration/Other
License: GPL
Url: http://www.altlinux.org/Installer/beans

Requires: alterator-bacula >= 0.7-alt3 bacula-director-sqlite3
Requires: alterator-lilo
Requires: alterator-notes

BuildArch: noarch

Source: %name-%version.tar

%description
This package contains steps and requirements 
for "system restore" wizard's branch.

%prep
%setup

%install
mkdir -p %buildroot%install2dir
install restore-steps %buildroot%install2dir/

%files
%install2dir/*

%changelog
* Wed Aug 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
