Name: autorepo-altnode-config
Version: 0.04
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: common configs for an automated packaging node
Group: System/Configuration/Other
License: GPL2+
#Url: 
Source: %name-%version.tar

Requires(pre): postfix rsync-server anonftp vsftpd

%description
%summary

%package nginx
Group: System/Configuration/Other
Summary: generic nginx config for an automated packaging node
Requires(pre): nginx

%description nginx
%summary nginx

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT%_sysconfdir/autorepo/apt
install -m 644 apt.conf.* sources.list.* $RPM_BUILD_ROOT%_sysconfdir/autorepo/apt/
install -D -m 644 nginx/autoports.conf %buildroot%_sysconfdir/nginx/sites-enabled.d/autorepo.conf

%post
# postfix
if ! grep '^relayhost' /etc/postfix/main.cf; then
    cat >> /etc/postfix/main.cf <<EOF
# altnode auto configuration
relayhost = [192.168.1.7]
EOF
    service postfix restart ||:
fi
# rsync-server
if ! grep '^\[pub\]' /etc/rsyncd.conf; then
    cat >> /etc/rsyncd.conf <<EOF
# altnode auto configuration
[pub]
path=/var/ftp/pub
use chroot
read only
list
EOF
    chkconfig rsync on
fi
# ftpd
chkconfig vsftpd on ||:
if grep 'only_from = 127.0.0.1' /etc/xinetd.conf; then
    sed -i -e 's,only_from = .*,only_from = 0.0.0.0,' /etc/xinetd.conf
fi
service xinetd restart

%post nginx
# nginx
service nginx restart ||:

%files
%_sysconfdir/autorepo/apt/apt.conf.*
%_sysconfdir/autorepo/apt/sources.list.*

%files nginx
%_sysconfdir/nginx/sites-enabled.d/autorepo.conf

%changelog
* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added initial xinetd configuration

* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- updated initial postfix configuration

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added %%post for initial service configuration

* Sat May 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
