%define _unpackaged_files_terminate_build 1
%define service service-chrony
Name: alterator-service-chrony
Version: 0.5
Release: alt1

Summary: Service for managment chrony
License: GPLv3
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-service-chrony

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: alterator-entry
%ifnarch %e2k
BuildRequires: shellcheck
%endif

Requires: alterator-module-executor >= 0.1.29
Requires: alterator-interface-service
Requires: alterator-entry >= 0.4.8
Requires: chrony

%description
Service for deploy chrony.

%prep
%setup

%install
mkdir -p %buildroot%_alterator_datadir/services
mkdir -p %buildroot%_localstatedir/alterator/service/chrony/config-backup

install -p -D -m755 %service %buildroot%_bindir/%service
install -p -D -m644 alterator/%service.backend %buildroot%_alterator_datadir/backends/%service.backend
install -p -D -m644 alterator/%service.service %buildroot%_alterator_datadir/services/%service.service
install -p -D -m644 default-chrony.conf %buildroot%_localstatedir/alterator/service/chrony/default-chrony.conf

%check
find ./alterator/ -type f -exec alterator-entry validate {} \+
%ifnarch %e2k
find service-* -type f -exec shellcheck {} \+
%endif

%files
%_alterator_datadir/backends/%service.backend
%_alterator_datadir/services/%service.service
%_bindir/%service
%_localstatedir/alterator/service/chrony/config-backup
%_localstatedir/alterator/service/chrony/default-chrony.conf

%changelog
* Thu Mar 26 2026 Evgenii Sozonov <arzdez@altlinux.org> 0.5-alt1
- Fix typo (Closes: #58119)
- Change service name
- Fixed comment for clients settings (thx Michael Mukhin)
- Moved alterator files to a separate folder (thx Michael Mukhin)
- Add Alterator file validation. Add shellcheck (thx Michael Mukhin)
- Removed serviceword and unused flag (thx Michael Mukhin)
- Edit .spec file (thx Michael Mukhin)
- Fixed backups folder (thx Michael Mukhin)
- Removed unused .json files (thx Michael Mukhin)

* Wed Jan 28 2026 Evgenii Sozonov <arzdez@altlinux.org> 0.4-alt1
- Fixed work with makestep field (thx Michael Mukhin)
- Fixed work with rtcsync field (thx Michael Mukhin)
- Fixed work with disableDefaultPool field (Closes: #57513) (thx Michael Mukhin)
- Fixed status function (Closes: #57515) (thx Michael Mukhin)
- Added array labels (thx Michael Mukhin)

* Thu Dec 25 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.3-alt1
- Fixed make_ntp_entry function (thx Michael Mukhin)
- Fixed parse_conf_file function (thx Michael Mukhin)
- Corrected required fields and default values (thx Michael Mukhin)
- Add diag-chrony (thx Michael Mukhin)
- Add 'exit_status = true' for new version of executor (thx Kirill Sharov)
- ci: add secret scanning (thx Maria Alexeeva)
- Remove unused functions (thx Michael Mukhin)
- Add a function for working with server, pool, and default pool
  strings (thx Michael Mukhin)
- Fix parser function (thx Michael Mukhin)
- Fix undeploy function (thx Michael Mukhin)
- Add new parameters to .service file (thx Michael Mukhin)
- Remove unused functions (thx Michael Mukhin)
- The service-chrony is adapted for POSIX (thx Michael Mukhin)
- The parse_conf_file function has been simplified. The
  make_ntp_entry function has been added to handle server, pool,
  and default pool json (thx Michael Mukhin)
- The name of the require parameter has been changed. (thx Michael Mukhin)
- The default pool, server, and pool settings have been fixed and
  adapted to the new Enum parameters. (thx Michael Mukhin)
- Information messages has been changed (thx Michael Mukhin)
- Change service name to chrony_service (thx Kirill Sharov)

* Fri Oct 03 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.2-alt1
- Add internal parameters. Fix status function

* Tue Sep 23 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.1.3-alt1
- Edit spec file
- Edit .service file
- Add config parser
- Add default chrony config file
- Backup directory has been changed, undeploy function has been fixed (thx Mukhin Michael)

* Thu Jul 31 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.1.2-alt1
- Backup directory has been changed, undeploy function has been fixed (thx Mukhin Michael)

* Tue Jul 15 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.1-alt1
- Initial commit