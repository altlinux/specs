Name: etcnethook-services-restart
Version: 0.0.1
Release: alt1

Summary: Restart specified services on network restart
License: %gpl2plus
Group: System/Base

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

Requires: etcnet alterator-service-functions

%define etcnetdir %_sysconfdir/net
%define restart_script %_libexecdir/%name/services-restart

%description
This package creates netup-post script for etcnet.
It will restart specified services on network restart.

%prep
%setup

%install
install -Dm0755 services-restart %buildroot%restart_script
install -Dm0644 services.list %buildroot%_sysconfdir/%name/services.list

%post
if [ "$1" -eq 1 -a \
	! -e %etcnetdir/netup-post ]; then
	ln -s %restart_script %etcnetdir/netup-post ||:
fi

%preun
if [ "$1" -eq 0 ]; then
	[ "$(readlink -q "%etcnetdir/netup-post")" != "%restart_script" ] ||
		rm -- "%etcnetdir/netup-post" ||:
fi

%files
%config(noreplace) %_sysconfdir/%name/
%_libexecdir/%name/

%changelog
* Wed Sep 30 2015 Mikhail Efremov <sem@altlinux.org> 0.0.1-alt1
- Initial build.

