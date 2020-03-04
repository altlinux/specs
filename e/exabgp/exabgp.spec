Name: exabgp
Version: 4.2.6
Release: alt1

Summary: The BGP swiss army knife of networking
License: BSD
Group: Security/Networking
Url: https://github.com/Exa-Networks/exabgp

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

Requires: python3-module-%name
%add_python3_req_skip _abcoll exabgp.vendoring.six.moves thread


%description
ExaBGP allows engineers to control their network from commodity
servers. Think of it as Software Defined Networking using BGP.

It can be used to announce ipv4, ipv6, vpn or flow routes (for DDOS
protection) from its configuration file(s). ExaBGP can also transform
BGP messages into friendly plain text or JSON which can be easily
manipulate by scripts and report peer announcements.

%package -n python3-module-%name
Summary: %name python library
Group: Development/Python3

%description -n python3-module-%name
%name python library

%prep
%setup

%build

%install
%__python3 setup.py install --root=%buildroot

install -pDm 644 etc/systemd/%name.service %buildroot%_unitdir/%name.service
install -pDm 644 doc/man/%name.1 %buildroot%_man1dir/%name.1
install -pDm 644 doc/man/%name.conf.5 %buildroot%_man5dir/%name.conf.5
mkdir -p %buildroot%_sysconfdir
mv -v %buildroot/usr/etc/%name %buildroot%_sysconfdir/%name

%files
%doc CHANGELOG.rst LICENCE.txt README.*
%_bindir/*
%config %_sysconfdir/%name
# %%_unitdir/%name.service
%_man1dir/*.1*
%_man5dir/*.5*

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/*.egg-info


%changelog
* Wed Mar 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.2.6-alt1
- Version updated to 4.2.6 (with python3 support).

* Sat Oct 29 2016 Terechkov Evgenii <evg@altlinux.org> 3.4.17-alt2
- Split exabgp library to separate subpackage

* Sat Oct 29 2016 Terechkov Evgenii <evg@altlinux.org> 3.4.17-alt1
- 3.4.17

* Sun Jul 31 2016 Terechkov Evgenii <evg@altlinux.org> 3.4.16-alt1
- Initial build for ALT Linux Sisyphus
