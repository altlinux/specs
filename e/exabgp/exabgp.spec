Name: exabgp
Version: 3.4.17
Release: alt2

Summary: The BGP swiss army knife of networking

Url: https://github.com/Exa-Networks/exabgp
License: BSD
Group: Security/Networking

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires: python-module-setuptools
Requires: python-module-%name

%description
ExaBGP allows engineers to control their network from commodity
servers. Think of it as Software Defined Networking using BGP.

It can be used to announce ipv4, ipv6, vpn or flow routes (for DDOS
protection) from its configuration file(s). ExaBGP can also transform
BGP messages into friendly plain text or JSON which can be easily
manipulate by scripts and report peer announcements.

%package -n python-module-%name
Summary: %name python library
Group: Development/Python

%description -n python-module-%name
%name python library

%prep
%setup
%patch -p1

%build

%install
python setup.py install --root=%buildroot

install -pDm 644 etc/systemd/%name.service %buildroot%_unitdir/%name.service
install -pDm 644 doc/man/%name.1 %buildroot%_man1dir/%name.1
install -pDm 644 doc/man/%name.conf.5 %buildroot%_man5dir/%name.conf.5
mkdir -p %buildroot%_sysconfdir
mv -v %buildroot/usr/etc/%name %buildroot%_sysconfdir/%name

%files
%_bindir/%name
%config %_sysconfdir/%name
%_unitdir/%name.service
%_man1dir/*.1*
%_man5dir/*.5*
%doc README.md

%files -n python-module-%name
%python_sitelibdir/%name
%python_sitelibdir/*.egg-info
%doc CHANGELOG

%changelog
* Sat Oct 29 2016 Terechkov Evgenii <evg@altlinux.org> 3.4.17-alt2
- Split exabgp library to separate subpackage

* Sat Oct 29 2016 Terechkov Evgenii <evg@altlinux.org> 3.4.17-alt1
- 3.4.17

* Sun Jul 31 2016 Terechkov Evgenii <evg@altlinux.org> 3.4.16-alt1
- Initial build for ALT Linux Sisyphus
