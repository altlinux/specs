%define _unpackaged_files_terminate_build 1

Name: installer-alterator-fs
Version: 0.0.1
Release: alt1

Summary: Installing a file system
License: GPL
Group: System/Configuration/Other
Url: https://www.altlinux.org/Installer
BuildArch: noarch

Source: %name-%version.tar

Requires: alterator
Requires: alterator-sh-functions
Requires: alterator-l10n
Requires: alterator-browser-qt
Requires: alterator-lookout
Requires: installer-scripts-remount-stage2
Requires: libshell

BuildRequires(pre): rpm-macros-alterator
BuildRequires: alterator

%description
This step takes the file system, which is packed in tar
and divided into parts, and puts it on the target system.

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%_alterator_backend3dir/*

%changelog
* Sat Dec 21 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.0.1-alt1
- The first version of the new installer step!
