# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define _unpackaged_files_terminate_build 1

Name:			rasdaemon
Version:		0.6.8
Release:		alt2
Summary:		Utility to receive RAS error tracings
Group:			System/Kernel and hardware
License:		GPL-2.0-only
URL:			http://git.infradead.org/users/mchehab/rasdaemon.git
Source0:		%{name}-%{version}.tar.gz

Source1:		rasdaemon.init

BuildRequires:		gettext-tools libasprintf-devel

BuildRequires: rpm-build-perl libsqlite3-devel
Requires: perl-DBD-SQLite

BuildRequires:		libudev-devel libsystemd-devel
#BuildRequires:		systemd systemd-analyze systemd-homed
#BuildRequires:		systemd-networkd systemd-portable systemd-sysvinit

%ifarch %{ix86} x86_64
Requires:		dmidecode
%endif

%description
%{name} is a RAS (Reliability, Availability and Serviceability) logging tool.
It currently records memory errors, using the EDAC tracing events.
EDAC is drivers in the Linux kernel that handle detection of ECC errors
from memory controllers for most chipsets on i386 and x86_64 architectures.
EDAC drivers for other architectures like arm also exists.
This userspace component consists of an init script which makes sure
EDAC drivers and DIMM labels are loaded at system startup, as well as
an utility for reporting current error counts from the EDAC sysfs files.

%prep
%setup -q
autoreconf -vfi

%build
sed -i 's|cat <<EOF|cat <<EOF > compile_time_options_summary.txt|' configure

%configure \
  --enable-sqlite3 \
  --enable-aer \
  --enable-mce \
  --enable-extlog \
  --enable-devlink \
  --enable-diskerror \
  --enable-memory-failure \
  --enable-abrt-report \
%ifarch %{arm} aarch64
  --enable-non-standard \
  --enable-arm \
  --enable-hisi-ns-decode \
%endif
  --with-sysconfdefdir=%{_sysconfdir}/sysconfig

cat compile_time_options_summary.txt

%make_build

%install
make install DESTDIR=%{buildroot}

install -D -p -m 0644 misc/rasdaemon.service	%buildroot%_unitdir/%name.service
sed -i "s|/etc/sysconfig/rasdaemon|/etc/sysconfig/rasdaemon.env|" %buildroot%_unitdir/%name.service
install -D -p -m 0644 misc/rasdaemon.env	%buildroot%_sysconfdir/sysconfig/%name.env

install -D -p -m 0644 misc/ras-mc-ctl.service	%buildroot%_unitdir/ras-mc-ctl.service

install -D -p -m 0755 %SOURCE1			%buildroot%_initdir/%name

rm INSTALL %{buildroot}/usr/include/*.h

%post
%post_service rasdaemon

%preun
%preun_service rasdaemon

%files
%doc AUTHORS ChangeLog COPYING README TODO compile_time_options_summary.txt
%_sbindir/rasdaemon
%_sbindir/ras-mc-ctl
%_mandir/*/*
%_unitdir/*.service
%_initdir/%name
%dir %_sysconfdir/ras
%dir %_sysconfdir/ras/dimm_labels.d
%config(noreplace) %_sysconfdir/sysconfig/%name.env

%changelog
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

