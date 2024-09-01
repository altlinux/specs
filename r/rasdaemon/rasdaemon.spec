# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: rasdaemon
Version: 0.8.1
Release: alt1
Summary: Utility to receive RAS error tracings
Group: System/Kernel and hardware
License: GPL-2.0-only
Url: https://github.com/mchehab/rasdaemon
Source0: %name-%version.tar.gz

Source1: rasdaemon.init

BuildRequires: libsqlite3-devel
BuildRequires: libtraceevent-devel
BuildRequires: rpm-build-perl

Requires: perl-DBD-SQLite
%ifarch %ix86 x86_64
Requires: dmidecode
%endif

%description
%name is a RAS (Reliability, Availability and Serviceability) logging tool.
It currently records memory errors, using the EDAC tracing events.
EDAC consists of drivers in the Linux kernel that handle detection of ECC errors
from memory controllers for most chipsets on i386 and x86_64 architectures.
EDAC drivers for other architectures like ARM also exist.
This userspace component consists of an init script which makes sure
EDAC drivers and DIMM labels are loaded at system startup, as well as
a utility for reporting current error counts from the EDAC sysfs files.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)

%autoreconf
sed -i 's|cat <<EOF|tee <<EOF compile_time_options_summary.txt|' configure

%configure \
	--enable-all \
	--with-sysconfdefdir=%_sysconfdir/sysconfig

%make_build

%install
make install DESTDIR=%buildroot

install -D -p -m 0644 misc/rasdaemon.service	%buildroot%_unitdir/%name.service
install -D -p -m 0644 misc/ras-mc-ctl.service	%buildroot%_unitdir/ras-mc-ctl.service
install -D -p -m 0644 misc/rasdaemon.env	%buildroot%_sysconfdir/sysconfig/%name
install -D -p -m 0755 %SOURCE1			%buildroot%_initdir/%name

rm %buildroot/usr/include/*.h

mkdir -p %buildroot%_localstatedir/lib/rasdaemon
touch %buildroot%_localstatedir/lib/rasdaemon/ras-mc_event.db

mkdir -p %buildroot%_libexecdir
cp -a contrib -T %buildroot%_libexecdir/%name

%check
./rasdaemon --version | grep -Fx '%name %version'
# Check it's not empty.
grep -q summary compile_time_options_summary.txt
# It's possible to test the tool using Linux fault injection capabilities.
# mce-inject - tested manually using debugfs method; the 12 years old mce-inject tool
#   does not work in ALT, because we don't have /dev/mcelog (deprecated interface).
# edac-fake-inject - is not tested as it requires hardware.

%triggerpostun -- %name < 0.8.1
f=%_sysconfdir/sysconfig/rasdaemon
# If config file is changed RPM will save it, otherwise it will delete it.
if [ -f "$f.env.rpmsave" ]; then
	mv "$f" "$f.rpmnew"
	mv -v "$f.env.rpmsave" "$f"
fi

%post
%post_service rasdaemon
%post_systemd ras-mc-ctl

%preun
%preun_service rasdaemon
%preun_systemd ras-mc-ctl

# Make compile_time_options_summary.txt accessible at fixed location.
%define _customdocdir %_docdir/%name

%files
%doc AUTHORS ChangeLog COPYING README.md TODO compile_time_options_summary.txt
%_sbindir/rasdaemon
%_sbindir/ras-mc-ctl
%_libexecdir/rasdaemon
%_localstatedir/lib/rasdaemon
%ghost %_localstatedir/lib/rasdaemon/ras-mc_event.db
%_sysconfdir/ras
%config(noreplace) %_sysconfdir/sysconfig/rasdaemon
%_initdir/rasdaemon
%_unitdir/ras*.service
%_man1dir/rasdaemon.1*
%_man8dir/ras-mc-ctl.8*

%changelog
* Sun Aug 11 2024 Vitaly Chikunov <vt@altlinux.org> 0.8.1-alt1
- Update to 0.8.1 (2024-07-16).
- spec: Packaging changed from srpms to gears+tarball with watchfile.
- spec: Changed Url to the main upstream repository.
- Config renamed from /etc/sysconfig/rasdaemon.env to /etc/sysconfig/rasdaemon
  (to match upstream and other distros).
- spec: Remove unneeded BuildRequires.
- spec: Add service hook calls for ras-mc-ctl systemd unit.
- spec: Package contrib scripts for testing purposes.

* Fri Feb 03 2023 Sergey Y. Afonin <asy@altlinux.org> 0.7.0-alt1
- new version

* Sun Oct 30 2022 Sergey Y. Afonin <asy@altlinux.org> 0.6.8-alt2
- moved to Sisyphus from Autoimports (ALT #43074)
- added init script for sysvinit
- built with --enable-memory-failure
- removed Requires for hwdata

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 0.6.8-alt1_2
- update to new release by fcimport

* Fri May 06 2022 Igor Vlasenko <viy@altlinux.org> 0.6.8-alt1_1
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.6.7-alt1_3
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.6.7-alt1_2
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.6.7-alt1_1
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.6.4-alt2_4
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt2_3
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_3
- update to new release by fcimport

* Tue Apr 07 2020 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_2
- update to new release by fcimport

* Tue Oct 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_1
- update to new release by fcimport

* Fri Oct 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.6.3-alt1_1
- new version

