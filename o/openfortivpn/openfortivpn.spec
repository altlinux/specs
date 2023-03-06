%define git %nil

Name: openfortivpn
Version: 1.20.1
Release: alt1

Summary: Client for PPP+SSL VPN tunnel services
License: GPLv3+
Group: System/Configuration/Networking

Url: https://github.com/adrienverge/openfortivpn
Source: https://github.com/adrienverge/openfortivpn/archive/v%version.tar.gz#/%name-%version.tar

BuildRequires: libssl-devel libsystemd-devel
Requires: ppp opensc

%description
openfortivpn is a client for PPP+SSL VPN tunnel services. It spawns a pppd
process and operates the communication between the gateway and this process.

It is compatible with Fortinet VPNs.

%prep
%setup

%build
%autoreconf
%configure --with-systemdsystemunitdir=%_unitdir
%make V=1

%install
%makeinstall systemdsystemunitdir=%buildroot%_unitdir

%files
%_bindir/openfortivpn
%_unitdir/*.service
%_man1dir/openfortivpn.1*
%dir %_sysconfdir/openfortivpn
%config(noreplace) %_sysconfdir/openfortivpn/config
%doc CHANGELOG.md README.md LICENSE

%changelog
* Mon Mar 06 2023 L.A. Kostis <lakostis@altlinux.ru> 1.20.1-alt1
- 1.20.1.

* Thu Jan 07 2021 L.A. Kostis <lakostis@altlinux.ru> 1.15.0-alt1
- 1.15.0.
- Add systemd support.

* Mon Oct 07 2019 L.A. Kostis <lakostis@altlinux.ru> 1.10.0-alt0.g320f95f
- Updated to v1.10.0-5-g320f95f (for pkcs11 support).
- spec: remove lcc hack (fixed by upstream).

* Sun Oct 06 2019 Michael Shigorin <mike@altlinux.org> 1.7.1-alt1.2
- E2K: avoid lcc-unsupported option.

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue Jul 10 2018 L.A. Kostis <lakostis@altlinux.ru> 1.7.1-alt1
- 1.7.1.

* Wed Feb 28 2018 L.A. Kostis <lakostis@altlinux.ru> 1.6.0-alt1
- 1.6.0.

* Thu Jan 11 2018 L.A. Kostis <lakostis@altlinux.ru> 1.5.0-alt1
- Rebuild for ALTLinux.

* Tue Aug 29 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.5.0-1
- Update to latest upstream version

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 7 2017 Adrien Vergé <adrienverge@gmail.com> - 1.3.0-2
- Fix compiler error, see https://github.com/adrienverge/openfortivpn/issues/81

* Tue Feb 7 2017 Adrien Vergé <adrienverge@gmail.com> - 1.3.0-1
- Update to latest upstream version

* Thu Sep 29 2016 Adrien Vergé <adrienverge@gmail.com> - 1.2.0-1
- Update to latest upstream version

* Sun Feb 14 2016 Adrien Vergé <adrienverge@gmail.com> - 1.1.4-1
- Update to latest upstream version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Adrien Vergé <adrienverge@gmail.com> - 1.1.3-1
- Update to latest upstream version

* Sat Dec 05 2015 Adrien Vergé <adrienverge@gmail.com> - 1.1.2-1
- Update to latest upstream version

* Mon Oct 05 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.1.0-1
- Update to a new upstream release

* Fri Sep 18 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.1-2.20150918gita31c599
- Update to latest pristine sources:
- Improve HTTP buffering
- Fix SSL verification

* Wed Sep 16 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.1-2.20150914gitb22d9eb
- Mark configuration file as noreplace (Christopher Meng, #1263008)

* Mon Sep 14 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.0.1-1.20150914gitb22d9eb
- Initial packaging
