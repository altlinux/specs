%define _unpackaged_files_terminate_build 1
%define service service-samba-ad
Name: alterator-service-samba-ad
Version: 0.7.4
Release: alt1

Summary: Service for Samba AD management
License: GPLv3
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-service-samba-ad

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator

Requires: alterator-module-executor
Requires: alterator-interface-service
Requires: alterator-entry >= 0.4.5
Requires: samba-dc

%description
Service for Samba AD management.

%prep
%setup

%install
mkdir -p %buildroot%_alterator_datadir/services
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_localstatedir/alterator/service/samba-ad
mkdir -p %buildroot%_localstatedir/alterator/service/samba-ad/config-backup

install -p -D -m755 %service %buildroot%_bindir/%service
install -p -D -m755 %service-bind %buildroot%_bindir/%service-bind
install -p -D -m755 %service-status %buildroot%_bindir/%service-status
install -p -D -m755 %service-configure %buildroot%_bindir/%service-configure
install -p -D -m755 %service-functions %buildroot%_bindir/%service-functions
install -p -D -m644 %service-entry-update %buildroot%_bindir/%service-entry-update
install -p -D -m644 %service.backend %buildroot%_alterator_datadir/backends/%service.backend
install -p -D -m644 %service.service %buildroot%_alterator_datadir/services/%service.service
install -p -D -m644 parameters/provision-parameters.schema.json %buildroot%_datadir/%name/provision-parameters.schema.json
install -p -D -m644 parameters/join-parameters.schema.json %buildroot%_datadir/%name/join-parameters.schema.json
install -pDm 644 %service.bash-completion \
     %buildroot%_datadir/bash-completion/completions/%service
install -p -D -m644 status.json %buildroot%_localstatedir/alterator/service/samba-ad/status.json

%files
%_bindir/%service
%_bindir/%service-bind
%_bindir/%service-status
%_bindir/%service-configure
%_bindir/%service-functions
%_bindir/%service-entry-update
%_alterator_datadir/backends/%service.backend
%_alterator_datadir/services/%service.service
%_datadir/bash-completion/completions/%service
%_datadir/%name/provision-parameters.schema.json
%_datadir/%name/join-parameters.schema.json
%_localstatedir/alterator/service/samba-ad/
%_localstatedir/alterator/service/samba-ad/config-backup
%_localstatedir/alterator/service/samba-ad/status.json

%changelog
* Mon Jan 26 2026 Evgenii Sozonov <arzdez@altlinux.org> 0.7.4-alt1
- Add default value for use-rfc2307 parameter
- Fix incorrect device name in setup network manager

* Thu Jan 22 2026 Evgenii Sozonov <arzdez@altlinux.org> 0.7.3-alt1
- Add Systemd resolved settings (Closes: #57497)
- Add Network Manager settings
- Fix typo
- Add disabling dnsstublistener and editing resolvconf.conf
- Fix incorrect path to smb.conf in get_forwarders_samba_internal function
- Fix enable unit function (Closes: 57494)
- Disable smb and nmb services (Closes: #57495)
- Fix domain controller name change when joining (Closes: #57498)
- Fix incorrect samba internal forwarders parsing (Closes: #57512)
- Add dinamic entry update
- Delete comment for name of domain controller
- Add array prefix for dns forwarders
- Disable shellcheck rule 1087
- Fix an incorrect hostname setting

* Thu Dec 25 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.7.2-alt1
- Fix other parsing errors
- Fix incorrect dns forwarders parsing (Closes: #57363)
- Fix grep error
- Add regexp for realm, netbios and hostname.
- Add force undeploy
- Add force deploy
- Remove incorrect resource from .service file
- Remove default name for realm, hostname and domain netbios name
- Fix enable_unit function
- Add the ability to change the hostname
- Fix Samba startup error before post diagnostics
- Change example description from uppercase to uppercase
- Edit name in service file

* Tue Dec 09 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.7.1-alt1
- Fix domain controller lookup error when joining a domain

* Mon Dec 08 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.7-alt1
- Rename start and stop functions
- Refactor main deploing function. Rename provision and join function
- Add configure method to main script
- Move utility functions to a separate file
- Add the ability to configure DNS backend
- Adapt .service for new enum subparameters
- Adapt status for new enum subparameters
- Fix for forwarders disappearing. Change path to bind settings.

* Fri Nov 28 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.6.1-alt1
- NMU: Add 'exit_status = true' for new version of executor

* Wed Nov 26 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.6-alt1
- Fix start, stop and restart function
- Fix status
- Hide bind settings prototype
- Set samba internal dns as default dns backend

* Tue Sep 30 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.5-alt1
- Add signals for start and stop methods
- Fix parsing of enum parameters
- Add internal parameters. Fix status function
- Fix starting service when bind not installed
- Remove unused function
- Add dynamic status
- Edit name in .service file
- fix: improve help text for NetBIOS name and backend store
  parameters (thx Oleg Chagaev)
- fix: add help comments for realm and site name parameters in
  Samba AD service (thx Oleg Chagaev)
- fix: update admin login description to use DC abbreviation
  consistently (thx Oleg Chagaev)
- fix: capitalize RFC 2307 in display names for consistency (thx Oleg Chagaev)
- Change exit code from 1 to 0 in status function
- Fix undeploy

* Fri Jul 25 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.4-alt1
- Add samba dc to requires
- Fix demote mode
- Fix join to domain
- Fix bind9 setup
- Add retval to prepare bind function
- Set dns backend selection as a required parameter
- Add the ability to select bind9 as a dns backend
- Add Kinit for demote dc controller
- Fix incorrect dns backend names

* Wed Jul 23 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.3.1-alt1
- Edit mode_value in dc provision function
- Change enum values. Edit service name
- Remove no_default_diag from service file
- Disable force deploy
- Change backend store selection logic
- Change read_stdin function

* Tue Jul 22 2025 Andrey Limachko <liannnix@altlinux.org> 0.3-alt1
- Move Samba AD service data to /var/lib/alterator/service.
- Rename service-samba-dc to service-samba-ad.
- Rename project to alterator-service-samba-ad.
- Fix URL in spec file.
- Add bind dns backend configuration. (thx Evgenii Sozonov)

* Mon Jul 14 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.2.3-alt1
- Add diag-domain-controller.
- Add return empty json if service is not deployed.

* Mon Jul 07 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.2.2-alt1
- Remove Stdout_string from backend file.
- Change default value of dns backend.
- Add hiding password when entering.
- Remove comments to some resources.

* Tue Jun 17 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.2.1-alt1
- Edit demote dc function. Add new steps.
- Edit service file. Add new var's for undeploy and configure methods.

* Mon Jun 16 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.2-alt1
- Fix parsing arguments. Add function for demote dc. Add force deploy.
- Add new var into service entry file.
- Edit doc.

* Tue Jan 28 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.1-alt1
- Initial commit.
