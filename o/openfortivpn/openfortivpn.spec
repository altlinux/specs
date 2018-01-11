Name: openfortivpn
Version: 1.5.0
Release: alt1
Summary: Client for PPP+SSL VPN tunnel services

Group: System/Configuration/Networking
License: GPLv3+
Url: https://github.com/adrienverge/openfortivpn
Source0: https://github.com/adrienverge/openfortivpn/archive/v%version.tar.gz#/%name-%version.tar.gz

BuildRequires: libssl-devel
Requires: ppp

%description
openfortivpn is a client for PPP+SSL VPN tunnel services. It spawns a pppd
process and operates the communication between the gateway and this process.

It is compatible with Fortinet VPNs.

%prep
%setup

%build
%autoreconf
%configure
%make V=1

%install
%makeinstall

%files
%_bindir/openfortivpn
%_man1dir/openfortivpn.1*
%dir %_sysconfdir/openfortivpn
%config(noreplace) %_sysconfdir/openfortivpn/config
%doc README.md LICENSE

%changelog
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
