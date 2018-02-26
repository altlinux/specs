Name: installer-feature-autoinstall-usbross
Version: 0.0.1
Release: alt1

Summary: Steps for auto-installation.
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar
Provides: installer-feature-autoinstall
Conflicts: installer-feature-autoinstall

%description
Instructions to Installer for auto-installation.

%prep
%setup

%build

%install
%define metadata %_datadir/install2/metadata
mkdir -p %buildroot%metadata
install -pm644 *.scm %buildroot%metadata/

%files
%metadata/*

%changelog
* Thu Aug 11 2011 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Add example for auto-installation.
