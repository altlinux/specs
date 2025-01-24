%define _unpackaged_files_terminate_build 1
%define diagnostic_tool domain-controller
Name: diag-%diagnostic_tool
Version: 0.2
Release: alt1

Summary: Domain Controller Diagnostic Tool
License: GPLv3
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/diag-domain-controller
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator

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
* Fri Jan 24 2025 Andrey Limachko <liannnix@altlinux.org> 0.2-alt1
- Add -a|--alterator option to output test results in
  alteratorctl/Adt
- Shellcheck refactoring

* Thu Dec 12 2024 Andrey Limachko <liannnix@altlinux.org> 0.1-alt1
- The structure of the files .diag and .backend has been rewritten
  to the toml format (thx Sergey Savelev)

* Fri Dec 06 2024 Evgenii Sozonov <arzdez@altlinux.org> 0.0.3-alt1
- The multiple systemctl call has been removed, and the
  is_domain_info_available function has been adjusted (thx Sergey Savelev)
- Added FQDN validation, removed multiple calls to samba-tool
  and systemctl (thx Sergey Savelev)
- Fixed a typo in the is_hostname_static_and_transient test (thx Sergey Savelev)
- Added a check for the existence of the timedatectl command in
  is_ntp_service_running (thx Sergey Savelev)
- Added a check for the existence of the timedatectl command in
  is_time_synchronization_enabled (thx Sergey Savelev)
- Fixed a typo in the is_domain_info_available test comment (thx Sergey Savelev)
- The output of archive creation information has been fixed and
  the archiving method has been changed from zip to tar (thx Sergey Savelev)
- Added a line to notify the user about using testparm in the test
  does_smb_realm_and_krb5_default_realm_it_match (thx Sergey Savelev)
- Added output of files from the sysvol directory in the
  is_not_empty_sysvol test (thx Sergey Savelev)
- Modify test correct hostname (thx Sergey Savelev)

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

