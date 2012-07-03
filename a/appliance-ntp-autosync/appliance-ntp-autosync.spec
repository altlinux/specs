Name: appliance-ntp-autosync
Summary: autosync with ntp servers
BuildArch: noarch
Version: 4.0.1
Release: alt1
License: GPL
Group: System/Base

Requires(post): openntpd

%post
cat > /etc/ntpd.conf << __EOF__
listen on *

servers pool.ntp.org
__EOF__
chown root:wheel /etc/ntpd.conf
chmod 0640 /etc/ntpd.conf

/sbin/chkconfig ntpd on
if [ -z "$DURING_INSTALL" ]; then
    /sbin/service ntpd restart
fi

%description
%summary

%files

%changelog
* Sun May 06 2012 Denis Smirnov <mithraen@altlinux.ru> 4.0.1-alt1
- initial build for ALT Linux Sisyphus

