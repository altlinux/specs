Name: dnscrypt-proxy
Version: 2.1.4
Release: alt1

Summary: A protocol for securing communications between a client and a DNS resolver

License: BSD
Group: Networking/Other
Url: https://github.com/jedisct1/dnscrypt-proxy

# Source-url: https://github.com/DNSCrypt/dnscrypt-proxy/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Source1: %name.service
#socket activation is currently broken, maybe removed in the future
Source2: %name.socket
#Source3: %name.toml

BuildRequires: golang
BuildRequires: pkgconfig(systemd)

#Requires: libunbound unbound unbound-control

%description
Dnscrypt-proxy provides local service which can be used directly as
your local resolver or as a DNS forwarder, encrypting and
authenticating requests using the DNSCrypt protocol and passing them
to an upstream server. The DNSCrypt protocol uses high-speed
high-security elliptic-curve cryptography and is very similar to
DNSCurve, but focuses on securing communications between a client and
its first-level resolver. While not providing end-to-end security, it
protects the local network, which is often the weakest point of the
chain, against man-in-the-middle attacks. It also provides some
confidentiality to DNS queries.

Recommends: unbound or dnsmask

%prep
%setup

%build
export GO111MODULE=off
pushd dnscrypt-proxy
export GOPATH=$PWD
ln -s ../vendor src
go build -ldflags="-s -w"
popd

%install
pushd dnscrypt-proxy
install -D -p -m 0755 ./dnscrypt-proxy %buildroot%_sbindir/dnscrypt-proxy
install -D -p -m 0644 example-*.txt -t %buildroot%_docdir/%name/
popd
install -D -p -m 0644 %SOURCE1 %buildroot%_unitdir/%name.service
install -D -p -m 0644 %SOURCE2 %buildroot%_unitdir/%name.socket
install -D -p -m 0644 dnscrypt-proxy/example-dnscrypt-proxy.toml %buildroot%_sysconfdir/%name.toml


%post
%post_service %name

%preun
%preun_service %name


%files
%doc README.md LICENSE
%config(noreplace) %_sysconfdir/dnscrypt-proxy.toml
%_unitdir/%name.service
%_unitdir/%name.socket
%_sbindir/%name
%_docdir/%name/*.txt

%changelog
* Sat Feb 25 2023 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- new version 2.1.4 (with rpmrb script)

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- new version 2.1.2 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Fri Oct 08 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt2
- pack config from upstream's example

* Fri Sep 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- new version 2.1.0 (with rpmrb script)

* Fri Sep 17 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.44-alt2
- human build for ALT Sisyphus

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.44-alt1_1
- update by mgaimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.39-alt1_1
- update by mgaimport

* Tue Mar 10 2020 Igor Vlasenko <viy@altlinux.ru> 2.0.23-alt1_2
- update by mgaimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.23-alt1_1
- new version

