%define confname tmp.cache.conf
%define unitname altlinux-apt-tmp-cache

Name: apt-conf-tmp-cache
Version: 1.0
Release: alt1

BuildArch: noarch

Summary: Temporary cache configuration files for apt

License: GPL
Group: System/Configuration/Packaging
Url: http://git.altlinux.org/people/sin/packages/apt-conf-tmp-cache.git

Packager: Evgemy Sinelnikov <sin@altlinux.ru>

Source: %name-%version.tar

%description
This package contains apt configuration for place cache in /tmp/.apt-cache

%prep
%setup -q

%install
mkdir -p %buildroot%_sysconfdir/apt/apt.conf.d
mkdir -p %buildroot%_unitdir
install -p -m644 %confname %buildroot%_sysconfdir/apt/apt.conf.d/%confname
install -m644 %unitname.service %buildroot%_unitdir/%unitname.service
install -m755 %unitname %buildroot/lib/systemd/%unitname

%files
%config(noreplace) %_sysconfdir/apt/apt.conf.d/%confname
/lib/systemd/%unitname
%_unitdir/%unitname.service

%changelog
* Thu Feb 09 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1.0-alt1
- Initial build for Sisyphus
