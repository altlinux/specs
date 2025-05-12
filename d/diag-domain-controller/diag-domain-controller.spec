%define _unpackaged_files_terminate_build 1
%define diagnostic_tool domain-controller
Name: diag-%diagnostic_tool
Version: 0.3
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
* Wed May 07 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.3-alt1
- fix: the fixed the is_sections_with_domain_name_in_krb5_empty test (thx Sergey Savelev)
- fix: fixed the does_sysvol_contain_necessary_files test (thx Sergey Savelev)
- For a test to verify that the [realms] and [domain_realm] sections
  from krb5.conf are empty, the corresponding section has been added
  to the .diag file (thx Sergey Savelev)
- Added check that [realms] and [domain_realm] sections are not empty (thx Sergey Savelev)
- The logic of the function for checking the caching of Kerberos
  tickets has been changed (thx Sergey Savelev)
- The function for checking the entry "nameserver 127.0.0.1" in
  the configuration file resolv.conf has been updated (thx Sergey Savelev)
- The logic of tests based on timedatectl has become simpler (thx Sergey Savelev)
- Changed the function to check if the samba service is running (thx Sergey Savelev)
- Added side function to check if service is active (thx Sergey Savelev)
- Fixed output of errors related to samba-tool (thx Sergey Savelev)
- To check the location of the folder with the domain name in sysvol
  in the file .diag has added a corresponding section (thx Sergey Savelev)
- Added a test to check for non-empty "Policies" and "scripts"
  folders in sysvol/<domain_name> (thx Sergey Savelev)
- The function for checking the domain name match from smb.conf
  and krb5.conf uses functions to get domain names from these files (thx Sergey Savelev)
- The function to check for the required domain name in resolv.conf
  uses the function to get the domain name from krb5.conf and the
  list of domain names from resolv.conf (thx Sergey Savelev)
- In the hostname validation test, a function is called to get the
  domain name from smb.conf (thx Sergey Savelev)
- Variables containing the domain name from different configuration
  files are rendered as separate functions (thx Sergey Savelev)
- Add port listening test to .diag (thx Sergey Savelev)
- Added a test to verify that certain ports are being listened to
  by the necessary services (thx Sergey Savelev)
- The function to verify that the "samba" package is installed
  in the system is simplified, a side function is used to check the
  installed packages (thx Sergey Savelev)
- Added a side function to check that packages are installed in
  the system (thx Sergey Savelev)

* Fri Feb 21 2025 Andrey Limachko <liannnix@altlinux.org> 0.2.1-alt1
- Fixed typo in is_ntp_service_running test

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

