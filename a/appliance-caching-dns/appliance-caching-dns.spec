Name: appliance-caching-dns
Summary: setup bind as caching DNS-server
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires(post): bind grep chrooted

%post
chkconfig bind on
if [ -z "$DURING_INSTALL" ]; then
    /sbin/service bind start
fi

if ! egrep -q '^nameserver 127.0.0.1$'; then
    echo "nameserver 127.0.0.1" > /etc/resolv.conf
    /sbin/update_chrooted all
fi

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

