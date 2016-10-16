Name: scst-utils
Version: 3.1.0
Release: alt1
Summary: SCST configuration tool
License: GPLv2
Group: System/Kernel and hardware
URL: http://scst.sf.net

Source: scstadmin-%version.tar.bz2
Source1: scst-load-modules
Patch: scstadmin-3.1.0-alt.patch

BuildRequires: perl-devel
BuildArch: noarch

%description
A tool for configuring SCST via the SCST sysfs interface. Allows to save,
restore and modify any aspect of the SCST configuration. An extensive set of
commands is available to modify any configurable parameter of target drivers,
target ports, SCST devices, LUNs, initiator groups and ALUA configuration
information.

%prep
%setup -q -n scstadmin-%version
%patch -p1

%build
%make

%install
%make DESTDIR=%buildroot install
install -pD -m0755 %SOURCE1 %buildroot/lib/systemd/scst-load-modules
mv %buildroot%_sysconfdir/default %buildroot%_sysconfdir/sysconfig
mv %buildroot/usr/local/sbin %buildroot%_sbindir
mkdir -p %buildroot%perl_vendor_privlib
mv %buildroot/usr/local/share/perl/*/SCST %buildroot%perl_vendor_privlib/
mkdir -p %buildroot%_mandir
mv %buildroot/usr/local/man/* %buildroot%_mandir/

touch %buildroot%_sysconfdir/scst.conf

mkdir -p %buildroot%_unitdir
cat << __EOF__ > %buildroot%_unitdir/scst.service
[Unit]
Description=Generic SCSI target subsystem
After=network.target
Conflicts=shutdown.target
ConditionPathExists=/etc/scst.conf

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStartPre=/lib/systemd/scst-load-modules
ExecStart=/usr/sbin/scstadmin -config /etc/scst.conf
ExecStop=/usr/sbin/scstadmin -force -noprompt -clear_config

[Install]
WantedBy=multi-user.target
__EOF__


%preun
if [ $1 -eq 0 ] ; then
	/sbin/systemctl disable scst.service > /dev/null 2>&1 || :
fi

%files
%doc README examples/scst.conf.sysfs
%ghost %_sysconfdir/scst.conf
%attr(0644,root,root) %_sysconfdir/sysconfig/scst
%attr(0755,root,root) /lib/systemd/scst-load-modules
%_unitdir/scst.service
%_sbindir/*
%perl_vendor_privlib/SCST
%_man1dir/*.1*
%_man5dir/*.5*

%changelog
* Sun Oct 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 3.1.0-alt1
- initial release

