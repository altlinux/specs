Name:           installer-feature-sp-stage3
Version:        0.1
Release:        alt1
Summary:        Installer stage3 for School Portal
License:        GPL
Group:          System/Configuration/Other
Url:            http://spcms.ru
Packager:       Andrey Stroganov <dja@altlinux.org>
Vendor:         SP Team
Requires:       installer-common-stage3 sp
ExclusiveArch:  %ix86

%description
Sets services autorun on which School Portal depends.

# installer-feature-nfs taken as a sample

%install
mkdir -p %buildroot

%post
chkconfig httpd2 on
chkconfig xinetd on
chkconfig squid on

%files

%changelog
* Tue Aug 30 2011 Andrey Stroganov <dja@altlinux.org> 0.1-alt1
- initial build for alt 6
