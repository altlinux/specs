Name: appliance-devel-distro
Summary: Packages useful for creating distro
BuildArch: noarch
Version: 4.0.1
Release: alt2
License: GPL
Group: Development/Other

Requires: sisyphus
Requires: sisyphus-mirror
Requires: mkimage
Requires: mkimage-profiles
Requires: mkisofs
Requires: git-core
Requires: hasher
Requires: multipath-tools

%description
%summary

%files

%changelog
* Mon Aug 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt2
- remove requires
    - distribute (multi-disk distributions very rare now)
    - spt, spt3 (obsoleted by mkimage)
- add requires
    - git-core
    - hasher
    - multipath-tools (kpartx needed for creating VM images)

* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

