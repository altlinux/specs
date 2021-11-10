Name:    nvmetcli
License: Apache-2.0
Summary: An adminstration shell for NVMe storage targets
Version: 0.7
Release: alt2
Group:   Other
URL:     ftp://ftp.infradead.org/pub/nvmetcli/

Source:  ftp://ftp.infradead.org/pub/nvmetcli/%name-%version.tar.gz
Patch00: 0001-nvmetcli-don-t-remove-ANA-Group-1-on-clear.patch
Patch01: 0002-README-Update-URL-for-configshell-fb.patch
Patch02: 0003-nvmetcli-Improve-IOError-handling-on-restore.patch
Patch03: 0004-nvme.py-Explicit-close-is-redundant.patch
Patch04: 0005-nvme.py-Sync-the-containing-directory.patch
Patch05: 0006-nvme.py-Make-modprobe-work-for-kmod-lib-too.patch
Patch06: 0007-test_nvmet.py-test_invalid_input-fails-for-py3.patch
Patch07: 0008-nvmetcli-Report-save-name-correctly.patch
Patch08: 0009-nvmetcli-Allow-different-devices-for-make-test.patch
Patch09: 0010-nvmetcli-Correct-xrange-usage-for-py3.patch
Patch10: 0011-nvmetcli-add-a-tcp-example-json.patch
Patch11: 0012-Documentation-fix-typo.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute asciidoc asciidoc-a2x xmlto
Source44: import.info

%py3_requires configshell kmod

%description
This package contains the command line interface to the NVMe over Fabrics
nvmet in the Linux kernel.  It allows configuring the nvmet interactively
as well as saving / restoring the configuration to / from a json file.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
%python3_build
cd Documentation
make

%install
%python3_install
mkdir -p %buildroot%_sysconfdir/nvmet
install -Dm644 nvmet.service %buildroot%_unitdir/nvmet.service
install -Dm644 Documentation/nvmetcli.8 %buildroot%_man8dir/nvmetcli.8

%post
%post_service nvmet

%preun
%preun_service nvmet

%files
%doc README
%python3_sitelibdir_noarch/*
%dir %_sysconfdir/nvmet
%_sbindir/nvmetcli
%_unitdir/nvmet.service
%_man8dir/nvmetcli.8*

%changelog
* Wed Nov 10 2021 Andrey Cherepanov <cas@altlinux.org> 0.7-alt2
- Inital build for Sisyphus.

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.7-alt1_4
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.7-alt1_3
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.7-alt1_2
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.4-alt2_12
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_12
- update to new release by fcimport

* Sat Jun 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_11
- update to new release by fcimport

* Tue Mar 10 2020 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_10
- update to new release by fcimport

* Tue Oct 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_9
- update to new release by fcimport

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_8
- new version

