%define parent make-initrd
%define child  bootchain

Name: %parent-%child
Version: 0.1.4
Release: alt1

Summary: %child modules set for %name
License: GPL-3.0
Group: System/Base
BuildArch: noarch

Packager: Leonid Krivoshein <klark@altlinux.org>

%ifnarch %e2k
BuildRequires: shellcheck
%endif

Requires: %name-core        = %version-%release
Requires: %name-getimage    = %version-%release
Requires: %name-waitdev     = %version-%release
Requires: %name-interactive = %version-%release
Requires: %name-altboot     = %version-%release
Requires: %name-localdev    = %version-%release
Requires: %name-nfs         = %version-%release
Requires: %name-cifs        = %version-%release
Requires: %name-liverw      = %version-%release

AutoReq: noshell, noshebang

Source0: %name-%version.tar

%description
Meta-package with full set of the %child modules for %parent

%package doc
Summary: %parent-%child documentation
Group: Documentation
BuildArch: noarch
AutoReq: noshell, noshebang

%description doc
Documentation, testing and development files for %parent-%child

%package core
Summary: %child-core module for %parent
Group: System/Base
BuildArch: noarch
Requires: %parent >= 2.9
AutoReq: noshell, noshebang

%description core
%child-core module for %parent

%package getimage
Summary: getimage sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-core = %version-%release
Requires: wget
AutoReq: noshell, noshebang

%description getimage
getimage sub-module for %name

%package waitdev
Summary: waitdev sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-core = %version-%release
AutoReq: noshell, noshebang

%description waitdev
waitdev sub-module for %name

%package interactive
Summary: interactive sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-core = %version-%release
Requires: console-vt-tools
Requires: dialog
Requires: less
Requires: pv
AutoReq: noshell, noshebang

%description interactive
interactive sub-module for %name

%package altboot
Summary: altboot sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-interactive = %version-%release
Requires: curl
Requires: losetup
AutoReq: noshell, noshebang

%description altboot
altboot sub-module for %name

%package localdev
Summary: localdev sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-altboot = %version-%release
AutoReq: noshell, noshebang

%description localdev
localdev sub-module for %name

%package nfs
Summary: nfs sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-altboot = %version-%release
Requires: nfs-utils
Requires: iproute2
AutoReq: noshell, noshebang

%description nfs
nfs sub-module for %name

%package cifs
Summary: cifs sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-altboot = %version-%release
Requires: cifs-utils
Requires: hostinfo
AutoReq: noshell, noshebang

%description cifs
cifs sub-module for %name

%package liverw
Summary: liverw sub-module for %name
Group: System/Base
BuildArch: noarch
Requires: %name-localdev = %version-%release
Requires: e2fsprogs
Requires: fdisk
Requires: sfdisk
AutoReq: noshell, noshebang

%description liverw
liverw sub-module for %name

%prep
%setup -q

%install
./mix-altboot.sh
mkdir -p -- "%buildroot%_datadir/%parent"/features "%buildroot%_docdir"
cp -aRf -- %child-* "%buildroot%_datadir/%parent"/features/
mv -f -- "%buildroot%_datadir/%parent/features/%child-doc" "%buildroot%_docdir/%name"

%ifnarch %e2k
%check
./check-scripts.sh --verbose
%endif

%files

%files doc
%_docdir/%name

%files core
%_datadir/%parent/features/%child-core

%files getimage
%_datadir/%parent/features/%child-getimage

%files waitdev
%_datadir/%parent/features/%child-waitdev

%files interactive
%_datadir/%parent/features/%child-interactive

%files altboot
%_datadir/%parent/features/%child-altboot

%files localdev
%_datadir/%parent/features/%child-localdev

%files nfs
%_datadir/%parent/features/%child-nfs

%files cifs
%_datadir/%parent/features/%child-cifs

%files liverw
%_datadir/%parent/features/%child-liverw

%changelog
* Sun Sep 12 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.4-alt1
- major fixes and improvements around using RAM-disks and tmpfs.
- package documentation reorganized and separated.
- old feature code and logs complete removed.

* Mon Sep 06 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.3-alt1
- localdev: no more choice dialog, if found single device.
- altboot/get_free_ramdisk(): added hack for RT kernels.

* Sun Sep 05 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.2-alt1
- major fixes, prepare to p10 netinstall, sample config updated.

* Sat Sep 04 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.1-alt1
- localdev: label globbing and 'fuid' option support added.

* Mon Aug 30 2021 Leonid Krivoshein <klark@altlinux.org> 0.1.0-alt1
- Experimental build for Sisyphus: WiP!

