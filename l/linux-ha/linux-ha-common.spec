Name: linux-ha
Version: 0.3
Release: alt2

Summary: The basic directory layout and rpm build macros for Linux-HA project apps
License: GPL
Group: System/Base
BuildArch: noarch

Packager: L.A. Kostis <lakostis@altlinux.ru>

%package common
Summary: The basic directory layout for Linux-HA project apps
License: GPL
Group: System/Base
Version: %version
Release: %release

Provides: %_sysconfdir/ha.d, %_sysconfdir/ha.d/resource.d

%package -n rpm-build-%name
Summary: RPM macros for Linux-HA project apps
License: GPL
Group: Development/Other
Version: %version
Release: %release

%description
The %name package is one of the basic packages that is installed on
a %distribution system; %name contains the basic directory layout
for the Linux HA project application (such heartbeat/drbd/ldirectord etc),
including the correct permissions for the directories.

This package also include RPM macros for linux-ha apps.

%description common
The %name package is one of the basic packages that is installed on
a %distribution system; %name contains the basic directory layout
for the Linux HA project application (such heartbeat/drbd/ldirectord etc),
including the correct permissions for the directories.

%description -n rpm-build-%name
RPM macros for Linux-HA project apps.

%install
mkdir -p %buildroot/%_sysconfdir/ha.d
mkdir -p %buildroot/%_sysconfdir/ha.d/resource.d
mkdir -p %buildroot/%_rpmmacrosdir

cat << EOF > %buildroot/%_rpmmacrosdir/linux-ha
%%_ha_dir %%_sysconfdir/ha.d
%%_ha_resource_dir %%_sysconfdir/ha.d/resource.d
EOF

%files common
%_sysconfdir/ha.d

%files -n rpm-build-%name
%_rpmmacrosdir/linux-ha

%changelog
* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 0.3-alt2
- NMU: use %%_rpmmacrosdir instead of /etc/rpm

* Sat Dec 02 2006 L.A. Kostis <lakostis@altlinux.ru> 0.3-alt1
- split out to many packages.

* Sat Dec 02 2006 L.A. Kostis <lakostis@altlinux.ru> 0.2-alt1
- add rpm macros;
- update description & provides.

* Sat Dec 02 2006 L.A. Kostis <lakostis@altlinux.ru> 0.1-alt1
- initial build for ALTLinux.

