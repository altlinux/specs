%define _unpackaged_files_terminate_build 1
Name: autorepo-altnode-config
Version: 0.20
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: automated packaging node common configs
Group: System/Configuration/Other
License: GPLv2+
# TODO: change to appropriate page when ready
# Url: https://www.altlinux.org/Autorepo
Url: https://watch.altlinux.org
Source: %name-%version.tar

Requires(pre): postfix rsync-server anonftp
Requires: autorepo-altnode-config-apt = %EVR

# paths expected and configured in autorepo-altnode-admin-create-node
Requires: hasher

%description
%summary

%package nginx
Group: System/Configuration/Other
Summary: generic nginx config for the automated packaging node
Requires(pre): nginx
Requires: autorepo-altnode-config = %EVR

%description nginx
%summary nginx

%if_with ftp
%package ftp
Group: System/Configuration/Other
Summary: generic ftp config for the automated packaging node
Requires(pre): vsftpd
Requires: autorepo-altnode-config = %EVR

%description ftp
%summary ftp
%endif

%package apt
Group: System/Configuration/Other
Summary: generic apt config for the automated packaging node
Requires: apt
Conflicts: autorepo-altnode-config < 0.13

%description apt
%summary apt

%prep
%setup

%build

%install
mkdir -p %buildroot%_sysconfdir/autorepo/apt
install -m 644 apt.conf.* sources.list.* %buildroot%_sysconfdir/autorepo/apt/
install -D -m 644 nginx/autoports.conf %buildroot%_sysconfdir/nginx/sites-enabled.d/autorepo.conf

mkdir -p %buildroot%_sysconfdir/monitrc.d
install -m 644 monit/* %buildroot%_sysconfdir/monitrc.d

mkdir -p %buildroot%_sysconfdir/sysctl.d
echo "vm.swappiness = 10" > %buildroot%_sysconfdir/sysctl.d/10-autorepo.conf

%post
# rsync-server
if ! grep '^\[pub\]' /etc/rsyncd.conf; then
    cat >> /etc/rsyncd.conf <<EOF
# altnode auto configuration
[pub]
path=/var/ftp/pub
#use chroot
read only
list
EOF
    chkconfig rsync on
fi
if ! grep '^\[altnode\]' /etc/rsyncd.conf; then
    cat >> /etc/rsyncd.conf <<EOF
# altnode auto configuration
[altnode]
path=/var/ftp/altnode
use chroot
read only
list
EOF
    chkconfig rsync on
fi
if grep 'only_from = 127.0.0.1' /etc/xinetd.conf; then
    sed -i -e 's,only_from = .*,only_from = 0.0.0.0,' /etc/xinetd.conf
fi
service xinetd restart
# postfix
if ! grep '^relayhost' /etc/postfix/main.cf; then
    cat >> /etc/postfix/main.cf <<EOF
# altnode auto configuration
relayhost = [relay.mskdc.altlinux.org]
EOF
    chkconfig postfix on ||:
    service postfix restart ||:
fi
if ! grep '^myhostname' /etc/postfix/main.cf; then
    echo "WARNING: myhostname not found in /etc/postfix/main.cf"
else
    mailfqdn=`grep '^myhostname' /etc/postfix/main.cf | awk '{print $3}'`
    if [ x$mailfqdn != x`hostname` ]; then
	echo "WARNING: myhostname in /etc/postfix/main.cf does not match hostname"
    fi
fi
service monit restart ||:

%post nginx
chkconfig nginx on ||:
service nginx restart ||:

if [ "$RPM_INSTALL_ARG1" -eq 1 ]; then
    service monit restart ||:
fi

%if_with ftp
%post ftp
chkconfig vsftpd on ||:
service xinetd restart
if [ "$RPM_INSTALL_ARG1" -eq 1 ]; then
    service monit restart ||:
fi
%endif


%files
%config %_sysconfdir/sysctl.d/10-autorepo.conf
%config %_sysconfdir/monitrc.d/00base.conf
%config %_sysconfdir/monitrc.d/10mail.conf
%config %_sysconfdir/monitrc.d/20httpd.conf
%config %_sysconfdir/monitrc.d/crond.conf
%config %_sysconfdir/monitrc.d/filesystems.conf
%config %_sysconfdir/monitrc.d/nginx.conf
%config %_sysconfdir/monitrc.d/postfix.conf
%config(noreplace) %_sysconfdir/monitrc.d/sshd.conf
%config %_sysconfdir/monitrc.d/xinetd.conf
%exclude %_sysconfdir/monitrc.d/nginx.conf
#%config %_sysconfdir/monitrc.d/system.conf

%files nginx
%_sysconfdir/nginx/sites-enabled.d/autorepo.conf
%config %_sysconfdir/monitrc.d/nginx.conf

%files apt
%_sysconfdir/autorepo/apt/apt.conf.*
%_sysconfdir/autorepo/apt/sources.list.*

%changelog
* Fri Nov 24 2023 Igor Vlasenko <viy@altlinux.org> 0.20-alt1
- cronbuild node support

* Thu Nov 16 2023 Igor Vlasenko <viy@altlinux.org> 0.19-alt1
- set vm.swappiness = 10

* Tue Nov 14 2023 Igor Vlasenko <viy@altlinux.org> 0.18-alt1
- changed relayhost
- removed ftp (deprecated service)
- added p11

* Sat Jan 15 2022 Igor Vlasenko <viy@altlinux.org> 0.17-alt1
- added p10

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- added armh and lowercase sisyphus

* Thu Jul 04 2019 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- added aarch64 and ppc64le

* Thu Mar 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- p9 support

* Sat Jan 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- apt configs moved out to apt subpackage

* Tue Apr 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added support for t8/p8

* Sun Apr 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- fixed monit misconfiguration

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- fixed port in monit for autoports (thanks to ldv@)

* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- rsync entry is adapted to common /space

* Sat Jul 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- p7 support

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt3
- altnode rsync entry

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2
- better nginx support

* Thu Jul 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- monit dependency and config files

* Wed Nov 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added debuginfo for t6 and p6

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- support for p6 and 5.1

* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added initial xinetd configuration

* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- updated initial postfix configuration

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added %%post for initial service configuration

* Sat May 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
