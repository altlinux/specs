Name: apcupsd-multiups
Version: 0.2
Release: alt1
Packager: Sergey Y. Afonin <asy@altlinux.ru>

Summary: apcupsd's configuration for monitoring multiple UPSes on one host
License: %gpl2only
Group: System/Servers
Url: http://git.altlinux.org/gears/a/apcupsd-multiups.git

Source: %name-%version.tar

BuildRequires: rpm-build-licenses

Requires: apcupsd
BuildArch: noarch

%description
Apcupsd's configuration for monitoring multiple UPSes on one host.
It installed as separated configuration for main apcupsd package
and it has not conflict with the basic configuration. Some
actions are disabled (reboot, shutdown and killpower).

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT{%_initdir,%_sysconfdir/%name}

cp apccontrol                   $RPM_BUILD_ROOT/%_sysconfdir/%name/
cp apcupsd.XXXXXX.conf.template $RPM_BUILD_ROOT/%_sysconfdir/%name/
cp doreboot                     $RPM_BUILD_ROOT/%_sysconfdir/%name/
cp doshutdown                   $RPM_BUILD_ROOT/%_sysconfdir/%name/
cp killpower                    $RPM_BUILD_ROOT/%_sysconfdir/%name/
cp README                       $RPM_BUILD_ROOT/%_sysconfdir/%name/
cp upsdmessages                 $RPM_BUILD_ROOT/%_sysconfdir/%name/

# creating symlinks for actions
pushd $RPM_BUILD_ROOT/%_sysconfdir/%name
	sh $RPM_BUILD_DIR/%name-%version/makesymlinks
popd

cp apcupsd-multiups.init         $RPM_BUILD_ROOT/%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%attr(0755,root,root) %config(noreplace) %_initdir/%name

%changelog
* Mon May 28 2012 Sergey Y. Afonin <asy@altlinux.ru> 0.2-alt1
- new version

* Fri May 04 2012 Sergey Y. Afonin <asy@altlinux.ru> 0.1-alt1
- Initial build
