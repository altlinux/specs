Name: bdsync
Version: 0.11.2
Release: alt3.1

Summary: Remote sync for block devices

License: GPLv2
Group: File tools
Url: http://bdsync.rolf-fokkens.nl/

# Source-url: https://github.com/rolffokkens/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

Patch1: bdsync-0.10-buildflags.patch

BuildRequires: libssl-devel
%ifnarch %e2k
BuildRequires: pandoc
%endif

%description
Bdsync can be used to synchronize block devices over a network. It generates
a "binary patchfile" in an efficient way by comparing MD5 checksums of 32k
blocks of the local block device LOCDEV and the remote block device REMDEV.

This binary patchfile can be sent to the remote machine and applied to its
block device DSTDEV, after which the local blockdev LOCDEV and the remote
block device REMDEV are synchronized.

bdsync was built to do the only thing rsync isn't able to do: synchronize
block devices.

%prep
%setup
%patch1 -p1

%build
%ifarch %e2k
%make_build %name
%else
%make_build
%endif

%check
make test

%install
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/%_man1dir/
cp %name %buildroot/%_bindir/%name
%ifnarch %e2k
cp %name.1 %buildroot/%_man1dir/%name.1
%endif

%files
%doc COPYING
%doc README.md
%_bindir/%name
%ifnarch %e2k
%_man1dir/%name.1*
%endif

%changelog
* Wed Apr 27 2022 Michael Shigorin <mike@altlinux.org> 0.11.2-alt3.1
- E2K: avoid pandoc (not available yet)

* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 0.11.2-alt3
- manually build for ALT Sisyphus

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.11.2-alt2_4
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.11.2-alt2_3
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt2_2
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.11.2-alt1_2
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1_3
- update to new release by fcimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.11.1-alt1_2
- new version

