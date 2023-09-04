%define _localstatedir %_var

Name: pdns-recursor
Version: 4.9.1
Release: alt1
Summary: Modern, advanced and high performance recursing/non authoritative name server
License: GPL-2.0
Group: System/Servers
URL: https://powerdns.com
Source0: https://downloads.powerdns.com/releases/%name-%version.tar.bz2
Source1: %name.watch

ExcludeArch: %arm %ix86

Provides: powerdns-recursor = %version-%release
BuildRequires: boost-complete
BuildRequires: gcc-c++
%ifarch %arm %ix86 x86_64 %mips aarch64
BuildRequires: libluajit-devel
%else
BuildRequires: lua-devel
%endif
%ifarch ppc64 ppc64le
BuildRequires: libatomic1
%endif
BuildRequires: libcap-devel
BuildRequires: libcurl-devel
BuildRequires: libfstrm-devel
BuildRequires: libprotobuf-devel
BuildRequires: libsodium-devel
BuildRequires: libssl-devel
BuildRequires: libsystemd-devel
BuildRequires: libudev-devel
BuildRequires: libudev-devel
BuildRequires: systemd-analyze
BuildRequires: systemd-homed
BuildRequires: systemd-networkd
BuildRequires: systemd-portable
BuildRequires: systemd-sysvinit

%description
PowerDNS Recursor is a non authoritative/recursing DNS server. Use this
package if you need a dns cache for your network.

%prep
%setup

%build
%configure \
    --sysconfdir=%_sysconfdir/%name \
    --with-libsodium \
    --enable-reproducible \
    --enable-dnstap \
    --enable-dns-over-tls \
%ifarch %arm %ix86 x86_64 %mips aarch64
    --with-lua=luajit \
%else
    --with-lua \
%endif
    --with-socketdir=%_runtimedir

%make_build


%install
%makeinstall_std

mv %buildroot%_sysconfdir/%name/recursor.conf{-dist,}

# add directories for newly-observed-domains/unique-domain-response
install -p -d -m 0755 %buildroot/%_sharedstatedir/%name/nod
install -p -d -m 0755 %buildroot/%_sharedstatedir/%name/udr

# change user and group to pdns-recursor
sed -i \
    -e 's/# setuid=/setuid=pdns-recursor/' \
    -e 's/# setgid=/setgid=pdns-recursor/' \
    -e 's/# security-poll-suffix=secpoll\.powerdns\.com\./security-poll-suffix=/' \
    %buildroot%_sysconfdir/%name/recursor.conf

# move systemd files
mkdir -p %buildroot/lib/systemd
mv %buildroot/usr/lib/systemd/* %buildroot%_unitdir

%pre
getent group pdns-recursor > /dev/null || groupadd -r pdns-recursor
getent passwd pdns-recursor > /dev/null || \
    useradd -r -g pdns-recursor -d / -s /sbin/nologin \
    -c "PowerDNS Recursor user" pdns-recursor
exit 0

%post
%post_service pdns-recursor

%preun
%preun_service pdns-recursor

%files
%doc README
%config(noreplace) %_sysconfdir/%name/recursor.conf
%_bindir/rec_control
%_sbindir/pdns_recursor
%_man1dir/pdns_recursor.1*
%_man1dir/rec_control.1*
%_unitdir/pdns-recursor.service
%_unitdir/pdns-recursor@.service
%dir %_sysconfdir/%name
%dir %attr(0755,pdns-recursor,pdns-recursor) %_sharedstatedir/%name
%dir %attr(0755,pdns-recursor,pdns-recursor) %_sharedstatedir/%name/nod
%dir %attr(0755,pdns-recursor,pdns-recursor) %_sharedstatedir/%name/udr

%changelog
* Mon Sep 04 2023 Andrey Cherepanov <cas@altlinux.org> 4.9.1-alt1
- New version.

* Fri Jul 07 2023 Andrey Cherepanov <cas@altlinux.org> 4.9.0-alt1
- New version.

* Fri May 05 2023 Andrey Cherepanov <cas@altlinux.org> 4.8.4-alt1
- New version initially built in Sisyphus.

* Wed Feb 22 2023 Igor Vlasenko <viy@altlinux.org> 4.7.2-alt1_2
- update to new release by fcimport

* Fri Sep 16 2022 Cronbuild Service <cronbuild@altlinux.org> 4.7.1-alt2_2
- rebuild to get rid of unmets

* Sun Aug 07 2022 Igor Vlasenko <viy@altlinux.org> 4.7.1-alt1_2
- update to new release by fcimport

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 4.7.0-alt1_1
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 4.5.4-alt1_5
- update to new release by fcimport

* Mon Sep 20 2021 Igor Vlasenko <viy@altlinux.org> 4.5.4-alt1_4
- update to new release by fcimport

* Sat Aug 21 2021 Igor Vlasenko <viy@altlinux.org> 4.5.4-alt1_3
- rebuild with boost

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 4.5.4-alt1_2
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 4.5.4-alt1_1
- update to new release by fcimport

* Wed Jun 16 2021 Cronbuild Service <cronbuild@altlinux.org> 4.4.2-alt3_6
- rebuild to get rid of unmets

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 4.4.2-alt2_6
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 4.4.2-alt2_3
- update to new release by fcimport

* Tue Jan 26 2021 Igor Vlasenko <viy@altlinux.ru> 4.4.2-alt1_3
- update to new release by fcimport

* Wed Jan 13 2021 Igor Vlasenko <viy@altlinux.ru> 4.4.2-alt1_2
- update to new release by fcimport

* Thu Nov 05 2020 Igor Vlasenko <viy@altlinux.ru> 4.3.5-alt1_1
- update

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1_3
- update to new release by fcimport

* Thu May 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.12-alt1_1
- update to new release by fcimport

* Fri Mar 29 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.11-alt2_1
- rebuild

* Fri Mar 08 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.11-alt1_1
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.9-alt1_3
- update to new release by fcimport

* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 4.1.9-alt1_2
- update to new release by fcimport

* Mon Dec 17 2018 Igor Vlasenko <viy@altlinux.ru> 4.1.8-alt1_1
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_3
- update to new release by fcimport

* Sun Jun 17 2018 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_2
- fc update

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_0.4.alpha2
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 3.7.3-alt1_5
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.2-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.1-alt1_1
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.0-alt1_2
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.6.0-alt1_1
- update to new release by fcimport

* Wed May 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.5.1-alt1_1
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_2
- initial fc import

