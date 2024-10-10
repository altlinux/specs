%define _unpackaged_files_terminate_build 1
%define diagnostic_tool domain-controller
Name: diag-%diagnostic_tool
Version: 0.0.2
Release: alt1

Summary: Domain Controller Diagnostic Tool
License: GPLv3
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/diag-domain-controller
BuildArch: noarch
Source: %name-%version.tar

BuildRequires: rpm-macros-alterator

%description
Domain Controller Diagnostic Tool.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name

%install
mkdir -p %buildroot%_alterator_datadir/diagnostictools/%name

install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D -m644 alterator/%name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D -m644 alterator/%diagnostic_tool.diag %buildroot%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
install -p -D %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%_bindir/%name
%_alterator_datadir/backends/%name.backend
%_alterator_datadir/diagnostictools/%diagnostic_tool.diag
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Thu Oct 10 2024 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.0.2-alt1
  Author: Sergey Savelev <savelevsa@basealt.ru>
- The version has been changed.
- Added a test to check the permanent and temporary hostname.
- Added a test to check for the presence of the krb5.conf file.
- Added a test to check for the presence of the smb.conf file.
- Added a test to check the method of caching Kerberos tickets.
- Added a verification test: for whether the search for the kerberos domain name
  via DNS is enabled.
- Added a test to check for the presence of the resolv.conf file.
- Added a test to check the match of the realm record from the krb5.conf file
  and the domain name from the resolv.conf file.
- Added a test to check the match of the realm record from the smb.conf file and
  from the krb5.conf file.
- Added the implementation of saving the report in the terminal and in ADT.

* Thu Aug 22 2024 Evgeny Sinelnikov <sin@altlinux.org> 0.0.1-alt2
- initial first build for Sisyphus

* Thu Aug 08 2024 Sergey Savelev <savelevsa@basealt.ru> 0.0.1-alt1
- initial build

